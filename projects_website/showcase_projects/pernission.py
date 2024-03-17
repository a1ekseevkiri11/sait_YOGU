def canAddProject(user):
    return user.has_perm('showcase_projects.add_project')

def canDeleteProject(user):
    return user.has_perm('showcase_projects.delete_project')

def canChangeStatusProject(user):
    return user.has_perm('showcase_projects.change_status_project')

def canAddParticipation(user):
    return user.has_perm('showcase_projects.add_participation')

def canDeleteParticipation(user):
    return user.has_perm('showcase_projects.delete_participation')

def canDownloadMotivationLetters(user):
    return user.has_perm('showcase_projects.download_motivationletters')

def canAddMotivationLetters(user):
    return user.has_perm('showcase_projects.add_motivationletters')

def canDeleteMotivationLetters(user):
    return user.has_perm('showcase_projects.delete_motivationletters')

def canChangeStatusMotivationLetters(user):
    return user.has_perm('showcase_projects.change_status_motivationletters')

