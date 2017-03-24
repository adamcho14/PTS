# PTS1 README
Program uchovava zoznam ucastnikov a ich aktualny stav bodov v sutazi.
Po spusteni si program od uzivatela vypyta heslo. Potom program caka na prikazy od uzivatela,
ktore nasledne vykona.

## Zoznam prikazov:

points <name> <number>  
  Prida hracovi <name> <number> bodov. Cislo moze byt aj zaporne.  
  Ak hrac <name> este nie je evidovany prida ho do zoznamu s <number> bodmi.  

reduce <number>  
  Znizi pocet bodov kazdeho hraca o <number>%. Vysledok sa zaokruhli na cele cisla nadol.  

junior <name>   
  Oznaci, ze hrac <name> je junior  

ranking   
  Vypise cele poradie. Hracov zoradime podla poctu bodov.  

ranking junior  
  Vypise poradie medzi juniormi.  

quit  
  Ukonci program.  


Ak uzivatel zada prikazy points, reduce, junior, a quit system si najprv vypyta password
a prikaz vykona iba v pripade, ze password je spravny.   

## Zoznam funkcii:
points(name, number)  
  Vykonava prikaz points so zadanymi <name> <number>  

reduce(number)  
  Vykonava prikaz reduce so zadanym <number>  

junior(name)  
  Vykonava prikaz junior so zadanym <name>  

ranking()  
  Vykonaca prikaz ranking  

ranking_junior()  
  Vykonava prikaz ranking junior  

quit()  
  Vykonava prikaz quit  

## Zoznam dekoratérov:
@password  
Vyžiada si pred vykonanim zadanych funkcii heslo.   
Ak je spravne, funkciu vykona.  
Ak nie, vypise hlasku.   
