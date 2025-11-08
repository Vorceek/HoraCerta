from django.contrib import admin
from django.urls import path

from apps.auth_app.views import AuthView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AuthView.as_view(), name='auth'),
]

