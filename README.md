# Banco-API-DJANGO-Rest-Framework

Operações presentes nesse exemplo:

Cadastrar ativos
Os ativos devem conter no mínimo as informações abaixo:
Nome - uma denominação para este ativo
Modalidade - renda fixa, renda variável ou cripto

Fazer aplicações e resgates em um ativo
Aplicação é quando o usuário aporta dinheiro em um ativo
Resgate é quando o usuário retira dinheiro de um ativo
Aplicações e resgates são transacionais e imutáveis. Uma vez realizada não há como alterar.
As aplicações e resgates devem conter no mínimo as informações abaixo:
Ativo - O ativo ao qual a aplicação/resgate se refere
Data de solicitação - a data em que a aplicação/resgate foi solicitada
Quantidade - número de ativos que foram aplicados/resgatados
Preço unitário - preço unitário do ativo na aplicação/resgate

Usuários podem fazer aplicações/resgate em ativos cadastrados por qualquer usuário

Exemplo:
O usuário A cadastra um ativo chamado BITCOIN e faz uma aplicação de mil reais
O usuário B pode aplicar no ativo BITCOIN também, pois ele já foi cadastrado pelo usuário A

Saldo da sua carteira de investimentos
O saldo da carteira é o somatório de saldos investidos em cada um dos ativos

#### Prerequisitos:
- Python
- Pip 
- Virtualenv 
- Django 

#### Django 

* Crie seu diretorio:
  `mkdir XXXXXXX`

* Entre no diretorio `XXXXXXX`

  `cd XXXXXXX`

* Crie um ambiente para instalar os pacotes.

  `virtualenv .env`

  `.env` diretorio onde os pacotes seram instalados.

* Ative o ambiente
   `source .env/bin/activate`

* Instalar o Django Framework
   `pip3 install django`

* Crie um projeto Django:
   `django-admin startproject XXXXXXXX`

* Rode o comando na pasta raiz que tem o arquivo `manage.py` 
    `./manage.py startapp api` isso ira criar a api
* Incluir `api` no `settings.py` que esta na pasta do projeto
    ```
      INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'api',
    ]
    
    ```
### Django Rest Framework

   ```
   pip install djangorestframework
   pip install markdown       
   pip install django-filter  
   ```
* Incluir `rest_framework` no `settings.py` que esta na pasta do projeto
    ```
      INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'api',
      'rest_framework',
    ]
    
    ```
* Para usar telas de login e logout para a API no browser, tem que incluir a linha abaixo no `urls.py` que esta na pasta do projeto
 e `from django.urls import include, path`
    ```
    urlpatterns = [
      path('admin/', admin.site.urls),
      path('', include('api.urls')),
    ]
    ```

### Criando superuser
  `python3 manage.py createsuperuser`
  exemplo: username:"sa" password:"sa123456" 

### Inicializar Servidor
  `python3 manage.py runserver`

### Migrar configurações iniciais
  `python3 manage.py migrate`

### Comando para migrar os modelos
  `python3 manage.py makemigrations`
  `python3 manage.py migrate`