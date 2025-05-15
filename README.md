
![Build](https://img.shields.io/badge/build-N/A-lightgrey)
![Python](https://img.shields.io/badge/python-3.12%2B-blue) ![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-Em%20Desenvolvimento-orange)

<h1 align="center">
  <a href="https://github.com/seu-usuario/projeto-final-python">🚀 Projeto Final do Curso QA Avançado - Instituto Joga Junto 🐍</a>
</h1>
<p align="center">
  Projeto final do curso QA Avançado, focado na garantia de qualidade do sistema de controle de estoque do Instituto Joga Junto (IJJ). Este repositório centraliza o planejamento de testes, casos de teste manuais, automação de testes de UI (Selenium e Behave) e de API (Python Requests), relatórios de bugs e métricas de qualidade. O objetivo principal é validar os requisitos da aplicação, executar um plano de testes abrangente e fornecer feedback claro sobre a qualidade do software.
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
  - [Testes de API (Python + Requests ou Postman)](#testes-de-api-python--requests-ou-postman)
- [📊 Cobertura de Testes](#-cobertura-de-testes)
- [✨ Funcionalidades Chave Validadas](#-funcionalidades-chave-validadas)
- [🚧 Status do Projeto (Atualizado em 14/05/2025)](#-status-do-projeto-atualizado-em-14052025)
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
- Desenvolvimento e execução de testes de API com Python e a biblioteca `requests` (quando aplicável).
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

- **Linguagem Principal:** Python 3.12+ (ex: 3.12.x, 3.13.x)
- **Testes de UI:** Selenium, Behave (BDD)
- **Testes de API:** Python Requests (ou Postman, conforme execução)
- **Gerenciamento de WebDriver:** WebDriver Manager
- **Variáveis de Ambiente:** python-dotenv
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

1. **Clone o Repositório:**

    ```bash
    git clone [https://github.com/](https://github.com/)[SEU_USUARIO_GITHUB]/[NOME_DO_SEU_REPOSITORIO].git
    cd [NOME_DO_SEU_REPOSITORIO]
    ```

2. **Crie e Ative um Ambiente Virtual Python:**
    Recomendado para isolar as dependências. Execute os comandos abaixo dentro da pasta raiz do projeto clonado (`[NOME_DO_SEU_REPOSITORIO]`) ou, se preferir, dentro da pasta específica de automação (ex: `tests/automacao_ui_behave/`).

    ```bash
    # Na pasta escolhida (ex: [NOME_DO_SEU_REPOSITORIO])
    python -m venv venv
    # No Windows:
    venv\Scripts\activate
    # No Linux/macOS:
    source venv/bin/activate
    ```

3. **Configure as Variáveis de Ambiente (Arquivo `.env`):**
    Dentro da pasta `tests/automacao_ui_behave/`, crie um arquivo chamado `.env` com o seguinte conteúdo:

    ```env
    BASE_URL="[https://projetofinal.jogajuntoinstituto.org/](https://projetofinal.jogajuntoinstituto.org/)"
    API_URL="[https://apipf.jogajuntoinstituto.org/swagger/](https://apipf.jogajuntoinstituto.org/swagger/)"
    ```

    *Os scripts de automação carregarão essas variáveis. Considere adicionar `.env` ao seu `.gitignore` se ele contiver informações sensíveis no futuro.*

4. **Instale as Dependências:**
    Com o ambiente virtual ativo, navegue até a pasta que contém o `requirements.txt` apropriado e instale:

    ```bash
    # Exemplo: Se o requirements.txt está em tests/automacao_ui_behave/
    cd tests/automacao_ui_behave/
    pip install -r requirements.txt
    ```

    (Certifique-se de que seu `requirements.txt` contenha `selenium`, `behave`, `webdriver-manager`, `python-dotenv`. Se tiver testes de API com Python Requests, adicione `requests` também).

---

## ▶️ Executando os Testes

### Testes Manuais

Os casos de teste manuais e a estratégia de execução estão detalhados no Plano de Teste.

- **Localização:** `docs/Plano de Teste - IJJ.docx` (ou o nome/caminho correto do seu arquivo de plano de teste).

### Testes Automatizados de UI (Behave + Selenium)

1. Certifique-se de que o ambiente virtual está ativo e as dependências estão instaladas.
2. Navegue até a pasta raiz dos testes Behave (onde está a subpasta `features/`):

    ```bash
    cd tests/automacao_ui_behave/
    ```

3. Execute os testes usando:

    ```bash
    behave
    ```

    Ou, se você configurou o script `run_test.py`:

    ```bash
    python run_test.py
    ```

### Testes de API (Python + Requests ou Postman)

- **Com Python + Requests:** Se você desenvolveu scripts (ex: em `tests/api_tests/`):
  
    ```bash
    # Exemplo, ajuste conforme seus arquivos
    cd tests/api_tests/
    python nome_do_seu_script_api.py
    ```

- **Com Postman:** Execute as coleções diretamente na ferramenta Postman. Exporte a coleção e o ambiente (se houver) e adicione-os ao repositório (ex: na pasta `tests/api_tests_postman/`) para referência.

---

## 📊 Cobertura de Testes

A abordagem de cobertura para este projeto concentra-se em:

1. **Cobertura de Requisitos:** Assegurar que todos os Requisitos Funcionais (RFs) e Não Funcionais (NFs) identificados no `Informações do Trabalho.docx` e no `Plano de Teste - IJJ.docx` possuam pelo menos um caso de teste correspondente (manual ou automatizado). O mapeamento e o status da cobertura de requisitos são gerenciados no Plano de Teste.
2. **Cobertura de Casos de Teste Automatizados:** Monitorar o percentual de cenários de teste manuais (especialmente os de alta prioridade e regressão) que foram automatizados.

*A medição de cobertura de código da aplicação alvo (`projetofinal.jogajuntoinstituto.org`) está fora do escopo deste projeto de teste externo.*

---

## ✨ Funcionalidades Chave Validadas

Este projeto foca na validação das seguintes funcionalidades do sistema de estoque:

- **Gerenciamento de Usuários:**
  - Autenticação via e-mail e senha (RF0002)
  - Cadastro restrito a administradores (RF0003)
  - Exibição de perfil de usuário (RF0009)
- **Operações de Produtos:**
  - Cadastro, edição e exclusão de produtos (RF0004, RF0005, RF0008)
  - Filtragem por categoria e preço (RF0006, RF0007)
  - Atualização automática de estoque após transações (RF0010)
- **Pedidos e Transações:**
  - Acompanhamento de pedidos de compra e prazos de entrega (RF0011)
  - Registro detalhado de todas as transações para auditoria (RF0012)
- **Internacionalização e Interface:**
  - Suporte a múltiplos idiomas (NF0002)
  - Interface intuitiva e identidade visual da marca (NF0001, NF0003)
- **Integração:**
  - Comunicação com sistemas de vendas e financeiro (NF0004)

---

## 🚧 Status do Projeto (Atualizado em 14/05/2025)

<p align="left">
  <img src="https://img.shields.io/badge/status-Em%20Desenvolvimento%20%7C%20Fase%20Final-orange" alt="Status do Projeto: Em Desenvolvimento | Fase Final">
</p>

- **Plano de Teste:** Concluído e documentado.
- **Casos de Teste Manuais (RFs):** Elaborados e documentados no Plano de Teste.
- **Execução de Testes Manuais:** Em andamento / Finalizando.
- **Testes de API (Postman):** Em execução / Resultados sendo coletados.
- **Testes Automatizados de UI (Behave/Selenium):** 1 cenário de login implementado e funcional.
- **Relatório de Bugs:** Em elaboração, com bugs sendo registrados e evidenciados.
- **Coleta de Evidências:** Em andamento, junto com a execução dos testes.

**Foco para 15/05/2025 (Dia da Entrega):**

- Finalizar a execução de todos os testes planejados.
- Completar e revisar o Relatório de Bugs, incluindo todas as evidências.
- Gerar estatísticas finais de execução de testes e métricas de qualidade.
- Finalizar e revisar todos os documentos entregáveis (Plano de Teste, README, etc.).
- Preparar e ensaiar a apresentação final do projeto.

---

## 👥 Como Contribuir

Este é um projeto de conclusão de curso, mas se fosse um projeto aberto, o fluxo seria:

1. Faça um Fork deste repositório.
2. Crie uma nova branch para sua feature/correção: `git checkout -b minha-contribuicao`
3. Faça commit das suas alterações: `git commit -m "feat: Descreve a contribuição"`
4. Faça push para a branch: `git push origin minha-contribuicao`
5. Abra um Pull Request detalhando suas mudanças.

---

## ❓ FAQ

**P: Como atualizar as dependências do projeto?**
R: Com o ambiente virtual ativo, ajuste o arquivo `requirements.txt` (localizado em `tests/automacao_ui_behave/` ou na raiz do projeto, conforme sua organização) e execute `pip install -r requirements.txt`. Para atualizar um pacote específico: `pip install --upgrade nome_do_pacote`.

**P: Onde encontro o Plano de Teste detalhado e os casos de teste manuais?**
R: O Plano de Teste, que inclui os casos de teste manuais, a estratégia e outras informações, está localizado em `docs/Plano de Teste - IJJ.docx` (ou o nome e formato exato do seu arquivo principal de planejamento).

---

## 📜 Licença

Este projeto está licenciado sob a Licença MIT. Recomenda-se adicionar um arquivo `LICENSE` na raiz do repositório com o texto completo da licença MIT.

---

## 👤 Autores e Contato
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/Edcleryton">
        <img src="https://avatars.githubusercontent.com/u/134793465?v=4" width="50px" alt="Edcleryton Silva"/>
      </a>
      <br/>
      <a href="https://github.com/Edcleryton">Edcleryton Silva</a>
    </td>
    <td align="center">
      <a href="https://github.com/daniloMelin">
        <img src="https://avatars.githubusercontent.com/u/127984038?v=4" width="50px" alt="Danilo Melin"/>
      </a>
      <br/>
      <a href="https://github.com/daniloMelin">Danilo Melin</a>
    </td>
    <td align="center">
      <a href="https://github.com/Priest-San"> <img src="https://avatars.githubusercontent.com/u/204785556?v=4" width="50px" alt="Daniel Santana"/>
      </a>
      <br/>
      <a href="https://github.com/Priest-San">Daniel Santana</a> </td>
  </tr>
</table>

---

## 🏆 Créditos e Agradecimentos

* Agradecimento especial ao **Instituto Joga Junto** pela oportunidade de aprendizado e desenvolvimento proporcionada pelo curso de QA Avançado.
* Às comunidades online e documentações oficiais das ferramentas utilizadas (Selenium, Behave, Python Requests, etc.) pelo vasto material de consulta que auxiliou neste projeto.

---

## 🎯 Conclusão

Este projeto de Garantia de Qualidade demonstra a aplicação prática de conceitos e ferramentas avançadas de teste de software no contexto do sistema de controle de estoque do Instituto Joga Junto. O objetivo é entregar uma análise de qualidade robusta, identificar possíveis falhas e áreas de melhoria, contribuindo assim para a evolução e confiabilidade do produto.

Sinta-se à vontade para explorar o repositório e, se desejar, dar uma ⭐!

---

## 🔗 Referências

- [Documentação Oficial do Python Requests](https://docs.python-requests.org)
- [Documentação Oficial do Behave](https://behave.readthedocs.io)
- [Documentação Oficial do Selenium](https://www.selenium.dev/docs/)
- [Documentação do python-dotenv](https://github.com/theskumar/python-dotenv)
- [Guia de Markdown do GitHub](https://guides.github.com/features/mastering-markdown/)