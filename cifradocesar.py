text = input('Palabra a cifrar: ')

#CREAMOS CADENA DE CARÁCTERES    
if text==text.upper () : 

#PARA MAYUSCULAS          
    abc="ABCDEFGHIJKLMNOPQRSTUVWXYZ"    
else:          
    abc="abcdefghijklmnopqrstuvwxyz" 
#DEFINIMOS VALOR DE DESPLAZAMIENTO  
k=int (input ("Valor de desplazamiento: "))    
 
cifrado=""    
#REALIZAMOS CIFRADO.  
for c in text:   
    if c in abc:
        cifrado+= abc [(abc.index(c)+k%(len(abc)))]
    else:       
        cifrado+=c    #VISUALIZAMOS TEXTO FINAL.  
print("texto cifrado: ",cifrado)  