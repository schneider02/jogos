import tkinter as tk
from tkinter import messagebox
import requests  

class ClientForm:
    def __init__(self, master):
        self.master = master
        master.title("Cadastro")

        master.configure(bg="#0c72ae")   

        self.form_frame = tk.Frame(master, bg="#0c72ae")
        self.form_frame.pack(pady=20, padx=40, expand=True)

        self.font = ("Arial", 10)

        self.cpf_label = tk.Label(self.form_frame, text="CPF/CNPJ:", bg="#0c72ae", font=self.font)
        self.cpf_label.grid(row=0, column=0, sticky="e", padx=10, pady=5)
        self.cpf_entry = tk.Entry(self.form_frame, font=self.font)
        self.cpf_entry.grid(row=0, column=1, padx=10, pady=5)

        self.name_label = tk.Label(self.form_frame, text="Nome:", bg="#0c72ae", font=self.font)
        self.name_label.grid(row=0, column=2, sticky="e", padx=10, pady=5)
        self.name_entry = tk.Entry(self.form_frame, font=self.font)
        self.name_entry.grid(row=0, column=3, padx=10, pady=5)

        self.razao_label = tk.Label(self.form_frame, text="Razão Social:", bg="#0c72ae", font=self.font)
        self.razao_label.grid(row=0, column=4, sticky="e", padx=10, pady=5)
        self.razao_entry = tk.Entry(self.form_frame, font=self.font)
        self.razao_entry.grid(row=0, column=5, padx=10, pady=5)

        self.pessoa_label = tk.Label(self.form_frame, text="Pessoa:", bg="#0c72ae", font=self.font)
        self.pessoa_label.grid(row=1, column=0, sticky="e", padx=10, pady=5)
        self.pessoa_var = tk.StringVar(self.master)
        self.pessoa_var.set("Física")  # Valor padrão
        self.pessoa_menu = tk.OptionMenu(self.form_frame, self.pessoa_var, "Física", "Jurídica")
        self.pessoa_menu.config(font=self.font, width=10)
        self.pessoa_menu.grid(row=1, column=1, padx=10, pady=5)

        self.contato_label = tk.Label(self.form_frame, text="Contato:", bg="#0c72ae", font=self.font)
        self.contato_label.grid(row=1, column=2, sticky="e", padx=10, pady=5)
        self.contato_entry = tk.Entry(self.form_frame, font=self.font)
        self.contato_entry.grid(row=1, column=3, padx=10, pady=5)

        self.telefone_label = tk.Label(self.form_frame, text="Telefone:", bg="#0c72ae", font=self.font)
        self.telefone_label.grid(row=1, column=4, sticky="e", padx=10, pady=5)
        self.telefone_entry = tk.Entry(self.form_frame, font=self.font)
        self.telefone_entry.grid(row=1, column=5, padx=10, pady=5)

        self.celular_label = tk.Label(self.form_frame, text="Celular:", bg="#0c72ae", font=self.font)
        self.celular_label.grid(row=2, column=0, sticky="e", padx=10, pady=5)
        self.celular_entry = tk.Entry(self.form_frame, font=self.font)
        self.celular_entry.grid(row=2, column=1, padx=10, pady=5)

        self.fax_label = tk.Label(self.form_frame, text="Fax:", bg="#0c72ae", font=self.font)
        self.fax_label.grid(row=2, column=2, sticky="e", padx=10, pady=5)
        self.fax_entry = tk.Entry(self.form_frame, font=self.font)
        self.fax_entry.grid(row=2, column=3, padx=10, pady=5)

        self.data_nasc_label = tk.Label(self.form_frame, text="Data Nascimento:", bg="#0c72ae", font=self.font)
        self.data_nasc_label.grid(row=3, column=0, sticky="e", padx=10, pady=5)
        self.data_nasc_entry = tk.Entry(self.form_frame, font=self.font)
        self.data_nasc_entry.grid(row=3, column=1, padx=10, pady=5)

        self.sexo_label = tk.Label(self.form_frame, text="Sexo:", bg="#0c72ae", font=self.font)
        self.sexo_label.grid(row=3, column=2, sticky="e", padx=10, pady=5)
        self.sexo_var = tk.StringVar(self.master)
        self.sexo_var.set("Masculino")  # Valor padrão
        self.sexo_menu = tk.OptionMenu(self.form_frame, self.sexo_var, "Masculino", "Feminino")
        self.sexo_menu.config(font=self.font, width=10)
        self.sexo_menu.grid(row=3, column=3, padx=10, pady=5)

        self.inscricao_estadual_label = tk.Label(self.form_frame, text="Inscrição Estadual:", bg="#0c72ae", font=self.font)
        self.inscricao_estadual_label.grid(row=3, column=4, sticky="e", padx=10, pady=5)
        self.inscricao_estadual_entry = tk.Entry(self.form_frame, font=self.font)
        self.inscricao_estadual_entry.grid(row=3, column=5, padx=10, pady=5)

        self.doc_label = tk.Label(self.form_frame, text="Documento:", bg="#0c72ae", font=self.font)
        self.doc_label.grid(row=4, column=0, sticky="e", padx=10, pady=5)
        self.doc_entry = tk.Entry(self.form_frame, font=self.font)
        self.doc_entry.grid(row=4, column=1, padx=10, pady=5)

        self.categoria_label = tk.Label(self.form_frame, text="Categoria:", bg="#0c72ae", font=self.font)
        self.categoria_label.grid(row=4, column=2, sticky="e", padx=10, pady=5)
        self.categoria_entry = tk.Entry(self.form_frame, font=self.font)
        self.categoria_entry.grid(row=4, column=3, padx=10, pady=5)

        self.endereco_label = tk.Label(self.form_frame, text="Endereço do Cliente:", bg="#0c72ae", font=self.font)
        self.endereco_label.grid(row=5, column=0, sticky="e", columnspan=2, padx=10, pady=10)

        self.cep_label = tk.Label(self.form_frame, text="CEP:", bg="#0c72ae", font=self.font)
        self.cep_label.grid(row=6, column=0, sticky="e", padx=10, pady=5)
        self.cep_entry = tk.Entry(self.form_frame, font=self.font)
        self.cep_entry.grid(row=6, column=1, padx=10, pady=5)
        self.cep_entry.bind("<KeyRelease>", self.buscar_endereco)

        self.endereco_label = tk.Label(self.form_frame, text="Endereço:", bg="#0c72ae", font=self.font)
        self.endereco_label.grid(row=6, column=2, sticky="e", padx=10, pady=5)
        self.endereco_entry = tk.Entry(self.form_frame, font=self.font)
        self.endereco_entry.grid(row=6, column=3, padx=10, pady=5)

        self.numero_label = tk.Label(self.form_frame, text="Número:", bg="#0c72ae", font=self.font)
        self.numero_label.grid(row=6, column=4, sticky="e", padx=10, pady=5)
        self.numero_entry = tk.Entry(self.form_frame, font=self.font)
        self.numero_entry.grid(row=6, column=5, padx=10, pady=5)

        # Botão
        self.save_button = tk.Button(master, text="Salvar", command=self.salvar, font=self.font, bg="#4CAF50", fg="white", width=20)
        self.save_button.pack(pady=10)

        self.clear_button = tk.Button(master, text="Limpar", command=self.limpar, font=self.font, bg="#f44336", fg="white", width=20)
        self.clear_button.pack(pady=5)

    def buscar_endereco(self, event=None):
        cep = self.cep_entry.get().strip()
        if len(cep) == 8:  
            try:
                response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
                data = response.json()
                if "erro" not in data:
                    self.endereco_entry.delete(0, tk.END)
                    self.endereco_entry.insert(0, data.get('logradouro', ''))

                    self.bairro_entry.delete(0, tk.END)
                    self.bairro_entry.insert(0, data.get('bairro', ''))

                    self.cidade_entry.delete(0, tk.END)
                    self.cidade_entry.insert(0, data.get('localidade', ''))

                    self.estado_entry.delete(0, tk.END)
                    self.estado_entry.insert(0, data.get('uf', ''))
                else:
                    messagebox.showerror("Erro", "CEP não encontrado.")
            except requests.exceptions.RequestException as e:
                messagebox.showerror("Erro", f"Erro na requisição: {e}")

    def salvar(self):
        messagebox.showinfo("Informação", "Dados salvos com sucesso!")

    def limpar(self):
        for widget in self.form_frame.winfo_children():
            if isinstance(widget, tk.Entry):
                widget.delete(0, tk.END)

def main():
    root = tk.Tk()
    form = ClientForm(root)
    root.mainloop()

if __name__ == "__main__":
    main()
