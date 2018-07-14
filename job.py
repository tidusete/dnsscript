import csv


dominis = ["example.es","laexample.com"]



for domini in dominis:
    
    from subprocess import call
    call(["python", "dnsrecon/dnsrecon.py", "-d", domini, "-t", "std", "-c", "csv_"+domini])
    with open ("csv_"+domini,"rb") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        aux=[][]
        for row in spamreader:
            print(row)
            trobat = 0
            cont = 0
            while (trobat == 0 and cont <= len(aux)):
                if row[0] is aux[cont][0]:
                    trobat = 1
                    aux[cont][1] = aux[cont][1]+"-"+row[1]+row[2]
                cont++
            if trobat == 0:
                aux[cont][0] = row[0]
            
                     

