def evaluate_expression(expression: str) -> str:
    # Não permite uso de ^, parênteses vazios ou expressão vazia
    if "^" in expression or "()" in expression or expression.strip() == "":
        return "Erro"
    try:
        # Avalia apenas expressões matemáticas simples
        result = eval(expression, {"__builtins__": None}, {})
        return str(result)
    except Exception:
        return "Erro"
