# app_barbearia/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.db.models import Q
from django.core.paginator import Paginator

from .models import Agendamento, Barbearia, Barbeiro, Servico


@login_required
def home_cliente(request):
    agora = timezone.localtime()
    hoje = agora.date()

    # ----------- parte que você já tinha -----------
    proximo_horario = (
        Agendamento.objects
        .filter(cliente=request.user, data__gte=hoje)
        .exclude(status='CANCELADO')
        .order_by('data', 'hora')
        .first()
    )

    ultimos_atendimentos = (
        Agendamento.objects
        .filter(cliente=request.user, status='CONCLUIDO')
        .order_by('-data', '-hora')[:4]
    )

    # ----------- NOVO: busca + filtros nas barbearias -----------
    q = request.GET.get("q", "").strip()
    ordem = request.GET.get("ordem", "").strip()

    barbearias_qs = Barbearia.objects.all()

    if q:
        barbearias_qs = barbearias_qs.filter(
            Q(nome__icontains=q) |
            Q(endereco__icontains=q)
            # se tiver bairro/cidade, pode incluir:
            # | Q(bairro__icontains=q)
            # | Q(cidade__icontains=q)
        )

    if ordem == "nota":
        barbearias_qs = barbearias_qs.order_by("-nota", "nome")
    elif ordem == "recentes":
        barbearias_qs = barbearias_qs.order_by("-created_at")  # ajuste se seu campo tiver outro nome
    else:
        barbearias_qs = barbearias_qs.order_by("nome")

    paginator = Paginator(barbearias_qs, 8)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    contexto = {
        # seus dados
        "proximo_horario": proximo_horario,
        "ultimos_atendimentos": ultimos_atendimentos,

        # barbearias paginadas
        "q": q,
        "ordem": ordem,
        "page_obj": page_obj,
        "barbearias": page_obj.object_list,
        "is_paginated": page_obj.has_other_pages(),

        "year": agora.year,
    }

    return render(request, "from_app/system_app/home_cliente.html", contexto)


@login_required
def agendar_horario(request):
    barbeiros = Barbeiro.objects.all().order_by('nome')
    servicos = Servico.objects.all().order_by('nome')
    agora = timezone.localtime()

    if request.method == 'POST':
        barbeiro_id = request.POST.get('barbeiro')
        servico_id = request.POST.get('servico')
        data = request.POST.get('data')
        hora = request.POST.get('hora')

        if barbeiro_id and servico_id and data and hora:
            barbeiro = get_object_or_404(Barbeiro, pk=barbeiro_id)
            servico = get_object_or_404(Servico, pk=servico_id)

            Agendamento.objects.create(
                cliente=request.user,
                barbeiro=barbeiro,
                servico=servico,
                data=data,
                hora=hora,
                status='PENDENTE',
            )
            return redirect('meus_horarios')

    contexto = {
        'barbeiros': barbeiros,
        'servicos': servicos,
        'year': agora.year,
        'modo_remarcar': False,
    }
    return render(request, 'from_app/system_app/agendar_horario.html', contexto)


@login_required
def meus_horarios(request):
    agora = timezone.localtime()
    hoje = agora.date()

    futuros = (
        Agendamento.objects
        .filter(cliente=request.user, data__gte=hoje)
        .exclude(status='CANCELADO')
        .order_by('data', 'hora')
    )

    passados = (
        Agendamento.objects
        .filter(cliente=request.user, data__lt=hoje)
        .exclude(status='CANCELADO')
        .order_by('-data', '-hora')
    )

    contexto = {
        'futuros': futuros,
        'passados': passados,
        'year': agora.year,
    }
    return render(request, 'from_app/system_app/meus_horarios.html', contexto)


@login_required
def lista_barbeiros(request):
    barbeiros = Barbeiro.objects.all().order_by('nome')
    agora = timezone.localtime()
    return render(request, 'from_app/system_app/lista_barbeiros.html', {
        'barbeiros': barbeiros,
        'year': agora.year,
    })

@login_required
def lista_servicos(request):
    servicos = Servico.objects.all().order_by('nome')
    agora = timezone.localtime()
    return render(request, 'from_app/system_app/lista_servicos.html', {
        'servicos': servicos,
        'year': agora.year,
    })


@login_required
def remarcar_horario(request, agendamento_id):
    agendamento = get_object_or_404(
        Agendamento,
        pk=agendamento_id,
        cliente=request.user,
    )
    barbeiros = Barbeiro.objects.all().order_by('nome')
    servicos = Servico.objects.all().order_by('nome')
    agora = timezone.localtime()

    if request.method == 'POST':
        barbeiro_id = request.POST.get('barbeiro')
        servico_id = request.POST.get('servico')
        data = request.POST.get('data')
        hora = request.POST.get('hora')

        if barbeiro_id and servico_id and data and hora:
            agendamento.barbeiro = get_object_or_404(Barbeiro, pk=barbeiro_id)
            agendamento.servico = get_object_or_404(Servico, pk=servico_id)
            agendamento.data = data
            agendamento.hora = hora
            agendamento.status = 'PENDENTE'
            agendamento.save()
            return redirect('meus_horarios')

    contexto = {
        'barbeiros': barbeiros,
        'servicos': servicos,
        'agendamento': agendamento,
        'modo_remarcar': True,
        'year': agora.year,
    }
    return render(request, 'from_app/system_app/agendar_horario.html', contexto)


@login_required
def detalhe_atendimento(request, agendamento_id):
    agendamento = get_object_or_404(
        Agendamento,
        pk=agendamento_id,
        cliente=request.user,
    )
    agora = timezone.localtime()
    return render(request, 'from_app/system_app/detalhe_atendimento.html', {
        'agendamento': agendamento,
        'year': agora.year,
    })
