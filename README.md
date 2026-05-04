# Elaw Io Auto Bot

Automação em Python para atualização de fases no sistema Elaw, com leitura de dados por Excel utilizando pandas e execução de comandos com base em elementos HTML e CSS com Selenium.

## Funcionalidades

- Login automatizado no sistema com `selenium`.
- Navegação em lote por URLs de pastas.
- Alteração de fase por item (ID da fase no Excel).
- Leitura de dados com `pandas`.

## Tecnologias

- [Python 3.10+](https://www.python.org/)
- [Selenium](https://www.selenium.dev/)
- [Pandas](https://pandas.pydata.org/)
- [Openpyxl](https://openpyxl.readthedocs.io/)

## Estrutura

```text
elawio-auto/
├── data/
│   ├── __init__.py
│   └── dados.py
├── src/
│   └── app/
│       ├── browser.py
│       ├── login.py
│       ├── processos.py
│       ├── alterar_fases.py
│       └── dados_excel.py
├── testes/
│   └── test_imports.py
├── main.py
├── requirements.txt
├── .env.example
└── .gitignore
```

## Como executar

1. Crie e ative um ambiente virtual.
2. Instale dependências:
   - `pip install -r requirements.txt`
3. Execute:
   - `python main.py`
4. Informe o caminho completo do Excel no terminal.

## Formato esperado da planilha

Colunas mínimas:
- `urls`: primeira linha = URL da home; linhas seguintes = URLs das pastas;
- `email`: credencial de login;
- `senha`: credencial de login;
- `valores` (ou `fase`/`fases`): IDs de fases, uma por pasta.

## Segurança para repositório público

- Nunca subir `.env`, credenciais reais ou planilhas sensíveis.
- O projeto já ignora `.venv`, cache Python, `.env` e `*.xlsx`.
- Mantenha no GitHub apenas dados de exemplo.

---

Desenvolvido por [Luiirye](https://github.com/luiirye)
