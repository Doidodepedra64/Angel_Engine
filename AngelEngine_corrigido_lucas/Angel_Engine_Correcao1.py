import os
import platform

def limpar_console():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

while True:
    import Titulo
    print('(1) Iniciar Experiência.\n(2) Sair do jogo.')
    opcao = input('Selecione sua opção: ')
    if opcao == '1':
        limpar_console()
        import Imagem_anjo
        print(
            '*(?????)*'
            '\n — "Dizem que os anjos descem à Terra para resgatar os pecadores.'
            ' Em momentos de desespero, as pessoas rezam, pedem, imploram por uma salvação divina.'
            '\n Mas o que acontece quando a sede por poder se torna mais forte que a fé na redenção?'
            '\n EU sei a resposta. Encontre-me... e descubra a verdade." —'
        )

        while True:
            print('(1) Seguir seus instintos curiosos.\n(2) Se manter na sombra do desconhecido.')
            opcao1 = input('Selecione uma opção: ')
            if opcao1 == '1':
                limpar_console()
               
                while True:
                    print(
                    '(1) - O que você quer de mim?\n(2) - Quem é você?\n(3) - Por que não me fala agora?\n(4) - Aonde devo ir?')
                
                    opcao_dialogo = input ('Selecione uma opção: ')
                    if opcao_dialogo in ['1']:
                        limpar_console()
                        print("Me ajude, me ajude, me ajude, e sua recompensa será virtuosa...")
                    elif opcao_dialogo in ['2']:
                        limpar_console()
                        print ("Eu já fui a última esperança. Desci dos céus para ajudar a todos, para livrá-los de seus pecados.")
                    elif opcao_dialogo in ['3']:
                        limpar_console()
                        print ("... A figura não responde. \nUm silêncio mortal se arrasta pela sua mente, e os zumbidos que o acompanham parecem ecoar dentro de você. Antes que essa pressão te esmague por completo...")
                    elif opcao_dialogo == '4':
                        limpar_console()
                        print(
                            '*A figura parece sorrir, mesmo com o rosto completamente desfigurado.*'
                            '\nTutorial para encontrar a Angel Engine:'
                            '\nEtapa Um: Viaje até a Terra Sagrada.'
                            '\nEtapa Dois: Procure, no terreno desolado, pelos grandes espinhos.'
                            '\nEtapa Três: Encontre meu sarcófago.'
                            '\nEtapa Quatro: Olhe para mim. Olhe para mim. Olhe para mim... e liberte-me.'
                            '\n*Após alguns segundos de silêncio, você sente seu corpo sendo arrancado do sonho à força.*')
                        print("Ao acordar, o som do despertador invade seus sentidos por alguns segundos."
                        "\nUma estranha sensação de que cada movimento seu está sendo julgado te afoga. Você se levanta, exausto, ainda preso às imagens da noite passada.")
                        print("Fora de casa, o mundo te recebe com o cheiro podre da morte e das mágoas acumuladas."
                        "\nO dia parece um eclipse eterno de fumaça e sol. As ruas estão desertas... mas isso não importa."
                        "\nNunca importou.")
                        print('(1) Seguir o caminho indicado.')
                       
                        while True:
                                opcao_dialogo2 = input ('Selecione uma opção: ')
                                if opcao_dialogo2 in ['1']:
                                    limpar_console()
                                    print("Você segue em um caminho sem fim, ainda com a sensação sobre seus ombros, ela não é pesada, somente o suficiente pra lembrar com oque você está lidando. \nApós longos dias de viagem, seguindo um caminho sem rumo, procurando algo que você nunca acreditou, finalmente surge na distancias, longos chifre que saem do chão, cobertos de mais espinhos, representando a sua chega na...")
                                    import Terrasagrada
                                    print('Antes de entrar a terra sagrada você é atingido por uma onda sonífera, a mesma sensação de quando você acordou nessa manhã.')
                                else:
                                    limpar_console()
                                    print('Você encara o vazio do espaço que está, percebendo que não existe essa opção')
                               
                                while True:
                                    print("(1) Descansar")
                                    opcao_dialogo3 = input('Selecione uma opção: ') #se vc não colocar nada só dar ENTER ele pula o dialogo todo e vai pro próximo while true :(
                                    if opcao_dialogo3 in ['1']:
                                        limpar_console()
                                        print("O cansaço é extremo, como se tivesse viajado por dias, bom, você nem se lembra se esse foi o caso, mas pouco importa. Você se deita no banco do carro, torcendo para essas terras sagradas não conterem perigo.")
                                        import Sonho
                                        print ("(1) - Deitar")
                                        input("Slecione um opção: ")
                                        print("No momento quer você encosta sua cabeça para finalmente descansar, seu repouso se torna vivido e a mesma figura que você sonhou na noite passada te aborda")
                                        import Demon
                                        print('*(O Anjo)*\n'
                                            '\nEu te sinto, você está no caminho certo'
                                            '\n*Desta vez você é agraciado pela visão da figura, com cabelos loiros e um sorriso gentil, apesar de estar sofrendo um terrível destino, presa em um peitoral, empalado por diversos cabos.*'
                                            '\nVamos, me pergunte oque te incomoda') #essa parte não ta aparecendo e eu não sei pq caralhos
                                        
                                        while True:
                                                print('(1)- Oque é você?\n(2) - Oque vai ser a minha recompensa? Se for pouco eu nem vou.\n(3) - Porque você precisa da MINHA ajuda?\n(4) - Onde eu encontro a maquina de anjos?')
                                                opcao_dialogo4 = input('Selecione uma opção: ')
                                                if opcao_dialogo4 in ['1']:
                                                    limpar_console()
                                                    print("Eu já fui um salvador, um ser divino a serviço do senhor, fui enviado sabendo que VOCÊS rezaram e aceitaram seus pecados.")
                                                elif opcao_dialogo4 in ['2']:
                                                    limpar_console()
                                                    print ('Então, no fim você vai querer uma recompensa? *A criatura parece surpresa com a sua pergunta.*\n(1) - Óbvio, você acha que eu estou fazendo isso de graça?\n(2) -Você me prometeu uma antes de vir')
                                                    
                                                    while True:
                                                        opcao_dialogo5 = input('Selecione uma opção ')
                                                        if opcao_dialogo5 in ["1"]:
                                                            limpar_console()
                                                            print ("*A figura parece descepcionada, em um movimento ela te agarra, ficando frente a frente com sua persona do sonho*\nNão é a toa que seu mundo se encontra nesse estado, seus pensamentos em adquirir poder sobrepõem totalmente a fé, você já perdeu sua humanidade a muito tempo, sua fé é corrupta e pagãos não serão perdoados, não mais.\n*Você sente uma onda de pressão, onde suas memórias vão sendo lentamente apagadas, destruídas, consumidas, enquanto a criatura te encara com um sorriso gentil, sabendo que seu destino é se tornar mais um…*")
                                                            import Esquecido
                                                            
                                                elif opcao_dialogo4 in ['3']:
                                                    limpar_console()
                                                    print ("... *a figura nâo responde, um silencio mortal toma conta da sua mente, você decide falar algo antes que ela te sufoque pela pressão")
                                                elif opcao_dialogo4 == '4':
                                                    limpar_console()
                                    else:
                                        limpar_console()
                                        print('Você encara o vazio do espaço que está, percebendo que não existe essa opção')                 
            elif opcao1 == '2':
                limpar_console()
                print('Com seus sentidos perturbados pela presença da figura, você decide ignorar o chamado e acordar.')
                print("Ao acordar, o som do despertador inibe seus sentidos por alguns segundos. A sensação de que cada ação sua está sendo julgado te afoga, enquanto você se levanta cansado, ainda pensando sobre oque sonhou na noite passada.")
               
                while True:
                    print('(1) - Ir Trabalhar')
                    opcao2_dialogo = input('Selecione um opção: ')
                    if opcao2_dialogo in ['1']:
                        limpar_console()
                        print ('O vazio da cidade te impressiona a cada dia que passa, os locais mais lotados são as igrejas, que agora existe uma a cada esquina, esperando para que você se junto na reza. Seu trabalho nunca foi especial, e você se sente orgulhoso de não fazer parte de algo maior, você sempre foi um esquecido.')
                       
                        while True:
                            opcao2_dialogo2 = input('(1) - Você entra no seu trabalho... ')
                            if opcao2_dialogo2 in ['1']:
                                limpar_console()
                                print('Ao chegar em seu trabalho, tudo parece comum, a produção ainda é a mesma, e seus colegas são os mesmos.No intervalo, você se senta para comer e ve um anuncio governamental na televisão, você nunca ligou muito pra isso, mas seus colegas parecem preocupados, quando você se senta, ve um figura familiar…')
                                import Presidente
                                print ("Boa noite, senhoras e senhores. *Você ve o presidente do pais, sua cara representa uma momento sério, o único som que você consegue escutar é o barulho que da transmissão.* Estou diante de você neste dia como homem, marido, pai, como seu Presidente, mas o mais importante, como cidadão deste país. Não vou adoçar nossa situação atual; Estamos à beira da guerra")
                                print("*O presidente faz uma pausa, ponderando oque suas próximas palavras podem fazer com o mundo, porém voce nota algo a mais. Uma figura, com grandes cabelos loiros, mãos apoiadas no encosto da cadeira, com olhos que penetram diretamente os seus. Voce olha para os seus companheiros esperando uma reação similar a sua, buscando conforto nos rostos conhecidos, porém nenhuma mudança de expressão pode ser avistada.\n Ao olhar novamente para a TV, o presidente tem sua cara arrancada, sobrando somente suas pupilas, e de detre do seu cranio voce consegue ouvir em sua voz.* Seus espaços vão desaparecer.")
                                print("Em corte brusco na transmissão, você sai do transe e retoma consciência sobre o espaço, percebendo que todos os seus colegas voltaram para o trabalho, você nota que a tv voltou a funcionar, e o pronuncimento do presidente voltou." 
                                "\n(1) - Seguir assintindo a transmissão"
                                "\n(2) - Voltar a trabalhar")
                                opcao2_dialogo3 = input("Selecione uma opção: ")
                                if opcao2_dialogo3 in ['1']:
                                    limpar_console()
                                    print("*Voce se mantem na sala, vidrado na tela onde o presidente continuar a falar*\nEste não é um teste; Isso não é uma piada.\nInfelizmente é a verdade.\nEnquanto falamos, nossos inimigos estão preparando seu arsenal nuclear.\n *O foco sai totalmente do presidente, mostrando um local diferente.\nVocê nunca viu algo parecido, duas portas de metal gigantescas, trancadas, com apenas um cientista na frente, ele parece ansioso para compartilhar sua descoberta, porém antes mesmo que ele possa falar, as portas se abrem, revelando o anjo, o anjo que nós humanos capturamos, que estamos mantem em cárcere, para que possamos ver essa transmissão.*")
                                    print("'Um...Anjo?'")
                                   
                                    while True:
                                        opcao2_dialogo4 = input('Selecione uma opção: ')
                                        if opcao2_dialogo4 in ['1']:
                                            print ("*Sem tempo de processar a aparição da figura, o cientista começa a falar.*\n Realizamos todos os testes no livro sobre esse cara aqui, e os resultados são incríveis.\nNão parece haver um limite para sua produção de energia, ou seja, se outras opções esgotarem, poderíamos alimentar o mundo inteiro por milênios.")
                                            import Doutor
                                            print ("Você encara a tela, com mil perguntas na sua cabeça, ‘como que prenderam um anjo?’, ‘porque ele ainda sorri depois de tudo isso?’ mas...")
                                            input('Aonde eu to? ')
                                           
                                            while True:
                                                    if opcao2_dialogo4 in['1']:
                                                        limpar_console()
                                                        print("Você se pergunta olhando ao redor, você esteve tão vidrado na tela que não percebeu que você foi movido.  Como se tivesse dormido por tempo demais, você se encontra deitado em uma sala fria, Há a existência de uma névoa espessa, que cobre a sua visão, bloqueando seus sentidos.")
                                                       
                                                        while True:
                                                            print("(1) - Tocar as paredes\n(2) - Gritar por ajuda\n(3) - Esperar")
                                                            opcao2_dialogo5 = input("Selecione uma opção: ")
                                                            if opcao2_dialogo5 in['1']:
                                                                limpar_console()
                                                                print("Você começa a gritar, seus pulmões ainda muito fracos, fazem sua voz ser demasiada fraca para chamar tanta atenção. Mesmo assim, sentado na sala, você aguarda uma resposta que possa te satisfazer.")
                                                            elif opcao2_dialogo5 in['2']:
                                                                limpar_console()
                                                                print("Você se levanta, ainda cansado, seus movimentos são lentos, você tenta tocar as paredes em busca de algo para se orientar. Elas são frias, com textura metálica, fazendo você se perguntar aonde foi levado.")
                                                            if opcao2_dialogo5 in['3']:
                                                                limpar_console()
                                                                print("Você decide esperar, paciente mente por algo acontecer, porém sua quietude revela algo, gritos, de outra pessoa, parece estar sendo arrastada, sua curiosidade lhe ataca, porém, essa prisão, onde você acha que está, foi trancada.")
                                                                
                                                                while True:
                                                                    input("Você escuta paços vindos do corredor: ")
                                                                    print('*Antes que você possa continuar a investigar na sala, uma porta grande de metal é aberta, revelando o cientista, o mesmo que falava sobre o programa da Maquina de anjos.*\nEntão, mais um objeto de teste\n*Ele fala isso pra outro cientista, uma mais velho, que anota em uma caderneta.*\nComêssemos, sem demora, se tivermos outra falha, os outros vão começar a suspeitar da gente.\n*O cientista fala isso, te puxando, para o corredor, onde a luz dele te cega brevemente.*')
                                                                    print("(1) - Se entregar\n(2) - Lutar contra")
                                                                    opcao2_dialogo6 = input ("Selecione um opção: ")
                                                                    if opcao2_dialogo6 in ["1"]:
                                                                        limpar_console()
                                                                        print("Você está muito fraco para lutar, se entregando enquanto é carregado em direção a uma sala de testes, você consegue escutar os gritos de outras vitimas.")
                                                                       
                                                                        while True:
                                                                            print("(1) - Lutar\n(2) - Desistir")
                                                                            opcao2_dialogo7 = input("Escolha uma opção: ")
                                                                            if opcao2_dialogo7 in ['1']:
                                                                                limpar_console()
                                                                                print("Você decide de impor, não é assim que você quer morrer, porém você não pode decidir isso mais.\nNo momento em que você tenta se soltar das mãos do doutor, ele rápidamente te imobiliza e coloca você em uma camara, que automaticamente injeta você com um liquido vermelho estranho, te desmaiando em poucos segundos, onde você observa o doutor encarando você, com uma expressão alexitimia no rosto.")
                                                                                import Confinado
                                                                                exit()
                                                                            elif opcao2_dialogo7 in ['2']:
                                                                                print("Você desiste de continuar tentando, suas forças se foram a muito tempo, até porque, um ser insignificante como você não foi capaz de concluir uma missão simples como essa, bom...você mereceu o seu destino... Rápidamente, colocam você em uma camara, que automaticamente injeta você com um liquido vermelho estranho, te desmaiando em poucos segundos, onde você observa o doutor encarando você, com uma expressão alexitimia no rosto.")
                                                                                import Confinado
                                                                    elif opcao2_dialogo6 in['2']:
                                                                        limpar_console()
                                                                        print('Você junta forçar quase divinas pra conseguir se soltar do braço do cientista, que com pouco tempo de reagir, solta seu corpo facilmente. Você corre sem rumo por corredores que parecem todos iguais, enquanto o doutor anuncia em um rádio:') 
                                                                        import Fugitivo                                        
                                                                        print("(1) - Virar a direita\n(2) - Virar a esquerda")
                                                                       
                                                                        while True:
                                                                            opcao2_dialogo8 = input("Selecione um opção: ")
                                                                            if opcao2_dialogo8 in ['1']:
                                                                                limpar_console()
                                                                                print("Você passa por mais corredores cinzas, as sirenes de repente soam, o cientista mais velho perde o ritmo e fica para trás, gritando pro seu companheiro não te perder de vista, suas forças já estão se esgotando e você encontra oque parece uma capsula de fuga.")
                                                                                print("(1) - Entrar na capsula\n(2) - Continua a correr")
                                                                               
                                                                                while True:
                                                                                    opcao2_dialogo9 = input("Selecione uma opção: ")
                                                                                    if opcao2_dialogo9 in ['1']:
                                                                                        limpar_console()
                                                                                        print("*No momento que você entra na capsula, ela se fecha automaticamente, de fundo a voz do cientista pode ser ouvida, enquanto você lentamente é submergido em um liquido viscoso e vermelho. *Sabe,  garoto, você tinha potencial, não tinha que ser assim, problema é... *Ele fala isso acionando algo fora da capsula, você se desespera ao sentir o sangue de ferro fortíssimo saindo do liquido.* Porém, agora você ta aqui, preso nessa engenhoca que inventamos, pronto pra virar um deles, eu me pergunto como é a experiência, normalmente vocês entram desacordados. *Antes que você possa dizer qualquer coisa, um estrondo desagradável atinge suas orelhas, fazendo elas sangrarem enquanto um zumbido desagradável faz sua cabeça girar, lentamente, você desmaia...*")
                                                                                        import Transtornado
                                                                                    elif opcao2_dialogo8 in ['2']:
                                                                                        limpar_console()
                                                                                        print("Você continua correndo por corredores infinitos, suas pernas cansadas e dormentes quase não respondem aos seus comandos, em uma certa parte, o outro cientista mais velho perde o ritmo e fica pra trás, porém você vê uma sala maior, com a porta aberta, e uma figura presa por cabos, você tem a sensação se ser chamado, e contra sua vontade.")
                                                                                    
                                                                                        while True:
                                                                                            print("(1) - Continuar a correr\n(2) - Entra na sala")
                                                                                            opcao2_dialogo10 = input('Selecione uma opção: ')
                                                                                            if opcao2_dialogo10 in ['1']:
                                                                                                limpar_console()
                                                                                                print('Você continua a correr, suas pernas cansadas fazem muito esforço para acompanhar o seu corpo, você leva ao máximo suas forças, até que avista uma grande porta, ele brilha, levando você acreditar que essa seria a escadaria para o paraíso, suas esperanças são esmagadas quando um soldado te desfere um soco. Seu corpo cai uma ultima vez, você observa a porta sendo fechada enquanto é fuzilado…')
                                                                                                import Patria
                                                                                                exit()
                                                                                            elif opcao2_dialogo10 in ['2']:
                                                                                                limpar_console()
                                                                                                print("Você entra rapidamente no grande salão, fechando a porta de metal, sem nenhuma saída, te prendendo nessa sala escura, no fundo dela você vê essa figura, com a figura, que parece perceber sua presença, porém, sua feição está selada por uma mascara de contenção transformando a figura divina um uma ferramenta, uma bateria viva.")
                                                                                                print("(1) - Liberar o Anjo\n(2) - Menter ele preso")

                                                                                                while True:
                                                                                                    opcao2_dialogo11 = input ('Selecione uma opção: ')
                                                                                                    if opcao2_dialogo11 in ['1']:
                                                                                                        limpar_console()
                                                                                                        print("*Você toma uma decisão rápida, rapidamente retirando todas os cabos conectados no anjo,  despertando ele de um profundo sono, após retirar todos os cabos, você se dirige para retirar a sua ultima contenção, quando a porta atrás de você se abre, revelando o cientista que te perseguia anteriormente.*\nCalma, não faz isso, ele tá mentindo, ele não vai trazer a salvação, não depois de tudo isso.\n*Você observa o doutor se aproximando lentamente, tentando te convencer a desistir da ideia de libertar o anjo.*\nEu sei que pode não acreditar em mim, mas se liberta-lo, será o nosso fim")


                                        else:
                                            limpar_console()
                                            print('Você encara o vazio do espaço que está, percebendo que essa opção não existe')
                                        
                                                

                                elif opcao2_dialogo3 in ['2']:
                                    limpar_console()
                                    print ('Você sai da sala, com a mente perturbada pelas imagens que acabou de ver, você se pergunta se tudo isso foi real. Você anda pelos corredores do seu trabalho, seus colegas te encarram enquanto você se dirige a sua sala. Ao sentar na sua cadeira, você rápidamente recebe mais declarações de óbitos, suas mãos ainda tremendo, você começa a realizar seu trabalho, no outro dia você repete o mesmo processo, e novamente no próximo dia...')
                                    import Medroso
                                    exit()
                            else:
                                limpar_console()
                                print('*Você encara o vazio do espaço que está, percebendo que não existe essa opção*')
                    else:
                        limpar_console()
                        print('*Você encara o vazio do espaço que está, percebendo que não existe essa opção*')
            else:
                limpar_console()
                print('*Você encara o vazio do espaço que está, percebendo que não existe essa opção*')





    elif opcao == '2':
        print("Você se perdeu!!!!")
        break