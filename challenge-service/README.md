# apis
Repositório da API Rest (micro-serviço).

<h3><b>PREPARAÇÃO DO AMBIENTE => CONFIGURAÇÃO E EXECUÇÃO</b></h3>

Os comandos abaixo foram executados para a inicialização do projeto e criação de um dos módulos.
<b>*Não é necessário executá-los novamente, basta clonar o projeto em sua máquina</b>

<blockquote>
django-admin startproject challenge_geral . <br>
django-admin startapp imovel
django-admin startapp anuncio
django-admin startapp reserva
</blockquote>

Design Pattern utilizados Django Rest Framework:
<b>Template Method Pattern, Adapter Pattern e outros.</b>

É utilizado uma organização de arquivos alem da estrutura inicial do django-admin startapp, e para isso executa-se o script create-scaffold para a criação dos novos arquivos da aplicação, que são os seguintes:

<b>serializers.py:</b> Criação dos campos que serão serializados.

<b>filters.py:</b> Criação de filtros de pesquisa aplicados no queryset, que é uma integração com a lib django-filter.

<b>repositories.py:</b> Utilização de métodos para a comunicação com a base de dados utilizando o ORM do django.

<b>business.py:</b> Utilização de métodos que se aplicam a regras de negócio da aplicação.

<b>urls.py:</b> Declaração das rotas da aplicação.

<blockquote>
python3 create-scaffold.py 'imovel'
python3 create-scaffold.py 'anuncio'
python3 create-scaffold.py 'reserva'
</blockquote>

Instalando os pacotes do projeto. Todas as libs estão no arquivo requirements.txt. Quando não há especificado a versão da lib, é instalado a versão mais atual.
<blockquote>pip3 install -r requirements.txt</blockquote>

Verificar python instalado na máquina e qual variável(alias) está o python 3. => python ou python3
<blockquote>python --version</blockquote>

<b>** Certifique-se que a variável python esteja com o valor de python3</b>

Rodando migrations (**sempre que necessário, quando há mudanças em models - base de dados)
<blockquote>
python3 manage.py makemigrations <br>
python3 manage.py migrate 
</blockquote>

Rodando a aplicação

É necessário antes de executar o projeto criar um usuário admin e cadastrar a aplicação challenge-service pois estamos utilizando para segurança de acesso aos endpoints OAuth Token 2.0 através da lib externa django-oauth-toolkit.

No terminal digitar:
<blockquote>
python manage.py createsuperuser --username lucas.amarante42 --email lucas.amarante42@gmail.com
digite a senha
</blockquote>

Para executar o projeto:
<blockquote>python3 manage.py runserver</blockquote>
<blockquote>python3 manage.py runserver 8002</blockquote>

Acessar ao portal Django Administration para cadastrar a aplicação e assim funcionar corretamente a requisição do token e usá-lo ao requisitar os endpoints.

<blockquote>
Acessar com as credenciais do usuário admin criado acima.
http://localhost:8002/admin

Localizar Applications -> Add Application para registrá-las:

Name: just a name of your choice => challenge-service
Client Type: confidential
Authorization Grant Type: Resource owner password-based

Copiar os valores de CLIENT_ID e CLIENT_SECRET nas variáveis de ambiente do settings do challenge-service
</blockquote>


