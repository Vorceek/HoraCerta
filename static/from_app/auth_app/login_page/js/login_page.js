// Seleciona elementos importantes
const authContainer = document.querySelector('.auth-container');
const loginForm = document.querySelector('.form-login');
const registerForm = document.querySelector('.form-register');

const goToRegisterBtn = document.getElementById('goToRegister');
const goToLoginBtn = document.getElementById('goToLogin');

// Troca para o formulário de registro
goToRegisterBtn.addEventListener('click', () => {
  loginForm.classList.remove('active');
  registerForm.classList.add('active');
  authContainer.classList.add('register-mode');
});

// Troca para o formulário de login
goToLoginBtn.addEventListener('click', () => {
  registerForm.classList.remove('active');
  loginForm.classList.add('active');
  authContainer.classList.remove('register-mode');
});

// Animação simples nos inputs ao focar (efeito de "pulso")
const inputs = document.querySelectorAll('.input-group input');

inputs.forEach((input) => {
  input.addEventListener('focus', () => {
    input.parentElement.classList.add('focused');
  });

  input.addEventListener('blur', () => {
    input.parentElement.classList.remove('focused');
  });
});

if (loginForm) {
  loginForm.addEventListener('submit', (e) => {
    loginForm.classList.add('sending');
    setTimeout(() => {
      loginForm.classList.remove('sending');
    }, 600);
  });
}

if (registerForm) {
  registerForm.addEventListener('submit', (e) => {
    registerForm.classList.add('sending');
    setTimeout(() => {
      registerForm.classList.remove('sending');
    }, 600);
  });
}
