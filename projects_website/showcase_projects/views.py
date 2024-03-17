from django.shortcuts import (
    redirect, 
    get_object_or_404
)

from django.contrib.auth.mixins import (
    UserPassesTestMixin
)

from django.http import (
    HttpResponse,
    HttpResponseForbidden,
)


from registration.models import(
    Profile
)


from django.views.generic import (
    ListView,
    DetailView,
    View
)

from .models import (
    Project, 
    Participation,
    MotivationLetters,
)

from .pernission import (
    canAddParticipation,
    canDeleteParticipation,
    canAddProject,
    canDownloadMotivationLetters,
    canAddMotivationLetters,


)

from .forms import (
    ConfirmationForm,
    MotivationLettersForm,
)



class ProjectListView(ListView):
    model = Project
    template_name = 'showcase_projects/home.html' 
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.filter(status='accepted')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['showButtonCreateProject'] = canAddProject(self.request.user)
        return context
    


class ProjectDetailView(DetailView, UserPassesTestMixin):
    model = Project
    template_name = 'showcase_projects/project_detail.html'

    def get_context_data(self, **kwargs):
        project = self.get_object()
        context = super().get_context_data(**kwargs)
        context['countFreePlace'] =  project.place - project.participation_set.count()
        if not self.request.user.is_authenticated:
            return context
        
        student =  self.request.user.profile
        if canAddParticipation(self.request.user):
            context['participationProject'] = project.freePlaces()
            context['studentInProject'] = Participation.objects.filter(student=student).exists()
            context['studentInThisProject'] = project.studentInThisProject(student)
        
        if canAddMotivationLetters(self.request.user):
            context['motivation_form'] =  MotivationLettersForm()
            
        return context
    
    def post(self, request, *args, **kwargs):
        project = self.get_object()
        user = self.request.user
        student = user.profile
    
        if 'add_partition' in request.POST:
            if canAddParticipation(user):
                project.addStudent(student)
                return redirect(request.path)


        if 'delete_partition' in request.POST:
            if canDeleteParticipation(user):
                project.deleteStudent(student)
                return redirect(request.path)
            
        if 'add_motivation_letter' in request.POST:
            if canAddMotivationLetters(user):
                motivation_form = MotivationLettersForm(request.POST, request.FILES)
                if motivation_form.is_valid():
                    project.addLetter(student, motivation_form.cleaned_data['letter'])
                    motivation_form.cleaned_data['letter']
                
        return redirect(request.path)
    
    def test_func(self):
        project = self.get_object()
        status = project.get_status('accepted')
        return status == 'accepted'


class ProjectCustomerListView(ListView):
    model = Project
    template_name = 'showcase_projects/project_user.html'
    context_object_name = 'projects'

    def get_queryset(self):
        user = get_object_or_404(Profile, user__username=self.kwargs.get('username'))
        return Project.objects.filter(customer=user)
    


class MotivationLetterDownload(View):
    def get(self, request, letter_id):
        if not canDownloadMotivationLetters(self.request.user):
            return HttpResponse(status=403)
        motivation_letter = get_object_or_404(MotivationLetters, id=letter_id)
        response = HttpResponse(motivation_letter.letter, content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{motivation_letter.letter.name}"'
        return response
    

