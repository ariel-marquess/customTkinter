import customtkinter as ctk


class MeuSistema(ctk.CTk):
    def __init__(self):
        super().__init__()

        # 1. Configuração da Janela (Root)
        self.geometry("800x600")
        self.grid_columnconfigure(1, weight=1)  # Coluna do conteúdo expande
        self.grid_rowconfigure(0, weight=1)  # Linha única ocupa tudo

        # 2. Sidebar (Frame Lateral)
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")

        # 3. Widgets da Sidebar
        self.label_titulo = ctk.CTkLabel(self.sidebar, text="Menu", font=("Roboto", 20, "bold"))
        self.label_titulo.pack(pady=20)

        self.btn_home = ctk.CTkButton(self.sidebar, text="Dashboard")
        self.btn_home.pack(pady=10, padx=10)

        # 4. Área de Conteúdo (Main Frame)
        self.main_content = ctk.CTkFrame(self, fg_color="transparent")
        self.main_content.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        self.welcome_msg = ctk.CTkLabel(self.main_content, text="Bem-vindo ao Sistema")
        self.welcome_msg.pack()


if __name__ == "__main__":
    app = MeuSistema()
    app.mainloop()