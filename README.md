# 🚀 Projeto final do curso QA Avançado - Instituto Joga Junto 🐍

![Build](https://img.shields.io/badge/build-n/a-lightgrey)
![Coverage](https://img.shields.io/badge/coverage-0%25-lightgrey)
![Python](https://img.shields.io/badge/python-3.13.1-blue)
![License](https://img.shields.io/badge/license-MIT-green)

<h1 align="center">
  <a href="https://github.com/seu-usuario/projeto-final-python">🔗 Projeto Final Python</a>
</h1>
<p align="center">Projeto final do curso QA Avançado, focado na garantia de qualidade do sistema de controle de estoque do Instituto Joga Junto. Reúne planos de teste, casos de teste manuais e automatizados (Selenium e Behave), relatórios de bugs, estatísticas de testes e cobertura. O principal objetivo é validar requisitos, criar plano de testes completo e gerar estatísticas de bugs para a próxima sprint.</p>

---

## 📝 Índice

* [Introdução](#introdução)
* [Descrição](#descrição)
* [Cronograma](#cronograma)
* [Tecnologias](#tecnologias)
* [configuração](#configuração)
* [Instalação](#instalação)
* [Uso](#uso)
* [Testes](#testes)
* [Cobertura](#cobertura)
* [Funcionalidades](#funcionalidades)
* [Status do Projeto](#status-do-projeto)
* [Contribuição](#contribuição)
* [FAQ](#faq)
* [Licença](#licença)
* [Autores e Contato](#autores-e-contato)
* [Créditos e Agradecimentos](#créditos-e-agradecimentos)
* [Conclusão](#conclusão)
* [Referências](#referências)


---

## 🌟 Introdução

Desafio final do módulo QA Avançado do Instituto Joga Junto. 
Este repositório organiza o fluxo completo de QA para o sistema de controle de estoque do Instituto Joga Junto. Inclui:

- Planejamento e documentação de testes manuais e automatizados
- Execução de cenários com Selenium e Behave
- Testes de API usando Python `requests`
- Relatórios de cobertura, bugs e métricas quantitativas.

---

## 📌 Descrição

Este repositório serve para validar e garantir a qualidade de todas as regras de negócio e requisitos do sistema de controle de estoque, conforme especificado:

### Regras de negócio principais
- **Acesso de usuário**: somente colaboradores do IJJ alocados em vendas e estoque podem acessar o backoffice.  
- **Atualização em tempo real**: produtos devem refletir alterações imediatamente após transações de e-commerce.  
- **Navegação multilingue**: interface deve oferecer opções de tradução e ser intuitiva globalmente.  
- **Organização de estoque**: localização de produtos em poucos cliques, de forma clara e eficiente.

### Requisitos Funcionais (RF)
- **RF0001**: não permitir cadastro de usuário externo.  
- **RF0002**: permitir login com e-mail e senha.  
- **RF0003**: cadastro de usuário apenas para administrador.  
- **RF0004**: permitir cadastro de produtos.  
- **RF0005**: permitir edição de produtos cadastrados.  
- **RF0006**: permitir filtragem de produtos por categoria.  
- **RF0007**: permitir filtragem de produtos por preço.  
- **RF0008**: permitir exclusão de produtos cadastrados.  
- **RF0009**: exibir dados do usuário em sua aba perfil.  
- **RF0010**: atualizar automaticamente a quantidade de produtos após cada transação.  
- **RF0011**: permitir acompanhamento de pedidos de compra e prazos de entrega.  
- **RF0012**: manter registro detalhado de todas as transações para auditoria.

### Requisitos Não-Funcionais (NF)
- **NF0001**: interface intuitiva e simples de usar.  
- **NF0002**: opções de tradução para colaboradores internacionais.  
- **NF0003**: identidade visual da marca presente em todos os elementos.  
- **NF0004**: integração eficiente com sistemas de vendas e financeiro.

---

## 📅 Cronograma

| Atividade                                                             | Duração | Início     | Término    |
| --------------------------------------------------------------------- | ------- | ---------- | ---------- |
| Análise da documentação, criação do repositório, definição dos testes | 1 dia   | 08/05/2025 | 08/05/2025 | 
| Redação do plano de testes, início dos testes manuais                 | 1 dia   | 09/05/2025 | 08/05/2025 |
| Continuação dos testes manuais + testes de API com requests           | 1 dia   | 10/05/2025 | 08/05/2025 |
| Implementação de testes automatizados viáveis com Python              | 1 dia   | 11/05/2025 | 09/05/2025 |
| Finalização do plano de teste e testes automatizados                  | 1 dia   | 12/05/2025 | 10/05/2025 |
| Execução completa dos testes, coleta de evidências                    | 1 dia   | 13/05/2025 | 11/05/2025 |
| Finalização de relatórios e bugreport                                 | 1 dia   | 14/05/2025 | 13/05/2025 |
|Revisão final, entrega e  apresentação                                 | 1 dia   | 15/05/2025 | 14/05/2025 |

---
## 🛠 Tecnologias

* Python 3.13.1
* Requests
* Selenium
* Behave
* pytest
* pytest-cov
* Git/GitHub

---

## ⚙️ Configuração

1. Crie e ative um virtualenv:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # ou .venv\Scripts\activate no Windows
 ´´´
2. Defina variáveis de ambiente:
   ```bash
   export BASE_URL=https://projetofinal.jogajuntoinstituto.org/
   export API_URL=https://apipf.jogajuntoinstituto.org/swagger/ 
   ```
3. Instale dependências:
   ```bash
   pip install -r requirements.txt 

---

## 📝 Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/projeto-final-python.git
   cd projeto-final-python
   ```
2. Instale dependências:

   ```bash
   pip install -r requirements.txt
   ```
> **Observação:** Dentro do virtualenv instalado, certifique-se de que as variáveis de ambiente estão configuradas.

---

## ▶️ Uso

Após configurar o ambiente (instalação + variáveis), você poderá executar os testes de diferentes formas:

📌 Testes de API com requests

Execute scripts de teste com chamadas diretas à API:

python tests/test_api_login.py
python tests/test_api_produtos.py

📌 Testes automatizados com Behave

Execute cenários em BDD:

behave features/

📌 Testes com Selenium

Scripts baseados em navegação automatizada (caso aplicável):

python tests/test_ui_login.py

Os testes devem retornar saídas padronizadas com logs e validações de status code e conteúdo de resposta.

---

## ✅ Testes

* Testes manuais descritos em `docs/test_plan.md`.
* Automatizados com Behave (cenários em `features/`) e Selenium (steps em `steps/`).
* Executar todos os testes:

  ```bash
  behave
  ```
---

📊 Cobertura

Run pytest with coverage to gerar relatório HTML e badge atualizada:
```bash
pytest --cov=src --cov-report=html:docs/coverage_report
```
Isso criará um relatório em docs/coverage_report/index.html e atualizará automaticamente o badge de cobertura.

Badge dinâmico (atualize manualmente no topo após geração):
```bash
![Coverage](https://img.shields.io/badge/coverage-<XX>%25-lightgrey)
```
Consulte o relatório em docs/coverage_report/index.html
---

## ✨ Funcionalidades

Este projeto abrange validação de funcionalidades essenciais do sistema de estoque:

Gerenciamento de usuários:

Autenticação via e-mail e senha (RF0002)

Cadastro restrito a administradores (RF0003)

Exibição de perfil de usuário (RF0009)

Operações de produtos:

Cadastro, edição e exclusão de produtos (RF0004, RF0005, RF0008)

Filtragem por categoria e preço (RF0006, RF0007)

Atualização automática de estoque após transações (RF0010)

Pedidos e transações:

Acompanhamento de pedidos de compra e prazos de entrega (RF0011)

Registro detalhado de todas as transações para auditoria (RF0012)

Internacionalização e interface:

Suporte a múltiplos idiomas (NF0002)

Interface intuitiva e identidade visual da marca (NF0001, NF0003)

Integração:

Comunicação com sistemas de vendas e financeiro (NF0004)

---

## 🚧 Status do Projeto

\:construction: Em desenvolvimento

---

## 👥 Contribuição

1. Fork deste repositório
2. `git checkout -b feature/nome-da-feature`
3. `git commit -m "feat: descrição da feature"`
4. `git push origin feature/nome-da-feature`
5. Abra Pull Request detalhando mudanças

---

## 📜 Licença

MIT License. Consulte o arquivo `LICENSE`.

---

## 👤 Autores e Contato
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/Edcleryton">
        <img src="https://avatars.githubusercontent.com/u/134793465?v=4" width="50px" alt="Edcleryton"/>
      </a>
      <br/>
      <a href="https://github.com/Edcleryton">Edcleryton</a>
    </td>
    <td align="center">
      <a href="https://github.com/daniloMelin">
        <img src="https://avatars.githubusercontent.com/u/127984038?v=4" width="50px" alt="Danilo Melin"/>
      </a>
      <br/>
      <a href="https://github.com/daniloMelin">Danilo Melin</a>
    </td>
    <td align="center">
      <a href="https://github.com/Priest-San">
        <img src="https://avatars.githubusercontent.com/u/204785556?v=4" width="50px" alt="Priest-San"/>
      </a>
      <br/>
      <a href="https://github.com/Priest-San">Priest-San</a>
    </td>
  </tr>
</table>
---

## ❓ FAQ

**P: Como atualizar dependências?**
R: Ajuste `requirements.txt` e rode `pip install -r requirements.txt`.

**P: Onde encontro os testes manuais?**
R: Em `docs/test_plan.md`.

---

## 🏆 Créditos e Agradecimentos

* Instituto Joga Junto: curso de QA básico e avançado.
* W3Schools: tutoriais de Python Requests
* Alura: guias de API em Python
* Comunidade Selenium e Behave for examples

---

## 🎯 Conclusão

Projeto de QA em Python para o Instituto Joga Junto. Contribuições e sugestões são bem-vindas. Dê uma ⭐ no repositório!

---

## 🔗 Referências

* [Python Requests](https://docs.python-requests.org)
* [Behave Docs](https://behave.readthedocs.io)
* [Selenium Docs](https://www.selenium.dev/docs/)
* [Guia de Markdown da Adobe](https://experienceleague.adobe.com/pt-br/docs/contributor/contributor-guide/writing-essentials/markdown)

---


