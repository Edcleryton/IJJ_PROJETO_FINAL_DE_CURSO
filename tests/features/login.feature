# features/login.feature
Feature: Login de Usuário

  Scenario: Login bem-sucedido com credenciais válidas
    Given que o usuário está na página de login
    When ele preenche o campo "email" com "usuario_valido@exemplo.com"
    And ele preenche o campo "senha" com "senha_correta"
    And ele clica no botão "Iniciar sessão"
    Then ele deve ser redirecionado para o dashboard
    And ele deve ver a mensagem "Bem-vindo, [Nome do Usuário]"