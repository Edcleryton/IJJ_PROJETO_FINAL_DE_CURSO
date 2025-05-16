from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

BASE_URL = "https://projetofinal.jogajuntoinstituto.org" # Confirme esta URL

@given('que o usuário está na página de login "{page_path}"')
def step_visit_login_page(context, page_path):
    context.driver.get(BASE_URL + page_path)

@when('ele preenche o campo de email com "{email}"')
def step_fill_email(context, email):
    # Assumindo que os IDs dos campos são 'email' e 'password'
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "email"))
    ).send_keys(email)

@when('ele preenche o campo de senha com "{password}"')
def step_fill_password(context, password):
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "password"))
    ).send_keys(password)

@when('ele clica no botão "{button_text}"')
def step_click_button(context, button_text):
    # Usar XPath para encontrar botão pelo texto é uma opção, mas ID/name é melhor se disponível
    button_xpath = f"//button[contains(text(),'{button_text}') or @value='{button_text}' or @id='btn_{button_text.lower().replace(' ', '_')}']" # Tentar algumas opções
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, button_xpath))
    ).click()

@then('ele deve ser redirecionado para a página de dashboard "{page_path}"')
def step_redirected_to_dashboard(context, page_path):
    WebDriverWait(context.driver, 10).until(
        EC.url_contains(page_path)
    )
    assert page_path in context.driver.current_url

@then('ele deve ver uma mensagem de boas-vindas contendo seu nome')
def step_see_welcome_message(context):
    # Precisa do seletor da mensagem de boas-vindas
    welcome_element_selector = (By.XPATH, "//*[contains(text(),'Bem-vindo')]") # Exemplo
    message = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located(welcome_element_selector)
    ).text
    # Aqui você precisaria de uma forma de obter o nome esperado do usuário, ou apenas verificar "Bem-vindo"
    assert "Bem-vindo" in message
