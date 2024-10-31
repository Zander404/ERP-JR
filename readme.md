
# ERP-JR

Sistema de ERP (Enterprise Resource Planning) voltado para empresas juniores do estado de Goiás.

Este sistema busca realizar o controle dos recursos de empresas juniores, auxiliando no organização administrativa, comercial, finaceira, gestão de pessoas e projetos. Possibilitando a integração de todas as áreas em apenas um sistema só, ajudando na eficiência e na produtividade de todas as áreas.

## Funcionalidades
 As Funcionalidades a qual esse projeto busca atender são as seguintes para cada área:
 
- ### Administrativa:
    - Visualização de Documentos de Regimento: 
    - Sistema para Preenchimento de Contratos
    - Visualização de Contratos
    - Gerenciamento de Documentos do Selo EJ
    - Gerador de Notas Fiscais

- ### Comercial
    - Processamento de Pedidos
    - Automatizar geração de Propostas
    - Monitoramento de Venda
    - Cadastro de Clientes

- ### Financeiro
    - Painel Financeiro
    - Automatização de Autorização de Pagamento
    - Gerenciamento de Fluxo de Caixa

- ### Gestão de Pessoas
    - Controle de Usuários
    - Quadro de Membros
    - Automatização de Termo de Adessão 
    - Automatização de Ficha de Membro
    - Automatização de Termo de Distrato

- ### Projetos 
    - Cadastro de Projetos
    - Sistema de Kanbam
    - Precificador de Projeto
    - Calculo de Estimativa de Tempo por Feature



## Stack utilizada

**Front-end:** NextJS, TailwindCSS, Daisy UI

**Back-end:** Django, Python, Celery, Django Rest Framework


## Variáveis de Ambiente

Para rodar esse projeto, você vai precisar adicionar as seguintes variáveis de ambiente no seu .env

**DJANGO**: 
`SECRET_KEY`
`DEBUG`
`ALLOWED_HOSTS`
`ENGINE_DB`

**POSTGRES**: 
`POSTGRES_DB`
`POSTGRES_USER`
`POSTGRES_PASSWORD`
`POSTGRES_HOST`
`POSTGRES_PORT`


## Instalação

Instale o projeto com:

- Linux
```bash
  python -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
  python manage.py runserver 8000
```

- Windows
```bash
  python -m venv .venv
  pip install -r requirements.txt
  .\.venv\Scripts\Activate.ps1
  python manage.py runserver 8000
  
```

- Docker
```bash
    docker pull zander404/erpjr
    docker run zander404/erpjr -port 8000
```

- Docker Compose
```bash
    docker compose up
```
## Autores

- [@octokatherine](https://www.github.com/octokatherine)


## Referência

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)

