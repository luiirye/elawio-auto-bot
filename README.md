# Elaw Io Auto Bot 

Este Projeto foi criado para desenvolver uma ferramenta de automação utilizando Python, Pandas e Selenium para otimizar a gestão de processos jurídicos no sistema Elaw. A automação lê dados de uma planilha de Excel (URLs de processos, credenciais e fases) e executa automaticamente as funções de login, navegação de pastas por URL e alteração de fases destas pastas.

## Funcionalidades desenvolvidas

- **Login Automatizado:** Abertura de navegador e acesso ao sistema utilizando as credenciais e URLS fornecidas na planilha.
- **Navegação em Massa:** Itera sobre uma lista de URLs de processos (pastas).
- **Alteração de Fase:** Abre o menu de fases e seleciona a fase para ser altearada de forma automática.
- **Leitura de Excel:** Integração com `pandas` para processamento de dados dinâmicos.

## Tecnologias Utilizadas

- [Python 3.10+](https://www.python.org/) - Linguagem de programação utilizada
- [Selenium 4.43.0](https://www.selenium.dev/) - Automação de navegador.
- [Pandas 3.0.2](https://pandas.pydata.org/) - Manipulação e extração de dados do Excel.
- [Openpyxl 3.1.5](https://openpyxl.readthedocs.io/) - Motor de leitura de planilhas `.xlsx`.

## Estrutura do Projeto

```text
elawio-auto/
├── data/
│   └── base.xlsx          # Planilha com os dados de entrada
├── src/
│   ├── app/
│   │   ├── browser.py     # Configuração do WebDriver (Selenium)
│   │   ├── login.py       # Lógica de autenticação
│   │   ├── processos.py   # Manipulação dos elementos do processo
│   │   ├── alterar_fases.py # Lógica de clique e seleção de fases
│   │   └── dados_excel.py # Classe de extração de dados via Pandas
├── main.py                # Ponto de entrada da aplicação
└── requirements.txt       # Dependências do projeto
```


---

*Este projeto foi feito com o intuíto de contribuir com as demandas do escritório de advocacia e principalmente para estudos e aprofundamento de meus conhecimentos*

---

desenvolvido por @Luiirye
