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

## 📄 License
Este projeto é apenas para fins acadêmicos.
