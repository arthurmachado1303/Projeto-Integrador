import re
import random
import time

def verificar_forca_senha(senha):

    # - Verifica se a senha é forte
    if (len(senha) >= 8 and
        re.search(r"[A-Z]", senha) and
        re.search(r"[a-z]", senha) and
        re.search(r"[0-9]", senha) and
        re.search(r"[!@#$%^&*()_+=\-{}[\]:;\"'<>,.?/]", senha)):
        return True
    return False

def gerar_token():

    # - Gera um token de 6 dígitos
    return str(random.randint(100000, 999999))

def enviar_token(email_ou_sms, token):

    # - Simula o envio do token para email ou celular
    print(f"\n[Simulação] Enviando token para {email_ou_sms}...")
    time.sleep(1)  # Simula tempo de envio
    print(f"[Simulação] Token enviado: {token}\n")

def validar_token(token_enviado):

    # - Valida se o token digitado pelo usuário é correto
    tentativa = input("Digite o token que você recebeu: ")
    if tentativa == token_enviado:
        print("\nToken validado com sucesso!")
    else:
        print("\nToken inválido. Tente novamente.")

def main():
    print("=== Verificador de Senha com Autenticação ===")
    senha = input("Digite sua senha para verificação: ")

    if verificar_forca_senha(senha):
        print("Senha forte!")
        
        # - Escolha de envio
        escolha = input("Deseja receber o token por [1] E-mail ou [2] SMS? ")
        if escolha == '1':
            destino = "usuario@exemplo.com"
        elif escolha == '2':
            destino = "+55 11 91234-5678"
        else:
            print("Opção inválida.")
            return

        token = gerar_token()
        enviar_token(destino, token)
        validar_token(token)

    else:
        print("Senha fraca. A senha precisa ter no mínimo:\n"
              "- 8 caracteres\n- 1 letra maiúscula\n- 1 letra minúscula\n"
              "- 1 número\n- 1 caractere especial")

if __name__ == "__main__":
    main()
