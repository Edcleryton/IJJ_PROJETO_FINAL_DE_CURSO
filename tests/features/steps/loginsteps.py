# features/steps/login_steps.py
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Assume que você tem uma URL base e WebDriver configurado
BASE_URL = "https://projetofinal.jogajuntoinstituto.org" # URL do seu ambiente de teste UI
# driver = webdriver.Chrome() # Ou outro driver

@given('que o usuário está na página de login')
def step_impl(context):
    context.driver = webdriver.Chrome() # Iniciar aqui ou globalmente
    context.driver.get(BASE_URL + "/login") # Ajuste o path se necessário

@when('ele preenche o campo "{field_name}" com "{value}"')
def step_impl(context, field_name, value):
    # Você precisará dos seletores corretos (ID, name, XPath, etc.)
    if field_name == "email":
        element = context.driver.find_element(By.ID, "email_input_id") # Exemplo de ID
    elif field_name == "senha":
        element = context.driver.find_element(By.ID, "password_input_id") # Exemplo de ID
    else:
        raise NotImplementedError(f'Campo "{field_name}" não implementado')
    element.send_keys(value)

@when('ele clica no botão "{button_name}"')
def step_impl(context, button_name):
    # Seletor do botão
    if button_name == "Iniciar sessão":
        button = context.driver.find_element(By.XPATH, "//button[contains(text(),'Iniciar sessão')]") # Exemplo de XPath
        button.click()
    else:
        raise NotImplementedError(f'Botão "{button_name}" não implementado')

@then('ele deve ser redirecionado para o dashboard')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.url_contains("/dashboard") # Ajuste a URL do dashboard
    )
    assert "/dashboard" in context.driver.current_url

@then('ele deve ver a mensagem "{message}"')
def step_impl(context, message):
    # Precisa do seletor do elemento da mensagem
    welcome_message_element = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "welcome_message_id")) # Exemplo
    )
    assert message.replace("[Nome do Usuário]", "Nome Esperado") in welcome_message_element.text # Ajuste para nome real
    # context.driver.quit() # Fechar o navegador ao final do cenário