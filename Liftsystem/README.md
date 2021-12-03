# Simprog

We hebben gekozen om een Finite State Machine te maken voor een liftsysteem.

We zijn begonnen met het modelleren van de machine. Het doel was om de machine zo simpel mogelijk te omtwerpen. Dat houdt in zo min mogelijk transities en states. Dus we zijn begonnen met een lift die één etage omhoog en omlaag kon. Uiteindelijk hebben we hem iets uitgebreider gemaakt. De lift kan nu manouvreren tussen drie etages. De begane grond, de eerste en de tweede etage. Ons model van de FSM ziet er als volgt uit.


![image](https://user-images.githubusercontent.com/74369553/143570243-c97ab0b8-0d61-4545-bd69-080c7f80e5c0.png)

Nu hebben we aan de hand van dit model onze code verder gebouwd. De code is onder verdeeld in drie verschillende classes. De lift class, de gebouw class en de klant class. Verder zijn er een aantal belangrijke aspecten in onze code. Om te beginnen werken we met een input die vraagt om de hoeveelheid klanten die op de lift staan te wachten. Als je de code liftsystem.py runt, worden er verschillende simulaties gemaakt. Eerst wordt er bepaald welke klant waar precies heen wilt. Vervolgens wordt er gesimuleerd hoe de lift beweegt om de klanten naar hun bestemming te brengen (Output). Dat ziet er als volgt uit. 

![image](https://user-images.githubusercontent.com/74369553/143574226-feba03d7-f1de-4a7e-be31-fe2503d474ab.png)
