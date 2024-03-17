# tasks.py

from celery import shared_task
from django.contrib.auth.models import Group, Permission
from django.utils import timezone


@shared_task
def inspectorTimePermissionTasks():
    from .models import TimePermission
    now = timezone.now()
    scheduled_tasks = TimePermission.objects.all()
    for task in scheduled_tasks:
        if task.time_delete <= now:
            task.deleteTask()
        elif task.time_add <= now:
            task.addTask()
        

@shared_task(bind=True)
def addPermissionToGroups(self, permission_id, group_name):
    try:
        permission = Permission.objects.get(id=permission_id)
        group = Group.objects.get(name=group_name)
        group.permissions.add(permission)
        group.save()

        return f"Permission {permission} added to group {group.name}"
    
    except Exception as e:
        return f"Error add permission: {e}"


@shared_task(bind=True)
def deletePermissionFromGroups(self, permission_id, group_name):
    try:
        permission = Permission.objects.get(id=permission_id)
        group = Group.objects.get(name=group_name)
        group.permissions.remove(permission)
        group.save()

        return f"Permission {permission} added to group {group.name}"
    except Exception as e:
        return f"Error removing permission: {e}"