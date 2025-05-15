# 📄 Plano de Teste – Sistema de Controle de Estoque – Instituto Joga Junto  
**Versão:** 1.0  
**Data de versão:** 08/05/2025  
**Autores:** Edcleryton da Silva, Danilo Melin, Daniel Ilha

---

## 1. Introdução

Este plano de teste descreve a estratégia de testes adotada para garantir a qualidade do sistema de controle de estoque do Instituto Joga Junto.  
O objetivo é assegurar que o produto atenda integralmente aos requisitos funcionais e não funcionais estabelecidos, com base nas normas:

- ISO/IEC 29119  
- ISO/IEC 25010  
- ISO/IEC 12207

---

## 2. Arquitetura do Sistema

Aplicação web com backend e API REST hospedados em nuvem, documentada via Swagger.  
Módulos integrados:
- Cadastro de usuários
- Cadastro de produtos
- Autenticação
- Atualização de estoque em tempo real

---

## 3. Ferramentas de Teste

| Tipo                      | Ferramenta                              |
|---------------------------|------------------------------------------|
| Testes de API             | Python + requests + jsonschema          |
| Testes BDD                | Behave (cenários Gherkin)               |
| Testes de Interface       | Selenium WebDriver + ChromeDriver       |
| Gerenciamento de Defeitos | Google Sheets                           |
| Relatórios                | Markdown + tabulate                     |
| Ambiente de Teste         | https://projetofinal.org                |
| Swagger da API            | https://apipf.example/swagger/          |

---

## 4. Estratégia de Teste

### 4.1 Tipos de Teste

- **Funcionais**: RF0002 a RF0012  
- **Não-funcionais**: usabilidade, portabilidade, acessibilidade e integração (NF0001 a NF0004)  
- **API**: endpoints, esquemas e códigos de status  
- **UI**: navegação, identidade visual, perfis de acesso

### 4.2 Técnicas Aplicadas (ISO/IEC 29119-4)

- Particionamento de equivalência  
- Análise de valor-limite  
- Tabela de decisão  
- Teste baseado em comportamento (Gherkin)

### 4.3 Critérios de Prioridade

- **Alta**: autenticação, restrições de acesso, CRUD de produtos  
- **Média**: filtros e visualização de dados  
- **Baixa**: identidade visual, idioma, integrações externas

---

## 5. Cronograma

| Atividade               | Início       | Término     |
|-------------------------|--------------|-------------|
| Análise e planejamento  | 08/05/2025   | 08/05/2025  |
| Elaboração dos casos    | 09/05/2025   | 10/05/2025  |
| Execução dos testes     | 11/05/2025   | 13/05/2025  |
| Coleta de evidências    | 13/05/2025   | 14/05/2025  |
| Relatórios e entrega    | 15/05/2025   | 15/05/2025  |

---

## 6. Métricas de Qualidade (ISO/IEC 25010)

- **Cobertura de requisitos**: ≥ 90%  
- **Taxa de sucesso de execução**: ≥ 95%  
- **Bugs críticos permitidos**: 0  
- **Usabilidade e acessibilidade**: checklist ISO + verificação manual

---

## 7. Casos de Teste Prioritários

### TC001 – Login com credenciais válidas (RF0002)
- **Pré-condição**: usuário válido já cadastrado  
- **Ação**: POST em `/login`  
- **Esperado**: status 200 + retorno de token JWT  
- **Técnica**: Particionamento de equivalência

### TC002 – Cadastro de produto com dados válidos (RF0004)
- **Pré-condição**: admin autenticado  
- **Ação**: POST em `/produtos` com nome, categoria, preço e estoque  
- **Esperado**: status 201 + dados corretos gravados  
- **Técnica**: Valor-limite e equivalência

### TC003 – Restrições de acesso a usuários externos (RF0001, RF0003)
- **Pré-condição**: login como usuário comum  
- **Ação**: tentar POST em `/usuarios`  
- **Esperado**: status 403  
- **Técnica**: Tabela de decisão

---

## 8. Classificação de Defeitos

| Classificação     | Descrição                                                      |
|-------------------|----------------------------------------------------------------|
| Blocker/Critical  | Impede o uso do sistema (ex: login inoperante)                |
| Alta              | Impede funções principais (ex: cadastro de produto inoperante) |
| Média             | Função disponível com erros de retorno ou exibição            |
| Baixa             | Erros visuais ou ortográficos sem impacto funcional           |

---

## 9. Considerações Finais

Este plano foi elaborado com base nas melhores práticas e normas da engenharia de software aplicáveis à qualidade, com foco em:

- Cobertura de testes  
- Rastreabilidade  
- Clareza de documentação  
- Priorização de riscos  

Todos os testes serão mantidos em repositório estruturado, com evidências e relatórios conforme descrito, garantindo a confiabilidade e a entrega segura do projeto.
