from datetime import date
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test

from .models import Agendamento

def is_barbeiro(user):
    return user.is_authenticated and hasattr(user, "perfil_barbeiro")

@login_required
@user_passes_test(is_barbeiro)
def dashboard_barbeiro(request):
    barbeiro = request.user.perfil_barbeiro
    hoje = date.today()

    ag_hoje = Agendamento.objects.filter(barbeiro=barbeiro, data=hoje).order_by("hora")
    pendentes = ag_hoje.filter(status="PENDENTE").count()
    confirmados = ag_hoje.filter(status="CONFIRMADO").count()

    proximos = Agendamento.objects.filter(
        barbeiro=barbeiro,
        data__gte=hoje
    ).exclude(status="CANCELADO").order_by("data", "hora")[:5]

    return render(request, "from_app/system_app/barbeiro/dashboard_barbeiro.html", {
        "ag_hoje": ag_hoje,
        "pendentes": pendentes,
        "confirmados": confirmados,
        "proximos": proximos,
        "hoje": hoje,
    })


@login_required
@user_passes_test(is_barbeiro)
def agenda_barbeiro(request):
    barbeiro = request.user.perfil_barbeiro

    q_status = request.GET.get("status", "")
    q_data = request.GET.get("data", "")

    qs = Agendamento.objects.filter(barbeiro=barbeiro)

    if q_status:
        qs = qs.filter(status=q_status)

    if q_data:
        qs = qs.filter(data=q_data)

    futuros = qs.filter(data__gte=date.today()).order_by("data", "hora")
    passados = qs.filter(data__lt=date.today()).order_by("-data", "-hora")[:50]

    return render(request, "from_app/system_app/barbeiro/agenda_barbeiro.html", {
        "futuros": futuros,
        "passados": passados,
        "q_status": q_status,
        "q_data": q_data,
    })


@login_required
@user_passes_test(is_barbeiro)
def detalhe_agendamento_barbeiro(request, pk):
    barbeiro = request.user.perfil_barbeiro
    ag = get_object_or_404(Agendamento, pk=pk, barbeiro=barbeiro)

    return render(request, "from_app/system_app/barbeiro/detalhe_agendamento_barbeiro.html", {
        "agendamento": ag
    })


@login_required
@user_passes_test(is_barbeiro)
def alterar_status_agendamento(request, pk, status):
    barbeiro = request.user.perfil_barbeiro
    ag = get_object_or_404(Agendamento, pk=pk, barbeiro=barbeiro)

    status_validos = ["PENDENTE", "CONFIRMADO", "CONCLUIDO", "CANCELADO"]
    if status not in status_validos:
        messages.error(request, "Status inválido.")
        return redirect("from_app/system_app/barbeiro/detalhe_agendamento_barbeiro", pk=pk)

    ag.status = status
    ag.save()

    messages.success(request, f"Agendamento atualizado para {ag.get_status_display()}.")
    return redirect("from_app/system_app/barbeiro/detalhe_agendamento_barbeiro", pk=pk)
