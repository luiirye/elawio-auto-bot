from selenium.webdriver.common.by import By


class Login():

    # Recebe o driver do Navegador para usar o navegador já aberto
    def __init__(self, driver):
        self.driver = driver

    def preencher(self, email, senha):
        # Encontra os campos e preenche com email e senha
        campo_email = self.driver.find_element(By.ID, "Email")
        campo_senha = self.driver.find_element(By.ID, "Password")

        campo_email.send_keys(email)
        campo_senha.send_keys(senha)

    def entrar(self):
        # Clica no botão de login
        botao = self.driver.find_element(By.ID, "btn-login")
        botao.click()

    def executar_login(self, email, senha):
        # Recebe credenciais externamente (Excel ou ambiente)
        self.preencher(email, senha)
        self.entrar()

        print("Login realizado com sucesso!")