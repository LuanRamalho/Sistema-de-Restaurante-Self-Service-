import tkinter as tk
from tkinter import ttk

# Função para calcular os valores
def calcular():
    try:
        # Valores fixos dos produtos
        preco_comida = 15.00
        preco_refresco = 2.00
        preco_refrigerante = 3.50
        preco_chocolate = 3.00
        preco_cupcake = 2.00
        preco_sorvete = 4.00

        # Quantidades inseridas pelo usuário
        qtd_comida = float(entry_comida.get())
        qtd_refresco = int(entry_refresco.get())
        qtd_refrigerante = int(entry_refrigerante.get())
        qtd_chocolate = int(entry_chocolate.get())
        qtd_cupcake = int(entry_cupcake.get())
        qtd_sorvete = int(entry_sorvete.get())

        # Cálculo dos valores individuais
        total_comida = qtd_comida * preco_comida
        total_refresco = qtd_refresco * preco_refresco
        total_refrigerante = qtd_refrigerante * preco_refrigerante
        total_chocolate = qtd_chocolate * preco_chocolate
        total_cupcake = qtd_cupcake * preco_cupcake
        total_sorvete = qtd_sorvete * preco_sorvete

        # Soma total
        total_geral = (total_comida + total_refresco + total_refrigerante +
                       total_chocolate + total_cupcake + total_sorvete)

        # Exibir os valores calculados
        resultado_texto = (
            f"Comida: R$ {total_comida:.2f}\n"
            f"Refresco: R$ {total_refresco:.2f}\n"
            f"Refrigerante: R$ {total_refrigerante:.2f}\n"
            f"Barra de Chocolate: R$ {total_chocolate:.2f}\n"
            f"Cupcake: R$ {total_cupcake:.2f}\n"
            f"Pote de Sorvete: R$ {total_sorvete:.2f}\n\n"
            f"Total Geral: R$ {total_geral:.2f}"
        )
        resultado_label.config(text=resultado_texto)

        # Calcular troco se o valor pago for inserido
        valor_pago = float(entry_pago.get()) if entry_pago.get() else 0
        troco = valor_pago - total_geral
        troco_label.config(text=f"Troco: R$ {troco:.2f}")
    except ValueError:
        resultado_label.config(text="Por favor, insira valores válidos.")

# Configuração da janela principal
root = tk.Tk()
root.title("Sistema de Restaurante - Self-Service")
root.geometry("500x700")
root.configure(bg="#e9f5db")

# Título
titulo = tk.Label(root, text="Restaurante Self-Service", font=("Arial Black", 18), bg="#e9f5db", fg="#2b7a0b")
titulo.pack(pady=20)

# Frame principal com barra de rolagem
frame_container = tk.Frame(root, bg="#e9f5db")
frame_container.pack(fill=tk.BOTH, expand=True)

canvas = tk.Canvas(frame_container, bg="#e9f5db")
scrollbar = ttk.Scrollbar(frame_container, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="#ffffff")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Labels e entradas
labels_entries = [
    ("Quantidade de Comida (kg):", "0.0"),
    ("Quantidade de Refresco:", "0"),
    ("Quantidade de Refrigerante:", "0"),
    ("Quantidade de Barra de Chocolate:", "0"),
    ("Quantidade de Cupcake:", "0"),
    ("Quantidade de Pote de Sorvete:", "0"),
    ("Valor Pago:", "0.0"),
]

entries = []
for text, default in labels_entries:
    label = tk.Label(scrollable_frame, text=text, font=("Arial", 12), bg="#ffffff", fg="#4CAF50", anchor="w")
    label.pack(fill=tk.X, padx=10, pady=5)
    entry = ttk.Entry(scrollable_frame, font=("Arial", 12))
    entry.insert(0, default)
    entry.pack(fill=tk.X, padx=10, pady=5)
    entries.append(entry)

(entry_comida, entry_refresco, entry_refrigerante, entry_chocolate, entry_cupcake, 
 entry_sorvete, entry_pago) = entries

# Botão Calcular
calcular_button = tk.Button(scrollable_frame, text="Calcular", font=("Arial Black", 14), bg="#4CAF50", fg="white", command=calcular)
calcular_button.pack(pady=20)

# Resultado
resultado_label = tk.Label(scrollable_frame, text="", font=("Arial", 12), bg="#ffffff", fg="#333333", justify="left", anchor="w")
resultado_label.pack(fill=tk.X, padx=10, pady=5)

# Troco
troco_label = tk.Label(scrollable_frame, text="Troco: R$ 0.00", font=("Arial Black", 14), bg="#ffffff", fg="#2b7a0b")
troco_label.pack(pady=20)

# Rodapé
rodape = tk.Label(scrollable_frame, text="Obrigado por usar nosso sistema!", font=("Arial", 12), bg="#ffffff", fg="#4CAF50")
rodape.pack(pady=10)

# Iniciar o aplicativo
root.mainloop()
