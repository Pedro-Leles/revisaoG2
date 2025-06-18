import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Sistema Escolar")
janela.geometry("400x300")

tk.Label(janela, text="Nome do aluno:").pack()
entrada_nome = tk.Entry(janela)
entrada_nome.pack()

def cadastrar_aluno():
    nome = entrada_nome.get()
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO Alunos (nome) VALUES (%s)", (nome,))
    conexao.commit()
    cursor.close()
    conexao.close()
    messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")

tk.Button(janela, text="Cadastrar Aluno", command=cadastrar_aluno).pack()

janela.mainloop()
