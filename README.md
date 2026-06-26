# Sistema de Gamificação de Hábitos

## Sobre o Projeto

Este projeto foi desenvolvido utilizando o framework Django com o objetivo de incentivar a realização de atividades e hábitos saudáveis por meio de um sistema de pontuação e acompanhamento de progresso dos usuários.

A aplicação permite o gerenciamento de usuários, grupos e atividades, registrando informações importantes para o acompanhamento do desempenho de cada participante.

## Funcionalidades

* Cadastro de usuários
* Edição de usuários
* Remoção de usuários
* Cadastro de grupos
* Cadastro de atividades
* Sistema de pontuação
* Controle de sequência de atividades
* Gerenciamento dos dados através do Django Admin

## Tecnologias Utilizadas

* Python
* Django
* SQLite
* HTML
* CSS

## Estrutura do Projeto

### Usuário

Armazena informações dos usuários cadastrados.

Campos:

* Nome
* E-mail
* Pontos
* Sequência

### Grupo

Armazena os grupos existentes na aplicação.

Campos:

* Nome
* Descrição

### Atividade

Armazena as atividades realizadas pelos usuários.

Campos:

* Usuário
* Tipo de atividade
* Duração
* Pontos obtidos

## Instalação

Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
```

Acesse a pasta do projeto:

```bash
cd projeto
```

Instale as dependências:

```bash
pip install django
```

Execute as migrações:

```bash
python manage.py migrate
```

Crie um superusuário:

```bash
python manage.py createsuperuser
```

Inicie o servidor:

```bash
python manage.py runserver
```

## Utilização

Após iniciar o servidor, acesse:

```text
http://127.0.0.1:8000/
```

Para acessar o painel administrativo:

```text
http://127.0.0.1:8000/admin/
```

## Objetivos do Projeto

* Aplicar conceitos de desenvolvimento web.
* Utilizar o framework Django.
* Trabalhar com banco de dados.
* Desenvolver funcionalidades de gerenciamento de usuários e atividades.


## Equipe

* Luis Gabriel Bretas Monteiro
* Lucca Borges Azambuja Midosi
* Guilherme Cabral M de Vasconcellos

## Licença

Projeto desenvolvido para fins acadêmicos.
