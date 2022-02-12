from django.contrib import admin
from django.urls import path, include

from runtrainapp import views

urlpatterns = [
    path('', views.index, name="index"),
    path('admin/', admin.site.urls),
    path('admin/form/management/', views.form_management, name='form management'),
    path('admin/form/responses/', views.form_responses, name='form responses'),
    path('admin/form/responses/<int:form_response_id>/', views.response, name='response'),
    path('admin/api/parse/', views.parse_responses, name='admin parse responses'),
    path('admin/api/read/', views.write_responses, name='admin write responses'),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', views.profile, name="account_profile"),
    path('training/', views.list_all_trainings, name="all trainings"),
    path('training/<int:training_id>', views.training, name="training"),
    path('training/user/', views.list_all_user_trainings, name="all user trainings"),
    path('training/running/', views.list_all_running_trainings, name="all running trainings"),
    path('training/running/user/', views.list_all_user_running_trainings, name="all user running trainings")
]

