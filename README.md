# daily-diet-app

Aplicação simples em Flask para registrar refeições e indicar se fazem parte da dieta.

**Status:** Protótipo — rotas REST básicas para criar, listar, atualizar e remover refeições.

**Tecnologias:**
- Python 3
- Flask
- Flask-SQLAlchemy

**Sumário**
- [Instalação](#instalação)
- [Como executar](#como-executar)
- [API / Endpoints](#api--endpoints)
- [Modelo de dados](#modelo-de-dados)
- [Estrutura do projeto](#estrutura-do-projeto)
- [Contribuição](#contribuição)

## Instalação

1. Crie e ative um ambiente virtual (recomendado):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Instale dependências:

```bash
pip install -r requirements.txt
```

> Dependências estão listadas em `requirements.txt` (Flask, Flask-SQLAlchemy, etc.).

## Como executar

Você pode rodar diretamente com Python:

```bash
python app.py
```

Ou usar o `flask` (opcional):

```bash
export FLASK_APP=app.py
flask run
```

Por padrão o servidor roda em `http://127.0.0.1:5000`.

Observação sobre o banco de dados: o projeto usa SQLite (`daily_diet.db`). Se for necessário criar o arquivo e as tabelas, execute um pequeno script ou utilize um shell Flask para inicializar o banco:

```py
from app import app
from database import db

with app.app_context():
		db.create_all()
```

## API / Endpoints

Todas as rotas retornam/aceitam JSON.

- `POST /meals` — Adiciona nova refeição
	- Body (JSON): `{ "name": "Almoço", "description": "Arroz e feijão", "diet": true }`
	- Resposta: `201 Created`

- `GET /meals` — Retorna lista de todas as refeições

- `GET /meals/<meal_id>` — Retorna dados da refeição com id

- `PUT /meals/<meal_id>` — Atualiza campos da refeição (name, description, diet)

- `DELETE /meals/<meal_id>` — Remove a refeição

Exemplo com `curl`:

```bash
curl -X POST http://127.0.0.1:5000/meals \
	-H "Content-Type: application/json" \
	-d '{"name":"Jantar","description":"Salada","diet":true}'
```

## Modelo de dados

Implementado em `models/meal.py` — `Meal` possui os campos:

- `id` (Integer, PK)
- `name` (String, obrigatória)
- `description` (String, opcional)
- `diet` (Boolean, indica se a refeição faz parte da dieta)
- `insert_timestamp` (DateTime, data de inserção)

O método `to_dict()` no modelo converte a instância para JSON serializável.

## Estrutura do projeto

- `app.py` — Entrypoint da aplicação e definição das rotas
- `database.py` — Inicialização do `SQLAlchemy` (`db`)
- `models/meal.py` — Modelo `Meal` e serialização
- `requirements.txt` — Dependências do projeto
