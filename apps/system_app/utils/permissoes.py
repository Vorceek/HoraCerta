# from_app/system_app/utils/permissoes.py
def is_barbeiro(user):
    return user.is_authenticated and hasattr(user, "perfil_barbeiro")
