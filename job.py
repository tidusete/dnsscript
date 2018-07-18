import csv


dominis = ["wowhead.com","wowchakra.com"]

from subprocess import call
header = ["dominio"]
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
                if (row[0] not in header):
                    header.append(row[0])
                 
                if (row[0] == tipus[cont]):
                    trobat=True
                    textAcumulat[cont]=textAcumulat[cont]+" + "+row[1]+" "+row[2]
                cont=cont+1
            if (not trobat):
                tipus.append(row[0])
                textAcumulat.append(row[1]+" "+row[2])
                

        #print(tipus)
        #print(textAcumulat)
        #print(domini)
        aux2 = [domini,tipus,textAcumulat]


        aux.append(aux2)
trash=[]
#abrimos csv final
with open('dnsfinal.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=",")
    spamwriter.writerow(header)
    for domini,nomdomini in enumerate(dominis):
        trash=[]

        trash.append(aux[domini][0])

        index=1
        while (index < len(header)):
            trobat3=False
            cont=1

            while (not trobat3 and cont < len(aux[domini][1])):
                if(aux[domini][1][cont] == header[index]):
                    trobat3=True
                    trash.append(aux[domini][2][cont])
                cont=cont+1
            if (not trobat3):
                trash.append(",")
            index=index+1
        spamwriter.writerow(trash)





