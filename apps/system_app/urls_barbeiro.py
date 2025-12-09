from django.urls import path
from . import views_barbeiro as v

urlpatterns = [
    path("barbeiro/", v.dashboard_barbeiro, name="dashboard_barbeiro"),
    path("barbeiro/agenda/", v.agenda_barbeiro, name="agenda_barbeiro"),
    path("barbeiro/agendamento/<int:pk>/", v.detalhe_agendamento_barbeiro, name="detalhe_agendamento_barbeiro"),
    path("barbeiro/agendamento/<int:pk>/status/<str:status>/", v.alterar_status_agendamento, name="alterar_status_agendamento"),
]
