Feature: Login de Usuário no Sistema IJJ

  Scenario: Login com credenciais válidas
    Given que eu estou na página de login do IJJ
    When eu preencho o campo de email com "macaco@gmail.com"
    And eu preencho o campo de senha com "senha123"
    And eu clico no botão "Entrar"
    Then eu devo ver o botão "Adicionar"
