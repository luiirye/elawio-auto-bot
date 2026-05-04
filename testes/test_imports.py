#!/usr/bin/env python3
"""
Script de validação de imports - verifica se todos os módulos estão importáveis
Executar a partir do diretório raiz do projeto
"""

import sys
from pathlib import Path

# Adiciona raiz ao path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

def test_imports():
    """Testa se todos os imports estão funcionando"""
    print("=" * 60)
    print("TESTANDO IMPORTS DO PROJETO")
    print("=" * 60)
    
    tests = []
    
    # Teste 1: Data/Dados
    try:
        from data.dados import Dados
        print("✅ data.dados.Dados - OK")
        tests.append(True)
    except Exception as e:
        print(f"❌ data.dados.Dados - ERRO: {e}")
        tests.append(False)
    
    # Teste 2: Browser
    try:
        from src.app.browser import Navegador
        print("✅ src.app.browser.Navegador - OK")
        tests.append(True)
    except Exception as e:
        print(f"❌ src.app.browser.Navegador - ERRO: {e}")
        tests.append(False)
    
    # Teste 3: Login
    try:
        from src.app.login import Login
        print("✅ src.app.login.Login - OK")
        tests.append(True)
    except Exception as e:
        print(f"❌ src.app.login.Login - ERRO: {e}")
        tests.append(False)
    
    # Teste 4: Processos
    try:
        from src.app.processos import Processos
        print("✅ src.app.processos.Processos - OK")
        tests.append(True)
    except Exception as e:
        print(f"❌ src.app.processos.Processos - ERRO: {e}")
        tests.append(False)
    
    # Teste 5: Fases
    try:
        from src.app.alterar_fases import Fases
        print("✅ src.app.alterar_fases.Fases - OK")
        tests.append(True)
    except Exception as e:
        print(f"❌ src.app.alterar_fases.Fases - ERRO: {e}")
        tests.append(False)
    
    # Teste 6: Excel Service
    try:
        from src.app.dados_excel import LeituraDeDados
        print("✅ src.app.dados_excel.LeituraDeDados - OK")
        tests.append(True)
    except Exception as e:
        print(f"❌ src.app.dados_excel.LeituraDeDados - ERRO: {e}")
        tests.append(False)
    
    print("=" * 60)
    passed = sum(tests)
    total = len(tests)
    print(f"RESULTADO: {passed}/{total} testes passaram")
    print("=" * 60)
    
    return all(tests)

if __name__ == "__main__":
    success = test_imports()
    sys.exit(0 if success else 1)
