# Magic Deckbuilder API

## Rotas

| Método | Rota | Descrição |
|--------|-------|------------|
| `GET` | `/cards/:card_name` | Obtém um deck pelo nome |
| `POST` | `/cards` | Busca todos os cards em uma lista |
| `GET` | `/autocomplete/:card_name` | Obtém 10 possiveis cartas |
| `GET` | `/commanders` | Obtém top 100 comandantes |


## Estrutura Visual das Rotas

```
/
├── cards
│   ├── (GET) - Obtém um deck pelo nome
│   └── (POST) - Busca todos os cards em uma lista
├── autocomplete (GET) - Obtém 10 possíveis cartas
└── commanders (GET) - Obtém top 100 comandantes
```

## Tecnologias Utilizadas

O backend deste projeto foi desenvolvido com foco em simplicidade, desempenho e facilidade de manutenção.  
A stack principal inclui:

| Tecnologia | Função |
|-------------|--------|
| **Python** | Linguagem principal utilizada no backend. Escolhida pela clareza e pelo forte ecossistema de bibliotecas. |
| **FastAPI** | Framework web assíncrono para criação de APIs REST de alta performance e tipadas. |
| **Postgres** | Banco de dados relacional. |

## Requisitos para Execução

Antes de executar o projeto, verifique se o ambiente atende aos seguintes requisitos mínimos:

| Tipo | Requisito | Descrição |
|------|------------|-----------|
| **Sistema Operacional** | Windows / Linux / macOS | Compatível com qualquer sistema que suporte Python 3.10+ |
| **Versão do Python** | ≥ 3.10 | FastAPI recomenda versões mais recentes do Python |
| **Banco de Dados** | Postgres | URL de um banco valido |
| **Gerenciador de Pacotes** | pip ou uv | Usado para instalar as dependências do projeto |

### Dependências Principais

```bash
pip install fastapi uvicorn sqlalchemy pydantic
```

## Executando o Servidor

Após instalar as dependências, inicie o servidor FastAPI com o comando:

```bash
uvicorn app.main:app --reload
```

Por padrão, o servidor será iniciado em:

```
http://127.0.0.1:8000
```

A documentação interativa da API estará disponível em:

```
http://127.0.0.1:8000/docs
```

### Estrutura Recomendada de Pastas

```
.
├── app
│   ├── config.py
│   ├── database.py
│   ├── main.py
│   ├── models
│   │   └── card_model.py
│   ├── routes
│   │   ├── auth_routes.py
│   │   └── card_routes.py
│   ├── schemas
│   │   └── card_schema.py
│   ├── security
│   │   ├── __init__.py
│   │   ├── api_key_generator.py
│   │   └── auth.py
│   └── services
│       └── card_service.py
├── pyproject.toml
└── uv.lock
```

