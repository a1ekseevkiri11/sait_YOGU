from django.urls import path

from .views import (
    ProjectListView,
    ProjectDetailView,
    ProjectCustomerListView,
    MotivationLetterDownload,
)

from .viewsAdministrator import (
    AdministratorProjectsAcceptanceView,
)

from .viewsCustomer import (
    OrderCreateView,
    OrderUpdateView,
    OrderDeleteView,
)

from .models import Project



urlpatterns = [
	path('', ProjectListView.as_view(model=Project), name='home'),
    # path('user/<str:username>/', ProjectCustomerListView.as_view(), name='project-user'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('downloadLetter/<int:letter_id>/', MotivationLetterDownload.as_view(), name='downloadLetter'),
    #customer
    path('order/new/', OrderCreateView.as_view(), name='order-create'),
    path('order/<int:pk>/update/', OrderUpdateView.as_view(), name='order-update'),
    path('order/<int:pk>/delete/', OrderDeleteView.as_view(), name='order-delete'),
    #administrator
    path('administrator/', AdministratorProjectsAcceptanceView.as_view(), name='administrator'),
]