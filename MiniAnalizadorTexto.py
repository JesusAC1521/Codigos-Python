texto = input("Buen dia, Ingresa el texto a analizar")
print("A continuacion ingresa las letras con las que vamos a trabajar ")
letras = []
letras.append(input("Ingresa la primer letra "))
# se puede ahorrar lineas poniendo:
# letras.append(input("Ingresa x letra").lower())
letras.append(input("Ingresa la segunda letra "))
letras.append(input("Ingresa la tercer letra "))
print(letras)
texto = texto.lower()
letraa = str(letras[0])
letrab = str(letras[1])
letrac = str(letras[2])
num_primera = texto.count(letraa.lower())
num_segunda = texto.count(letrab.lower())
num_tercera = texto.count(letrac.lower())
print(f"La letra {letras[0]} aparece {num_primera}, la letra {letras[1]} aparece {num_segunda} veces y la letra {letras[2]} aparece {num_tercera} veces")
texto_lista = texto.split()
total_palabras = len(texto_lista)
print(f"El texto tiene un total de {total_palabras} palabras")
primera_palabra = texto_lista[0]
ultima_palabra = texto_lista.pop()
# para usar metodo de la indexacion
# ultima_palabra = texto_lista[-1]
# correccion de que era letra y no palabra
# Para solucionar eso es usar directamente texto
print(f"La primer palabra del texto es '{primera_palabra}' y la ultima es '{ultima_palabra}'")
texto_lista = texto.split()
texto_lista.reverse()
texto_reverso = " ".join(texto_lista)
# Se ahorra una linea de codigo pues " " ya es un str
# recordad que join unira la lista y usara como separador al tring
print(f"El texto con todo al revez es: {texto_reverso}")
aparece = "python" in texto
dic = {True:"si aparece",False:"no aparece"}
print(f"La palabra 'python' {dic[aparece]} en el texto")
