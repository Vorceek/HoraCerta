from django.contrib import admin
from django.urls import path, include

from apps.auth_app.views import AuthView

urlpatterns = [
    path('admin/', admin.site.urls),

    # login (mantém)
    path('accounts/login/', AuthView.as_view(), name='auth'),

    # inclui urls do auth_app (pra existir pos-login/)
    path('accounts/', include('apps.auth_app.urls')),

    # landing pública
    path('', include('apps.home_app.urls')),

    # área do sistema (cliente + barbeiro)
    path('system/', include('apps.system_app.urls')),
]
