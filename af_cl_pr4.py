print("Un brăduţ este împodobit cu globuleţe albe, roşii şi albastre. Numărul globuleţelor albe se citeşte de la tastatură. Câte globuleţe are brăduţul, ştiind că numărul de globuleţe roşii este cu 3 mai mare decât numărul de globuleţe albe, iar globuleţele albastre sunt cu 2 mai puţine decât totalul celor albe şi roşii.")
ga = int(input("dati numarul de globulete albe:"))
gr = ga+3
gb = (gr+ga)-2
gt = ga+gr+gb
print("Pe bard sunt",gt,"globulete")