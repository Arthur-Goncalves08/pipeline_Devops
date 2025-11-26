# 🚀 API Flask Protegida com JWT e CI/CD via GitHub Actions

Este projeto implementa uma **API RESTful simples** utilizando o framework **Flask** do Python, com proteção de rotas através de **JWT (JSON Web Tokens)**. A aplicação é totalmente conteinerizada com **Docker** e inclui uma pipeline de **Integração Contínua (CI)** robusta, definida com **GitHub Actions**..

## ✨ Funcionalidades da API

A API oferece as seguintes rotas:

| Rota | Método | Descrição | Requer JWT |
| :--- | :----: | :--- | :---: |
| `/` | `GET` | Retorna um status simples de que a API está rodando. | Não |
| `/items` | `GET` | Retorna uma lista estática de itens. | Não |
| `/login` | `POST` | Gera e retorna um **Access Token JWT**. | Não |
| `/protected` | `GET` | Rota protegida. Requer o **Access Token** no cabeçalho `Authorization: Bearer <token>`. | Sim |

A documentação interativa da API (Swagger UI) está disponível em `/swagger`.

## 🛠️ Tecnologias Utilizadas

* **Python 3.9**
* **Flask**: Micro-framework web para Python.
* **Flask-JWT-Extended**: Extensão para autenticação JWT.
* **Docker**: Para conteinerização e padronização do ambiente.
* **Docker Compose**: Para orquestração da API e ambiente de testes.
* **GitHub Actions**: Para a pipeline de CI (Build e Teste).
* **`unittest`**: Framework de testes embutido do Python.

## 📦 Estrutura do Projeto

| Arquivo/Diretório | Descrição |
| :--- | :--- |
| `app.py` | Código principal da aplicação Flask, definindo rotas e configurando JWT/Swagger. |
| `requirements.txt` | Lista de dependências Python necessárias (`Flask`, `Flask-JWT-Extended`, etc.). |
| `Dockerfile` | Define como a imagem Docker da API deve ser construída. |
| `docker-compose.yml` | Configuração para rodar a aplicação localmente e para executar os testes em ambiente isolado. |
| `test_app.py` | Contém os **testes unitários** para verificar a integridade das rotas e a segurança JWT. |
| `ci.yml` | Define o **GitHub Actions Workflow** para Build e Teste contínuos. |
| `README.md` | Este arquivo de documentação. |

## ⚙️ Configuração e Execução Local (Docker)

Para executar a API localmente, você precisa ter o **Docker** e o **Docker Compose** instalados.
.
### 1. Construir e Iniciar os Serviços

Use o Docker Compose para construir a imagem e iniciar o container da API.

```bash
docker-compose up --build -d