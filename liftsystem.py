import random
import time


class Gebouw:                                                                                                                         # defines class building
    aantal_etages = 3                                                                                                                # sets number_of_floors variable to 0
    Klanten_lijst = []                                                                                                                  # creates an empty array for customer_list
    lift = 0                                                                                                                        # sets elevator variable to 0

    def __init__(self, etages, klanten):
        self.Aantal_etages = etages                                                                                                  # assigns floors entered to number_of_floors
        for klantid in range(1, klanten + 1):                                                                                      # assigns number of customers entered to customer_list in order
            new = Klant(klantid,self.Aantal_etages)                                                                            # creates an instance called new of Customer class for number of customers entered in input
            self.Klanten_lijst.append(new)                                                                                              # appends new instance of customer to customer_list
        self.Klanten_lijst.sort(key = lambda x: x.hudige_etage)                                                                        # sorts customer_list by current_floor customer is on                                               # prints
        self.lift = Lift(etages,self.Klanten_lijst)                                                                             # creates instance of elevator with inputted floors and assigns customer_list to register_list                                                                            # prints
        self.run()                                                                                                                      # runs run method below

    def run(self):                                                                                                                      # method to operate the elevator
        print('************** LIFT START NU **************')                                                      # prints
        print('Er zijn %d klanten in het gebouw' % (len(self.Klanten_lijst)))                                                     # prints
        aantal_klanten = len(self.Klanten_lijst)                                                                                   # assigns current number of customers to number_of_customers variable
        self.output()                                                                                                                   # runs output method below

    def output(self):
        for Klant in self.Klanten_lijst:                                                                                                   #prints lists of customers in building and their details
            print("Klant",Klant.klantid,"is op de vloer",Klant.hudige_etage,"en wil naar",Klant.bestemming_verdieping)

        #ELEVATOR MOVING UP LOOP
        while (self.lift.hudige_etage < self.lift.aantal_etages):

            print('LIFT BEWEEGT OMHOOG')
            print(len(self.Klanten_lijst),'Klanten in de lift.')
            print('***********************************************')
            print('Etage',self.lift.hudige_etage)
            self.lift.hudige_etage += 1

            for klant in self.Klanten_lijst:                                                                                             # Loop for each instance of Custumer in customer_list
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

        print('Er Zijn ',len(self.Klanten_lijst),'opgesloten in de lift')                                                            #prints
        print('Er zijn',len(Lift.register_lijst),'mensen die nog op het register staan')
        print('Lift run is gedaan!!!')                                                                                                #prints

        print('KLANTEN DIE IN LIFT zitten, ZIJN HIERONDER:')
        for stuck in self.Klanten_lijst:
            print('Klant. ID:',stuck.klantid,'Bestemming. verdiping:',stuck.bestemming_verdieping,'Huidge. verdiping:',stuck.hudige_etage,'In lift',stuck.in_lift,'Richting',stuck.klant_richting)


class Lift:
    aantal_etages = 0                                                                                                # the number of floors
    register_lijst = []                                                                                                  # the list of customers in the elevator
    hudige_etage = 0                                                                                                   # the current floor of the elevator
    omhoog = 1                                                                                                              # moves the elevator up
    omlaag = -1                                                                                                           # moves the elevator down

    def __init__(self, aantal_etages, register_lijst):
        self.aantal_etages = aantal_etages
        self.register_lijst = register_lijst

    def beweeg(self):                                                                                                     # method to move the elevator by 1 floor
        pass;

    def klant_registreren(self, klanten):                                                                             # customer goes into elevator
        for reg in klanten:
            self.register_lijst.append(reg)



    def klant_annuleren(self, Klanten):                                                                               # customer goes out of the elevator
        pass;


class Klant:
    hudige_etage = 0                                                                                                   # the current floor of the elevator
    bestemming_verdieping = 0                                                                                               # the destination floor of the elevator
    klantid = 0                                                                                                      # the customers ID
    in_lift = False                                                                                                 # denotes whether customer is in the elevator
    voltooid = False                                                                                                    # denotes whether customer has reached the destination floor
    klant_richting = 0

    def __init__(self, klantid, etages):                                                                             # initilize Customer class
        self.klantid = klantid                                                                                    # assigns self.customerID to customerID
        self.hudige_etage = random.randint(1, etages)                                                                  # assigns self.current_floor to random int between 1 and floors entered
        self.bestemming_verdieping = random.randint(1, etages)                                                              # assigns seslf.destination_floor to random int between 1 and floors entered
        while self.bestemming_verdieping == self.hudige_etage:
            self.bestemming_verdieping = random.randint(1, etages)
        if self.hudige_etage < self.bestemming_verdieping:
            self.klant_richting = 1
        else:
            self.klant_richting = -1


def main():                                                                                                             # main method
    try:                                                                                                                # try/except for user input menu
        etages = 3                                                             # enter floors and assign to floors
        Klanten = int(input('Vul het aantal klanten in: '))                                                           # enter customers and assign to customers
        gebouw = Gebouw(etages, Klanten)  # instance of building created with inputs of floors and customers      # create instance of Building class (building)
    except ValueError:
        print('U HEBT GEEN NUMMER INGEVOERD. OPNIEUW BEGINNEN.')
        main()


if __name__ == "__main__":
    # header()
    main()