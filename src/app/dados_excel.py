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
            
    def extrair_home_url(self):
        
        # Extrai a URL da página inicial para login
        
        # Verifica se o DF existe e se a coluna 'urls'ou 'URLS' existe
        if self.df is not None and ('urls' in self.df.columns or 'URLS' in self.df.columns):
            # Caso sim, retorna o valor da primeira linha da coluna 'urls'
            print("Coluna 'urls' encontrada. Extraindo URL da página inicial para login")
            return self.df['urls'].iloc[0] # iloc[0] acessa a primeira linha da coluna 'urls'
            # Retorna a primeira linha da coluna 'urls' (URL da página inicial para login)
        else:
            print("Coluna 'urls' não encontrada.")
            return None
            # Retorna vazaio caso o DF ou a coluna 'urls' não existam

    def extrair_urls_pastas(self):
        
        # Se não for vazia e a coluna 'urls existir, extrai as URLs das pastas a partir da SEGUNDA linha 
        if self.df is not None and 'urls' in self.df.columns:
            print("Coluna 'urls' encontrada. Extraindo URLs das pastas")
            # A função dropna() é usada para remover valores ausentes (NaN) da série resultante, garantindo que apenas URLs válidas sejam retornadas.
            # O método tolist() converte a série resultante em uma lista de URLs. 
            urls_pastas = self.df['urls'].iloc[1:].dropna().tolist()
            return urls_pastas
            # Retorna as URLs das pastas a partir da segunda linha da coluna 'urls', removendo valores ausentes e convertendo para uma lista.
        else:
            print("Coluna 'urls' não encontrada.")
            return None
        
            
    def extrair_fases(self):
        
        # Fase extraída: Linha 26: PROCESSO CONCLUÍDO (PASTA ARQUIVDA) : bs-select-9-25
        
        # verfica se DF existe e se a coluna 'valores' existe.
        if self.df is not None and 'valores' in self.df.columns:
            # Existindo, retorna o valor da linha 26 da coluna 'valores' (Fase do processo)
            print("Coluna encontrada, extraindo a fase")
            fases = self.df['valores'].iloc[25]
            print(f'fase extraída: {fases}')  
            return fases
            # Retorna a fase extraída e converte para uma lista
        else:
            print("Coluna 'valores' não encontrada.")
            return None
            
    def extrair_credenciais(self):
        
        # Verifica se o DF existe e se as colunas 'email' e 'senha' existem
        if self.df is not None and 'email' in self.df.columns and 'senha' in self.df.columns:
            print("Colunas 'email' e 'senha' encontradas. Extraindo credenciais.")
            email = self.df['email'].iloc[0]
            
            senha = self.df['senha'].iloc[0]
            
            # Retorna o email e a senha extraídos da primeira linha das colunas 'email' e 'senha', respectivamente.
            print(f"Email extraído: {email}")
            print(f"Senha extraída: {senha}")
            
            return email, senha

        else:
            print("Colunas 'email' ou 'senha' não encontradas.")
            return None, None
        