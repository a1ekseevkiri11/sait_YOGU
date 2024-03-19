from .models import TimePermission
from django.contrib.auth.models import Permission
from django.utils import timezone

APP_NAME = 'showcase_projects'

def permissionIsActiv(name_permission, groups):
    try:
        permission = Permission.objects.get(codename=name_permission)
        print(permission)
        if not TimePermission.objects.filter(permission=permission).exists():
            return True
        
        if TimePermission.objects.filter(permission=permission, group__in=groups, time_start__lte=timezone.now(), time_finish__gte=timezone.now()).exists():
            return True
        
        return False
    except:
        pass
    return False


#
#
# ПЕРЕПИСАТЬ ВО Views()!!!
#
#
def canAddProject(user):
    name_permission = 'add_project'
    return user.has_perm(APP_NAME + '.' + name_permission) and permissionIsActiv(name_permission, user.groups.all())


def canDeleteProject(user):
    name_permission = 'delete_project'
    return user.has_perm(APP_NAME + '.' + name_permission) and permissionIsActiv(name_permission, user.groups.all())


def canChangeStatusProject(user):
    name_permission = 'change_status_project'
    return user.has_perm(APP_NAME + '.' + name_permission) and permissionIsActiv(name_permission, user.groups.all())


def canAddParticipation(user):
    name_permission = 'add_participation'
    return user.has_perm(APP_NAME + '.' + name_permission) and permissionIsActiv(name_permission, user.groups.all())

def canDeleteParticipation(user):
    name_permission = 'delete_participation'
    return user.has_perm(APP_NAME + '.' + name_permission) and permissionIsActiv(name_permission, user.groups.all())


def canDownloadMotivationLetters(user):
    name_permission = 'download_motivationletters'
    return user.has_perm(APP_NAME + '.' + name_permission) and permissionIsActiv(name_permission, user.groups.all())


def canAddMotivationLetters(user):
    name_permission = 'add_motivationletters'
    return user.has_perm(APP_NAME + '.' + name_permission) and permissionIsActiv(name_permission, user.groups.all())


def canDeleteMotivationLetters(user):
    name_permission = 'delete_motivationletters'
    return user.has_perm(APP_NAME + '.' + name_permission) and permissionIsActiv(name_permission, user.groups.all())


def canChangeStatusMotivationLetters(user):
    name_permission = 'change_status_motivationletters'
    return user.has_perm(APP_NAME + '.' + name_permission) and permissionIsActiv(name_permission, user.groups.all())

