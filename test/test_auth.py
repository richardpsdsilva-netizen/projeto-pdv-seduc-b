from app.auth import hash_senha , verificar_senha

#RODAR O TESTE: python -m pytest

#INSTALAR O : pip install pytest

#Testar funções do arquivo auth.py


def test_hash_senha_gera_string_diferente_original():

    senha = "minhasenha"

    hash_gerado = hash_senha(senha) #asfjsldfkjsiodngsdf

    #TESTAR A FUNÇÃO
    assert senha != hash_gerado

#TESTAR A FUNÇÃO VERIFICAR SENHA
def test_verificar_senha_aceita_senha_correta():
    senha = "santos@123"
    hash_gerado = hash_senha(senha)

    resultado = verificar_senha(senha , hash_gerado)


#TESTAR A FUNÇÃO 
#assert resultado == True
    assert resultado is True

# Criar a função para verificar se a senha rejeita uma senha errada!!!

def test_verificar_senha_rejeita_senha_incorreta():
    senha_correta = "santos@123"
    senha_incorreta = "santos@890"

    hash_gerado = hash_senha(senha_correta)

    resultado = verificar_senha(senha_incorreta, hash_gerado)
#TESTE DE REJEIÇÃO
    #assert resultado is False
    assert resultado == False


