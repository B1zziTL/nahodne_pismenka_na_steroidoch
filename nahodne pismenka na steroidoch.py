#importovanie .py suboru a modulu
import poprehadzovany_text2_pomiesaj
import string

#zadeklarovanie premennych a zoznamov
znak = "nic"
daco = 1
slovicko = []
vystup = []
spec_znaky = ['?','.',':',',','"','(',')','!']

#otvorenie suborov
subor = open("poprehadzovany_text_vstup2.txt","r")
subor1 = open("poprehadzovany_text.txt","w")

for riadok in subor: #cyklus pre riadky v subore
    #rozdelenie riadku
    riadocek = riadok.split()
    
    for slovo in riadocek: #cyklus pre slova v rozdelenom riadku
        #zmena pomocnej premennej
        daco = 1

        #podmienka ak nejde o jednohlaskove slovo
        if not len(slovo) == 1:
            #podmienky pre urcenie prveho a posledneho pismena
            if slovo[-1] in spec_znaky:
                posledne = slovo[-2]
            else:
                posledne = slovo[-1]
            if slovo[0] in spec_znaky:
                prve = slovo[1]
            else:
                prve = slovo[0]

            #zmena pomocnej premennej ak je prve a posledne slovo rovnake
            if prve == posledne:
                daco = 2
                
            for pismeno in slovo: #cyklus pre pismena v slove
                #podmienka pre vlozenie pismena do zoznamu
                if pismeno not in spec_znaky:
                    if pismeno != prve and pismeno != posledne:
                        slovicko.append(pismeno)
                    else:
                        pocet = slovo.count(pismeno)
                        if pocet > daco:
                            daco += 1
                            slovicko.append(pismeno)
                else:
                    znak = pismeno
    
            #konverzia zoznamu na string
            retazec = "".join(slovicko)

            #vymazanie zoznamu
            slovicko.clear()

            #vyvolanie .py suboru a vlozenie vysledku do premennej
            pismenka = poprehadzovany_text2_pomiesaj.pomiesaj(retazec)

            #podmienky na spravne zapisanie znakov
            if znak == "nic":
                nove_slovo = prve + pismenka + posledne
            elif slovo.index(znak) == len(slovo)-1:
                nove_slovo = prve + pismenka + posledne + znak
            elif slovo.index(znak) == 0:
                nove_slovo = znak + prve + pismenka + posledne
            if slovo.count(znak) == 2:
                nove_slovo = znak + prve + pismenka + posledne + znak
            znak = "nic"

        #zmena premennych ak je jednohlaskove slovo        
        else:
            nove_slovo = slovo
            posledne = ""
            prve = ""

        #vlozenie noveho slova do zoznamu
        vystup.append(nove_slovo)

    #konverzia zoznamu na string    
    novy_riadok = " ".join(vystup)

    #vymazanie zoznamu
    vystup.clear()

    #zapisanie riadku do suboru
    subor1.write(novy_riadok + "\n")

#zatvorenie suborov
subor.close()
subor1.close()
