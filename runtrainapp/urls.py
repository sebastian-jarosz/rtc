from django.contrib import admin
from django.urls import path, include

from runtrainapp import views

urlpatterns = [
    path('', views.index, name="index"),
    path('admin/', admin.site.urls),
    path('admin/parse', views.parse_responses, name='admin parse responses'),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', views.profile, name="account_profile"),
    path('training/', views.list_all_trainings, name="all trainings"),
    path('training/<int:training_id>', views.training, name="training"),
    path('training/user/', views.list_all_user_trainings, name="all user trainings"),
    path('training/running/', views.list_all_running_trainings, name="all running trainings"),
    path('training/running/user/', views.list_all_user_running_trainings, name="all user running trainings")
]

