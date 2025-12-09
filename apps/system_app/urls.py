from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home_cliente, name='home_cliente'),

    path('agendar/', views.agendar_horario, name='agendar_horario'),
    path('meus-horarios/', views.meus_horarios, name='meus_horarios'),

    path('barbeiros/', views.lista_barbeiros, name='lista_barbeiros'),
    path("barbeiros-por-barbearia/", views.barbeiros_por_barbearia, name="barbeiros_por_barbearia"),
    path('servicos/', views.lista_servicos, name='lista_servicos'),

    path('remarcar/<int:agendamento_id>/', views.remarcar_horario, name='remarcar_horario'),
    path('atendimento/<int:agendamento_id>/', views.detalhe_atendimento, name='detalhe_atendimento'),

    path('', include('apps.system_app.urls_barbeiro')),
]
