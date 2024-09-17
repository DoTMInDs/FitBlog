from django.urls import path # type: ignore
from . import views 
# from django.contrib.auth import views as auth_view

urlpatterns = [
    # path('', auth_view.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('', views.login_user, name='login'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('reset_password/', views.reset_password, name='reset-password'),
    path('logout_user/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('user_dashboard/', views.user_dashboard, name='user-dashboard'),
    path('user_dashboard_edit/<int:pk>/', views.user_dashboard_edit, name='user-dashboard-edit'),
    path('user_post_delete/<int:pk>/', views.user_post_delete, name='user-post-delete'),

]
