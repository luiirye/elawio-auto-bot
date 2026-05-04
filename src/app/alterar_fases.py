from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class Fases():
    # Recebe o driver do Navegador para usar o navegador já aberto
    
    
    
    def __init__(self, driver):
        self.driver = driver

    def abrir_menu(self):
        # Clica no menu "Fases"
        wait = WebDriverWait(self.driver, 10)
        menu = self.driver.find_element(By.ID, 'buttonAlterarFase')
        wait.until(EC.element_to_be_clickable(menu))
        menu.click()

    def seleciona_fase(self, id_fase):
        
        wait = WebDriverWait(self.driver, 10)
        
        # Clica em "Selecione")
        selecionar = self.driver.find_element(By.XPATH, '//button[contains(@class, "btn dropdown-toggle bs-placeholder btn-default")]')
        wait.until(EC.element_to_be_clickable(selecionar))
        selecionar.click()
        
        # Clica na fase do menu
        fase = self.driver.find_element(By.ID, id_fase)
        wait.until(EC.element_to_be_clickable(fase))
        fase.click()
        
        # Clica no botão de Salvar
        salvar = self.driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary.salvar')
        salvar.click()
        