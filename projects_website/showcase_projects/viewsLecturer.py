from django.urls import (
    reverse_lazy,
)

from django.shortcuts import (
    redirect,
    get_object_or_404,
)

from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin
)

from django.views.generic import (
    ListView,
    DetailView
)

from .models import (
    Project,
    Lecturer,
    MotivationLetters
)

from .permission import (
    canDo
)


class LecturerProject(ListView, UserPassesTestMixin, LoginRequiredMixin):
    model = Project
    template_name = 'showcase_projects/lecturer_project.html'
    context_object_name = 'projects'
    paginate_by = 6

    
    def get_queryset(self):
        user = get_object_or_404(Lecturer, user__username=self.request.user.username)
        return Project.objects.filter(lecturer=user)
    
    
    def test_func(self):
        return self.request.user.groups.filter(name='lecturer').exists()
    

class LecturerMotivationLetter(DetailView, UserPassesTestMixin, LoginRequiredMixin):
    model = MotivationLetters

    def post(self, request, *args, **kwargs):    

        if 'add_motivation_letter' in request.POST:
            if canDo(self.request.user,'change_status_motivationletters'):
                letter_id = request.POST.get('letter_id')
                try:
                    letter = MotivationLetters.objects.get(id=letter_id)
                    if 'accept' in request.POST:
                        letter.set_status('accepted')  
                        letter.project.addStudent(letter.student.user.student)
                    
                    if 'reject' in request.POST:
                        letter.set_status('rejected')
                except:
                    pass
                 
        return redirect(request.path)

    

