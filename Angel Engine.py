
import tkinter as tk

# Importações seguras de ASCII
try:
    from Imagens.Imagem_anjo import ascii_anjo
    from Imagens.Demon import ascii_demon
    from Imagens.Presidente import ascii_presidente
    from titulos.Confinado import ascii_confinado
    from Imagens.Doutor import ascii_doutor
    from titulos.Esquecido import ascii_esquecido
    from titulos.Fugitivo import ascii_fugitivo
    from titulos.Medroso import ascii_medroso
    from titulos.Patria import ascii_patria
    from titulos.Terrasagrada import ascii_terra
    from titulos.Sonho import ascii_sonho
    from titulos.Transtornado import ascii_transtornado
    from titulos.Titulo import ascii_titulo
    from titulos.Euxarido import ascii_Euxarido
    from Imagens.Observadora import ascii_Observadora
    from Imagens.esquecido import ascii_esquecido
except ImportError:
    ascii_anjo = ascii_demon = ascii_presidente = ascii_confinado = ascii_doutor = ascii_esquecido = ""
    ascii_fugitivo = ascii_medroso = ascii_patria = ascii_terra = ascii_sonho = ascii_transtornado = ""
    ascii_titulo = ascii_Euxarido = ascii_maquinaAnjo = ascii_Observadora = ""

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
        self.escrever(ascii_titulo)
        self.adicionar_botao("Iniciar Experiência", self.introducao)
        self.adicionar_botao("Sair do jogo", self.root.destroy)

    def introducao(self):
        self.limpar_interface()
        self.escrever(
            'Você se encontra deitado em sua cama. A suave luz da lua atravessa a janela e repousa delicadamente sobre um canto do colchão.' 
            '\nSeus olhos pesam, vencidos pelo cansaço de um longo dia de trabalho. O silêncio da noite te envolve, e, aos poucos, o sono começa a te levar.' 
            )
        self.adicionar_botao("Dormir", self.conversa_anjo)

    def conversa_anjo(self):
        self.limpar_interface()
        self.escrever(ascii_esquecido)
        self.escrever(
            '*(?????)*'
            '\n — "Dizem que os anjos descem à Terra para resgatar os pecadores.'
            '\n Em momentos de desespero, as pessoas rezam, pedem, imploram por uma salvação divina.'
            '\n Mas o que acontece quando a sede por poder se torna mais forte que a fé na redenção?'
            '\n EU sei a resposta. Encontre-me... e descubra a verdade." —'
        )
        self.adicionar_botao("Seguir seus instintos curiosos", self.dialogo_inicial)
        self.adicionar_botao("Se manter na sombra do desconhecido", self.final_sombra)
    
    def dialogo_inicial(self):
        self.limpar_interface()
        self.escrever(ascii_anjo)
        self.adicionar_botao("O que você quer de mim?", lambda: self.mensagem("Me ajude, Me ajude, Me ajude, e sua recompensa será virtuosa", self.dialogo_inicial))
        self.adicionar_botao("Quem é você?", lambda: self.mensagem("Eu já fui a última esperança, desci dos céus para ajudar a todos, livrá-los de seus pecados", self.dialogo_inicial))
        self.adicionar_botao("Por que não me fala agora?", lambda: self.mensagem("... *a figura não responde, um silêncio mortal toma conta da sua mente...*", self.dialogo_inicial))
        self.adicionar_botao("Aonde devo ir?", self.tutorial_angel_engine)

    def final_sombra(self):
        self.limpar_interface()
        self.escrever("Você decide ignorar o chamado.\n" + ascii_medroso)
        self.adicionar_botao("Voltar ao menu", self.exibir_titulo)

    def tutorial_angel_engine(self):
        self.limpar_interface()
        self.escrever(
            '*A figura parece sorrir, mesmo com o rosto completamente desfigurado.*'
            '\nTutorial para encontrar a Angel Engine:'
            '\nEtapa Um: Viaje até a Terra Sagrada.'
            '\nEtapa Dois: Procure, no terreno desolado, pelos grandes espinhos.'
            '\nEtapa Três: Encontre meu sarcófago.'
            '\nEtapa Quatro: Olhe para mim. Olhe para mim. Olhe para mim... e liberte-me.'
            '\n*Após alguns segundos de silêncio, você sente seu corpo sendo arrancado do sonho à força.*'
        )
        self.adicionar_botao("Acordar", self.acordar)

    def acordar(self):
        self.limpar_interface()
        self.escrever(
            'Ao acordar, o som do despertador invade seus sentidos por alguns segundos.'
            '\nUma estranha sensação de que cada movimento seu está sendo julgado te afoga. Você se levanta, exausto, ainda preso às imagens da noite passada'
            '\nFora de casa, o mundo te recebe do jeito que ele se tornou, o céu escuro coberto pela fumaças das Fábricas que Nunca Param, as ruas lotadas de lixo e de corpos de "Indignos", pessoas que os religiosos achavam ser pecadores'
            '\nFechando a porta de casa, seu caminho será como nos outros dias, desafiador, mas isso não importa mais.'
            '\nNunca importou.')
        self.adicionar_botao("Seguir o caminho", self.terra_sagrada)
        

    def terra_sagrada(self):
        self.limpar_interface()
        self.escrever(ascii_terra)
        self.escrever('Você caminha por dias, o cansaço te consome ao longo do caminho, porém de longe você vê, longos empinhos que saem do chão cobrem uma longa paisagem desértica'
                      '\nFinalmente chegando na Terra Sagrada. Deseja descansar?')
        
        self.adicionar_botao("Descansar", self.sonho)
        self.adicionar_botao("Continuar a caminhar", self.caminho_cansado)
    
    def caminho_cansado(self):
        self.limpar_interface()
        self.escrever('Você continua a caminhar, seu cansaço torna seus passos mais pesados, como se seus ossos fossem feitos de pedra e o mundo estivesse empurrando você de volta. O chão seco da Terra Sagrada range sob seus pés, coberto por espinhos negros que se erguem como nervuras de um corpo moribundo.'
                    'Eles não se movem. Eles não têm vida. Você repete isso mentalmente. Mas, a cada passo, você jura que um ou dois estão mais próximos — como se crescessem atrás de você.'
                    'Ao longe, é possível ver uma estrutura impossível, erguida de maneira que desafia as leis da física, guardando a única esperança da humanidade: a Máquina de Anjos')
        
        self.adicionar_botao('Seguir o caminho até a Máquina de anjos', self.observadora)
        self.adicionar_botao('Procurar um lugar para descançar', self.sonho)
    
    def observadora(self):
        self.limpar_interface()
        self.escrever('Você continuar a caminhar em direção a máquina de anjos, desesperado para cumprir a sua missão, a cada passo dado mais seus movimentos se tornam mais atrapalhados.\n' 
                    'O sol lentamente começa a cair, e a escuridão vai tomando conta, você começa a ter dificuldade de enchergar a direção de onde está indo.' 
                    'A medida que se avança em direção a Máquina de Anjos, você pode ver ao lado uma grande cratera, onde você consegue observar uma criatura de joelhos rezando, no centro dela.')
        
        self.adicionar_botao('Continuar a caminhar', self.fim_desprotegido) 
        self.adicionar_botao('Procurar um lugar para descançar', self.local_descanco)
    
    def local_descanco(self):
        self.escrever("penis")


    def fim_desprotegido(self):
        self.limpar_interface()
        self.escrever('Ignorando o ambiente se escurecendo, você continua a caminhar em direção a Máquina de anjos, o cansaço quase vence do seu corpo, quando você finalmente se encontra cara a cara com as grandes portas que bloqueiam a passagem para entrar na Máquina de anjos.\n' \
        'Você começa a procurar por uma maneira de entrar, quando derepente de tráz da Máquina de Anjos, você uma figura surgindo, ciculando a estrutura que a mantém presa por uma corrente, porém isso não há impede de perceber a sua presença, onde sua presença faz seus olhos derreterem, deixando como a ultima coisa que vocë escuta sendo um grito de uma mulher distorcida.')
        self.escrever(ascii_Observadora)
                      

    def sonho(self):
        self.limpar_interface()
        self.escrever(ascii_sonho)
        self.escrever(ascii_demon)
        self.escrever(
            "*(O Anjo)*\n"
            "Eu te sinto, você está no caminho certo...\n"
            "Desta vez, você é agraciado pela visão da figura: cabelos loiros, sorriso gentil, empalada por cabos.\n"
            "Vamos, me pergunte o que te incomoda."
        )
        self.adicionar_botao('O que é você?', lambda: self.mensagem("Eu já fui um salvador, um ser divino a serviço do senhor, fui enviado sabendo que VOCÊS rezaram e aceitaram seus pecados.", self.sonho))
        self.adicionar_botao('Oque vai ser a minha recompensa? Se for pouco eu nem vou', self.recompensa)
        self.adicionar_botao("Por que precisa da minha ajuda?", lambda: self.mensagem("... * a figura nâo responde, um silêncio toma conta da sua mente, você decide falar algo antes que ela te sufoque pela pressão", self.sonho))
        self.adicionar_botao("Onde encontro a máquina de anjos?", self.maquina_anjos)

    def recompensa(self):
        self.limpar_interface()
        self.escrever("Então, no fim você vai querer uma recompensa?")
        self.adicionar_botao("1 - Óbvio, você acha que faço isso de graça?", self.fim_egoismo)
        self.adicionar_botao("2 - Você me prometeu uma antes de vir", lambda: self.mensagem("A figura parece entender e sorri levemente.", self.sonho))

    def fim_egoismo(self):
        self.limpar_interface()
        self.escrever('*A figura parece descepcionada, em um movimento ela te agarra, ficando frente a frente com sua persona do sonho*\n'
                    'Não é a toa que seu mundo se encontra nesse estado, seus pensamentos em adquirir poder sobrepõem totalmente sua fé, sua humanidade é corrupta e pagãos não serão perdoados, não mais.\n'
                    '*Você sente uma onda de pressão, onde suas memórias vão sendo lentamente apagadas, destruídas, consumidas, enquanto a criatura te encara com um sorriso gentil, sabendo que seu destino é se tornar mais um…*')
        self.adicionar_botao("Esquecido", self.esquecido)
    
    def esquecido(self):
        self.limpar_interface()
        self.escrever(ascii_esquecido)
        self.adicionar_botao("Voltar ao menu", self.exibir_titulo)

    def mensagem(self, texto, proximo_estado):
        self.limpar_interface()
        self.escrever(texto)
        self.adicionar_botao("Voltar", proximo_estado)

    def maquina_anjos(self):
        self.limpar_interface
        self.escrever('Como chegar na Máquina de Anjos:\n'
                    'Passo 1: Pacote suprimentos suficientes. Não haverá nenhum.\n'
                    'Passo 2: Não deixe que os esquecidos te encontrem. Eles não levam gentilmente a estrangeiros.\n'
                    'Passo 3: Não olhe para o céu. Seus olhos, eles irão derreter.')
        
        self.adicionar_botao("Acordar", self.dia2)
        self.adicionar_botao("Voltar", self.sonho)


if __name__ == "__main__":
    root = tk.Tk()
    app = AngelEngineGUI(root)
    root.mainloop()

