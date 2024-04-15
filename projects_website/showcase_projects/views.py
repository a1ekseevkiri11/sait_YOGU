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
    Customer
)


from django.views.generic import (
    ListView,
    DetailView,
    View
)

from django.db.models import Q

from .models import (
    Project, 
    Participation,
    MotivationLetters,
)

from .permission import (
    canAddParticipation,
    canDeleteParticipation,
    canDownloadMotivationLetters,
    canAddMotivationLetters,
    canDo

)

from .forms import (
    ConfirmationForm,
    MotivationLettersForm,
)

from .filters import ProjectFilter


class ProjectListView(ListView):
    queryset = Project.objects.all()
    template_name = 'showcase_projects/home.html' 
    context_object_name = 'projects'
    paginate_by = 4

    def get_queryset(self):
        queryset = super().get_queryset()
        
        query = self.request.GET.get('q')
        filters = self.request.GET
        
        if query:
            queryset = queryset.filter(Q(order__title__icontains=query))
        
        self.filterset = ProjectFilter(filters, queryset=queryset)
        return self.filterset.qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['projectFilter'] = self.filterset.form
        
        context['applied_filters'] = self.request.GET.urlencode()
        
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
        
        if self.request.user.groups.filter(name='student').exists():
            context['participationProject'] = project.freePlaces()
            if canDo(self.request.user, 'add_participation'):
                student = self.request.user.student
                context['canAddToProject'] = True
                context['studentInProject'] = Participation.objects.filter(student=student).exists()
                context['studentInThisProject'] = project.studentInThisProject(student)
            
            if canDo(self.request.user, 'add_motivationletters'):
                context['motivation_form'] =  MotivationLettersForm()

        if self.request.user.groups.filter(name='lecturer').exists():
            if self.request.user.lecturer == project.lecturer:
                context['letters'] = MotivationLetters.objects.filter(project=project, status='processing')
            
        return context
    
    def post(self, request, *args, **kwargs):
        project = self.get_object()
        user = self.request.user
        student = user.student
    
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
        if self.request.user.groups.filter(name='administrator').exists():
            return True
        
        project = self.get_object()
        if self.request.user.custome == project.customer:
            return True
        
        return False


class ProjectCustomerListView(ListView):
    model = Project
    template_name = 'showcase_projects/project_user.html'
    context_object_name = 'projects'

    def get_queryset(self):
        user = get_object_or_404(Customer, user__username=self.kwargs.get('username'))
        return Project.objects.filter(customer=user)
    


class MotivationLetterDownload(View):
    def get(self, request, letter_id):
        if not canDownloadMotivationLetters(self.request.user):
            return HttpResponse(status=403)
        motivation_letter = get_object_or_404(MotivationLetters, id=letter_id)
        response = HttpResponse(motivation_letter.letter, content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{motivation_letter.letter.name}"'
        return response
    

