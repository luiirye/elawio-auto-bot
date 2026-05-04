import time
from src.app.browser import Navegador
from src.app.login import Login
from src.app.alterar_fases import Fases
from src.app.dados_excel import LeituraDeDados

# Inicialização dos componentes
nav = Navegador()
login = Login(nav.driver)
dados = LeituraDeDados()

caminho = input("Digite o caminho da pasta (completo) onde se encontra os arquivos excel: ")
#Exemplo:  C:\\Users\\ADVOCACIA\\Documents\\LuisFelipe\\dev\\projetos\\elawio-auto\\data\\base.xlsx

print("=" * 50)
dados.ler_dados(caminho)

# Extração de dados via Pandas
url_home = dados.extrair_home_url()
lista_pastas = dados.extrair_urls_pastas()
email, senha = dados.extrair_credenciais()

# CAPTURA AS FASES EXTRAÍDAS DO EXCEL
# retorna uma lista de IDs como ['bs-select-9-25', ...]
lista_de_fases = dados.extrair_fases() 

print("=" * 100)
print(f"Foram encontradas {len(lista_pastas)} pastas para processar.")
print("=" * 100)

print(f'Navegando até a tela inicial: {url_home}')
nav.go_to_page(url_home)
time.sleep(5)

print(f'Login: {email}')
if not email or not senha:
    raise ValueError("Credenciais ausentes na planilha. Verifique as colunas 'email' e 'senha'.")

login.executar_login(email, senha) 
print("Efetuando login...")
time.sleep(5) 


for i, url_pasta in enumerate(lista_pastas):
    print("=" * 100)
    print(f'Navegando dentro da pasta: {url_pasta}')
    nav.go_to_page(url_pasta)
    time.sleep(5)

    try:
        fase_automacao = Fases(nav.driver)
        print("Abrindo o menu...")
        fase_automacao.abrir_menu()
        time.sleep(5)
        
        if lista_de_fases and i < len(lista_de_fases):
            fase_id = lista_de_fases[i]
            print(f"Selecionando fase com ID: {fase_id}...")
            
            fase_automacao.seleciona_fase(fase_id) 
            print("Fase alterada com sucesso!")
            
        else:
            print("Aviso: Nenhuma fase encontrada no Excel para esta pasta.")
        
    except Exception as e:
        print(f"Falha ao alterar fase na pasta {url_pasta}. Erro: {e}")
        
    time.sleep(5)

print("=" * 100)
print("Automação finalizada com sucesso!")

input("Pressione qualquer tecla para encerrar o browser")
nav.fechar()