list_of_questions = ['1. Quali materie ti appassionano di piu\'?',
                     '2. I tuoi compiti a casa di solito sono?',
                     '3. Hai un’ora libera, scegli di:',
                     '4. Come ti definiresti?',
                     '5. Qual e\' il tuo sogno nel cassetto?',
                     '6. In quale di queste affermazioni ti riconosci di piu\'?',
                     '7. Immaginati sul tuo futuro luogo di lavoro: come ti vedi?',
                     '8. I tuoi compagni di classe ti chiedono aiuto piu\' spesso per:',
                     '9. Il miglior insegnamento arriva da:',
                     '10. Di cosa hai bisogno per organizzarti al meglio?']

lists_of_answers = [[' 1. Italiano e storia\n', '2. Matematica\n', '3. educazione tecnica e scienze\n', '4. educazione fisica\n', '5. arte e musica\n'],
                    [' 1. Nella mia mente\n', '2. Perfetti\n', '3. Un po\' disordinati ma li faccio sempre tutti\n', '4. Noiosi\n', '5. Utili per scandire il ritmo del pomeriggio\n'],
                    [' 1. leggere un libro\n', '2. progettare applicazioni per il web\n',  '3. realizzare abiti e oggetti\n', '4. praticare attivita\' fisica\n', '5. ascoltare musica o disegnare\n'],
                    [' 1. curioso e indagatore\n', '2. pratico e concreto\n', '3. creativo e artistico\n', '4. sportivo e dinamico\n', '5. fantasioso e sensibile\n'],
                    [' 1. scrivere un romanzo\n', '2. contribuire ad un\'importante scoperta scientifica\n', '3. condurre un talk-show in prima serata\n', '4. allenare la Nazionale di calcio\n', '5. dipingere un\'opera d\'arte\n'],
                    [' 1. faccio amicizia facilmente\n', '2. mi piacciono le sfide\n', '3. ho una buona manualita\'\n', '4. ho un senso dell\'orientamento molto sviluppato\n', '5. ho un senso estetico spiccato\n'],
                    [' 1. con una penna seduto ad una scrivania\n', '2. in un laboratorio con il camice bianco\n', '3. con le mani “in pasta”\n', '4. sempre in movimento\n', '5. con un pennello o uno strumento musicale in mano\n'],
                    [' 1. correggere gli errori di grammatica\n', '2. fare i conti\n', '3. aggiustare qualcosa che si e\' rotto\n', '4. allenarsi\n', '5. leggere le note dello spartito o disegnare un particolare\n'],
                    [' 1. i grandi personaggi storici\n', '2. dallo studio\n', '3. dal realizzare qualcosa\n', '4. mettendomi sempre alla prova\n', '5. i grandi compositori e artisti\n'],
                    [' 1. di un buon rapporto con le persone che mi circondano\n', '2. di sapere cosa ci si aspetta esattamente da me\n', '3. di raccogliere tutte le informazioni utili\n', '4. di una buona dose di autonomia\n', '5. di poter improvvisare\n']]


def startSurvey():
  array_answer = []

  for each_question, each_answer in zip(list_of_questions, lists_of_answers):
    answer = input('\n\n' + each_question + '\n' + ' '.join(each_answer) + '\n> ')
    array_answer.append(int(answer))

  return array_answer

# startSurvey()