# CNAB-parser-lVladimirl
>Uma api back-end voltada para o uso em agencias bancarias com o objetivo de armazenar registros de transações em um banco de dados relacional, a api é feita com o uso de um administrador em mente por conta disso as rotas de criação de usuario e loja possuem autenticação de super usuario.

## Tecnologias Usadas
- python 3.10.7
- django rest_framework
- banco de dados postgreSQL

## Passos de Instalação
- Clone o repositorio e acesse a pasta:
```Github link
https://github.com/lVladimirl/CNAB-parser-lVladimirl.git
```

- Abra o terminal crie um ambiente virtual
```terminal
python -m venv venv 
```

- Ative o ambiente virtual
```terminal
.\venv\Scripts\activate 
```

- Utilize o requirements.txt para instalar as dependencias
```terminal
pip install -r requirements.txt
```

## Passos para execução em ambiente de desenvolvimento (local).
- Crie um banco de dados PostgreSQL 
```DB manager
CREATE DATABASE nome_do_banco_de_dados
```

- Faça uma copia do arquivo .env.example, altere o nome para apenas '.env' e preencha os dados nescessarios para a criação do banco de dados
```python
#.env
SECRET_KEY="segredo"
POSTGRES_DB="nome_do_banco_de_dados"
POSTGRES_USER="usuario_postgres"
POSTGRES_PASSWORD="senha_usuario_postgres"
DATABASE_URL="url_fornecida_para_deploy"
```

- Criando as migrations
```terminal
python manage.py makemigrations
```

- Rodando as migrations (certifique que o banco de dados foi criado)
```terminal
python manage.py migrate
```

- Rodando a aplicação localmente
```terminal
python manage.py runserver
```

## Funcionamento
- Crie um superusuario atraves do terminal 
```terminal
python manage.py createsuperuser

username: exemplo
email: exemplo@gmail.com
password: ExemploS3nha
password(confirm): ExemploS3nha
```

- Fazendo login no insomnia é possivel criar e visualizar usuarios e lojas, mas para utilizar a funcionalidade de envio dos formularios ainda não é nescessario.

- Para enviar um formulario acesse a rota 'cnabs/form/' e escolha o arquivo de texto desejado, fazendo o upload a pagina sera redirecionada para 'cnabs/parser/' mostrando os registros  cadastrados.