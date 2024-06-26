from django.contrib.auth.mixins import (
    UserPassesTestMixin
)

from .models import(
    Lecturer,
    Customer,
    Student
)

from django.views.generic import (
    ListView,
    View,
)

from django.urls import reverse
from django.shortcuts import (
    render, 
    redirect,
    get_object_or_404,
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from showcase_projects.models import (
    Participation,
    Project,
    Order,
    MotivationLetters,
)

from showcase_projects.permission import (
    canDo,
    canAddProject,
    canChangeStatusMotivationLetters,
    canDeleteMotivationLetters
)

class CustomLoginView(LoginView):
    def get_success_url(self):
        groups = self.request.user.groups
        if groups.filter(name='administrator').exists():
            return reverse_lazy('administrator')
        else:
            return super().get_success_url()





@login_required
def profile(request):
    groups = request.user.groups
    if groups.filter(name='customer').exists():
        return redirect(reverse('profileCustomer'))
    if groups.filter(name='lecturer').exists():
        return redirect(reverse('profileLecturer'))
    if groups.filter(name='student').exists():
        return redirect(reverse('profileStudent'))
    return render(template_name='registration/profile.html', request=request)


class CustomerProfile(ListView, UserPassesTestMixin):
    model = Order
    template_name = 'registration/profileCustomer.html'
    context_object_name = 'orders'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['showButtonCreateProject'] = canAddProject(self.request.user)
        return context
    
    def get_queryset(self):
        user = get_object_or_404(Customer, user__username=self.request.user.username)
        return Order.objects.filter(customer=user)
    
    def test_func(self):
        return self.request.user.groups.filter(name='customer').exists()
    


class LecturerProfile(View, LoginRequiredMixin):

    def post(self, request, *args, **kwargs):
        if not canDo(self.request.user,'change_status_motivationletters'):
            return redirect('home')
        letter_id = request.POST.get('letter_id')
        try:
            letter = MotivationLetters.objects.get(id=letter_id)
            if 'accept' in request.POST:
                letter.set_status('accepted')  
                letter.project.addStudent(letter.student.user.student)
            
            if 'reject' in request.POST:
                letter.set_status('rejected')
            
            return redirect('project-detail', pk=letter.project.id)
        
        except:
            pass

        return redirect('home')
                 
        
    
    
    def test_func(self):
        return self.request.user.groups.filter(name='lecturer').exists()
    

class StudentProfile(View, LoginRequiredMixin):

    def get(self, request, *args, **kwargs):
        user = self.request.user
        project = None
        try:
            participation = Participation.objects.get(student=user.student)
            project = participation.project
        except:
            pass
        letters = MotivationLetters.objects.filter(student=user.student)
        buttonDeleteMotivationLetter = canDeleteMotivationLetters(user)
        context = {'project' : project, 'letters': letters, 'buttonDeleteMotivationLetter': buttonDeleteMotivationLetter,}
        return render(request, 'registration/profileStudent.html', context)
    
    def post(self, request, *args, **kwargs):
        letter_id = request.POST.get('letter_id')
        letter = get_object_or_404(MotivationLetters, id=letter_id)
        if 'delete_motivation_letter' in request.POST:
            if not canDeleteMotivationLetters(self.request.user):
                return redirect(request.path)
            
            letter.delete()

        return redirect(request.path)
    
    def test_func(self):
        return self.request.user.groups.filter(name='student').exists()