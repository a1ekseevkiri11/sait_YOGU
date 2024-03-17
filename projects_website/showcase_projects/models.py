from django.db import models
from registration.models import Profile
from django.contrib.auth.models import Group, Permission
from django.db.models import UniqueConstraint

from .tasks import (
    addPermissionToGroups,
    deletePermissionFromGroups,
)

class ModelWithStatus(models.Model):

    class Meta:
        abstract = True
    
    STATUS_CHOICES = [
        ('accepted', 'Принят'),
        ('processing', 'В обработке'),
        ('rejected', 'Отклонен'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='processing')

    def set_status(self, new_status):
        self.status = new_status
        self.save()
            
    def get_status(self):
        return self.status



class Project(ModelWithStatus):
    class Meta:
        permissions = [
            ("change_status_project", "Can change status project"),
        ]
    title = models.CharField(max_length=100)
    place = models.IntegerField(default=6)
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='customer')
    lecturer = models.ForeignKey(Profile, on_delete=models.CASCADE, default=None, null=True, blank=True, related_name='lecturer')

    
    def freePlaces(self):
        return self.place > self.participation_set.count()

    def studentInThisProject(self, student):
        return self.participation_set.filter(student=student).exists()

    def addStudent(self, student):
        if Participation.objects.filter(student=student).exists():
            return

        if not self.freePlaces():
            return

        Participation.objects.create(project=self, student=student)

    def deleteStudent(self, student):
        try:
            participation = Participation.objects.get(project=self, student=student)
            participation.delete()
        except Participation.DoesNotExist:
            pass

    def addLetter(self, student, letter):
        if Participation.objects.filter(student=student).exists():
            return

        if MotivationLetters.objects.filter(student=student).exists():
            return
        
        MotivationLetters.objects.create(project=self, student=student, letter=letter)

    def addRejectionComment(self, comment):
        if comment != '':
            RejectionComment.objects.create(project=self, comment=comment)

    def deleteRejectionComment(self):
        try:
            comment = RejectionComment.objects.get(project=self)
            comment.delete()
        except RejectionComment.DoesNotExist:
            pass

    def __str__(self):
        return self.title
    


class Participation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    student = models.OneToOneField(Profile, on_delete=models.CASCADE)
    

class MotivationLetters(ModelWithStatus):

    class Meta:
        permissions = [
            ("download_motivationletters", "Can download motivation letters"),
            ("change_status_motivationletters", "Can change status motivation letters"),
        ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    student = models.ForeignKey(Profile, on_delete=models.CASCADE)
    letter = models.FileField(upload_to='letters/')


class RejectionComment(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name='rejection_comment')
    comment = models.TextField()




class TimePermission(models.Model):
    GROUP_NAMES = list(Group.objects.values_list('name', 'name'))

    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
    group = models.CharField(max_length=127, choices=GROUP_NAMES)
    time_add = models.DateTimeField()
    time_delete = models.DateTimeField()
    completed_add = models.BooleanField(default=False)
    completed_delete = models.BooleanField(default=False)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['permission', 'group'], name='unique_permission_group')
        ]

    def addTask(self):
        if not self.completed_add:
            self.completed_add = True
            self.save()
            addPermissionToGroups.delay(self.permission.pk, self.group)


    def deleteTask(self):
        if not self.completed_delete:
            self.completed_delete = True
            self.save()
            deletePermissionFromGroups.delay(self.permission.pk, self.group)

    def save(self, *args, **kwargs):
        completed_add = False
        completed_delete = False
        return super().save(*args, **kwargs)