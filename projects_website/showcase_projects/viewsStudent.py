from django.urls import (
    reverse_lazy,
)

from django.shortcuts import (
    render, 
    redirect,
    get_object_or_404,
)

from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView
)

from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin
)


from django.contrib.auth.decorators import login_required

from .models import (
    Project,
    Participation,
    MotivationLetters
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
    


class StudentMotivationLetter(ListView, UserPassesTestMixin, LoginRequiredMixin):
    model = MotivationLetters
    template_name = 'showcase_projects/motivation_letter.html'
    context_object_name = 'letters'
    paginate_by = 6

    
    def get_queryset(self):
        return MotivationLetters.objects.filter(student=self.request.user.student)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['buttonDeleteMotivationLetter'] = canDo(self.request.user, 'delete_motivationletters')
        return context

    def post(self, request, *args, **kwargs):
        letter_id = request.POST.get('letter_id')
        letter = get_object_or_404(MotivationLetters, id=letter_id)
        if 'delete_motivation_letter' in request.POST:
            if not canDo(self.request.user, 'delete_motivationletters'):
                return redirect(request.path)
            
            letter.delete()

        return redirect(request.path)
    
    def test_func(self):
        return self.request.user.groups.filter(name='student').exists()