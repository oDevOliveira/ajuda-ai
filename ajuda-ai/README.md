# Ajuda.ai

O **Ajuda.ai** é uma aplicação web desenvolvida em Python com Flask, voltada à publicação de pedidos de ajuda e à interação entre usuários por meio de uma rede social solidária.

## Funcionalidades

- Cadastro e autenticação de usuários.
- Gerenciamento de contas e perfis.
- Publicação de pedidos de ajuda.
- Comentários nas publicações.
- Armazenamento de senhas com hash.
- Banco de dados SQLite.
- Organização do projeto com Blueprints do Flask.

## Tecnologias utilizadas

- **Python** — linguagem principal.
- **Flask** — framework web.
- **Flask-SQLAlchemy** — integração com banco de dados.
- **Flask-Login** — gerenciamento de autenticação.
- **SQLite** — banco de dados.
- **HTML, CSS e JavaScript** — interface da aplicação.

## Estrutura do projeto

```text
ajuda-ai/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── principal/
│   ├── autenticacao/
│   ├── conta/
│   ├── templates/
│   └── static/
├── config.py
├── run.py
├── requirements.txt
└── README.md
```

*Observação: a estrutura acima é uma referência; ajuste os caminhos para corresponder aos arquivos reais do projeto.*

## Como executar localmente

**1. Clone o repositório**

```bash
git clone URL_DO_REPOSITORIO
cd ajuda-ai
```

**2. Instale as dependências**

```bash
pip install -r requirements.txt
```

**3. Configure a chave secreta**

Defina a variável de ambiente `SECRET_KEY` antes de iniciar a aplicação. Não compartilhe chaves secretas publicamente.

**4. Execute a aplicação**

```bash
python run.py
```

Acesse o endereço local exibido no terminal.

## Banco de dados

O projeto utiliza SQLite para armazenar os dados da aplicação. A criação e a inicialização do banco devem seguir a configuração definida no código.

## Objetivo

O Ajuda.ai busca oferecer um espaço digital para conectar pessoas, divulgar necessidades e facilitar a interação entre quem precisa de ajuda e quem deseja colaborar.

## Status

Projeto em desenvolvimento.

## Autor

Filipe Oliveira