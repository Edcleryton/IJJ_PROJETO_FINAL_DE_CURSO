
![Build](https://img.shields.io/badge/build-N/A-lightgrey)
![Python](https://img.shields.io/badge/python-3.12%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-Concluído%20para%20Entrega-brightgreen)

<h1 align="center">
  <a href="https://github.com/[SEU-USUARIO]/[NOME-DO-SEU-REPOSITORIO]">🚀 Projeto Final do Curso QA Avançado - Instituto Joga Junto 🐍</a>
</h1>

<p align="center">
  Projeto final do curso QA Avançado, focado na garantia de qualidade do sistema de controle de estoque do Instituto Joga Junto (IJJ). Este repositório centraliza o planejamento de testes, casos de teste manuais, automação de testes de UI (Selenium e Behave) e de API (Postman), relatórios de bugs e métricas de qualidade. O objetivo principal é validar os requisitos da aplicação, executar um plano de testes abrangente e fornecer feedback claro sobre a qualidade do software.
</p>

---

## 📝 Índice

- [📝 Índice](#-índice)
- [🌟 Introdução](#-introdução)
- [📌 Descrição do Projeto](#-descrição-do-projeto)
  - [Regras de Negócio Principais](#regras-de-negócio-principais)
  - [Requisitos Funcionais (RF)](#requisitos-funcionais-rf)
  - [Requisitos Não Funcionais (NF)](#requisitos-não-funcionais-nf)
- [🛠 Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [📂 Estrutura do Projeto de Testes](#-estrutura-do-projeto-de-testes)
- [⚙️ Configuração do Ambiente](#️-configuração-do-ambiente)
- [▶️ Executando os Testes](#️-executando-os-testes)
  - [Testes Manuais](#testes-manuais)
  - [Testes Automatizados de UI (Behave + Selenium)](#testes-automatizados-de-ui-behave--selenium)
  - [Testes de API (Postman / Newman)](#testes-de-api-postman--newman)
- [📊 Cobertura de Testes](#-cobertura-de-testes)
- [✨ Funcionalidades Chave Validadas](#-funcionalidades-chave-validadas)
- [🚧 Status do Projeto (Atualizado em 15/05/2025)](#-status-do-projeto-atualizado-em-15052025)
- [👥 Como Contribuir](#-como-contribuir)
- [❓ FAQ](#-faq)
- [📜 Licença](#-licença)
- [👤 Autores e Contato](#-autores-e-contato)
- [🏆 Créditos e Agradecimentos](#-créditos-e-agradecimentos)
- [🎯 Conclusão](#-conclusão)
- [🔗 Referências](#-referências)

---

## 🌟 Introdução

Este repositório representa o desafio final do módulo QA Avançado do Instituto Joga Junto. O projeto visa aplicar um fluxo completo de Garantia de Qualidade (QA) ao sistema de controle de estoque do IJJ, incluindo:

- Planejamento estratégico e documentação de testes (manuais e automatizados).
- Desenvolvimento e execução de cenários de teste de UI com Selenium e Behave.
- Elaboração e execução de testes de API com Postman.
- Geração de relatórios de bugs, métricas de execução e cobertura de requisitos.

---

## 📌 Descrição do Projeto

O foco deste projeto é validar e assegurar a qualidade das regras de negócio e requisitos do sistema de controle de estoque do IJJ.

### Regras de Negócio Principais

- **Acesso de Usuário:** Apenas colaboradores do IJJ alocados nas áreas de vendas e estoque podem acessar o backoffice.
- **Atualização em Tempo Real:** O estoque de produtos deve ser atualizado imediatamente após transações no e-commerce.
- **Navegação Multilíngue:** A interface do sistema deve suportar múltiplos idiomas para atender equipes globais de forma intuitiva.
- **Organização de Estoque:** A localização de produtos deve ser eficiente, clara e realizar-se em poucos cliques.

### Requisitos Funcionais (RF)

* **RF0001:** O sistema não deve permitir cadastro de usuário externo.
* **RF0002:** O sistema deve permitir login com e-mail e senha.
* **RF0003:** O cadastro de usuário deve ser permitido apenas para o perfil administrador.
* **RF0004:** O sistema deve permitir o cadastro de produtos.
* **RF0005:** O sistema deve permitir a edição de produtos cadastrados.
* **RF0006:** O sistema deve permitir a filtragem de produtos por categoria.
* **RF0007:** O sistema deve permitir a filtragem de produtos por preço.
* **RF0008:** O sistema deve permitir a exclusão de produtos cadastrados.
* **RF0009:** O sistema deve exibir os dados do usuário em sua aba de perfil.
* **RF0010:** O sistema deve atualizar automaticamente a quantidade de produtos disponíveis após cada transação (compras, vendas, devoluções).
* **RF0011:** O sistema deve permitir o acompanhamento de pedidos de compra e seus prazos de entrega.
* **RF0012:** O sistema deve manter um registro detalhado de todas as transações para fins de auditoria e históricos.

### Requisitos Não Funcionais (NF)

* **NF0001:** A interface do usuário deve ser intuitiva e simples de usar.
* **NF0002:** O sistema deve oferecer opções de tradução para facilitar a compreensão por colaboradores internacionais.
* **NF0003:** A identidade visual da marca IJJ deve estar presente e consistente em todos os elementos do produto.
* **NF0004:** O sistema deve ser capaz de integrar-se com outros sistemas da loja (ex: vendas, financeiro) de forma eficiente.

---

## 🛠 Tecnologias Utilizadas

- **Linguagem Principal (Testes Automatizados):** Python 3.12+
- **Testes de UI:** Selenium, Behave (BDD)
- **Testes de API:** Postman, Newman (para execução em linha de comando e relatórios)
- **Gerenciamento de WebDriver:** WebDriver Manager (para Selenium)
- **Variáveis de Ambiente:** python-dotenv (para scripts Python)
- **Controle de Versão:** Git / GitHub
- **Documentação:** Markdown

---

## 📂 Estrutura do Projeto de Testes

O projeto está organizado da seguinte forma na raiz `IJJ_PROJETO_FINAL_DE_CURSO/`:

```text

IJJ\_PROJETO\_FINAL\_DE\_CURSO/
├── docs/
│   └── Plano de Teste - IJJ.docx  
├── tests/
│   ├── behave/
│   │   └── features/
│   │       ├── login.feature
│   │       └── steps/
│   │           └── login\_steps.py
│   ├── .env
│   └── requirements.txt
├── .gitignore
└── README.md

```

---

## ⚙️ Configuração do Ambiente

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/](https://github.com/)[SEU-USUARIO]/IJJ_PROJETO_FINAL_DE_CURSO.git
    cd [NOME-DO-SEU-REPOSITORIO]
    ```

2.  **Crie e Ative um Ambiente Virtual Python:**
    Recomendado para isolar as dependências do projeto. Execute os comandos abaixo dentro da pasta raiz do projeto clonado (`[NOME-DO-SEU-REPOSITORIO]`):
    ```bash
    python -m venv venv
    ```
    *No Windows:*
    ```bash
    venv\Scripts\activate
    ```
    *No Linux/macOS:*
    ```bash
    source venv/bin/activate
    ```

3.  **Configure as Variáveis de Ambiente (Arquivo `.env`):**
    Se seus testes (especialmente Behave/Selenium) utilizam um arquivo `.env` para carregar URLs base ou credenciais, certifique-se de que ele está configurado corretamente. Este arquivo deve estar localizado na pasta `Tests/` ou na subpasta específica dos testes que o utilizam (ex: `Tests/behave/.env`).

    Exemplo de conteúdo para `Tests/behave/.env` (ajuste conforme sua necessidade):
    ```env
    BASE_URL="[https://projetofinal.org/](https://projetofinal.org/)"
    API_URL_SWAGGER="[https://apipf.projetodinal.org/swagger/](https://apipf.projetofinal.org/swagger/)"

    ```
    *Lembre-se de adicionar o arquivo `.env` ao seu `.gitignore` se ele contiver informações sensíveis.*

4.  **Instale as Dependências Python:**
    Com o ambiente virtual ativo, instale as bibliotecas listadas no arquivo `Tests/requirements.txt`:
    ```bash
    pip install -r Tests/requirements.txt
    ```
    *(Certifique-se de que `Tests/requirements.txt` inclui `selenium`, `behave`, `webdriver-manager`, `python-dotenv`, e `requests` se você tiver scripts Python para testes de API).*

5.  **Instale o Newman (para testes de API via linha de comando):**
    Requer [Node.js e npm](https://nodejs.org/) previamente instalados. Execute o comando abaixo uma vez para instalação global:
    ```bash
    npm install -g newman newman-reporter-htmlextra
    ```

---

## ▶️ Executando os Testes

### Testes Manuais

Os casos de teste manuais e a estratégia de execução estão detalhados nos seguintes documentos:
-   Plano de Teste: [`docs/test_plan.md`](./docs/test_plan.md)
-   Casos de Teste Manuais Detalhados: [`docs/CasosDeTesteManuais.md`](./docs/CasosDeTesteManuais.md)
    *(Se o seu plano de teste principal ainda for o arquivo `Plano de Teste - IJJ.docx`, você pode referenciá-lo também: `docs/Plano de Teste - IJJ.docx`)*

### Testes Automatizados de UI (Behave + Selenium)

1.  Certifique-se de que o ambiente virtual Python está ativo e as dependências de `Tests/requirements.txt` estão instaladas.
2.  Navegue até a pasta que contém os testes Behave (geralmente a pasta `Tests/` se suas features estão em `Tests/behave/features/`):
    ```bash
    cd Tests/
    # Ou, alternativamente, se você executa de dentro da pasta behave:
    # cd Tests/behave/
    ```
3.  Execute os testes Behave:
    ```bash
    behave
    ```
    *(Se você tiver um script customizado como `run_test.py` para executar os testes, inclua as instruções específicas para ele aqui).*

### Testes de API (Postman / Newman)

Os testes de API foram desenvolvidos e gerenciados utilizando Postman.

1.  **Execução Manual/Exploratória no Postman:**
    * Abra o aplicativo Postman.
    * Importe a Collection de testes: [`Tests/API/IJJ_Estoque_API.postman_collection.json`](./Tests/API/IJJ_Estoque_API.postman_collection.json).
    * (Opcional) Importe o Environment correspondente: [`Tests/API/IJJ_Estoque_API.postman_environment.json`](./Tests/API/IJJ_Estoque_API.postman_environment.json) e selecione-o como ativo no Postman.
    * Execute as requisições da collection individualmente ou em grupo, conforme os cenários de teste definidos.

2.  **Execução Automatizada via Linha de Comando com Newman (Gera Relatório):**
    * Certifique-se de que o Newman e o reporter `newman-reporter-htmlextra` estão instalados (conforme a seção "Configuração do Ambiente").
    * A partir da pasta raiz do projeto, execute o seguinte comando no terminal:
        ```bash
        newman run Tests/API/IJJ_Estoque_API.postman_collection.json -e Tests/API/IJJ_Estoque_API.postman_environment.json -r cli,htmlextra --reporter-htmlextra-export reports/Newman_API_Test_Report.html
        ```
    * Este comando executará todos os testes da collection especificada e gerará um relatório HTML detalhado em `reports/Newman_API_Test_Report.html`.

---
---

## 📊 Cobertura de Testes

A abordagem de cobertura para este projeto concentra-se em:

1.  **Cobertura de Requisitos:** Assegurar que todos os Requisitos Funcionais (RFs) e Não Funcionais (NFs) identificados nos documentos de especificação (ex: [`docs/Projeto_Final_QA_Documentacao.pdf`](./docs/Projeto_Final_QA_Documentacao.pdf)) e no Plano de Teste ([`docs/test_plan.md`](./docs/test_plan.md)) possuam pelo menos um caso de teste correspondente (manual ou automatizado). O mapeamento e o status da cobertura de requisitos são gerenciados no Plano de Teste.
2.  **Cobertura de Casos de Teste Automatizados:** Monitorar o percentual de cenários de teste manuais (especialmente os de alta prioridade e regressão) que foram automatizados (tanto para UI quanto para API).

*A medição de cobertura de código da aplicação alvo (`projetofinal.jogajuntoinstituto.org`) está fora do escopo deste projeto de teste externo.*

---

## ✨ Funcionalidades Chave Validadas

Este projeto foca na validação das seguintes funcionalidades do sistema de estoque:

-   **Gerenciamento de Usuários:**
    -   Autenticação via e-mail e senha (RF0002)
    -   Cadastro restrito a administradores (RF0003)
    -   Exibição de perfil de usuário (RF0009)
-   **Operações de Produtos:**
    -   Cadastro, edição e exclusão de produtos (RF0004, RF0005, RF0008)
    -   Filtragem por categoria e preço (RF0006, RF0007)
    -   Atualização automática de estoque após transações (RF0010)
-   **Pedidos e Transações:**
    -   Acompanhamento de pedidos de compra e prazos de entrega (RF0011)
    -   Registro detalhado de todas as transações para auditoria (RF0012)
-   **Internacionalização e Interface:**
    -   Suporte a múltiplos idiomas (NF0002)
    -   Interface intuitiva e identidade visual da marca (NF0001, NF0003)
-   **Integração:**
    -   Comunicação com sistemas de vendas e financeiro (NF0004)

---


## 🚧 Status do Projeto (Atualizado em 15/05/2025)

<p align="left">
  <img src="https://img.shields.io/badge/status-Concluído%20para%20Entrega-brightgreen" alt="Status do Projeto: Concluído para Entrega">
</p>

**Atividades Realizadas / Entregáveis Chave (15/05/2025):**

-   Finalização da execução dos testes manuais e de API (via Postman).
-   (Se aplicável) Geração do relatório de execução dos testes de API com Newman ([`reports/Newman_API_Test_Report.html`](./reports/Newman_API_Test_Report.html)).
-   Elaboração do Relatório de Resumo de Testes ([`docs/RelatorioResumoTestes.md`](./docs/RelatorioResumoTestes.md)).
-   Documentação e registro de Bug Reports na pasta [`reports/bugs/`](./reports/bugs/).
-   Consolidação de todos os artefatos de teste (scripts, collections Postman, features Behave) e documentação no repositório GitHub.
-   Revisão e finalização deste `README.md`.
-   Preparação para a apresentação final do projeto.

---

## 🚀 Melhoria Contínua e Automação

### Scripts de Automação

Para facilitar a execução dos testes, crie scripts automatizados. Exemplos:

- **Windows (run_tests.bat):**
  ```bat
  @echo off
  call venv\Scripts\activate
  echo Executando testes Behave...
  behave
  echo Executando testes Newman...
  newman run tests\API\API_IJJ.postman_collection.json -e tests\API\API_IJJ.postman_environment.json -r cli,htmlextra --reporter-htmlextra-export reports\Newman_API_Test_Report.html
  pause
  ```
- **Linux/Mac (run_tests.sh):**
  ```sh
  #!/bin/bash
  source venv/bin/activate
  echo "Executando testes Behave..."
  behave
  echo "Executando testes Newman..."
  newman run tests/API/API_IJJ.postman_collection.json -e tests/API/API_IJJ.postman_environment.json -r cli,htmlextra --reporter-htmlextra-export reports/Newman_API_Test_Report.html
  ```

### Integração Contínua (CI)

Sugestão de workflow para GitHub Actions (`.github/workflows/ci.yml`):
```yaml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Configurar Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.12'
      - name: Instalar dependências
        run: |
          python -m venv venv
          source venv/bin/activate
          pip install -r tests/requirements.txt
          npm install -g newman newman-reporter-htmlextra
      - name: Executar testes Behave
        run: |
          source venv/bin/activate
          behave tests/features/
      - name: Executar testes Newman
        run: |
          newman run tests/API/API_IJJ.postman_collection.json -e tests/API/API_IJJ.postman_environment.json -r cli,htmlextra --reporter-htmlextra-export reports/Newman_API_Test_Report.html
      - name: Salvar relatório
        uses: actions/upload-artifact@v3
        with:
          name: relatorio-newman
          path: reports/Newman_API_Test_Report.html
```

### Cobertura de Testes

Para medir a cobertura dos testes Python, adicione `coverage` ao `requirements.txt` e execute:
```bash
coverage run -m behave tests/features/
coverage report -m
```

### Padronização de Código

Utilize linters para manter a qualidade do código:
- Adicione ao `requirements.txt`: `flake8`, `pylint`
- Execute:
  ```bash
  flake8 tests/features/steps/
  pylint tests/features/steps/
  ```

### EditorConfig

Crie um arquivo `.editorconfig` na raiz do projeto para padronizar a formatação:
```
root = true
[*]
charset = utf-8
indent_style = space
indent_size = 4
end_of_line = lf
insert_final_newline = true
trim_trailing_whitespace = true
```

### Testes de Performance e Segurança

- Considere adicionar scripts de performance (ex: Locust, JMeter) e cenários de segurança (ex: entradas inválidas, SQL Injection) nos testes de API.

---

## 👥 Como Contribuir

Este é um projeto de conclusão de curso. Para projetos abertos, o fluxo de contribuição geralmente envolve:

1.  Fazer um Fork do repositório.
2.  Criar uma nova branch para sua feature/correção (`git checkout -b minha-feature`).
3.  Fazer commit das suas alterações (`git commit -am 'Adiciona nova feature'`).
4.  Fazer push para a branch (`git push origin minha-feature`).
5.  Abrir um Pull Request.

---

## ❓ FAQ

**P: Como atualizar as dependências do projeto Python?**
R: Com o ambiente virtual ativo, navegue até a pasta `Tests/` (ou onde seu `requirements.txt` principal está localizado) e execute `pip install -r requirements.txt`. Para atualizar um pacote específico: `pip install --upgrade nome_do_pacote`.

**P: Onde encontro o Plano de Teste detalhado e os casos de teste manuais?**
R: O Plano de Teste está em [`docs/test_plan.md`](./docs/test_plan.md). Os casos de teste manuais detalhados estão em [`docs/CasosDeTesteManuais.md`](./docs/CasosDeTesteManuais.md). Documentos de referência adicionais, como o escopo do projeto ([`docs/Projeto_Final_QA_Documentacao.pdf`](./docs/Projeto_Final_QA_Documentacao.pdf)) e a documentação da API ([`docs/API_jogajunto.pdf`](./docs/API_jogajunto.pdf)), também estão na pasta `docs/`.

---

## 📜 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` na raiz do repositório para mais detalhes.
*(Se você não possui um arquivo `LICENSE` na raiz do projeto, crie um contendo o texto da licença MIT, ou remova esta última frase).*

---

## 👤 Autores e Contato

<table>
  <tr>
    <td align="center" valign="top">
      <a href="https://github.com/Edcleryton">
        <img src="https://avatars.githubusercontent.com/u/134793465?v=4" width="50px" alt="Edcleryton Silva"/><br />
        <sub><b>Edcleryton Silva</b></sub>
      </a>
    </td>
    <td align="center" valign="top">
      <a href="https://github.com/daniloMelin">
        <img src="https://avatars.githubusercontent.com/u/127984038?v=4" width="50px" alt="Danilo Melin"/><br />
        <sub><b>Danilo Melin</b></sub>
      </a>
    </td>
    <td align="center" valign="top">
      <a href="https://github.com/Priest-San">
        <img src="https://avatars.githubusercontent.com/u/204785556?v=4" width="50px" alt="Daniel Santana"/><br />
        <sub><b>Daniel Santana</b></sub>
      </a>
    </td>
  </tr>
</table>

---

## 🏆 Créditos e Agradecimentos

-   Agradecimento especial ao **Instituto Joga Junto** pela oportunidade de aprendizado e desenvolvimento proporcionada pelo curso de QA Avançado.
-   Às comunidades online e documentações oficiais das ferramentas utilizadas (Selenium, Behave, Postman, Newman, Python, etc.) pelo vasto material de consulta que auxiliou neste projeto.

---

## 🎯 Conclusão

Este projeto de Garantia de Qualidade demonstra a aplicação prática de conceitos e ferramentas avançadas de teste de software no contexto do sistema de controle de estoque do Instituto Joga Junto. O objetivo foi entregar uma análise de qualidade robusta, identificar possíveis falhas e áreas de melhoria, e documentar todo o processo de forma clara e profissional, contribuindo assim para a evolução e confiabilidade do produto.

Sinta-se à vontade para explorar o repositório e, se desejar, dar uma ⭐!

---

## 🔗 Referências

-   [Documentação Oficial do Postman](https://learning.postman.com/docs/getting-started/introduction/)
-   [Documentação Oficial do Newman](https://learning.postman.com/docs/collections/using-newman-cli/command-line-integration-with-newman/)
-   [Documentação Oficial do Behave](https://behave.readthedocs.io)
-   [Documentação Oficial do Selenium (Python)](https://selenium-python.readthedocs.io/)
-   [Guia de Markdown do GitHub](https://guides.github.com/features/mastering-markdown/)
-   [Shields.io (para Badges)](https://shields.io/)
