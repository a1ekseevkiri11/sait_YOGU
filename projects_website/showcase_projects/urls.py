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
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDeleteView,
)



urlpatterns = [
	path('', ProjectListView.as_view(), name='home'),
    path('user/<str:username>', ProjectCustomerListView.as_view(), name='project-user'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('downloadLetter/<int:letter_id>/', MotivationLetterDownload.as_view(), name='downloadLetter'),
    #customer
    path('project/new/', ProjectCreateView.as_view(), name='project-create'),
    path('post/<int:pk>/update/', ProjectUpdateView.as_view(), name='project-update'),
    path('post/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),
    #administrator
    path('administrator/', AdministratorProjectsAcceptanceView.as_view(), name='administrator'),
]