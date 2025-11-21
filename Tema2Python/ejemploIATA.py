canary_iata = ( 'TFN' , 'TFS' , 'LPA' , 'GMZ' , 'VDE' , 'SPC' , 'ACE' , 'FUE' )
f = open('aeropuertosCanarios.txt', 'a')
for codigo in canary_iata:
    f.write(codigo + '\n')
f.close()


