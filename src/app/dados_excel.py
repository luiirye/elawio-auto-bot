import pandas as pd

class LeituraDeDados:
    
    def __init__(self, caminho=None): # caminho = none inicia vazio pois o caminho só será definido quando informado pelo usuário na função main
        self.df = None # iniciado como vazio
        # Usar df (dataframe) é o padrão no pandas
        # df -> Estrutura de dados principal do Pandas, para trabalhar com dados tabulares (tabelas, linhas, colunas)
        self.caminho = caminho # -> Armazena o endereço informado da planilha a ser lida
        
    def ler_dados(self, caminho):
        
        try:
            # Tenta realizar essa operação
            self.df = pd.read_excel(caminho) # -> Lê o arquivo Excel e armazena na variável do dataframe
            print('Planilha lida com sucesso!')
        
        except Exception as erro:
            # Caso a operação "try" falhe, o bloco "except" será executado. O erro da quebra será armazenado na variável "erro" e exibido no console
            print(f"Erro ao ler o arquivo: {erro}")
            
        return self.df

    def _get_coluna(self, *nomes):
        """
        Busca coluna de forma case-insensitive e ignora espacos extras.
        Ex.: "URLS", "urls", " Urls ".
        """
        if self.df is None:
            return None

        colunas_normalizadas = {
            str(col).strip().lower(): col for col in self.df.columns
        }

        for nome in nomes:
            coluna = colunas_normalizadas.get(str(nome).strip().lower())
            if coluna is not None:
                return coluna
        return None
            
    def extrair_home_url(self):
        
        # Extrai a URL da página inicial para login
        
        coluna_urls = self._get_coluna('urls')
        if coluna_urls is not None:
            print("Coluna 'urls' encontrada. Extraindo URL da página inicial para login")
            return self.df[coluna_urls].iloc[0]

        print("Coluna 'urls' não encontrada.")
        return None

    def extrair_urls_pastas(self):
        
        coluna_urls = self._get_coluna('urls')
        if coluna_urls is not None:
            print("Coluna 'urls' encontrada. Extraindo URLs das pastas")
            urls_pastas = self.df[coluna_urls].iloc[1:].dropna().tolist()
            return urls_pastas

        print("Coluna 'urls' não encontrada.")
        return []

    def extrair_fases(self):
        coluna_fases = self._get_coluna('valores', 'fases', 'fase')
        if coluna_fases is not None:
            print("Coluna de fases encontrada. Extraindo lista de fases.")
            # Pula a linha de configuracao (mesmo padrao de URLs) e remove vazios.
            fases = self.df[coluna_fases].iloc[1:].dropna().tolist()
            return fases

        print("Coluna de fases não encontrada.")
        return []

    def extrair_credenciais(self):
        coluna_email = self._get_coluna('email', 'e-mail')
        coluna_senha = self._get_coluna('senha', 'password')
        if coluna_email is not None and coluna_senha is not None:
            print("Colunas 'email' e 'senha' encontradas. Extraindo credenciais.")
            email = self.df[coluna_email].iloc[0]
            senha = self.df[coluna_senha].iloc[0]
            print(f"Email extraído: {email}")
            print(f"Senha extraída: {senha}")
            return email, senha

        print("Colunas 'email' ou 'senha' não encontradas.")
        return None, None