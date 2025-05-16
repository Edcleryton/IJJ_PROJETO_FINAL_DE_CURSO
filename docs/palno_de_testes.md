# Plano de Teste – Sistema de Controle de Estoque – Instituto Joga Junto (Versão 2.0)

**Squad:** MaQAcos

- Danilo Melin
- Daniel Santana
- Edcleryton da Silva

---

## Índice

1.  [Introdução](#1-introdução)
2.  [Arquitetura do Sistema Alvo](#2-arquitetura-do-sistema-alvo)
3.  [Ferramentas de Testes](#3-ferramentas-de-testes)
4.  [Estratégias de Testes](#4-estratégias-de-testes)
    * [4.1. Tipos de Teste](#41-tipos-de-teste)
    * [4.2. Técnicas Aplicadas (ISO/IEC 29119-4)](#42-técnicas-aplicadas-isoiec-29119-4)
    * [4.3. Critérios de Prioridade](#43-critérios-de-prioridade)
5.  [Cronograma](#5-cronograma)
6.  [Métricas de Qualidade (ISO/IEC 25010)](#6-métricas-de-qualidade-isoiec-25010)
7.  [Classificação dos Bugs](#7-classificação-dos-bugs)
8.  [Cenários de Testes](#8-cenários-de-testes)
    * [8.1. Testes Funcionais](#81-testes-funcionais)
        * [8.1.1. Cadastro de Usuário (RF001 e RF003)](#811-cadastro-de-usuário-rf001-e-rf003)
        * [8.1.2. Login de usuário (RF-002)](#812-login-de-usuário-rf-002)
        * [8.1.3. Cadastro de Produto (RF004)](#813-cadastro-de-produto-rf004)
        * [8.1.4. Edição de Produto (RF005)](#814-edição-de-produto-rf005)
        * [8.1.5. Filtragem de Produtos por Categoria/Preço (RF006 e RF007)](#815-filtragem-de-produtos-por-categoriapreço-rf006-e-rf007)
        * [8.1.6. Exclusão de Produto (RF008)](#816-exclusão-de-produto-rf008)
        * [8.1.7. Exibição de Dados do Perfil do Usuário (RF009)](#817-exibição-de-dados-do-perfil-do-usuário-rf009)
        * [8.1.8. Atualização automática da quantidade de produtos disponíveis (RF010)](#818-atualização-automática-da-quantidade-de-produtos-disponíveis-rf010)
        * [8.1.9 Acompanhamento de pedidos de compra e Registro detalhado de transações realizadas (RF011 e RF012)](#819-acompanhamento-de-pedidos-de-compra-e-registro-detalhado-de-transações-realizadas-rf011-e-rf012)
    * [8.2. Testes Não Funcionais](#82-testes-não-funcionais)
    * [8.3. Testes de API](#83-testes-de-api)
9.  [Sugestões de Melhorias](#9-sugestões-de-melhorias)
    * [9.1. Melhorias na API REST](#91-melhorias-na-api-rest)
    * [9.2. Melhorias na Interface do Usuário (UI) e Funcionalidades Gerais](#92-melhorias-na-interface-do-usuário-ui-e-funcionalidades-gerais)
10. [Considerações Finais](#10-considerações-finais)

---

## 1. Introdução

Este plano de teste descreve a estratégia de testes adotada para garantir a qualidade do sistema de controle de estoque do Instituto Joga Junto. O objetivo é assegurar que o produto atenda integralmente aos requisitos funcionais e não funcionais estabelecidos, com base nas normas ISO/IEC 29119, ISO/IEC 25010 e processos definidos na ISO/IEC 12207.

---

## 2. Arquitetura do Sistema Alvo

O sistema está estruturado como uma aplicação web em ambiente de testes, com backend e API REST documentada via Swagger, hospedada em nuvem. A arquitetura integra módulos de cadastro de usuários, produtos, autenticação e atualização de estoque em tempo real.

---

## 3. Ferramentas de Testes

Serão utilizadas as seguintes ferramentas para testes:

| Tipo de Teste                 | Ferramenta                                                                                                |
| ----------------------------- | --------------------------------------------------------------------------------------------------------- |
| Testes de API                 | Postman (para design, execução manual/exploratória e scripts de teste), Newman (para execução CLI e relatórios), Python + requests + jsonschema (para automação complementar, se necessário) |
| Testes BDD (UI)               | Behave (cenários Gherkin)                                                                                 |
| Testes de Interface (UI)      | Selenium WebDriver + ChromeDriver                                                                         |
| Gerenciamento de Defeitos     | Issues do GitHub / Planilha Google Sheets (Report de Bug.xlsx)                                            |
| Relatórios                    | Newman (HTML - htmlextra), Markdown                                                                        |
| Ambiente de Teste (Frontend)  | [https://projetofinal.jogajuntoinstituto.org](https://projetofinal.jogajuntoinstituto.org)                |
| Documentação da API (Swagger) | [https://apipf.jogajuntoinstituto.org/swagger/](https://apipf.jogajuntoinstituto.org/swagger/)              |
| Teste de Performance Mobile   | Google Lighthouse (para mobile, verificando desempenho e otimizações para dispositivos Android)         |

**Nota:** O Google Lighthouse será utilizado para avaliar a qualidade geral da aplicação web (e sua visualização em mobile), verificando as métricas de desempenho, acessibilidade, práticas recomendadas e SEO. Essas métricas ajudarão a identificar melhorias técnicas e de usabilidade.

---

## 4. Estratégias de Testes

### 4.1. Tipos de Teste

-   **Funcionais:** Validação dos requisitos RF001 a RF012, cobrindo os fluxos de negócio principais da aplicação.
-   **Não Funcionais:** Foco em usabilidade, portabilidade (compatibilidade entre navegadores), acessibilidade e integração (NF001 a NF004).
-   **API:** Validação de endpoints da API REST (conforme Swagger) para verificar contratos (schemas), códigos de status HTTP, respostas para dados válidos e inválidos, autenticação e autorização.
-   **UI (Interface do Usuário):** Validação da navegação, consistência da identidade visual, interações do usuário e acesso por perfil através de testes manuais e automatizados (Behave/Selenium).

### 4.2. Técnicas Aplicadas (ISO/IEC 29119-4)

As seguintes técnicas de projeto de teste serão aplicadas:

-   **Particionamento de Equivalência:** Para reduzir o número de casos de teste, agrupando entradas com comportamentos esperados similares.
-   **Análise de Valor Limite:** Para focar testes em valores nas fronteiras das partições de equivalência, onde erros são mais comuns.
-   **Tabela de Decisão:** Para cenários com múltiplas condições e ações complexas.
-   **Teste Baseado em Comportamento (BDD):** Utilizando cenários Gherkin para descrever o comportamento esperado do sistema do ponto de vista do usuário (aplicado nos testes de UI com Behave).
-   **Teste Exploratório:** Aplicado para descobrir defeitos não cobertos por casos de teste formais, especialmente na UI e em fluxos de API.

### 4.3. Critérios de Prioridade

Os testes serão priorizados com base no risco e na criticidade das funcionalidades:

-   **Alta Prioridade:** Autenticação, restrições de acesso por perfil, funcionalidades CRUD (Criar, Ler, Atualizar, Deletar) de produtos, fluxo de cadastro de usuário.
-   **Média Prioridade:** Filtros de produtos, visualização de dados de perfil, funcionalidades de acompanhamento de pedidos.
-   **Baixa Prioridade:** Consistência da identidade visual, internacionalização (idioma), integração com sistemas externos (se mockada ou fora do escopo de controle direto).

---

## 5. Cronograma

| Atividade                    | Duração | Data de Início | Data de Término |
| ---------------------------- | ------- | -------------- | --------------- |
| Análise e Planejamento       | 1 dia   | 08/05/2025     | 08/05/2025      |
| Elaboração dos Casos de Teste | 2 dias  | 09/05/2025     | 10/05/2025      |
| Execução dos Testes          | 3 dias  | 11/05/2025     | 13/05/2025      |
| Coleta de Evidências         | 2 dias  | 13/05/2025     | 14/05/2025      |
| Relatórios e Entrega Final   | 1 dia   | 15/05/2025     | 15/05/2025      |

---

## 6. Métricas de Qualidade (ISO/IEC 25010)

As seguintes métricas serão utilizadas para avaliar a qualidade do produto:

-   **Cobertura de Requisitos Funcionais:** ≥ 90% dos RFs identificados devem ser cobertos por casos de teste.
-   **Taxa de Sucesso de Execução de Testes:** ≥ 95% dos casos de teste planejados (especialmente os de alta e média prioridade) devem passar.
-   **Bugs Críticos/Blocker em Produção (Critério de Saída):** 0 (Zero) bugs classificados como Críticos/Blocker podem estar presentes na versão a ser liberada.
-   **Conformidade com Usabilidade e Acessibilidade:** Avaliação através de checklist baseado nas diretrizes da ISO e execução de testes exploratórios focados nestes aspectos. Verificação manual + Google Lighthouse.
-   **Taxa de Aceitação (Critério de Saída):** Não serão aceitos bugs classificados como Blocker/Critical ou Grave que impeçam fluxos de negócio principais.
-   **Taxa de Aprovação dos Usuários (se aplicável em fase de Homologação):** Para o lançamento, usuários chave da versão em homologação devem relatar uma experiência satisfatória com os fluxos principais.

---

## 7. Classificação dos Bugs

Os defeitos encontrados serão classificados da seguinte forma:

-   **Blocker / Critical (Bloqueador / Crítico):** Impede o teste ou o uso de uma ou mais funcionalidades principais; não há workaround aceitável. O sistema não pode ser liberado com bugs desta natureza.
-   **Grave (High / Major):** Afeta severamente funcionalidades principais, mas existe um workaround (mesmo que difícil). O usuário consegue usar o sistema, mas com grande dificuldade em certas partes.
-   **Moderada (Medium / Normal):** Causa comportamento incorreto, mas não afeta funcionalidades principais; ou afeta funcionalidades menores. O impacto na experiência do usuário é perceptível, mas não impeditivo.
-   **Leve (Low / Minor):** Pequenos erros visuais, ortográficos, ou problemas de usabilidade que não afetam a funcionalidade, mas podem causar leve inconveniência.

**Tempo de Resposta para Correção dos Bugs (Sugestão):**

-   Blocker e Grave: Devem ser corrigidos com prioridade máxima (ex: em até 3 dias úteis).

**Nota:** Os bugs encontrados serão documentados em arquivos Markdown individuais na pasta `reports/bugs/` e sumarizados no `docs/RelatorioResumoTestes.md`.

---

## 8. Cenários de Testes

Esta seção detalha os cenários de teste que serão executados. Para os casos de teste manuais detalhados, consulte o arquivo [`docs/CasosDeTesteManuais.md`](./docs/CasosDeTesteManuais.md). Para os testes de API, consulte a collection Postman e o [`Tests/API/README_API_Tests.md`](./Tests/API/README_API_Tests.md).

### 8.1. Testes Funcionais

#### 8.1.1. Cadastro de Usuário (RF001 e RF003)

**Abordagem:**

* **Tipo de teste:** Funcional
* **Subtipo de teste:** Manual (UI), API (se endpoint disponível)
* **Objetivo dos testes:** Validar todo o fluxo de cadastro de usuário, garantindo que apenas administradores possam criar contas válidas e que sejam aplicadas as validações de e-mail corporativo (se aplicável), unicidade de e-mail e consistência de senha.
* **Output esperado:** Nenhum usuário deve ser criado se o perfil não for “admin”; e-mail não for corporativo (se regra); e-mail já existir; senha e confirmação divergirem. Em caso de sucesso, usuário criado corretamente. Em caso de falha, exibir mensagem apropriada.
* **Requisitos motivadores:** RF001 – “O sistema não deve permitir cadastro de usuário externo.”, RF003 – “O sistema permite cadastro de usuário apenas para administrador.”
* **Regra relacionada:** Usuário: Apenas colaboradores de vendas e estoque (e administradores) podem acessar o backoffice.

**Principais Casos de Teste (IDs do seu DOCX):**

* CAD-001: Cadastro de um novo usuário com perfil administrador.
* CAD-002: Colaborador não-admin tenta cadastrar novo usuário.
* CAD-003: Tentativa de cadastro sem perfil definido.
* CAD-004: Formulário de cadastro não exposto a usuário externo.
* CAD-005: Tentativa de cadastro com e-mail duplicado.
* CAD-006: Senha e confirmação de senha divergentes.
* CAD-007: SSO não permitido no backoffice.


**Exemplo para 8.1.2:**

#### 8.1.2. Login de usuário (RF-002)

**Abordagem:**

* **Tipo de teste:** Funcional
* **Subtipo de teste:** Manual (UI), API
* **Objetivo dos testes:** Validar o processo de login com e-mail e senha, cobrindo tanto tentativas válidas quanto falhas por campos inválidos, vazios ou conta restrita.
* **Output esperado:** Apenas usuários válidos e ativos conseguem autenticar-se com sucesso. O sistema deve exibir mensagens claras para falhas de autenticação.
* **Requisitos motivadores:** RF002 – “O sistema deve permitir login com e-mail e senha.”
* **Regra relacionada:** Apenas colaboradores autorizados e com conta ativa (vendas ou estoque) podem acessar o backoffice do sistema.

**Principais Casos de Teste (IDs do seu DOCX):**

* LOG-001: Login bem-sucedido com credenciais válidas.
* LOG-002: Login falha por e-mail inválido.
* LOG-003: Login falha por senha incorreta.
* LOG-004: Toggle visibilidade da senha.
* LOG-005: Login com campos em branco.
* LOG-006: Login com e-mail válido e senha vazia (ou tentativa de recuperação de senha).
* LOG-007: Login com conta bloqueada.
* LOG-008: Login com e-mail em formato inválido (repetido, avaliar se necessário ou se coberto por LOG-002).
* LOG-009: Login com Conta expirada.
* LOG-010: Falha de login com API indisponível.

---

### 8.2. Testes Não Funcionais

**Abordagem:**

* **Tipo de teste:** Não Funcional
* **Subtipo de teste:** Usabilidade, Portabilidade (Compatibilidade), Acessibilidade, Desempenho (Tempo de Sincronização/Resposta).
* **Objetivo dos testes:** Avaliar a conformidade do sistema com os atributos de qualidade definidos na norma ISO/IEC 25010: usabilidade, acessibilidade, compatibilidade e atualização em tempo real/performance.
* **Output esperado:** O sistema deve ser fácil de usar, funcionar corretamente nos navegadores alvo, permitir navegação por teclado e ser compatível com leitores de tela (como NVDA), e apresentar tempos de resposta aceitáveis para operações chave. O estoque deve ser atualizado automaticamente (se aplicável).
* **Requisitos motivadores:** NF001, NF002, NF003, NF004.
* **Regra relacionada:** Usuário, Produtos, Navegação e Estoque.

**Principais Casos de Teste (IDs do seu DOCX):**

* NF-0001: Compatibilidade da aplicação entre navegadores (listar navegadores alvo).
* NF-0002: Desempenho da busca de produtos com grande volume de dados.
* NF-0003: Responsividade em dispositivos mobile e tablet (listar dispositivos ou resoluções alvo).
* NF-0004 & NF-0005: Adaptação ao tema claro e escuro do sistema/navegador.
* NF-0006: Opções de tradução para colaboradores internacionais (se aplicável).
* NF-0007: Identidade visual da marca em todos os elementos.
* NF-0008: Integração com sistemas de vendas e financeiros (verificar se é teste de contrato API ou observação de logs).

---

### 8.3. Testes de API

**Abordagem:**

* **Tipo de teste:** Funcional (API)
* **Subtipo de teste:** API REST – Requisições HTTP (Postman/Newman)
* **Objetivo dos testes:** Validar se os endpoints da API implementados estão em conformidade com a documentação Swagger, retornando corretamente os dados esperados, os códigos de status HTTP apropriados para diversos cenários (sucesso, erro do cliente, erro do servidor), e se os esquemas JSON das respostas estão corretos. Validar autenticação e autorização.
* **Output esperado:** Para cada endpoint e cenário, espera-se o retorno do status HTTP adequado (200, 201, 400, 401, 403, 404, 409, 422, 5xx etc.), bem como uma estrutura JSON no corpo da resposta que seja aderente ao contrato definido no Swagger. Mensagens de erro devem ser claras e em formato JSON.
* **Requisitos motivadores:** Funcionalidades da aplicação que dependem da API, Requisitos Não Funcionais (NF001-NF004 implicitamente).
* **Regra relacionada:** Usuário (controle de acesso via API), Produtos (manipulação e visualização via API), Navegação (se controlada ou influenciada por dados da API), Estoque (visibilidade e integridade dos dados via API).

**Casos de Teste de API (IDs do seu DOCX):**
*Referenciar o arquivo [`Tests/API/README_API_Tests.md`](./Tests/API/README_API_Tests.md) e a collection Postman para os detalhes dos testes de API.*

* API-0001: Disponibilidade da API (`GET /api`).
* API-0002: Tentativa de acesso a endpoint inexistente (`GET /apii` - esperando 404).
* API-0003: Autenticação com sucesso (`POST /login` - credenciais válidas).
* API-0004: Autenticação com senha incorreta (`POST /login`).
* API-0005: Autenticação com JSON incompleto (`POST /login` - faltando email ou senha).
* API-0006: Autenticação com corpo de requisição em formato inválido (`POST /login` - ex: texto puro).
* API-0007: Registro de usuário com dados válidos (`POST /register`).
* API-0008: Registro com email duplicado (`POST /register`).
* API-0009: Registro com campos obrigatórios ausentes (`POST /register` - email ou senha faltando).
* API-0010: Registro com formato de e-mail inválido (`POST /register`).
* API-0011: Listagem de produtos com Token Válido (`GET /produtos`).
* API-0012: Acesso à listagem de produtos sem Token (`GET /produtos`).
* API-0013: Acesso à listagem de produtos com Token Inválido (`GET /produtos`).
* API-0014: Listagem de produtos resultando em array vazio (após limpar produtos do usuário).
* API-0015: Validação de Campos Obrigatórios na resposta da listagem de produtos.
* API-0016: Cadastrar Produto Válido (`POST /` ou `POST /produtos` - verificar endpoint correto no Swagger).
* API-0017: Cadastro de produto com campos Obrigatórios em Branco.
* API-0018: Cadastro de produto com Preço Inválido (formato texto).
* API-0019: Cadastro de produto com Categoria Inexistente.
* API-0020: Upload de Imagem no cadastro de produto.
* API-0021 (repetido? parece com API-0025): Deletar Produto com Token Inválido.
* API-0022: Deletar Produto Válido (`DELETE /{produtoId}`).
* API-0023: Deletar Produto Inexistente (`DELETE /{produtoId}`).
* API-0024: Deletar Produto acessando sem token.
* API-0025: Deletar Produto usando token Inválido (verificar diferença com API-0021 e API-0023).
* API-0026: Deletar Produto com formato de `produtoId` Inválido.

---

## 9. Sugestões de Melhorias

Esta seção consolida as sugestões de melhoria identificadas durante a análise do sistema e planejamento/execução dos testes, visando aprimorar a usabilidade, segurança e robustez do Sistema de Controle de Estoque do Instituto Joga Junto.

### 9.1. Melhorias na API REST

#### 9.1.1. Padronização e Semântica de Status Codes HTTP

* **Observação:** A API apresentou inconsistências no uso de status codes HTTP (ex: 200 OK para operações falhas de login, 500 Internal Server Error para erros de validação de entrada). Uso de 403 Forbidden onde 401 Unauthorized seria mais preciso.
* **Recomendação:** Revisar e alinhar todos os endpoints para utilizar os status codes HTTP conforme as melhores práticas RESTful (ex: 401 para falhas de autenticação, 400/422 para erros de validação do cliente, 404 para recurso não encontrado, 201 para criação bem-sucedida).
* **Referência ISO/IEC 25010:** Confiabilidade (Maturidade), Usabilidade (Operabilidade para desenvolvedores).

#### 9.1.2. Consistência e Clareza das Mensagens de Erro

* **Observação:** Mensagens de erro genéricas, irrelevantes e, em alguns casos, respostas de erro em texto puro (Forbidden) quando a API majoritariamente retorna JSON.
* **Recomendação:** Padronizar todas as respostas de erro da API para o formato JSON, contendo uma mensagem clara, específica ao contexto do erro. Considerar a inclusão de códigos de erro internos.
* **Referência ISO/IEC 25010:** Usabilidade (Inteligibilidade, Operabilidade).

#### 9.1.3. Segurança - Autenticação e Autorização

* **Observação CRÍTICA:** O endpoint `DELETE /{produtoId}` permite a exclusão de produtos sem qualquer token de autenticação.
* **Recomendação:** Implementar e impor a verificação obrigatória de token de autenticação JWT válido em todos os endpoints que manipulam dados (POST, PUT, DELETE) ou expõem dados sensíveis. Avaliar a necessidade de mecanismos de autorização baseados em papéis/permissões.
* **Referência ISO/IEC 25010:** Segurança (Confidencialidade, Integridade, Autenticidade, Responsabilidade).

#### 9.1.4. Tratamento Robusto de Entradas Inválidas

* **Observação CRÍTICA:** Múltiplos cenários com entradas inválidas resultaram em 500 Internal Server Error.
* **Recomendação:** Fortalecer a validação de entrada em todos os endpoints. Rejeitar requisições inválidas com status codes 4xx apropriados e mensagens de erro claras.
* **Referência ISO/IEC 25010:** Confiabilidade (Tolerância a Falhas, Maturidade).

#### 9.1.5. Lógica de Negócio para IDs Inexistentes

* **Observação:** API `DELETE /{produtoId}` retorna 200 OK mesmo ao tentar deletar um `produtoId` inexistente.
* **Recomendação:** API deve retornar 404 Not Found para operações em recursos específicos inexistentes.
* **Referência ISO/IEC 25010:** Adequação Funcional (Corretude).

#### 9.1.6. Tipo de Dados para Campos Monetários

* **Observação:** Campos `price` e `shipment` retornados como strings.
* **Recomendação:** Considerar retornar campos monetários como tipo numérico ou documentar a decisão se a string for intencional.
* **Referência ISO/IEC 25010:** Usabilidade (Operabilidade).

#### 9.1.7. Documentação da API (Swagger)

* **Observação:** Pequenas inconsistências entre descrições, exemplos e divergências de endpoints.
* **Recomendação:** Manter a documentação Swagger rigorosamente atualizada, precisa e refletindo a implementação real.
* **Referência ISO/IEC 25010:** Manutenibilidade (Analisabilidade), Usabilidade.

### 9.2. Melhorias na Interface do Usuário (UI) e Funcionalidades Gerais

#### 9.2.1. Tratamento de Erros da API na Interface

* **Observação:** Falta de feedback ao usuário na UI para erros da API (ex: erro 502 no login).
* **Recomendação:** Implementar tratamento de erro robusto na UI com mensagens amigáveis.

#### 9.2.2. Segurança de Contas de Usuário

* **Observação:** Ausência de política de complexidade de senha e recuperação de senha.
* **Recomendação:** Implementar política de senha forte e fluxo de recuperação de senha.
* **Referência ISO/IEC 25010:** Segurança.

#### 9.2.3. Validação de Dados e Usabilidade em Formulários

* **Observação:** Campo "Frete" aparentemente irrelevante; falta de indicação de campos obrigatórios; inconsistência de idioma nas validações UI; ausência de validação de produtos duplicados e limite na descrição.
* **Recomendação:** Revisar campo "Frete"; sinalizar campos obrigatórios; padronizar idioma das mensagens; implementar validação de unicidade de produtos e limite na descrição.
* **Referência ISO/IEC 25010:** Usabilidade, Adequação Funcional.

#### 9.2.4. Escopo da Consulta de Produtos

* **Observação:** API `GET /produtos` retorna apenas produtos do usuário autenticado.
* **Recomendação:** Clarificar com stakeholders se perfis admin devem ver todos os produtos e planejar ajuste se necessário.

---

## 10. Considerações Finais

O ciclo de testes para o Sistema de Controle de Estoque IJJ foi crucial para avaliar a qualidade da aplicação, com foco especial na API REST. Embora o escopo original fosse amplo, a profundidade dos problemas na API direcionou maior esforço para esta camada.

Técnicas como particionamento de equivalência e análise de valor limite foram aplicadas, principalmente via Postman. A estratégia cobriu fluxos de autenticação, gerenciamento de usuários (implícito), consulta, cadastro e exclusão de produtos.

Os resultados revelaram que, enquanto algumas funcionalidades da API funcionam para cenários de sucesso, foram identificados **[Número Total de Bugs, ex: cinquenta e nove]** bugs, dos quais **[Número, ex: Quatorze]** são classificados como Críticos/Blocker e **[Número, ex: vinte e um]** como Graves.

**Principais Problemas Encontrados:**

* **Falhas de Segurança Graves:** Ex: Deleção de produtos via API sem autenticação.
* **Instabilidade da API:** Ocorrência de erros 500 Internal Server Error em múltiplos cenários. O endpoint de cadastro de produto (`POST /` ou `POST /produtos`) ficou bloqueado para validação de campos devido a erros 500 em tentativas autenticadas.
* **Inconsistências no Tratamento de Erros:** Uso incorreto de status codes HTTP e mensagens de erro inconsistentes.
* **Problemas de Lógica de Negócio:** Ex: Permissão para "deletar" produtos com IDs inexistentes resultando em sucesso (200 OK).

Apesar dos desafios, os testes geraram informações valiosas. Os testes de API foram documentados no Postman, e os defeitos registrados. A automação de UI (Python, Selenium, Behave) teve sua estrutura inicial e cenários Gherkin desenvolvidos para fluxos críticos; sua implementação completa é recomendada após a estabilização da API.

**Conclui-se que o sistema possui vulnerabilidades e instabilidades significativas em sua API e interface que necessitam de correção urgente.** As "Sugestões de Melhorias" oferecem um roteiro para o aprimoramento. Recomenda-se priorizar a correção dos bugs críticos/graves. Após correções, um ciclo completo de re-testes e testes de regressão será essencial. A expansão dos testes automatizados (API e UI) é fortemente recomendada.

Este esforço de teste cumpriu seu objetivo de diagnosticar a qualidade do software e fornecer direcionamentos para melhoria.
