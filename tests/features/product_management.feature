Feature: Gerenciamento de Produtos

  Background: Usuário está logado
    Given que o usuário está na página de login "/login"
    When ele preenche o campo de email com "usuario_valido_para_produtos@exemplo.com"
    And ele preenche o campo de senha com "senha_correta_produtos"
    And ele clica no botão "Entrar"
    Then ele deve ser redirecionado para a página de dashboard "/dashboard"

  Scenario: Tentativa de cadastro de produto com dados válidos
    Given que o usuário está na página de listagem de produtos "/products" # Ajuste o path
    When ele clica no botão "Adicionar Produto"
    Then ele deve ser redirecionado para a página de cadastro de produto "/products/new" # Ajuste
    When ele preenche o campo "Nome do Produto" com "Camiseta Teste UI"
    And ele preenche o campo "Descrição" com "Descrição da camiseta de teste via UI"
    And ele preenche o campo "Preço" com "59.90"
    And ele seleciona a categoria "Roupas"
    And ele preenche o campo "Frete" com "10.00"
    And ele faz upload do arquivo de imagem "caminho/para/imagem_teste.png" no campo "Imagem do Produto"
    And ele clica no botão "Salvar Produto"
    Then ele deve ver uma mensagem de "Produto cadastrado com sucesso!" # OU uma mensagem de erro da API, que validaremos como UI tratando o erro

  Scenario: Tentativa de exclusão de produto existente
    Given que existe um produto com nome "Produto para Deletar via UI" na listagem "/products"
    When o usuário clica no ícone de "excluir" para o produto "Produto para Deletar via UI"
    And o usuário confirma a exclusão na caixa de diálogo
    Then o produto "Produto para Deletar via UI" não deve mais ser visível na listagem "/products"
    And ele deve ver uma mensagem de "Produto excluído com sucesso!"