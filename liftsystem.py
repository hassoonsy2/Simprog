import random
import time



class Lift:
    aantal_etages = 0           # Het aantal etage's
    register_lijst = []         # De lijst van klanten in de lift
    hudige_etage = 0            # Het huidige etage van de lift
    omhoog = 1                  # het bewegen van de lift omhoog
    omlaag = -1                 #het bewegen van de lift omlaag

    def __init__(self, aantal_etages, register_lijst):
        self.aantal_etages = aantal_etages
        self.register_lijst = register_lijst


    def klant_registreren(self, klanten):     # klant gaat de lift in
        for reg in klanten:
            self.register_lijst.append(reg)


class Klant:
    hudige_etage = 0                  # het huidige etage van de klant
    bestemming_verdieping = 0         # de gewilde bestemming van de klant
    klantid = 0                       # de ID van de klant
    in_lift = False                   # aangeven of de klant in de lift is
    voltooid = False                  # aangeven of de klant zijn bestemming heeft bereikt
    klant_richting = 0

    def __init__(self, klantid, etages):
        self.klantid = klantid                                        # self.customerID toewijzen aan customerID
        self.hudige_etage = random.randint(1, etages)                 # self.current_floor toewijzen aan random int tussen  1 en  etage ingevoerd
        self.bestemming_verdieping = random.randint(1, etages)        # seslf.destination_floor toewijzen aan random int tussen 1 en  etage ingevoerd
        while self.bestemming_verdieping == self.hudige_etage:
            self.bestemming_verdieping = random.randint(1, etages)
        if self.hudige_etage < self.bestemming_verdieping:
            self.klant_richting = 1
        else:
            self.klant_richting = -1






class Gebouw:
    aantal_etages = 3   # stel de variabele aantal_etages in op 3
    Klanten_lijst = []  # maakt een lege lijst voor Klanten_lijst
    lift = 0            # stel de variable lift op 0
    def __init__(self, etages, klanten):
        self.Aantal_etages = etages                                      # ingevoerde etage toewijzen aan number_of_floors
        for klantid in range(1, klanten + 1):                            # toegevoegde aantal klanten toewijzen aan to Klanten_lijst
            new = Klant(klantid,self.Aantal_etages)                      # maakt een instantie met de naam new van Klant class voor het aantal ingevoerde klanten
            self.Klanten_lijst.append(new)                               # appends new instance aan Klanten_lijst
        self.Klanten_lijst.sort(key = lambda x: x.hudige_etage)          # sorteer Klanten_lijst bij hudige_etage                                               # prints
        self.lift = Lift(etages,self.Klanten_lijst)                      # maakt een instantie van lift met ingevoegde etage's en wijs Klanten_lijst toe aan register_lijst                                                                            # prints
        self.run()

    def run(self):                                                                 # methode om de lift te bedienen
        print('************** LIFT START NU **************')
        print('Er zijn %d klanten in het gebouw' % (len(self.Klanten_lijst)))
        aantal_klanten = len(self.Klanten_lijst)                                   # wijs huidige aantal van klanten toe aan de variable aantal_klanten
        self.output()

    def output(self):
        for Klant in self.Klanten_lijst:                        #print lijsten af van klanten in het gebouw en hun gegevens
            print("Klant",Klant.klantid,"is op de vloer",Klant.hudige_etage,"en wil naar",Klant.bestemming_verdieping)

        #ELEVATOR MOVING UP LOOP
        while (self.lift.hudige_etage < self.lift.aantal_etages):

            print('LIFT BEWEEGT OMHOOG')
            print(len(self.Klanten_lijst),'Klanten in de lift.')
            print('***********************************************')
            print('Etage',self.lift.hudige_etage)
            self.lift.hudige_etage += 1

            for klant in self.Klanten_lijst:                              # Loop voor elk instantie van Klant in Klanten_lijst
                if (self.lift.hudige_etage == klant.hudige_etage) & klant.klant_richting == 1:
                    klant.in_lift = True
                    print('Klant',klant.klantid,'is de lift ingegaan')
                if (self.lift.hudige_etage == klant.bestemming_verdieping) & (klant.in_lift == True) & klant.klant_richting ==1:
                    klant.in_lift = False
                    self.Klanten_lijst.remove(klant)
                    print(klant.klantid,'heeft hun bestemming bereikt')


        #ELEVATOR MOVING DOWN LOOP
        while (self.lift.hudige_etage <= self.aantal_etages) & (self.lift.hudige_etage > 1):
            self.lift.hudige_etage -= 1
            print(len(self.Klanten_lijst),'Klanten in de lift.')
            print('LIFT DIE NAAR BENEDEN GAAT')
            print('++++++++++++++++++++++++++++++++++++++++++++++++++++')
            print('Etage',self.lift.hudige_etage)


            for klant in self.Klanten_lijst:
                if (klant.in_lift == True):
                    klant.current_floor = self.lift.hudige_etage
                if (self.lift.hudige_etage == klant.bestemming_verdieping) & (klant.in_lift == True) & (klant.klant_richting == -1):
                    klant.in_lift = False
                    self.Klanten_lijst.remove(klant)
                    print('Klant',klant.klantid,'heeft hun bestemming bereikt')

        print('Er Zijn ',len(self.Klanten_lijst),'opgesloten in de lift')
        print('Er zijn',len(Lift.register_lijst),'mensen die nog op het register staan')
        print('Lift run is gedaan!!!')

        print('KLANTEN DIE IN LIFT zitten, ZIJN HIERONDER:')
        for stuck in self.Klanten_lijst:
            print('Klant. ID:',stuck.klantid,'Bestemming. verdiping:',stuck.bestemming_verdieping,'Huidge. verdiping:',stuck.hudige_etage,'In lift',stuck.in_lift,'Richting',stuck.klant_richting)




def main():
    try:
        etages = 3                                                             # etages invoeren en toewijzen aan etages
        Klanten = int(input('Vul het aantal klanten in: '))                    # klanten invoeren en toewijzen aan klanten
        gebouw = Gebouw(etages, Klanten)                                       # instantie van gebouw gemaakt met invoer van verdiepingen en klanten
    except ValueError:
        print('U HEBT GEEN NUMMER INGEVOERD. OPNIEUW BEGINNEN.')
        main()


if __name__ == "__main__":
    main()