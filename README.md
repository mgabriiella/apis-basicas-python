# APIs Básicas em Python

Este repositório contém exemplos de implementações básicas de APIs utilizando Python. O objetivo é demonstrar conceitos fundamentais de desenvolvimento de APIs, incluindo criação de rotas, manipulação de requisições e respostas, bem como integração com bancos de dados.

## Tecnologias Utilizadas

- **Python** (versão 3.x)
- **Flask** (ou FastAPI, dependendo da implementação)
- **SQLite** (ou outro banco de dados conforme necessidade)
- **Postman** (para testes de requisições)

## Como Executar

1. Clone o repositório:
   ```sh
   git clone https://github.com/mgabriiella/apis-basicas-python.git
   ```
2. Acesse o diretório do projeto:
   ```sh
   cd apis-basicas-python
   ```
3. Crie um ambiente virtual e ative-o:
   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   ```
4. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```
5. Execute a aplicação:
   ```sh
   python app.py
   ```
6. Acesse a API no navegador ou via Postman:
   ```
   http://localhost:5000
   ```

## Estrutura do Projeto

```
/apis-basicas-python
│-- app.py  # Arquivo principal da API
│-- requirements.txt  # Dependências do projeto
│-- README.md  # Documentação do projeto
│-- models.py  # Definição dos modelos de dados
│-- routes.py  # Definição das rotas da API
│-- database.db  # Banco de dados (se aplicável)
│-- tests/  # Testes unitários
```

## Endpoints

Exemplo de endpoints que podem estar incluídos:

- `GET /items` - Retorna uma lista de itens.
- `GET /items/{id}` - Retorna um item específico pelo ID.
- `POST /items` - Adiciona um novo item.
- `PUT /items/{id}` - Atualiza um item existente.
- `DELETE /items/{id}` - Remove um item.



