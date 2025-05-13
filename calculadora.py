import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        op = operation.get()
        resultado = None

        if op == '+':
            resultado = a + b
        elif op == '-':
            resultado = a - b
        elif op == '*':
            resultado = a * b
        elif op == '/':
            resultado = a / b if b != 0 else None
        elif op == '^':
            resultado = a ** b

        if resultado is None:
            raise ValueError
        result_label.config(text=f"Resultado: {resultado}")
    except Exception:
        messagebox.showerror("Erro", "Entrada ou operação inválida!")

# Janela principal
root = tk.Tk()
root.title("Calculadora GUI")

# Inputs
entry1 = tk.Entry(root, width=10)
entry1.grid(row=0, column=0, padx=5, pady=5)
operation = tk.StringVar(root)
operation.set('+')  # valor padrão
ops_menu = tk.OptionMenu(root, operation, '+', '-', '*', '/', '^')
ops_menu.grid(row=0, column=1, padx=5, pady=5)
entry2 = tk.Entry(root, width=10)
entry2.grid(row=0, column=2, padx=5, pady=5)

# Botão de calcular
calc_btn = tk.Button(root, text="Calcular", command=calcular)
calc_btn.grid(row=1, column=0, columnspan=3, pady=10)

# Label de resultado
result_label = tk.Label(root, text="Resultado: ")
result_label.grid(row=2, column=0, columnspan=3, pady=5)

root.mainloop()
