
import os
Rijec = input("Unesite skrivenu rijec ")
os.system("cls")

brslova = 0
SkrivenaRijec = '' #odvojena rijec za onoga ko pogadja
for q in Rijec:
    SkrivenaRijec += '_'
    brslova += 1
Rijec = list(Rijec) #radimo sa listama zbog manipulacija
SkrivenaRijec = list(SkrivenaRijec)
BrojPokusaja = 4
i = 1 #indeks za numeraciju pokusaja
poz = 0 #indeks za poziciju slova pri kretanju kroz rijec
prisutnost = 0 #ovo znaci da slovo nije pogodjeno (bice 1 ukoliko postoji vise istih slova u rijeci)
PrintIndikator = 0 #nije stampano (bice 1 ako je vec 1 slovo pogodjeno pa da ne stampa poruku ponovo)
print(f'Zadata rijec ima {brslova} slova.')
NizPokusaja = [] #Inicijalizacija praznog niza radi skladistenja vec pokusanih slova

while BrojPokusaja > 0:
    Pokusaj = input(f'Unesite vas {i}. pokusaj: ').lower() #unesemo pokusaj    
    if len(Pokusaj) == 1 and Pokusaj.isalpha(): #ako je samo 1 slovo uneseno(ne pusta brojeve ili ostalo)
        if Pokusaj not in NizPokusaja:  #Ako nismo to slovo nijednom probali, idi dalje, u suprotnom mora da se proba nesto drugo
            for p in Rijec: #prolazimo kroz slova rijeci
                if Pokusaj == p: #ako je nas pokusaj slova tacan
                    SkrivenaRijec[poz] = Pokusaj #u skrivenu rijec upisi na konkretnom mjestu pokusaj
                    poz += 1 #indeks pozicije slova(nije isti za string i listu pa moramo korigovat)
                    if PrintIndikator == 0: #znaci da prvi put pogadjamo(slucaju da postoji vise istih slova)
                        print('Pogodili ste slovo')
                        PrintIndikator = 1 #da ne bi stampalo vise puta poruku za ista slova
                        NizPokusaja.append(Pokusaj) #dodajemo konkretno slovo u niz vec probanih slova
                        i += 1 #indeks za novi pokusaj
                    prisutnost = 1 #Znaci da konkretni pokusaj postoji u rijeci() Da li smo stigli do kraja i da li se pojavljuje to slovokad ga nadje 1 da ne stampa odma poruku

                else: #treba nesto da ne stampa kad promasimo da smo pogrijesili, DA LI SMO ZAVRSILI SA ISPITIVANJEM SLOVA I DA LI NEMA POGODJENIH
                    poz += 1 
                    if poz >= len(Rijec) and  prisutnost == 0: # Ako smo prosli kroz citavu rijec i nema naseg pokusaja
                        print('Pogrijesili ste slovo, pokusajte ponovo.')
                        BrojPokusaja -= 1
                        print(f'Preostalo vam je {BrojPokusaja}. pokusaja.') 
                        NizPokusaja.append(Pokusaj)
                        i += 1

            poz = 0 #kad zavrsi sva slova kroz rijec, resetuj poziciju i pocni sledeci pokusaj     
            prisutnost = 0 #resetujemo prisutnost za novi pikusaj
            PrintIndikator = 0 #reset prepoznavanje duplikata za novi pokusaj
            print(SkrivenaRijec) #pokazuje trenutno stanje
    
     #Nakon pokusaja, provjerava da li smo pogodili rijec
            for x in range(len(SkrivenaRijec)):  #prolazimo kroz trenutno pogadjanje (current progress)
                if SkrivenaRijec == Rijec: #nema vise donjih crta
                    print(f"Pogodili ste trazenu rijec u {i-1} pokusaja!")
                    BrojPokusaja = 0 #da ne bi ulazilo u while petlju
                    break
                elif SkrivenaRijec != Rijec and BrojPokusaja > 0: #Ako nismo pogodili rijec a imamo jos sansi za pogadjanje, nastavi dalje
                    continue
                else: #ako nismo pogodili rijec i nemamo sansi
                    print(f'Niste pogodili rijec, trazena rijec je: {Rijec}')
                    break
        else: #Ako je nas pokusaj vec proban, ne modifikuj nista i kreni opet
            print('Vec ste probali to slovo ili ste lose unijeli, pokusajte opet')
    else:
        print('Vec ste probali to slovo ili ste lose unijeli, pokusajte opet')