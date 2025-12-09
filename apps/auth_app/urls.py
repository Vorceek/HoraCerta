from django.urls import path
from .views import redirect_after_login, logout_view

urlpatterns = [
    path("pos-login/", redirect_after_login, name="redirect_after_login"),
    path("logout/", logout_view, name="logout"),
]
