from django.urls import path
from .views import *
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('emp/', emp_view),
    path('addemp/', emp_add),
    path('update/<int:id>/', emp_update),
    path('delete/<int:id>/', emp_delete),
    path("login/", auth_view.LoginView.as_view(template_name="app/login.html")),
    path("logout/", auth_view.LogoutView.as_view(template_name="app/logout.html")),

]
