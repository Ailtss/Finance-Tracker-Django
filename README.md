📌 Finance Project – Controle Financeiro Pessoal

Aplicação web desenvolvida em Django para gerenciar lançamentos financeiros, categorias e usuários. O sistema permite criar, listar e organizar transações de forma simples, com suporte a HTMX para interações rápidas sem recarregar a página.

🔧 Tecnologias Utilizadas

Python 3

Django 4

SQLite3

HTMX

Tailwind/DaisyUI (via CDN)

django-allauth (autenticação)

django-debug-toolbar

widget-tweaks

django-filters

🚀 Funcionalidades
✔️ Usuários

Autenticação com Django Allauth

Cadastro, login e logout

Usuário customizado (tracker.User)

✔️ Categorias

Criar novas categorias

Listar categorias

Selecionar categoria ao criar lançamentos

✔️ Lançamentos (Transações)

Criar lançamentos (receitas/despesas)

Listar lançamentos com paginação

Filtros por nome, categoria, data, tipo

Interações dinâmicas usando HTMX (hx-get, hx-post)

📁 Estrutura de Pastas
finance_project/
│
├── tracker/                # App principal
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── filters.py
│   └── templates/tracker/
│       ├── index.html
│       ├── transactions-list.html
│       ├── create-transaction.html
│       ├── categories-list.html
│       ├── category-form.html
│       └── partials/
│           └── transaction-form.html
│
├── finance_project/
│   ├── settings.py
│   ├── urls.py
│   └── templates/
│       └── base.html
│
└── static/                 # Arquivos estáticos

🛠️ Instalação e Execução
1) Clone o repositório
git clone https://github.com/SEU-USUARIO/seu-repositorio.git
cd seu-repositorio

2) Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3) Instale as dependências
pip install -r requirements.txt

4) Execute as migrações
python manage.py migrate

5) Rode o servidor
python manage.py runserver


Acesse em:
http://127.0.0.1:8000/

📝 Como usar

Crie sua conta ou faça login

Crie categorias

Adicione lançamentos

Veja a lista com filtros e paginação

📄 License

Este projeto é apenas para fins acadêmicos.

Se quiser, posso:

✅ adicionar badges (Python, Django, HTMX, etc.)
✅ colocar screenshots do projeto
✅ deixar mais profissional para o LinkedIn
✅ escrever uma seção “Sobre o Projeto” contando a motivação
