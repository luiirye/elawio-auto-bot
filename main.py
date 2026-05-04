import time
from src.app.browser import Navegador
from src.app.login import Login
from src.app.alterar_fases import Fases
from src.app.dados_excel import LeituraDeDados

def executar_automacao(caminho_excel):
    # Inicialização dos componentes
    nav = Navegador()
    login = Login(nav.driver)
    dados = LeituraDeDados()

    try:
        print("=" * 50)
        dados.ler_dados(caminho_excel)

        # Extração de dados via Pandas
        url_home = dados.extrair_home_url()
        lista_pastas = dados.extrair_urls_pastas()
        email, senha = dados.extrair_credenciais()
        lista_de_fases = dados.extrair_fases()

    
        # raise ValueError("Teste de erro: URL inicial ausente na planilha (coluna 'urls').")  # Teste de erro para URL inicial ausente
        if not url_home:
            raise ValueError("URL inicial ausente na planilha (coluna 'urls').")
        if not lista_pastas:
            raise ValueError("Nenhuma pasta encontrada na planilha (coluna 'urls').")
        if not email or not senha:
            raise ValueError("Credenciais ausentes na planilha. Verifique as colunas 'email' e 'senha'.")

        print("=" * 100)
        print(f"Foram encontradas {len(lista_pastas)} pastas para processar.")
        print("=" * 100)

        print(f'Navegando até a tela inicial: {url_home}')
        nav.go_to_page(url_home)
        time.sleep(5)

        print(f'Login: {email}')
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

                if i < len(lista_de_fases):
                    fase_id = lista_de_fases[i]
                    print(f"Selecionando fase com ID: {fase_id}...")
                    fase_automacao.seleciona_fase(fase_id)
                    print("Fase alterada com sucesso!")
                else:
                    print("Aviso: Nenhuma fase encontrada no Excel para esta pasta.")

            except Exception as erro:
                print(f"Falha ao alterar fase na pasta {url_pasta}. Erro: {erro}")

            time.sleep(5)

        print("=" * 100)
        print("Automação finalizada com sucesso!")
    finally:
        input("Pressione qualquer tecla para encerrar o browser")
        nav.fechar()


if __name__ == "__main__":
    caminho = input(
        "Digite o caminho completo do arquivo Excel (ex: C:\\Users\\...\\base.xlsx): "
    )
    executar_automacao(caminho)