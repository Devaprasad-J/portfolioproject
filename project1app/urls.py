from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_view, name='profile'),  # Ensure there's a home view
    path('profile/', views.profile_view, name='profile'),
    path('portfolio/', views.portfolio_view, name='portfolio'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('portfolio/add_project/', views.add_project, name='add_project'),
    path('portfolio/add_work_experience/', views.add_work_experience, name='add_work_experience'),
    path('portfolio/add_education/', views.add_education, name='add_education'),
    path('portfolio/add_certification/', views.add_certification, name='add_certification'),
    path('portfolio/delete/<int:pk>/', views.delete_project, name='delete_project'),
    path('portfolio/update_project/<int:pk>/', views.update_project, name='update_project'),
    path('delete_profile/', views.delete_profile, name='delete_profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
