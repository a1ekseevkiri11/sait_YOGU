from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import m2m_changed


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
    )

    class Meta:
        abstract = True


    def __str__(self):
        return self.user.username


@receiver(m2m_changed, sender=User.groups.through)
def update_user_profile(sender, instance, action, **kwargs):
    if action == 'post_add':
        if instance.groups.filter(name='student').exists():
            Student.objects.get_or_create(user=instance)

        if instance.groups.filter(name='lecturer').exists():
            Lecturer.objects.get_or_create(user=instance)

        if instance.groups.filter(name='customer').exists():
            Customer.objects.get_or_create(user=instance)
    
    elif action == 'post_remove':
        if not instance.groups.filter(name='student').exists(): 
            Student.objects.filter(user=instance).delete()

        if not instance.groups.filter(name='lecturer').exists():
            Lecturer.objects.filter(user=instance).delete()

        if not instance.groups.filter(name='customer').exists():
            Customer.objects.filter(user=instance).delete()



class Student(Profile):
    pass


class Customer(Profile):
    pass


class Lecturer(Profile):
    pass