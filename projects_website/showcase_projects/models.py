from django.db import models
from registration.models import (
    Customer,
    Lecturer,
    Student
)
from django.contrib.auth.models import Group, Permission
from django.db.models import UniqueConstraint

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
    




class DirectionIdentity(models.Model):
    title = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.title


class Spheres(models.Model):
    title = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.title


class Types(models.Model):
    title = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.title
    

class Order(ModelWithStatus):
    title = models.CharField(max_length=100)
    # description = models.TextField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer')
    directionIdentity = models.ManyToManyField(DirectionIdentity)
    spheres = models.ManyToManyField(Spheres)
    types = models.ManyToManyField(Types)

    def addRejectionComment(self, comment):
        self.deleteRejectionComment()
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

class Project(models.Model):
    class Meta:
        permissions = [
            ("change_status_project", "Can change status project"),
        ]

    CUSTOMER_TYPE = [
        ('external' ,'Внешний'),
        ('interior' ,'Внутренний'),
    ]

    order = models.OneToOneField(Order, on_delete=models.CASCADE, default=None, null=True, blank=True,)
    place = models.IntegerField(default=6)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE, default=None, null=True, blank=True, related_name='lecturer')
    customer_type = models.CharField(max_length=20, choices=CUSTOMER_TYPE, default='processing')
    

    
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




class Participation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    

class MotivationLetters(ModelWithStatus):

    class Meta:
        permissions = [
            ("download_motivationletters", "Can download motivation letters"),
            ("change_status_motivationletters", "Can change status motivation letters"),
        ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    letter = models.FileField(upload_to='letters/')


class RejectionComment(models.Model):
    project = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='rejection_comment')
    comment = models.TextField()



class TimePermission(models.Model):

    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    time_start = models.DateTimeField()
    time_finish = models.DateTimeField()

    class Meta:
        constraints = [
            UniqueConstraint(fields=['permission', 'group'], name='unique_permission_group')
        ]


    