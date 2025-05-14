# 🧮 Calculadora GUI em Python

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Status](https://img.shields.io/badge/status-conclu%C3%ADdo-brightgreen)
![Testes](https://github.com/MateusFernandesPereira/calculadora-python/actions/workflows/python-app.yml/badge.svg)

Este repositório apresenta uma aplicação de calculadora com interface gráfica, desenvolvida em Python, utilizando a biblioteca Tkinter/ttk.
O projeto foi elaborado como parte da resolução de um exercício proposto na disciplina Fundamentos de Sistemas de Informação, ministrada pelo docente Higor Amario de Souza, no curso de Bacharelado em Sistemas de Informação da UNESP – Universidade Estadual Paulista “Júlio de Mesquita Filho”.

---

## 📑 Funcionalidades

- **Interface Gráfica**: GUI implementada com tema `clam`, utilizando widgets `ttk` para aparência consistente.  
- **Operações Suportadas**:  
  - Adição (`+`)  
  - Subtração (`-`)  
  - Multiplicação (`*`)  
  - Divisão (`/`) com tratamento de divisão por zero  
  - Potenciação (`^`)  
- **Recursos Adicionais**:  
  - Suporte a números negativos e valores decimais  
  - Botão **C** para limpeza completa da expressão  
  - Validação de entrada e exibição de mensagens de erro por meio de diálogos  

---

## 🧪 Testes Automatizados

O projeto inclui uma suíte de testes automatizados utilizando o framework [pytest](https://pytest.org/). Os testes garantem que a função principal de avaliação das expressões matemáticas (`evaluate_expression`) está funcionando corretamente, cobrindo casos válidos e inválidos, incluindo operações matemáticas, divisões por zero, entradas vazias e sintaxes incorretas.

### Como executar os testes

1. Certifique-se de ter o `pytest` instalado:
    ```bash
    pip install pytest
    ```

2. Execute os testes na raiz do projeto:
    ```bash
    pytest
    ```

Se todos os testes passarem, você verá uma mensagem indicando sucesso. Caso algum teste falhe, o terminal mostrará detalhes para facilitar a correção.

---

## 🏁 Instruções de Uso

### Pré‑requisitos

- Python 3.10 ou superior  
- Tkinter (normalmente incluído nas instalações padrão do Python; em sistemas Linux, pode ser necessário instalar o pacote `python3-tk`)

### Passo a Passo

1. **Clone** o repositório:  
   ```bash
   git clone https://github.com/MateusFernandesPereira/calculadora-python.git
   cd calculadora-python
   ```

2. Execute a aplicação:
    ```bash
    python calculadora_gui.py
    ```

// ... existing code ...
## 📂 Estrutura do Projeto

```plaintext
calculadora-python/
├── .git/                   # Dados do repositório Git
├── .github/                # Workflows e configurações do GitHub Actions
├── assets/                 # Imagens de screenshots da interface
│   ├── screenshot1.png
│   ├── screenshot2.png
│   └── screenshot3.png
├── README.md               # Documento de instruções e descrição do projeto
├── calculadora.py          # Implementação da classe Calculator e execução da GUI
├── calculator_core.py      # Função de avaliação das expressões matemáticas
└── test_calculator.py      # Testes automatizados com pytest

```
## 📸 Capturas de Tela

### 🖥️ Interface Inicial
![Interface Inicial](assets/screenshot1.png)

---

### 🔢 Exemplo de Cálculo
![Uso da Calculadora](assets/screenshot2.png)

---

### ⚠️ Mensagem de Erro
![Mensagem de Erro](assets/screenshot3.png)
