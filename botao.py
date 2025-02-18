import tkinter as tk
from tkinter import messagebox

# Criando a janela principal
root = tk.Tk()
root.title("Exemplo de MessageBox")
root.geometry("400x300")

# Função para exibir diferentes tipos de MessageBox
def mostrar_info():
    messagebox.showinfo("Informação", "Esta é uma mensagem informativa.")

def mostrar_alerta():
    messagebox.showwarning("Aviso", "Cuidado! Algo pode estar errado.")

def mostrar_erro():
    messagebox.showerror("Erro", "Ocorreu um erro inesperado!")

def perguntar():
    resposta = messagebox.askquestion("Pergunta", "Você deseja continuar?")
    if resposta == "yes":
        messagebox.showinfo("Resposta", "Você escolheu continuar.")
    else:
        messagebox.showinfo("Resposta", "Você cancelou a operação.")

def confirmar():
    resposta = messagebox.askokcancel("Confirmação", "Deseja salvar as alterações?")
    if resposta:
        messagebox.showinfo("Confirmado", "Alterações salvas com sucesso!")
    else:
        messagebox.showinfo("Cancelado", "Nenhuma alteração foi salva.")

def confirmar_exclusao():
    resposta = messagebox.askyesno("Confirmação", "Tem certeza que deseja excluir este item?")
    if resposta:
        messagebox.showinfo("Exclusão", "Item excluído com sucesso!")
    else:
        messagebox.showinfo("Exclusão", "A exclusão foi cancelada.")

# Criando botões para exibir os MessageBox
tk.Button(root, text="Mostrar Informação", command=mostrar_info).pack(pady=5)
tk.Button(root, text="Mostrar Alerta", command=mostrar_alerta).pack(pady=5)
tk.Button(root, text="Mostrar Erro", command=mostrar_erro).pack(pady=5)
tk.Button(root, text="Perguntar (Sim/Não)", command=perguntar).pack(pady=5)
tk.Button(root, text="Confirmar (OK/Cancelar)", command=confirmar).pack(pady=5)
tk.Button(root, text="Confirmar Exclusão (Sim/Não)", command=confirmar_exclusao).pack(pady=5)

# Executando a interface gráfica
root.mainloop()