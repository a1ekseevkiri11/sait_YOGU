from django.shortcuts import (
    redirect, 
)

from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin
)

from django.views.generic import (
    ListView,
)

from .models import (
    Project, 
)

from .formsAdministrator import (
    AcceptProjectForm,
    RejectProjectForm,
)


class AdministratorProjectsAcceptanceView(ListView, LoginRequiredMixin, UserPassesTestMixin):
    model = Project
    template_name = 'showcase_projects/administrator/acceptanceProjects.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.filter(status='processing')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accept_form'] = AcceptProjectForm()
        context['reject_form'] = RejectProjectForm()
        return context
    
    def post(self, request, *args, **kwargs):
        project_id = request.POST.get('project_id')
        project = Project.objects.get(id=project_id)
        if 'accept' in request.POST:
            form = AcceptProjectForm(request.POST)
            if form.is_valid():
                project.set_status('accepted')  

        if 'reject' in request.POST:
            form = RejectProjectForm(request.POST)
            if form.is_valid():
                project.set_status('rejected')
                comment = form.cleaned_data['comment']
                project.addRejectionComment(comment)

        return redirect('administrator')


    def test_func(self):
        return self.request.user.groups.filter(name='administrator').exists()