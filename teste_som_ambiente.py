import tkinter as tk
import pygame

# Inicializa o mixer do Pygame
pygame.mixer.init()

# Caminho para o arquivo de som ambiente local
sound_path = r'D:/Programa/AngelEngine/BlackWeald - Astral Chasm _ Dark Ambient Horror Soundscape [jJS-1mtZHIc].mp3'

# Carrega o som ambiente
pygame.mixer.music.load(sound_path)

# Toca o som em loop
pygame.mixer.music.play(-1)

class AngelEngineGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Angel Engine")
        self.texto_principal = tk.Text(root, wrap="word", bg="black", fg="white", font=("Courier", 11))
        self.texto_principal.pack(expand=True, fill=tk.BOTH)
        self.botoes_frame = tk.Frame(root, bg="black")
        self.botoes_frame.pack(fill=tk.X)
        self.exibir_titulo()

    def limpar_interface(self):
        self.texto_principal.delete(1.0, tk.END)
        for widget in self.botoes_frame.winfo_children():
            widget.destroy()

    def escrever(self, texto):
        if texto:
            self.texto_principal.insert(tk.END, texto + "\n")
            self.texto_principal.see(tk.END)

    def adicionar_botao(self, texto, comando):
        tk.Button(self.botoes_frame, text=texto, command=comando, width=50).pack(pady=2)

    def exibir_titulo(self):
        self.limpar_interface()
        self.escrever("Bem-vindo ao Angel Engine!")
        self.adicionar_botao("Iniciar", self.introducao)
        self.adicionar_botao("Sair", self.root.destroy)

    def introducao(self):
        self.limpar_interface()
        self.escrever("Você se encontra em um mundo misterioso.")
        self.adicionar_botao("Continuar", self.exibir_titulo)

if __name__ == "__main__":
    root = tk.Tk()
    app = AngelEngineGUI(root)
    root.mainloop()
