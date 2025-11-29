---

# 📌 Finance Project – Controle Financeiro Pessoal

Aplicação web desenvolvida em **Django** para gerenciar lançamentos financeiros, categorias e usuários.
O sistema permite criar, listar e organizar transações de forma simples, com suporte a **HTMX** para interações rápidas sem recarregar a página.

---

## 🔧 Tecnologias Utilizadas

* **Python 3**
* **Django 4**
* **SQLite3**
* **HTMX**
* **Tailwind/DaisyUI (via CDN)**
* **django-allauth** (autenticação)
* **django-debug-toolbar**
* **widget-tweaks**
* **django-filters**

---

## 🚀 Funcionalidades

### ✔️ Usuários

* Autenticação com Django Allauth
* Cadastro, login e logout
* Usuário customizado (`tracker.User`)

### ✔️ Categorias

* Criar e listar categorias
* Seleção de categoria ao criar lançamentos

### ✔️ Lançamentos (Transações)

* Criar receitas e despesas
* Listar lançamentos com paginação
* Filtrar por nome, categoria, data e tipo
* Interações dinâmicas com **HTMX** (`hx-get`, `hx-post`)

### ✔️ Gráficos

* Gráfico de barras
* Gráfico de pizza

---

## 🛠️ Pré-requisitos

* **Python 3.12.10**
  ⚠️ *Evite Python 3.14 ou superior (causa erros com dependências).*
* **Git**
* (Opcional) **VS Code**, PyCharm, etc.

### 🔽 Windows

Baixe Python 3.12.10

> Marque a opção **"Add Python to PATH"** durante a instalação.

---

## 📥 Clonar o projeto

```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd <NOME_DO_REPOSITORIO>
```

---

## 🐍 Criar e ativar o ambiente virtual

### **Windows**

```bash
python -m venv venv
.\venv\Scripts\activate
```

### **Linux/macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

> Sempre ative o ambiente virtual antes de instalar pacotes ou rodar o projeto.

---

## ⚡ Atualizar pip e setuptools

```bash
pip install --upgrade pip
pip install "setuptools<81"
```

> Isso evita erros relacionados ao `pkg_resources`.

---

## 📦 Instalar dependências

```bash
pip install -r requirements.txt
```

---

## 🗄️ Configurar banco de dados

```bash
python manage.py migrate
python manage.py createsuperuser
```

Crie um superusuário para acessar o painel administrativo.

---

## 🌐 Rodar o servidor

```bash
python manage.py runserver
```

Acesse no navegador:
👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## ✨ Dicas úteis

* Sempre use **Python 3.12.10**.
* Certifique-se de que o **ambiente virtual está ativo**.
* Para instalar novos pacotes:

```bash
pip install <pacote>
pip freeze > requirements.txt
```

* Avisos sobre `pkg_resources` podem ser ignorados.
* Se ocorrer *ModuleNotFoundError*, confirme se:

  * o pacote está instalado no ambiente virtual
  * ele existe no `requirements.txt`

---

## 📄 License

Este projeto é apenas para fins acadêmicos.

---
