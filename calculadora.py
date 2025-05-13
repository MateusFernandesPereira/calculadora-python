def calcular(valor1, valor2, operacao):
    """
    Realiza a operação matemática 'operacao' entre valor1 e valor2.
    Operações suportadas: '+', '-', '*', '/', '^'.
    Retorna o resultado ou None se entrada/operacao inválida.
    """
    # Tenta converter para float
    try:
        a = float(valor1)
        b = float(valor2)
    except (ValueError, TypeError):
        return None

    # Dicionário de operações
    operacoes = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else None,  # evita divisão por zero
        '^': lambda x, y: x ** y,
    }

    # Escolhe e executa a operação
    func = operacoes.get(operacao)
    if not func:
        return None  # operação desconhecida

    try:
        return func(a, b)
    except Exception:
        return None


if __name__ == "__main__":
    # Exemplo de uso no terminal
    v1 = input("Digite o primeiro valor: ")
    v2 = input("Digite o segundo valor: ")
    op = input("Digite a operação (+, -, *, /, ^): ")

    resultado = calcular(v1, v2, op)
    if resultado is None:
        print("Entrada ou operação inválida!")
    else:
        print(f"Resultado: {resultado}")
