from selenium import webdriver


class Navegador():

    # Cria e armazena o navegador ao inicializar
    def __init__(self):
        self.driver = webdriver.Chrome()

    # Navega até a URL recebida
    def go_to_page(self, url):
        self.driver.get(url)

    # Encerra o navegador
    def fechar(self):
        self.driver.quit()