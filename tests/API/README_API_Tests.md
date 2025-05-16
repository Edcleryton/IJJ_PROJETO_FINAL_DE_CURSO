# Testes da API Joga Junto  1.0.0

Este diretório contém os artefatos para teste da API [API Joga Junto  1.0.0] utilizando Postman e Newman.

## Pré-requisitos

1.  **Postman Instalado:** Para execução manual, exploração e depuração dos testes. [Download Postman](https://www.postman.com/downloads/).
2.  **Node.js e npm:** Necessários para executar o Newman.
    -   Verifique a instalação: `node -v` e `npm -v`.
    -   Se não instalados, baixe em [https://nodejs.org/](https://nodejs.org/).
3.  **Newman e Reporter htmlextra:** Utilitário de linha de comando para Postman e reporter para gerar relatórios HTML.
    -   Instale globalmente (execute uma vez no terminal):
        ```bash
        npm install -g newman newman-reporter-htmlextra
        ```
    -   (Opcional, se a instalação global falhar) Alternativamente, instale localmente no projeto (requer um `package.json` na raiz do projeto):
        ```bash
        # Na raiz do projeto (onde está o package.json)
        npm install --save-dev newman newman-reporter-htmlextra
        ```

## Artefatos de Teste

-   **`API_IJJ.postman_collection.json`**: A collection principal do Postman contendo todas as requisições e scripts de teste para a API.
-   **`API_IJJ.postman_environment.json`**: (Opcional) O arquivo de environment do Postman contendo variáveis específicas do ambiente (como `baseURL`, tokens de autenticação, etc.). Certifique-se de configurá-lo corretamente antes da execução se ele for necessário.

## Execução dos Testes

### 1. Execução via Interface do Postman (Manual/Exploratória)

-   Abra o aplicativo Postman.
-   Importe a Collection `API_IJJ.postman_collection.json`.
-   Importe o Environment `API_IJJ.postman_environment.json` e selecione-o como o ambiente ativo.
-   Execute as requisições individualmente ou use o "Collection Runner" do Postman para executar toda a collection ou pastas específicas.

### 2. Execução via Linha de Comando com Newman (Automatizada e para Geração de Relatórios)

Navegue até a **raiz do projeto principal** no seu terminal.

-   **Se o Newman foi instalado globalmente OU localmente e você está usando `npx`:**
    ```bash
    npx newman run Tests/API/API_IJJ.postman_collection.json -e Tests/API/API_IJJ.postman_environment.json --reporters htmlextra --reporter-htmlextra-export reports/Newman_API_Test_Report.html
    ```
    *Substitua `Tests/API/` pelo caminho correto se seus arquivos estiverem em outro local em relação à raiz do projeto.*
    *O relatório HTML (`Newman_API_Test_Report.html`) será gerado na pasta `reports/` na raiz do projeto.*

-   **Se o Newman foi instalado localmente e você configurou um script no `package.json` (ex: `npm run test:api`):**
    ```bash
    npm run test:api
    ```
  

## Estrutura dos Testes na Collection Postman

Descreva brevemente como sua collection está organizada:
-   Ex: "A collection está organizada em pastas por funcionalidade (Autenticação, Gerenciamento de Produtos, etc.)."
-   Ex: "Cada requisição contém scripts na aba 'Tests' para validar o código de status da resposta, o schema do JSON de resposta e valores específicos."
-   Mencione se você usa variáveis de collection ou environment e como elas são importantes.

## Troubleshooting / Solução de Problemas Comuns

-   **Erro: `newman: could not find "..." reporter`**
    -   **Causa:** O Newman não conseguiu encontrar o reporter especificado.
    -   **Solução:**
        1.  Verifique se o reporter (ex: `newman-reporter-htmlextra`) está instalado corretamente (globalmente ou localmente).
        2.  Tente reinstalar o reporter: `npm install -g newman-reporter-htmlextra` (ou localmente: `npm install --save-dev newman-reporter-htmlextra`).
        3.  Se estiver usando instalação local, certifique-se de executar o Newman via `npx newman ...` ou através de um script no `package.json`.
        4.  Verifique se não há erros de digitação no nome do reporter no comando Newman (`--reporters htmlextra`).

-   **Testes Falhando Inesperadamente:**
    -   Verifique se o ambiente da API está no ar e acessível.
    -   Confirme se as variáveis de environment (ex: `baseURL`, tokens) estão corretas e atualizadas.
    -   Examine os detalhes da requisição e resposta no relatório Newman ou diretamente no Postman para identificar a causa da falha (ex: payload incorreto, resposta inesperada da API).

-   **Problemas com `npm install -g ...` (Permissões no Linux/macOS):**
    -   Pode ser necessário usar `sudo npm install -g ...`. Considere configurar o npm para não precisar de sudo: [Resolving EACCES permissions errors when installing packages globally](https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally).

## O que é Testado (Exemplos)

Descreva de forma geral o que seus testes de API cobrem:
-   Validação de códigos de status HTTP para diferentes cenários (sucesso, erro do cliente, erro do servidor).
-   Verificação da estrutura (schema) das respostas JSON.
-   Teste de valores específicos nos campos da resposta.
-   Testes de fluxo (ex: criar um recurso, depois buscá-lo, depois atualizá-lo, depois deletá-lo).
-   Testes de autenticação e autorização (se aplicável).
-   Testes de validação de entrada (enviando dados inválidos para verificar o tratamento de erro da API).

---
