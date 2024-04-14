from django.urls import (
    reverse_lazy,
)

from django.shortcuts import (
    render, 
    redirect,
    get_object_or_404,
)


from django.contrib.auth.decorators import login_required

from .models import (
    Project,
    Participation
)

from .permission import (
    canDo
)


@login_required
def projectMy(request):
    student = request.user.student

    if not student:
        return reverse_lazy('home')
    
    try:
        participation = Participation.objects.get(student=student)
        return redirect('project-detail', pk=participation.project.id)
    except:
        return render(template_name='showcase_projects/project_detail_empty.html', request=request)
    
   