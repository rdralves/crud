# CRUD de Usuários com Flask e SQLAlchemy

## Descrição
Este é um projeto simples de CRUD (Create, Read, Update, Delete) de usuários utilizando Flask e SQLAlchemy. O sistema permite cadastrar, listar, editar e excluir usuários armazenados em um banco de dados SQLite.

## Tecnologias Utilizadas
- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- Werkzeug (para hashing de senhas)

## Estrutura do Projeto
```
/
|-- models/
|   |-- user.py  # Modelo de dados do usuário
|
|-- routes/
|   |-- user_routes.py  # Rotas para gerenciamento de usuários
|
|-- templates/
|   |-- users.html  # Lista de usuários
|   |-- new_user.html  # Formulário para adicionar novo usuário
|   |-- edit_user.html  # Formulário para editar usuário
|
|-- app.py  # Arquivo principal para iniciar a aplicação
|-- site.db  # Banco de dados SQLite (gerado automaticamente)
```

## Instalação e Execução

### 1. Clonar o Repositório
```sh
git clone https://github.com/rdralves/crud

```

### 2. Criar e Ativar um Ambiente Virtual (Opcional, mas Recomendado)
```sh
python -m venv venv
# Ativar no Windows:
venv\Scripts\activate
# Ativar no Linux/macOS:
source venv/bin/activate
```

### 3. Instalar Dependências
```sh
pip install flask flask-sqlalchemy werkzeug
```

### 4. Executar a Aplicação
```sh
python app.py
```

A aplicação estará disponível em: `http://127.0.0.1:5000/`

## Como Usar

### Criar um Novo Usuário
1. Acesse `http://127.0.0.1:5000/users/new`
2. Preencha o formulário e clique em "Salvar"

### Listar Usuários
1. Acesse `http://127.0.0.1:5000/`

### Editar um Usuário
1. Na lista de usuários, clique em "Editar"
2. Atualize os dados e clique em "Salvar"

### Excluir um Usuário
1. Na lista de usuários, clique em "Excluir"
2. O usuário será removido do banco de dados



