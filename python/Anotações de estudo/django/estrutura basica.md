## Django admin

O Django Admin é uma interface administrativa gerada automaticamente. Ele fornece uma interface gráfica pronta para uso para que os administradores do site possam criar, visualizar, atualizar e deletar registros no banco de dados. É altamente personalizável e extensível, permitindo aos desenvolvedores adicionar funcionalidades adicionais conforme necessário. O Django Admin é uma ferramenta poderosa que acelera significativamente o desenvolvimento de aplicações web, facilitando a gestão de conteúdo e a administração do site sem a necessidade de escrever formulários específicos para essas tarefas.

## Manage.py

O manage.py é um utilitário de linha de comando que acompanha cada projeto Django. Ele é gerado automaticamente quando você cria um novo projeto Django e serve como uma ferramenta de conveniência para interagir com o projeto de várias maneiras.

A principal razão para usar manage.py em vez de django-admin diretamente é que manage.py é automaticamente configurado com as definições do seu projeto. Isso significa que ele sabe como importar as configurações do seu projeto e aplicá-las aos comandos que você executa. Isso facilita a execução de tarefas como iniciar o servidor de desenvolvimento, criar migrações de banco de dados, aplicar essas migrações e muitas outras tarefas relacionadas ao desenvolvimento e administração do seu projeto Django, sem a necessidade de passar constantemente as configurações do projeto como argumentos.

Em resumo, manage.py oferece uma interface de linha de comando personalizada para o seu projeto Django, simplificando a execução de comandos específicos do projeto e evitando a necessidade de especificar as configurações do projeto manualmente a cada comando.

## WSGI

Web server gateway interface - interface de porta de entrada do servidor web

plataforma padrao para aplicações web em python

serve de interface do servidor web e a aplicação web

o django com o comando starproject inicia uma configuração wsgi padrão para que se possa executar sua aplicação web

quando se inicia a aplicação django com o comando runserver é iniciado um servidor de aplicação web leve. esse servidor é especifica pela configuração WSGI_APPLICATION


## SETTINGS.py

é o responsavel pelas configurações do django

nele é possivel configurar por exemplo apps, conexão com o banco de dados, templates, time zone, cache, segurança, arquivos estativos, etc.

## URLS

É um schema de URL

responsavel por gerenciar as rotas da URLs, onde é possivel configurar pra onde cada rota sera executada

é uma forma limpa e elegante para gerenciar URLs

## URLs

Este arquivo contém as funções de visualização (ou classes, se você estiver usando visualizações baseadas em classe). Uma função de visualização recebe informações da requisição web e retorna uma resposta. A resposta pode ser uma página HTML, um redirecionamento, um arquivo para download, uma resposta JSON, entre outros. A função de visualização é onde você coloca a lógica de como os dados devem ser processados e apresentados ao usuário.

## MODELS

O arquivo models.py em um projeto Django é crucial para definir a estrutura dos dados que sua aplicação irá manipular. Ele serve como uma abstração que representa as tabelas do banco de dados em forma de classes Python. Cada classe definida em models.py corresponde a uma tabela no banco de dados, e cada atributo da classe representa um campo na tabela.

## STATIC

Respondavel por armazenar os arquivos estaticos

CSS,javaScript, imagens

## Templates

Responsavel por armazanar os arquivos HTML

o diretorio templates é diretorio padrão para armazenar todo o conteudo html da nossa aplicação

