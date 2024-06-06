Devemos sempre criar um ambiente virtual para cada projeto, para criar utilizamos esse comando:
```python
python -m venv .venv
```
entao temos que ativar o ambiente.

```python
.\.venv\Scripts\activate
```

pode acontecer um erro por causa das configurações do powershell, para resolver usamos esse comando:
```cmd
Set-ExecutionPolicy -Scope Process -ExecutionPolicy bypass
```

em seguida usa o comando para ativar o ambiente virtual.

depois do ambiente ativo, toda instalação de pacotes python vão ser feitas nesse ambiente virtual, assim n havera problemas de compatibilidade em outros projetos.

instalando o Django:
```python
    pip install django
```
para instalar uma versão especifica use '==' ex.:
```python
    pip install django==4.2.1
```


Agora Criamos um projeto Django com o seguinte comando
```python
django-admin startproject setup .
```
para rodar o projeto usamos o seguinte comando:
```python
python manage.py runserver
```

para acessar o projeto vamos buscar localhost:8000 no navegador


configurações interesantes:
ir em settings.py e mudar o LANGUAGE_CODE = 'en-us' para 'pt-br'

### Como é a estrutura de pastas de um projeto Django e como criar uma app


#### diferença entre app e project

No Django, um projeto é a coleção completa de configurações e aplicações, enquanto uma aplicação é um módulo dentro do projeto que realiza uma tarefa específica.

Project: É a soma de todas as suas aplicações e configurações. Ele contém a configuração geral do seu site, como a configuração do banco de dados, configurações específicas do Django, etc. Quando você inicia um novo projeto Django, ele cria uma estrutura de diretórios com alguns arquivos que incluem configurações para o seu projeto.

App: É um módulo dentro do seu projeto que realiza uma tarefa específica. Por exemplo, se você estiver criando um site de blog, pode ter uma aplicação para lidar com a criação de posts, outra aplicação para lidar com comentários, etc. Cada aplicação é um pacote Python que é plugável em qualquer projeto Django.

Em resumo, um projeto é composto por várias aplicações e uma aplicação pode ser usada em vários projetos.


### Criando um app

usamos o comando
```python
python manage.py startapp nome_do_app
```

as apps precisam ser instaladas no projeto, para isso, vamos na pasta setup e em settings.py procuramos por INSTALLED_APPS, existe duas formas de adicionar, vc pode colocar o nome do app, e na outra seguindo a documentação, vc adiciona o caminho completo, ex.:


pasta.apps.nomedaclass

```python
'todos.apps.TodosConfig'
```

## Entendendo o padrão MTV(Model-Template-View)


é um padrão de design usado no Django, que é uma variação do padrão MVC (Model-View-Controller). Aqui está uma explicação de cada componente:

Model (Modelo): O modelo é a representação dos seus dados. É um lugar onde você define a estrutura dos seus bancos de dados. Um modelo é uma classe Python que é derivada da classe django.db.models.Model e inclui variáveis que representam um campo no banco de dados.

Template (Modelo): O template é onde você define como o usuário vê e interage com o seu site. É um arquivo HTML que pode exibir dados do banco de dados consultando o modelo.

View (Visão): A view é onde a "lógica de negócios" é manipulada. É uma ponte entre o modelo e o template. Uma view pode ser uma função Python ou uma classe baseada em view que recebe uma solicitação web, recupera os dados do modelo e envia os dados para o template.

O fluxo de trabalho do MTV é o seguinte:

1.O usuário faz uma solicitação para uma URL.
2.Django usa o URLconf para encontrar a view associada à URL.
3.A view recupera os dados necessários do modelo.
4.A view passa os dados para o template.
5.O template renderiza a página HTML com os dados fornecidos.
6.Django envia a página HTML de volta ao usuário.


no views criamos funções onde devem rebecer um argumento request

```python
def home(request):
    return render(request, 'todos/home.html')
```

esta pegando um template e colocando na pagina web

na pasta do projeto devemos criar uma pasta template e dentro dela uma pasta com o msm nome do projeto, la criaremos nossos templates, que são arquivos html.