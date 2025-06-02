"""Crie um programa que gera um perfil de usuário aleatório usando a API 'Random User Generator'. O programa deve exibir o nome, email e país do usuário gerado."""

import requests
def gerar_perfil_usuario():
    """Gera um perfil de usuário aleatório usando a API 'Random User Generator'."""
    url = "https://randomuser.me/api/"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        usuario = data['results'][0]
        
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']
        
        return nome, email, pais
    else:
        raise Exception("Erro ao acessar a API.")
def main():
    print("=== Gerador de Perfil de Usuário Aleatório ===")
    try:
        nome, email, pais = gerar_perfil_usuario()
        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
        print(f"País: {pais}")
    except Exception as e:
        print(f"Erro: {e}")
if __name__ == "__main__":
    main()
# Fim do programa