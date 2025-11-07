# HoraCerta

O projeto **HoraCerta** é um sistema web desenvolvido para otimizar o processo de agendamento de horários em salões de beleza, barbearias e estúdios de estética.  
O sistema busca oferecer uma solução tecnológica prática e acessível para microempreendedores, permitindo melhor organização, controle e comunicação entre profissionais e clientes.

---

## 1. Contextualização

Nos últimos anos, o setor da beleza tem se destacado no cenário econômico, com o aumento do número de salões, barbearias e estúdios de estética.  
Apesar desse crescimento, muitos microempreendedores ainda enfrentam dificuldades na organização de horários e controle de agendamentos, utilizando métodos manuais como agendas físicas ou aplicativos de mensagens.  

Esses métodos são propensos a erros, dificultam o controle de disponibilidade e prejudicam o atendimento.  
O **HoraCerta** surge como uma solução tecnológica voltada para facilitar o gerenciamento de agendas e permitir que clientes realizem seus agendamentos de forma autônoma, rápida e organizada.

---

## 2. Objetivo do Projeto

O objetivo do projeto é facilitar a gestão de agendamentos em salões e barbearias, proporcionando:

- Organização de horários e serviços;
- Autonomia para clientes realizarem agendamentos;
- Melhoria na comunicação entre profissional e cliente;
- Aumento da produtividade e eficiência no atendimento;
- Fortalecimento do microempreendedorismo local.

---

## 3. Requisitos Funcionais

| Código | Descrição |
|--------|------------|
| RF001 | O sistema deve permitir o cadastro de profissionais e dos serviços oferecidos. |
| RF002 | O sistema deve permitir o cadastro de clientes com informações básicas (nome, telefone, e-mail). |
| RF003 | O sistema deve possibilitar o agendamento de horários pelos clientes, com base na disponibilidade. |
| RF004 | O sistema deve permitir ao profissional visualizar, confirmar, reagendar ou cancelar atendimentos. |
| RF005 | O sistema deve enviar notificações automáticas de lembrete aos clientes sobre os horários agendados. |
| RF006 | O sistema deve exibir em tempo real os horários disponíveis e ocupados. |
| RF007 | O sistema deve possuir uma interface intuitiva, simples e adaptável a diferentes dispositivos (desktop e mobile). |

---

## 4. Requisitos Não Funcionais

| Código | Descrição |
|--------|------------|
| RNF001 | O sistema deve apresentar boa usabilidade, com navegação simples e linguagem clara. |
| RNF002 | O sistema deve carregar as páginas e atualizar as agendas de forma rápida. |
| RNF003 | O sistema deve ser acessível por meio de navegadores, sem necessidade de instalação. |
| RNF004 | O sistema deve garantir a segurança e confidencialidade das informações dos usuários. |
| RNF005 | O sistema deve ser desenvolvido de modo a permitir manutenção e futuras atualizações. |
| RNF006 | O sistema deve garantir confiabilidade, evitando perda de dados em caso de falhas. |

---

## 5. Protótipo

O protótipo proposto apresenta uma interface moderna e intuitiva, voltada para a praticidade de profissionais e clientes.

### 5.1 Tela Inicial
- Logotipo e nome do sistema: HoraCerta
- Menu de navegação: Início | Serviços | Agendamento | Contato
- Banner com o lema: “Agende seu horário de forma simples e rápida.”
- Botão de ação: “Agendar Agora”

### 5.2 Tela de Serviços
- Lista de serviços disponíveis (exemplo: corte masculino, coloração, hidratação, barba);
- Descrição de cada serviço com preço e duração estimada.

### 5.3 Tela de Agendamento
- Calendário interativo exibindo horários livres e ocupados;
- Campos para selecionar o profissional e o serviço desejado;
- Botão “Confirmar Agendamento”.

### 5.4 Painel do Profissional
- Visualização completa da agenda diária e semanal;
- Funções para confirmar, reagendar ou cancelar atendimentos;
- Opção para adicionar novos serviços e ajustar horários disponíveis.

---

## 6. Tecnologias Utilizadas

- Python 3.x  
- Django (framework principal)  
- HTML5 / CSS3 / JavaScript  
- SQLite (banco de dados local)  
- Bootstrap (para estilização responsiva)  
- django-environ (para gerenciamento de variáveis de ambiente)

---

## 7. Como Executar o Projeto

### 7.1 Clonar o repositório
```bash
git clone https://github.com/Vorceek/HoraCerta.git
cd HoraCerta
```

### 7.2 Criar e ativar o ambiente virtual
```bash
python -m venv venv
venv\Scripts\activate   # Windows
# ou
source venv/bin/activate  # Linux/Mac
```

### 7.3 Instalar dependências
```bash
pip install -r requirements.txt
```

### 7.4 Configurar variáveis de ambiente
```bash
SECRET_KEY=sua_chave_aqui
DEBUG=True
```

### 7.5 Executar migrações e iniciar o servidor
```bash
python manage.py migrate
python manage.py runserver
```

Acesse o projeto no navegador:
http://127.0.0.1:8000/

## 8. Considerações Finais

O projeto HoraCerta propõe uma solução eficiente para o gerenciamento de agendamentos em salões de beleza e barbearias, promovendo organização, economia de tempo e melhoria na experiência do cliente.
Além de contribuir com a gestão e profissionalização dos microempreendedores, o projeto reforça o papel da extensão universitária ao aplicar o conhecimento tecnológico em benefício da comunidade.

## 9. Autor
Desenvolvido por Vinicios Mensen
GitHub: https://github.com/Vorceek

## 10. Licença
Este projeto é de uso acadêmico e educativo.
Todos os direitos reservados © 2025.