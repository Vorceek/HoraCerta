from django.views import View
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

class AuthView(View):
    template_name = 'from_app/auth_app/login_page.html'

    def get(self, request):
        # Só renderiza a tela
        return render(request, self.template_name)

    def post(self, request):
        form_type = request.POST.get('form_type')

        if form_type == 'login':
            return self.handle_login(request)
        elif form_type == 'register':
            return self.handle_register(request)
        else:
            messages.error(request, "Requisição inválida.")
            return redirect('auth')  # nome da url

    # --- Métodos auxiliares ---

    def handle_login(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Se você estiver usando username = email:
        try:
            user_obj = User.objects.get(email=email)
            username = user_obj.username
        except User.DoesNotExist:
            messages.error(request, "Usuário não encontrado.")
            return redirect('auth')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login realizado com sucesso!")
            return redirect('home_cliente')  # troque para sua rota pós-login
        else:
            messages.error(request, "E-mail ou senha inválidos.")
            return redirect('auth')

    def handle_register(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if password != password_confirm:
            messages.error(request, "As senhas não conferem.")
            return redirect('auth')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Já existe um usuário com esse e-mail.")
            return redirect('auth')

        username = email  # ou gera outro username, se quiser
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=name
        )

        messages.success(request, "Conta criada com sucesso! Você já pode fazer login.")
        return redirect('auth')

@login_required
def redirect_after_login(request):
    if hasattr(request.user, "perfil_barbeiro"):
        return redirect("dashboard_barbeiro")
    return redirect("redirect_after_login")

@login_required
def logout_view(request):
    logout(request)
    return redirect("landing")