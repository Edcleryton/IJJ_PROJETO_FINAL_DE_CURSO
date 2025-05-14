from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("BASE_URL")

@given('que eu estou na página de login do IJJ')
def step_impl(context):
    options = webdriver.ChromeOptions()
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    context.driver.maximize_window()
    context.driver.get(BASE_URL)

@when('eu preencho o campo de email com "{email}"')
def step_impl(context, email):
    context.driver.find_element(By.NAME, "email").send_keys(email)

@when('eu preencho o campo de senha com "{senha}"')
def step_impl(context, senha):
    context.driver.find_element(By.ID, "outlined-adornment-password").send_keys(senha)

@when('eu clico no botão "Entrar"')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[contains(text(), 'Iniciar sessão')]").click()

@then('eu devo ver o botão "Adicionar"')
def step_impl(context):
    try:
        wait = WebDriverWait(context.driver, 10)
        # Localiza o botão pelo texto visível
        adicionar_button = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(., 'Adicionar')]"))
        )
        assert adicionar_button.is_displayed(), "O botão 'Adicionar' não está visível após o login."
    finally:
        context.driver.quit()