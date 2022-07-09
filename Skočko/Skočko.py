import random

print('Dobrodosli u igru pogadjanja! \nPotrebno je da pogodite tacne pozicije brojeva 1-6. \nPravila su sledeca: \nImate 6 pokusaja. Unosite 4 broja, a nakon pokusaja prikazuje status: \n1 - tacno mjesto \n0 - postoji negdje \nX - ne postoji \nSrecno!')
GBox = '123456'
sol = ''.join(random.choice(GBox) for x in range(4))
solL = list(sol)
Final = '' #Result string
pozs = 0    #Keeps track of position in solution
pozg = 0    #Keeps track of position in guess
GuessNMBR = 6   #Keeps track of number of guesses left
BrojPokusaja = 0    #Keeps track of number of guesses done
MogucaSlova = []    #Array for symbols not in actual place, but they exist
PozicijeMogucihSlova = []   #Array for positions of said symbols
NizTacnosti = []    #Array that keeps track of how many correct guesses of said symbols we made
SlovaKojaSuTu = []  #Array that keeps track of letters that exist in the solution

for i in sol:
    if i not in SlovaKojaSuTu:
        SlovaKojaSuTu.append(i)
       
while GuessNMBR > 0:
    BrojPokusaja += 1
    Guess = input('Unesite vas pokusaj: ')
    if Guess == sol:
        print(f'Pogodili ste u {BrojPokusaja}. pokusaju! Rjesenje je bilo {sol} ')
        break
    GuessL = list(Guess)
    while pozg < 4:
        if GuessL[pozg] in sol:
            if GuessL[pozg] == solL[pozs]:
                Final += '1' #in correct place
            elif GuessL[pozg] != solL[pozs]: 
                MogucaSlova.append(GuessL[pozg])
                PozicijeMogucihSlova.append(pozg)
                Final += '2' #Exists but not in correct place (used for detailed checking later)
        else: 
            Final += 'X' #does not exist
        pozg += 1
        pozs += 1
    FinalL = list(Final)
    
    for i in MogucaSlova: 
        KolikoJePogodjeno = 0
        for p in range(4):
            if GuessL[p] == i and solL[p] == i:
                KolikoJePogodjeno += 1
        NizTacnosti.append(KolikoJePogodjeno)
    PozicijaFinal = 0 
    
    PomocniNiz = [] 
    for i in MogucaSlova: 
        Povecanje = 0
        KolikoKonkretnogSimbola = 0
        for j in sol: 
            if i == j:
                KolikoKonkretnogSimbola += 1
        if i in PomocniNiz: 
            for k in PomocniNiz:
                if k == i:
                    Povecanje += 1
        PomocniNiz.append(i)            
        NizTacnosti[PozicijaFinal] += Povecanje 
        if NizTacnosti[PozicijaFinal] >= KolikoKonkretnogSimbola:
            FinalL[PozicijeMogucihSlova[PozicijaFinal]] = 'X'
            PozicijaFinal += 1
        else:
            FinalL[PozicijeMogucihSlova[PozicijaFinal]] = '0'
            PozicijaFinal += 1
    
    Final = ' '.join(FinalL)
    List1 = []
    List0 = []
    ListX = []
    for i in FinalL:  #Sorting
        if i == '1':
            List1.append(i)
        elif i == '0':
            List0.append(i)
        else:
            ListX.append(i)
    FinalL = List1 + List0 + ListX
    print(FinalL)
   
    GuessNMBR -= 1
    if GuessNMBR == 0 and Final != sol: 
        print(f'Izgubili ste, rjesenje je bilo: {sol}')
        break
    else:
        print('Probajte ponovo')
        print(f'Preostali broj pokusaja je: {GuessNMBR}')
        pozg = 0
        pozs = 0
        Final = ''
        MogucaSlova = []
        PozicijeMogucihSlova = []
        NizTacnosti = []
        KolikoKonkretnogSimbola = 0
        PomocniNiz = []
        continue