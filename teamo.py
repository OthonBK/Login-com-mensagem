import tkinter as tk
from tkinter import ttk, messagebox

def verificar_senha():
    nome = nome_entry.get()
    senha = senha_entry.get()

    if senha == "segredo":
        messagebox.showinfo("Mensagem", "A maioria das pessoas perdeu a habilidade de ver o lado bom das coisas, embora a luz por trás das nuvens seja uma prova de que ele existe. Ps: Eu te amo, " + nome)
    else:
        messagebox.showerror("Erro", "Senha incorreta. Tente novamente.")

# Cria a janela principal
janela = tk.Tk()
janela.title("S2")

# Define o estilo do aplicativo
style = ttk.Style(janela)
style.theme_use('clam')

# Define a largura e a altura da janela
janela_width = 300
janela_height = 200

# Obtém a largura e a altura da tela do usuário
screen_width = janela.winfo_screenwidth()
screen_height = janela.winfo_screenheight()

# Calcula a posição central da janela
pos_x = int((screen_width / 2) - (janela_width / 2))
pos_y = int((screen_height / 2) - (janela_height / 2))

# Define a posição da janela na tela
janela.geometry("{}x{}+{}+{}".format(janela_width, janela_height, pos_x, pos_y))

# Cria o rótulo e a caixa de entrada para o nome
nome_label = ttk.Label(janela, text="Digite seu nome:")
nome_label.pack(pady=10)
nome_entry = ttk.Entry(janela)
nome_entry.pack(pady=5, padx=20)

# Cria o rótulo e a caixa de entrada para a senha
senha_label = ttk.Label(janela, text="Digite sua senha:")
senha_label.pack(pady=10)
senha_entry = ttk.Entry(janela, show="*")
senha_entry.pack(pady=5, padx=20)

# Cria o botão para verificar a senha
verificar_button = ttk.Button(janela, text="Verificar senha", command=verificar_senha)
verificar_button.pack(pady=10)

# Inicia o loop principal da interface gráfica
janela.mainloop()
