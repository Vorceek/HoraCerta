from django.contrib import admin
from django.urls import path, include

from apps.auth_app.views import AuthView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', AuthView.as_view(), name='auth'),
    path('', include('apps.home_app.urls')),

    path('system/', include('apps.system_app.urls')),
]

