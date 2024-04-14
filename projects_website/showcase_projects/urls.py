from django.urls import path

from .views import (
    ProjectListView,
    ProjectDetailView,
    ProjectCustomerListView,
    MotivationLetterDownload,
)

from .viewsAdministrator import (
    AdministratorOrderAcceptanceView,
    AdministratorProjectCreateView,
    AdministratorOrderDeleteView
)

from .viewsCustomer import (
    OrderCreateView,
    OrderUpdateView,
    OrderDeleteView,
    CustomerOrder,
)

from .models import Project



urlpatterns = [
	path('', ProjectListView.as_view(model=Project), name='home'),
    # path('user/<str:username>/', ProjectCustomerListView.as_view(), name='project-user'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('downloadLetter/<int:letter_id>/', MotivationLetterDownload.as_view(), name='downloadLetter'),
    #customer
    path('order/my', CustomerOrder.as_view(), name='order-my'),
    path('order/new/', OrderCreateView.as_view(), name='order-create'),
    path('order/<int:pk>/update/', OrderUpdateView.as_view(), name='order-update'),
    path('order/<int:pk>/delete/', OrderDeleteView.as_view(), name='order-delete'),
    #administrator
    path('administrator/', AdministratorOrderAcceptanceView.as_view(), name='administrator'),
    path('project/new/<int:pk>/', AdministratorProjectCreateView.as_view(), name='project-create'),
    path('administrator/order/<int:pk>/delete/', AdministratorOrderDeleteView.as_view(), name='administrator-order-delete'),
]