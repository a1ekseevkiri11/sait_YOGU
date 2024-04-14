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
    CreateView,
    UpdateView,
    DeleteView,
    ListView
)

from .models import (
    Order, 
    Customer
)

from .formsCustomer import (
    OrderForm,
)

from .permission import (
    canDo
)


class CustomerOrder(ListView, UserPassesTestMixin):
    model = Order
    template_name = 'showcase_projects/customer_order.html'
    context_object_name = 'orders'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['showButtonCreateProject'] = canDo(self.request.user, 'add_order')
        return context
    
    def get_queryset(self):
        user = get_object_or_404(Customer, user__username=self.request.user.username)
        return Order.objects.filter(customer=user)
    
    def test_func(self):
        return self.request.user.groups.filter(name='customer').exists()



class OrderCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('order-my')

    def form_valid(self, form):
        form.instance.customer = self.request.user.customer
        return super().form_valid(form)
    
    def test_func(self):
        return canDo(self.request.user, 'add_order')



class OrderUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('order-my')

    def form_valid(self, form):
        form.instance.customer = self.request.user.customer
        form.save()
        order = self.get_object()
        order.set_status('processing')
        return redirect(self.success_url)

    def test_func(self):
        order = self.get_object()
        return self.request.user.customer == order.customer
    
    


class OrderDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Order
    success_url = reverse_lazy('order-my')

    def test_func(self):
        order = self.get_object()
        return self.request.user.customer == order.customer