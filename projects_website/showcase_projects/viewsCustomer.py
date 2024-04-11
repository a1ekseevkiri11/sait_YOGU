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
    Order, 
)

from .permission import (
    canDo
)

from django.shortcuts import (
    redirect, 
)

from .formsCustomer import (
    OrderForm,
)



class OrderCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('profileCustomer')

    def form_valid(self, form):
        form.instance.customer = self.request.user.customer
        return super().form_valid(form)
    
    def test_func(self):
        return canDo(self.request.user, 'add_project')



class OrderUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('profileCustomer')

    def form_valid(self, form):
        form.instance.customer = self.request.user.customer
        form.save()
        post = self.get_object()
        post.set_status('processing')
        return redirect(self.success_url)

    def test_func(self):
        order = self.get_object()
        return self.request.user.customer == order.customer
    
    


class OrderDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Order
    success_url = reverse_lazy('profileCustomer')

    def test_func(self):
        order = self.get_object()
        return self.request.user.customer == order.customer