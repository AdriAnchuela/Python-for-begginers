import time





def factoring(n): #descomposición en factores primos
  text= str(n) + ' = '
  i = 1
  for i in range(1, int(n/2)+1, 2):      # recorre los impares
    if i==1: i=2                         # salvo el 1 que será 2
    counter = 0
    while n % i == 0:
      n /= i
      counter += 1
    if counter == 1:
      text += str(i)+ ' × '
    elif counter > 1:
      text += str(i) + '^' + str (counter) + ' × '
  if text[-2] == "=":       # si no hay divisores
    text += str(n) + ' × '  # en ese caso el propio n será primo
  text += '1'
  return text

if __name__ == "__main__":
  while True:
    try:
      n = int(input('Introduzca el número a factorizar: ') or 202)
      start_time = time.time()
      if 1 < n <= 1e10:
        break
      else:
        print('Por favor, introduzca un número en el rango [2,10_000_000_000]')
    except ValueError:
      print('Por favor itroduzca un número entero positivo.')

  print(factoring(n))
  print("--- %s seconds ---" % (time.time() - start_time))