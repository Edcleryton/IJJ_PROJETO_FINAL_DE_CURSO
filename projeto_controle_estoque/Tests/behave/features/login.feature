Feature: Login de Usuário no Sistema IJJ

  Scenario: Tentativa de login com credenciais inválidas
    Given que eu estou na página de login do IJJ
    When eu preencho o campo de email com "usuario@invalido.com"
    And eu preencho o campo de senha com "senhaSuperErrada123"
    And eu clico no botão "Entrar"
    Then eu devo ver uma mensagem de erro de login como "E-mail ou senha inválidos."