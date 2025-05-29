from tkinter import ttk
import pygame
import tkinter as tk
pygame.mixer.init()

#SOU GAY

#def tocar_musica(cenario):
#    pygame.mixer.music.stop()
#    pygame.mixer.music.load(musicas[cenario])
#    pygame.mixer.music.play(-1) 

#musicas = {
#    "introducao": r'D:\Programa\AngelEngine\Angel_Engine-main\Passado Misterioso [NGCtEepSTJI].mp3',
#    "acordar": r'D:\Programa\AngelEngine\Angel_Engine-main\BlackWeald - Astral Chasm _ Dark Ambient Horror Soundscape [jJS-1mtZHIc].mp3',
#    "terra_sagrada": r'D:\Programa\AngelEngine\Angel_Engine-main\Encontrei Algo Aqui_ [WkSbALPTcuQ].mp3'
#}

#click_sound = None
#try:
#   click_sound = pygame.mixer.Sound()  # coloque aqui o caminho certo do seu arquivo de clique
#except Exception as e:
#    print(f"Erro ao carregar som de clique: {e}")

#def play_click_sound():
#    if click_sound:
#        click_sound.play()

try:
    from titulos.SHC import ascii_SHC
    from Imagens.Anjo import ascii_anjo
    from Imagens.Anjo2 import ascii_demon
    from Imagens.Anjo3 import ascii_Anjo3
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
        self.fullscreen = True
        self.root.attributes('-fullscreen', self.fullscreen)
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TButton",
                        font=("JetBrains Mono", 12, "bold"),
                        padding=5,
                        width=50,
                        foreground="white",
                        background="#333",
                        borderwidth=10)
        style.map("TButton",
                  foreground=[('pressed', 'white'), ('active', 'white')],
                  background=[('pressed', '#555'), ('active', '#555')])
        self.texto_principal = tk.Text(root, wrap="word", bg="black", fg="white", font=("Courier", 11))
        self.texto_principal.pack(expand=True, fill=tk.BOTH)
        self.botoes_frame = tk.Frame(root, bg="black")
        self.botoes_frame.pack(fill=tk.X)
        self.exibir_titulo()

    def limpar_interface(self):
        self.texto_principal.delete(1.0, tk.END)
        for widget in self.botoes_frame.winfo_children():
            widget.destroy()

    def alternar_fullscreen(self):
        self.fullscreen = not self.fullscreen
        self.root.attributes('-fullscreen', self.fullscreen)

    def escrever_ascii(self, texto):
        if texto:
            self.texto_principal.insert(tk.END, texto + "\n")
            self.texto_principal.see(tk.END)

    def escrever(self, texto, indice=0):
     if indice < len(texto):
        self.texto_principal.insert(tk.END, texto[indice])
        self.texto_principal.see(tk.END)
        indice += 1
        self.root.after(25, self.escrever, texto, indice)

    def adicionar_botao(self, texto, comando):
        def comando_com_som():
            #play_click_sound()
            comando()
        btn = ttk.Button(self.botoes_frame, text=texto, command=comando_com_som)
        btn.pack(pady=5, padx=10, fill='x')

    def adicionar_botao_lado(self, texto, comando):
        def comando_com_som():
            #play_click_sound()
            comando()
        btn = ttk.Button(self.botoes_frame, text=texto, command=comando_com_som)
        btn.pack(side="left", padx=5, pady=5)

    def exibir_titulo(self):
        self.limpar_interface()
        self.escrever_ascii(ascii_titulo)
        self.adicionar_botao("Iniciar Experiência", self.introducao)
        self.adicionar_botao("Sair do jogo", self.root.destroy)
        #tocar_musica("introducao")


    def introducao(self):
        self.limpar_interface()
        self.escrever(
            'Você se encontra deitado em sua cama. A suave luz da lua atravessa a janela e repousa delicadamente sobre um canto do colchão.' 
            '\nSeus olhos pesam, vencidos pelo cansaço de um longo dia de trabalho. O silêncio da noite te envolve, e, aos poucos, o sono começa a te levar.' 
            )
        self.adicionar_botao("Dormir", self.conversa_anjo)

    def conversa_anjo(self):
        self.limpar_interface()
        self.escrever_ascii(ascii_anjo)
        self.escrever(
            '*(?????)*'
            '\n— "Dizem que os anjos descem à Terra para resgatar os pecadores.'
            '\nEm momentos de desespero, as pessoas rezam, pedem, imploram por uma salvação divina.'
            '\nMas o que acontece quando a sede por poder se torna mais forte que a fé na redenção?'
            '\nEU sei a resposta. Encontre-me... e descubra a verdade.'
        )
        self.adicionar_botao("Seguir seus instintos curiosos", self.caminho1)
        self.adicionar_botao("Se manter na sombra do desconhecido", self.caminho2)
    
    def caminho1(self):
        self.limpar_interface()
        self.escrever_ascii(ascii_anjo)
        self.adicionar_botao("O que você quer de mim?", lambda: self.mensagem("Me ajude, Me ajude, Me ajude, e sua recompensa será virtuosa", self.caminho1))
        self.adicionar_botao("Quem é você?", lambda: self.mensagem("Eu já fui a última esperança, desci dos céus para ajudar a todos, livrá-los de seus pecados", self.caminho1))
        self.adicionar_botao("Por que não me fala agora?", lambda: self.mensagem("... *a figura não responde, um silêncio mortal toma conta da sua mente...*", self.caminho1))
        self.adicionar_botao("Aonde devo ir?", self.tutorial_angel_engine)

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
            '\nUma estranha sensação de que cada movimento seu está sendo julgado te afoga. Você se levanta, exausto, ainda preso às imagens da noite passada')
        self.adicionar_botao("Sair de casa", self.Sair_de_Casa)
        #tocar_musica("acordar")
        
    def Sair_de_Casa(self):
        self.limpar_interface()
        self.escrever('Fora de casa, o mundo te recebe do jeito que ele se tornou, o céu escuro coberto pela fumaças das Fábricas que Nunca Param, as ruas lotadas de lixo e de corpos de "Indignos", pessoas que os religiosos achavam ser pecadores.'
            '\nFechando a porta de casa, seu caminho será como nos outros dias, desafiador, mas isso não importa mais.'
            '\nNunca importou.')
        self.adicionar_botao('Arrumar sua casa', self.escolher_item)
        self.adicionar_botao('Seguir o caminho indicado', self.terra_sagrada)
        self.adicionar_botao('Esquecer de tudo isso e ir trabalhar', self.ir_trabalhar)
        

    def escolher_item(self):
        self.limpar_interface()
        self.escrever('Sua casa sempre foi bagunçada, suas roupas estendidas na cadeira, empilhadas em camadas de dias esquecidos. Há copos com restos de café frio em cantos onde a luz quase não alcança, e um cobertor meio caído do sofá, como se tivesse sido abandonado às pressas.\n' \
                    'Na bagunça de seu quarto, você encontra um antigo presente dado pela sua mãe, um lido cachecol tricotado por ela mesma usando a mesma estampa brega que ela sempre usou, ao lado dele você vê seu antigo revolver, uma arma leve mas mortal.')
        self.adicionar_botao('Levar o cachecol', lambda: self.definir_item("Cachecol"))
        self.adicionar_botao('Levar o revoler', lambda: self.definir_item("Revolver"))

    def definir_item(self, item):
        self.item_escolhido = item
        self.escrever(f"Você escolheu o {item}. Essa escolha afetará seu caminho.", self.Sair_de_Casa2)

    def terra_sagrada(self):
        self.limpar_interface()
        self.escrever(ascii_terra)
        self.escrever('Você caminha por dias, o cansaço te consome ao longo do caminho, porém de longe você vê, longos empinhos que saem do chão cobrem uma longa paisagem desértica'
                      '\nFinalmente chegando na Terra Sagrada. Deseja descansar?')
        
        self.adicionar_botao("Descansar", self.sonho)
        self.adicionar_botao("Continuar a caminhar", self.caminho_cansado)
        #tocar_musica("terra_sagrada")
    
    def caminho_cansado(self):
        self.limpar_interface()
        self.escrever('Seguindo seu rumo, o cansaço torna seus passos mais pesados, como se seus ossos fossem feitos de pedra e o mundo estivesse empurrando você de volta. O chão seco da Terra Sagrada range sob seus pés, coberto por espinhos negros que se erguem como nervuras de um corpo moribundo.'
                    'Eles não se movem. Eles não têm vida. Você repete isso mentalmente. Mas, a cada passo, você jura que um ou dois estão mais próximos — como se crescessem atrás de você.'
                    'Ao longe, é possível ver uma estrutura impossível, erguida de maneira que desafia as leis da física, guardando a única esperança da humanidade: a Máquina de Anjos')
        
        self.adicionar_botao('Seguir o caminho até a Máquina de anjos', self.caminho_cansado2)
        self.adicionar_botao('Procurar um lugar para descançar', self.local_descanco)
    
    def caminho_cansado2(self):
        self.limpar_interface()
        self.escrever('Você continuar a caminhar em direção a máquina de anjos, desesperado para cumprir a sua missão, a cada passo dado torna seus movimentos mais atrapalhados.\n' 
                    'O sol lentamente começa a cair, e a escuridão vai tomando conta, você começa a ter dificuldade de enchergar a direção de onde está indo.' 
                    'A medida que se avança em direção a Máquina de Anjos, você pode ver ao lado uma grande cratera, onde você consegue observar, no centro dela, uma criatura de joelhos rezando.')
        
        self.adicionar_botao('Continuar a caminhar', self.observadora) 
        self.adicionar_botao('Descançar', self.local_descanco)

    def local_descanco(self):
        self.limpar_interface()
        self.escrever('Com as pernas dormentes, você observa o caminho.')

    def observadora(self):
        self.limpar_interface()
        self.escrever_ascii(ascii_Observadora)
        self.escrever('Ignorando o ambiente se escurecendo, você continua a caminhar em direção a Máquina de anjos, o cansaço quase vence do seu corpo, quando você finalmente se encontra cara a cara com as grandes portas que bloqueiam a passagem para entrar na Máquina de anjos.\n' \
        'Você começa a procurar por uma maneira de entrar, quando derepente de tráz da Máquina de Anjos, você uma figura surgindo, ciculando a estrutura que a mantém presa por uma corrente, porém isso não há impede de perceber a sua presença...')
        self.adicionar_botao('Sair correndo', self.correr)
        self.adicionar_botao('Fechar os olhos e tapar os ouvidos', self.se_proteger)

    def correr(self):
        self.limpar_interface()
        self.escrever('Se virando rápidamente antes que a criatura possa abrir seus olhos, Você junta forças sobrehumanas e sai correndo. A sensação de estar sendo perseguido te acompanha até conseguir se esconder em um espinhos próximo da Máquina de anjos.\n'
        'Hiperventilando, você se escora em um dos espinhos. Quando você olha de volta para a criatura...')
        self.adicionar_botao('- Ela não....estava ali?', self.fim_observadora)

    def se_proteger(self):
        self.limpar_interface()
        self.escrever('Você cobre suas orelhas e fecha seus olhos da melhor maneira que pode, seus batimentos acelerados é a unica coisa que você escuta.')
        self.adicionar_botao('Abrir os olhos', self.fim_observadora2)
        self.adicionar_botao('Manter eles fechados', lambda: self.escrever('Mentendo suas orelhas e olhos fechados, seus batimentos acelerados é a unica coisa que você escuta.'))

    def fim_observadora(self):
        self.limpar_interface()
        self.escrever(ascii_SHC)
        self.escrever("Quando você fala isso é agarrado imediatamente pela criatura, abrindo um grande sorriso enquanto seus grandes olhos cruzam com os seus, fazendo suas pupilas fritarem em uma dor insuportável que se espalha pelo seu corpo inteiro...")
        self.adicionar_botao("Voltar ao menu", self.exibir_titulo)

    def fim_observadora2(self):
        self.limpar_interface()
        self.escrever(ascii_SHC)
        self.escrever('Você abre seus olhos, na esperança que a criatura tenha sumido, apenas para dar de cara com grandes olhos que cruzam com os seus, fazendo suas pupilas fritarem em uma dor insuportável que se espalha pelo seu corpo inteiro... ')
        self.adicionar_botao("Voltar ao menu", self.exibir_titulo)

    def sonho(self):
        self.limpar_interface()
        self.escrever_ascii(ascii_sonho)
        self.escrever_ascii(ascii_demon)
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
        self.escrever('A figura parece descepcionada, em um movimento ela te agarra, ficando frente a frente com sua persona do sonho\n'
                    '- Não é a toa que seu mundo se encontra nesse estado, seus pensamentos em adquirir poder sobrepõem totalmente sua fé, sua humanidade é corrupta e pagãos não serão perdoados, não mais.\n'
                    'Você sente uma onda de pressão, onde suas memórias vão sendo lentamente apagadas, destruídas, consumidas, enquanto a criatura te encara com um sorriso gentil, sabendo que seu destino é se tornar mais um…')
        self.adicionar_botao("Esquecido", self.esquecido)
    
    def esquecido(self):
        self.limpar_interface()
        self.escrever_ascii(ascii_esquecido)
        self.adicionar_botao("Voltar ao menu", self.exibir_titulo)

    def mensagem(self, texto, proximo_estado):
        self.limpar_interface()
        self.escrever(texto)
        self.adicionar_botao("Voltar", proximo_estado)

    def maquina_anjos(self):
        self.limpar_interface()
        self.escrever('- Como chegar na Máquina de Anjos:\n'
                    '- Passo 1: Cubra seus ouvidos, ou eles seram estourados\n'
                    '- Passo 2: Não deixe que os esquecidos te encontrem. Eles não acolhem os estrangeiros.\n'
                    '- Passo 3: Não olhe para o céu. Seus olhos, eles irão derreter.\n' \
                    '- Ele está aqui. Cubra seus olhos. Cubra seus ouvidos. Não pare. Ele vai te pegar. Não escute. Não acredite. O enganador não pode prejudicar sua alma.')
        
        self.adicionar_botao("Acordar", self.dia2)
        self.adicionar_botao("Voltar", self.sonho)

    def dia2(self):
        self.limpar_interface()
        self.escrever('Ao acordar, você sente um alivio, como se tivesse dormido por dias.'
                    'Explorar as terras sagradas não é oque você pensava, com seus olhos e ouvidos tapados, a única coisa que você sente são seus paços em uma largo campo de areia, enquanto esbarra nos espinhos longos')
        self.adicionar_botao('Socorro', self.dia2)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    def caminho2(self):
        self.limpar_interface()
        self.escrever('Com seus sentidos perturbados pela presença da figura, você decide ignorar o chamado e acordar.\n'
                    'Ao acordar, o som do despertador inibe seus sentidos por alguns segundos. A sensação de que cada ação sua está sendo julgado te afoga, enquanto você se levanta cansado, ainda pensando sobre oque sonhou na noite passada.')
        self.adicionar_botao('Arrumar a casa', self.escolher_item2)
        self.adicionar_botao('Sair de casa', self.Sair_de_Casa2)

    def escolher_item2(self):
        self.limpar_interface()
        self.escrever('Sua casa sempre foi bagunçada, suas roupas estendidas na cadeira, empilhadas em camadas de dias esquecidos. Há copos com restos de café frio em cantos onde a luz quase não alcança, e um cobertor meio caído do sofá, como se tivesse sido abandonado às pressas.\n' \
                  'Na bagunça de seu quarto, você encontra um antigo presente dado pela sua mãe, um lido cachecol tricotado por ela mesma usando a mesma estampa brega que ela sempre usou, ao lado dele você vê seu antigo revolver, uma arma leve mas mortal dada pelo seu pai no dia que você saiu de casa.')
        
        self.adicionar_botao('Levar o cachecol', lambda: self.definir_item2("Cachecol"))
        self.adicionar_botao('Levar o revolver', lambda: self.definir_item2("Revolver"))

    def definir_item2(self, item):
        self.item_escolhido = item
        self.escrever(f"Você escolheu o {item}. Essa escolha afetará seu caminho.")
        self.Sair_de_Casa2()

    
    def Sair_de_Casa2(self):
        self.limpar_interface()
        self.escrever('Fora de casa, o mundo te recebe do jeito que ele se tornou, o céu escuro coberto pela fumaças das Fábricas que Nunca Param, as ruas lotadas de lixo e de corpos de "Indignos", pessoas que os religiosos achavam ser pecadores.'
            '\nFechando a porta de casa, seu caminho será como nos outros dias, desafiador, mas isso não importa mais.'
            '\nNunca importou.')
        
        self.adicionar_botao('Ir trabalhar', self.ir_trabalhar)
        self.adicionar_botao('Regredir e escutar o Anjo', self.regredir)

    def ir_trabalhar(self):
        self.limpar_interface()
        self.escrever('Bora trabaiaaaaaaaaa')
    
    def regredir(self):
        self.limpar_interface()
        self.escrever('Você decide ajudar o anjo, se entregrando a aquela pressão estranha que ele fazia...')
        self.adicionar_botao('Ouvir oque ele tem pra dizer', self.caminho1)



if __name__ == "__main__":
    root = tk.Tk()
    app = AngelEngineGUI(root)
    root.mainloop()

