from django.urls import reverse_lazy
from django.shortcuts import (
    redirect, 
)

from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin
)

from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView
)

from .models import (
    Project, 
    Order
)

from .formsCustomer import (
    OrderForm,
)

from .formsAdministrator import (
    ProjectForm
)


class AdministratorOrderAcceptanceView(ListView, LoginRequiredMixin, UserPassesTestMixin):
    model = Order
    template_name = 'showcase_projects/administrator/acceptanceProjects.html'
    context_object_name = 'orders'
    paginate_by = 6
    
    def get_queryset(self):
       return Order.objects.filter(status='processing')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['administrator'] = True
        return context

    def test_func(self):
        return self.request.user.groups.filter(name='administrator').exists()
    

class AdministratorProjectCreateView(UpdateView, LoginRequiredMixin):
    model = Order
    form_class = OrderForm
    template_name = 'showcase_projects/administrator/project_form.html'
    success_url = reverse_lazy('administrator')

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = self.get_object()
        project_exists = Project.objects.filter(order=order).exists()
        form_project = ProjectForm()
        if project_exists:
            project = Project.objects.get(order=order)
            form_project = ProjectForm(instance=project)
            
        context['form_project'] = form_project
        return context
    
    def form_valid(self, form):
        form.save()
        order = self.get_object()
        order.set_status('accepted')
        form_project = ProjectForm(self.request.POST)
        if form_project.is_valid():
            project_exists = Project.objects.filter(order=order).exists()
            if project_exists:
                project = Project.objects.get(order=order)

                project.place = form_project.cleaned_data['place']
                project.lecturer = form_project.cleaned_data['lecturer']
                project.customer_type = form_project.cleaned_data['customer_type']
                project.save()
            else:
                project = form_project.save(commit=False)
                project.order = order
                project.save()
            
            return redirect(self.success_url)
        else:
            return self.form_invalid(form)
    
    def test_func(self):
        return self.request.user.groups.filter(name='administrator').exists()
    


class AdministratorOrderDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Order
    success_url = reverse_lazy('administrator')

    def test_func(self):
        if self.request.user.groups.filter(name='administrator').exists():
            return True


