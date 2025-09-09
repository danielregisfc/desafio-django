Criar diretório do projeto
Criar ambiente virtual
python -m venv venv
Ativar ambiente virtual
.\venv\Scripts\activate
Instalar django
pip install django

Selecionar interpretador python no vscode
CTRL+SHIFT+P Python Select Interpreter

iniciar projeto
django-admin startproject film_review .
cd

Em todo projeto novo no django é preciso rodas as migrations
python manage.py migrate

Iniciar o servidor
python manage.py runserver

Criar um app separado para reviews
python manage.py startapp reviews

Informar ao projeto principal que o app secundário foi adicionado 
Adicionar o nome do app em settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'reviews',
]

Criar os models em reviews

Não precisa informar o campo id no django (ele resolve direto isso)


Rodar o makemigrations para verificar se o model foi criado corretamente
python manage.py makemigrations

Posso ver como seria o SQL dessa migration (Para conferencia)
python manage.py sqlmigrate reviews 0001

Migrar o banco de dados
python manage.py migrate reviews



Criar super user do django admin

python manage.py createsuperuser 
Criei o daniel como exemplo, criar um admin tbm senha do NOR

python manage.py runserver  

http://127.0.0.1:8000/admin


Definir quais models serão administrados por essa interface admin do django
Configurar no arquivo admin.py


> from django.contrib import admin
> from .models import Review

> admin.site.register(Review)

Atualiza a página admin que aparecerá uma nova sessão com o app Review
