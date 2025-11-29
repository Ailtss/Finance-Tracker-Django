# 📌 Finance Project – Controle Financeiro Pessoal

Aplicação web desenvolvida em **Django** para gerenciar lançamentos financeiros, categorias e usuários.  
O sistema permite criar, listar e organizar transações de forma simples, com suporte a HTMX para interações rápidas sem recarregar a página.

---

## 🔧 Tecnologias Utilizadas

- **Python 3**
- **Django 4**
- **SQLite3**
- **HTMX**
- **Tailwind/DaisyUI (via CDN)**
- **django-allauth** (autenticação)
- **django-debug-toolbar**
- **widget-tweaks**
- **django-filters**

---

## 🚀 Funcionalidades

### ✔️ Usuários
- Autenticação com Django Allauth  
- Cadastro, login e logout  
- Usuário customizado (`tracker.User`)

### ✔️ Categorias
- Criar novas categorias  
- Listar categorias  
- Selecionar categoria ao criar lançamentos  

### ✔️ Lançamentos (Transações)
- Criar lançamentos (receitas/despesas)  
- Listar lançamentos com paginação  
- Filtros por nome, categoria, data, tipo  
- Interações dinâmicas usando HTMX (`hx-get`, `hx-post`)

### ✔️ Gráficos (Transações)
- Visualização de gráficos
- Barra e Pizza

---

### 🛠️ Pré-requisitos
- Python 3.12.10 (⚠️ Não usar Python 3.14 ou superior)
- Git
- (Opcional) Editor de código: VS Code, PyCharm, etc.

- Windows: Baixe o Python 3.12.10
. Durante a instalação, marque “Add Python to PATH”.
  
---

### 📥 Clonar o projeto
- git clone <URL_DO_SEU_REPOSITORIO>
- cd <NOME_DO_REPOSITORIO>

---

### 🐍 Criar e ativar o ambiente virtual

Windows:

python -m venv venv
.\venv\Scripts\activate

Linux/macOS:

python3 -m venv venv
source venv/bin/activate

Sempre ative o ambiente virtual antes de instalar pacotes ou rodar o projeto.

---

### ⚡ Atualizar pip e setuptools

pip install --upgrade pip
pip install "setuptools<81"
Evita erros com pkg_resources deprecated

---

### 📦 Instalar dependências

pip install -r requirements.txt

---

### 🗄️ Configurar banco de dados

python manage.py migrate
python manage.py createsuperuser

Crie um superusuário para acessar o admin.

---

### 🌐 Rodar o servidor

python manage.py runserver

Acesse no navegador:

http://127.0.0.1:8000/

---

### ✨ Dicas úteis

Sempre use Python 3.12.10.

Certifique-se de que o ambiente virtual está ativo.

Se precisar instalar pacotes extras:

pip install <pacote>
pip freeze > requirements.txt

Avisos sobre pkg_resources podem ser ignorados.

Para erros de módulo não encontrado, verifique se o pacote está no requirements.txt e se foi instalado no ambiente virtual correto.

---


## 📄 License
Este projeto é apenas para fins acadêmicos.
