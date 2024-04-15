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
    AdministratorOrderDeleteView,
)

from .viewsCustomer import (
    OrderCreateView,
    OrderUpdateView,
    OrderDeleteView,
    CustomerOrder,
)

from .viewsLecturer import (
    LecturerProject,
    LecturerMotivationLetter
)

from .viewsStudent import (
    projectMy,
    StudentMotivationLetter,
)

from .models import Project



urlpatterns = [
	path('', ProjectListView.as_view(model=Project), name='home'),
    # path('user/<str:username>/', ProjectCustomerListView.as_view(), name='project-user'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('downloadLetter/<int:letter_id>/', MotivationLetterDownload.as_view(), name='downloadLetter'),
    #lecturer
    path('project/my_lead/', LecturerProject.as_view(), name='project-my-lead'),
    #student
    path('project/my/', projectMy, name='project-my'),
    path('motivationLetter/my/', StudentMotivationLetter.as_view(), name='motivation-letter-my'),
    #customer
    path('order/my', CustomerOrder.as_view(), name='order-my'),
    path('order/new/', OrderCreateView.as_view(), name='order-create'),
    path('order/<int:pk>/update/', OrderUpdateView.as_view(), name='order-update'),
    path('order/<int:pk>/delete/', OrderDeleteView.as_view(), name='order-delete'),
    #administrator
    path('administrator/', AdministratorOrderAcceptanceView.as_view(), name='administrator'),
    path('project/new/<int:pk>/', AdministratorProjectCreateView.as_view(), name='project-create'),
    path('project/<int:pk>/delete/', AdministratorProjectCreateView.as_view(), name='project-delete'),
    path('administrator/order/<int:pk>/delete/', AdministratorOrderDeleteView.as_view(), name='administrator-order-delete'),
]