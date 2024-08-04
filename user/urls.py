from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    # path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    # path("login/", views.login, name="login"),
    # path("logout/", views.logout, name="logout"),
]
