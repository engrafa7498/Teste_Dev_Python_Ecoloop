#Resposta questão 3

def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def analisar_numero(numero):
    par_ou_impar = "par" if numero % 2 == 0 else "ímpar"
    primo = "primo" if eh_primo(numero) else "não é primo"
    return par_ou_impar, primo

def main():
    try:
        num1 = int(input("Digite o primeiro número inteiro: "))
        num2 = int(input("Digite o segundo número inteiro: "))

        # Operações matemáticas
        print(f"\nSoma: {num1 + num2}")
        print(f"Subtração: {num1 - num2}")
        print(f"Multiplicação: {num1 * num2}")
        if num2 != 0:
            print(f"Divisão: {num1 / num2:.2f}")
        else:
            print("Divisão: Não é possível dividir por zero.")

        # Análise do primeiro número
        par_ou_impar1, primo1 = analisar_numero(num1)
        print(f"\nNúmero 1 ({num1}):")
        print(f"- É {par_ou_impar1}")
        print(f"- {primo1}")

        # Análise do segundo número
        par_ou_impar2, primo2 = analisar_numero(num2)
        print(f"\nNúmero 2 ({num2}):")
        print(f"- É {par_ou_impar2}")
        print(f"- {primo2}")

    except ValueError:
        print("Por favor, digite apenas números inteiros.")

if __name__ == "__main__":
    main()
