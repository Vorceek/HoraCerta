
from django.views.generic import ListView

from apps.system_app.models import Barbearia

class LandingPageView(ListView):
    model = Barbearia
    template_name = "from_app/home_app/home.html"
    context_object_name = "barbearias"
    ordering = ['-nota'] 
