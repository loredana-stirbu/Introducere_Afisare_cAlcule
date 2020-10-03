print("Măriuca ţine evidenţa iepurilor din crescătorie. Ea îşi notează câţi iepuri sunt la începutul fiecărei luni, câţi au murit şi câţi s-au născut în cursul fiecăei luni. Puteţi să realizaţi un program care, primind aceste date, să afişeze la sfârşitul fiecărei luni câţi iepuri sunt în crescătorie?")
a = int(input("Numarul de iepuri la inceput de luna: "))
b = int(input("Numarul de iepuri morti: "))
c = int(input("Numarul de iepuri nascuti: "))
s=a-b+c
print("La sfarsitul lunii in crescatorie sunt",s,"iepuri")