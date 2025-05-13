import tkinter as tk
from tkinter import ttk, messagebox

class Calculator(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.title("Calculadora Super Descolada")
        self.parent.geometry("300x400")
        self.parent.resizable(False, False)
        
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TButton', font=('Helvetica', 14), padding=10)
        self.style.configure('TLabel', font=('Helvetica', 18))
        
        self.total_expression = ''
        self.current_expression = ''
        
        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()
        
        self.display_label = self.create_display_label()
        self.create_buttons()

    def create_display_frame(self):
        frame = ttk.Frame(self.parent)
        frame.pack(expand=True, fill='both')
        return frame

    def create_display_label(self):
        label = ttk.Label(self.display_frame, text=self.current_expression or '0', anchor=tk.E)
        label.pack(expand=True, fill='both')
        return label

    def create_buttons_frame(self):
        frame = ttk.Frame(self.parent)
        frame.pack(expand=True, fill='both')
        return frame

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('.', 4, 2), ('+', 4, 3),
            ('^', 5, 0), ('=', 5, 1, 1, 3)
        ]

        for (text, row, col, rowspan, colspan) in map(lambda b: b if len(b)==5 else (*b,1,1), buttons):
            btn = ttk.Button(self.buttons_frame, text=text, command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan, sticky=tk.NSEW)

        for i in range(6):
            self.buttons_frame.rowconfigure(i, weight=1)
            if i < 4:
                self.buttons_frame.columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.current_expression = ''
        elif char == '=':
            self.evaluate()
        else:
            self.current_expression += str(char)
        self.update_display()

    def evaluate(self):
        try:
            result = eval(self.current_expression)
            self.current_expression = str(result)
        except Exception:
            messagebox.showerror("Erro", "Expressão inválida!")
            self.current_expression = ''

    def update_display(self):
        self.display_label.config(text=self.current_expression or '0')

if __name__ == '__main__':
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
