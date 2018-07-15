import csv


dominis = ["wowhead.com","wowchakra.com"]

from subprocess import call

aux = []
for domini in dominis:
    

    call(["python", "dnsrecon/dnsrecon.py", "-d", domini, "-t", "std", "-c", "csv_"+domini])
    with open ("csv_"+domini,"rb") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')

        tipus = []
        textAcumulat = []
        #aux = [tipus, textAcumulat, domini]
        
        for row in spamreader:
            #print(row)
            trobat=False
            cont= 0

            while (not trobat and cont < len(tipus)):

                if (row[0] == tipus[cont]):
                    trobat=True
                    textAcumulat[cont]=textAcumulat[cont]+""+row[1]+" "+row[2]+"||"
                cont=cont+1
            if (not trobat):
                tipus.append(row[0])
                textAcumulat.append(row[1]+" "+row[2]+"||")
                

        #print(tipus)
        #print(textAcumulat)
        #print(domini)
        aux2 = [domini,tipus,textAcumulat]
        aux.append(aux2)
 
print(aux)
