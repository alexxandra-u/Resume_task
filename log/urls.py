from django.urls import path
from . import views

urlpatterns = [
    path('sign_up', views.signup_view, name='sign_up'),
    path('log_in', views.login_view, name='log_in'),
    path('log_out', views.logout_view, name='log_out')
]