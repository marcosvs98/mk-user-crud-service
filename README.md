# mk-user-crud-service

## 📋 Sumário

- [📋 Sumário](#-sumário)
- [🛠 Tecnologias utilizadas](#-tecnologias-utilizadas)
- [🗂 Estrutura de pastas](#-estrutura-de-pastas)
- [▶️Executando o projeto](#-executando-o-projeto)
- [⚙ Comnandos extras](#-comandos-extras)
- [📚 Como utilizar este projeto](#-como-utilizar-este-projeto)


## 🛠 Tecnologias e Padrões utilizados

Para o desenvolvimento deste projeto, as seguintes tecnologias foram usadas:

- **Python 3.9**
- **FastAPI (Rest API)**
- **Poetry** (Gerenciador de pacotes python)
- **SQLAlchemy** (ORM)
- **Alembic** (Migrations)
- **AioRedis** (Cache Async)

Esse projeto possui uma estrutura que visa o máximo desacoplamento entre camadas com o objetivo de dar
suporte para criação de componentes que sejam reutilizaveis por todo o domínio de negócio. O mesmo possui um CRUD de Usuários simples com
exemplos de organização de pacotes e testes.

Além de outros, o principal pattern que guia este projeto é o Hexagonal (+ Clean Architecture), em resumo, esse padrão
fornece uma maneira de organizar o código de forma que a lógica de negócio seja encapsulada, mas separada do mecanismo de
entrega. Isso permite uma melhor manutenção e menos dependências.

A estrutura do código segue uma organização de pacote por domínio, ou seja, vamos supor que Usuário seja um domínio
mapeado em nossa estrutura de domínios, nesse caso, teremos na pasta `src.packages` a parte `users` que conterá todo o
código necessário para o tratamento de usuários com baixo acoplamento e contexto bem delimitado.

## 🗂 Estrutura de pastas

```bash
/src
  /adapters # Adaptadores globais (inbound ou outbound adapters)
  /database # Caso opte por usar banco de dados, aqui ficam armazenados as migrations, regra de conexão e também os modelos de ORM
  /exceptions # Classes de exceção globais
  /packages # Cada pasta dentro de packages diz respeito a um domínio
    /users
      /controllers # Ou inbound adapters
      /exceptions # Classes de exceções específicas do domínio
      /ports # Interfaces dos quais nossos adapters e services devem implementar
      /repository # Ou outbound adapters
      /schemas # Entidades do domínio, que podem ou não contem regras de negócio (A critério)
      /services # Camada de casos de uso que podem implementar regras de negócio, ou regras da aplicação
  /ports # Interfaces globais
  /utils # Funções secundárias, que estão fora do contexto do domínio
  /tests
    /users # Como sugestão, devemos isolar nossas suites de testes por domínio
```

## ▶️ Executando o projeto

### Opção 1 - Via Docker Compose

#### Execute o docker-compose

Por fim, execute o projeto e as suas dependências em segundo plano através do comando
```bash
docker-compose up -d
```

### Opção 2 - Via IDE (Pycharm)

Ao importar o projeto a ferramenta irá identificar duas configurações
padrão versionadas na pasta `.idea/runConfigurations`:
- Run App

#### Run App Config

Para utilizar a config `Run App` você deverá ter instalando o plugin `EnvFile`, sem seguida, apenas adicione um arquivo
`.env` na raiz do seu projeto e adicionar as variáveis de ambiente manualmente.

### Preparando as dependêncas

Para esse projeto, utilizamos o **Poetry** como gerenciador de pacotes. A sua escolha foi devida a simplicidade em manipular pacotes
e a sua impresisonante capacidade de resolver problema de dependências.

Após importar o projeto, instale o poetry de acordo com a documentação https://python-poetry.org/docs/

Após ter instalado e configurado o poetry, instale as dependências do projeto:
```bash
poetry install
```

Você poderá encontrar mais instruções sobre o poetry na sua [documentação oficial](https://python-poetry.org/docs/)

## ⚙️ Comandos Extras

O projeto possui um arquivo `Makefile` com alguns comandos make que facilitam a preparação de dependências.

Criar uma nova migration:
```bash
make migrate-revision
```

Executar as migrations:
```bash
make migrate-upgrade
```

Executar revisão e  atualização no conteiner
```bash
docker-compose run web {make COMANDO}
```

Levantar todas as dependências:
```bash
make up
```

Executar todos os testes:
```bash
make tests
```

## 📚 Como utilizar este projeto

Criar um novo usuário:
```bash
$ --request POST 'http://{ENDPOINT}/api/users/' \
   --header 'Content-Type: application/json' \
   --data-raw '{
                 "email": "marcosvs@protonmail.com",
                 "first_name": "Marcos",
                 "last_name": "Silveira",
                 "age": 24
               }'
```
Resposta: 
```json
{
    "id": "b49dc1ff-0897-4b73-bdc0-811533586b9a",
    "email": "marcosvs@protonmail.com",
    "first_name": "Marcos",
    "last_name": "Silveira",
    "age": 24
}
```

Obter um usuário:
```bash
$ curl --request GET 'http://{ENDPOINT}/api/users/acba5cb6-c4ef-40ae-b6ca-4a34e138f9de'
```
Resposta:
```json
{
    "id": "b49dc1ff-0897-4b73-bdc0-811533586b9a",
    "email": "marcosvs@protonmail.com",
    "first_name": "Marcos",
    "last_name": "Silveira",
    "age": 24
}
```

Listar todos usuários:
```bash
$ curl --request GET 'http://{ENDPOINT}/api/users/' 
```
Resposta:
```json
[
    {
        "id": "b49dc1ff-0897-4b73-bdc0-811533586b9a",
        "email": "marcosvs@protonmail.com",
        "first_name": "Marcos",
        "last_name": "Silveira",
        "age": 24
    }
]
```

Atualizar um usuário:
```bash
$ curl --request PUT 'http://{ENDPOINT}/api/users/032f682b-5dec-4819-9fef-c57c761a8e3e' \
       --header 'Content-Type: application/json' \
       --data-raw '{
            "email": "marcolino@protonmail.com",
            "first_name": "Marcolino",
            "last_name": "Vinicios",
            "age": 24
       }'
```
Resposta:
```json
{
    "id": "b49dc1ff-0897-4b73-bdc0-811533586b9a",
    "email": "marcolino@protonmail.com",
    "first_name": "Marcolino",
    "last_name": "Vinicios",
    "age": 27
}
```

Remover um usuário:
```bash
$ curl --request DELETE 'http://{ENDPOINT}/api/users/b49dc1ff-0897-4b73-bdc0-811533586b9a'
```


## Referências

- [Hexagonal Architecture](https://herbertograca.com/2017/11/16/explicit-architecture-01-ddd-hexagonal-onion-clean-cqrs-how-i-put-it-all-together/)
- [Domain Driven Design - DDD](https://lyz-code.github.io/blue-book/architecture/domain_driven_design/)
- [Repository Pattern](https://lyz-code.github.io/blue-book/architecture/repository_pattern/)
- [Service Layer Pattern](https://www.cosmicpython.com/book/chapter_04_service_layer.html)
- [SQL Alchemy](https://docs.sqlalchemy.org/en/14/orm/quickstart.html)
- [Alembic](https://alembic.sqlalchemy.org/en/latest/)
