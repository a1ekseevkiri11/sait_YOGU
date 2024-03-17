from django.urls import reverse_lazy

from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin
)

from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView
)

from .models import (
    Project, 
)

from .pernission import (
    canAddProject,
)

from django.shortcuts import (
    redirect, 
)


class ProjectCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Project
    fields =  ['title', 'place']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.customer = self.request.user.profile
        return super().form_valid(form)
    
    def test_func(self):
        return canAddProject(self.request.user)



class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    fields = ['title', 'place']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.customer = self.request.user.profile
        form.save()
        post = self.get_object()
        post.set_status('processing')
        return redirect(self.success_url)

    def test_func(self):
        post = self.get_object()
        return self.request.user.profile == post.customer
    
    


class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    success_url = reverse_lazy('home')

    def test_func(self):
        post = self.get_object()
        return self.request.user.profile == post.customer