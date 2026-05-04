import time
from selenium.webdriver.common.by import By


class Processos():

    # Recebe o driver do Navegador para usar o navegador já aberto
    def __init__(self, driver):
        self.driver = driver

    def abrir_menu(self):
        # Clica no menu "Processos"
        menu = self.driver.find_element(By.CSS_SELECTOR, 'a[href="#processos"]')
        menu.click()
        time.sleep(5)

    def consultar(self):
        # Clica na opção "Consultar"
        consultar = self.driver.find_element(
            By.XPATH, '//a[@href="/processo/list?cache=false"]'
        )
        self.driver.execute_script("arguments[0].click()", consultar)

    def executar_processos(self):
        # Executa a navegação completa até Consultar
        self.abrir_menu()
        self.consultar()