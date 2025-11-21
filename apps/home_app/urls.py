from django.urls import path

from apps.home_app.views import LandingPageView


urlpatterns = [
    path('', LandingPageView.as_view(), name='landing'),
]