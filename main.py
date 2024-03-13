import itertools, math

# definicion de codigo:  [n, M, d]-codigo en q(binario, ternario) es un conjunto de M palabras de longitud n, con una distancia minima d entre ellas 

def distanciaHamming(code_Word_1, code_word_2) -> int:
  """
  Calculates the Hamming distance between two code words.

  Parameters:
  code_Word_1 (str): The first code word.
  code_word_2 (str): The second code word.

  Returns:
  int: The Hamming distance between the two code words. Returns -1 if the code words have different lengths.
  """
  if len(code_Word_1) != len(code_word_2):
    return -1
  distancia = 0
  for i in range(len(code_Word_1)):
    if code_Word_1[i] != code_word_2[i]:
      distancia += 1
  return distancia

def esfera(codigo: str, base: int, t: int) -> list[str]:
  """
  Genera una lista de códigos a partir de un código base, reemplazando dígitos en posiciones específicas.

  Args:
    codigo (str): El código base a partir del cual se generarán los códigos.
    base (int): La base numérica utilizada para los reemplazos.
    t (int): El número máximo de dígitos a reemplazar en cada código generado.

  Returns:
    list: Una lista de códigos generados a partir del código base, con los reemplazos realizados.

  """
  longitud = len(codigo)
  esfera = [codigo]
  for r in range(1, t+1):
    for indices in itertools.combinations(range(longitud), r):
      for replacements in itertools.product(range(1, base), repeat=r):
        nuevo_codigo = list(codigo)
        for index, replacement in zip(indices, replacements):
          nuevo_codigo[index] = str(replacement)
        esfera.append(''.join(nuevo_codigo))
  return esfera

def esValido(codigo: list, longitud: int, base: int, distancia_min: int) -> bool:
  """
  Verifica si un código es válido según ciertos criterios.

  Args:
    codigo (list): La lista que representa el código.
    longitud (int): La longitud del código.
    base (int): La base del código.
    distancia_min (int): La distancia mínima permitida.

  Returns:
    bool: True si el código es válido, False en caso contrario.
  """
  return len(codigo) <= (base ** longitud) / (valor_esfera(longitud, base, errores_corrige(distancia_min))) # usa la cota de hamming

def esPerfecto(codigo: list, longitud: int, base: int, distancia_min: int) -> bool:
  return len(codigo) == (base ** longitud) / (valor_esfera(longitud, base, errores_corrige(distancia_min))) # usa la cota de hamming

def errores_corrige(distancia_min: int) -> int:
  return math.floor((distancia_min - 1)/2)

def errores_detecta(distancia_min: int) -> int:
  return math.floor(distancia_min/2)

def minima_distancia(codigo: list) -> int:
  min = int('inf')
  for c in codigo:
     for c2 in codigo:
       if distanciaHamming(c, c2) < min:
          min = distanciaHamming(c, c2)
  return min
      
def valor_esfera(longitud: int, base: int, radio: int) -> int:
  return sum([(math.factorial(longitud)/(math.factorial(r)*math.factorial(longitud-r)))*(base - 1)**r for r in range(radio+1)])

def empaquetamiento_esferico(base: int, longitud: int, t: int) -> list:
  todas_las_palabras = [''.join(map(str, x)) for x in itertools.product(range(base), repeat=longitud)]
  paquete = []

  for palabra in todas_las_palabras:
    if all(distanciaHamming(palabra, p) > t for p in paquete):
      paquete.append(palabra)

  return paquete

def cumple_cota_de_singleton(codigo: list, longitud: int, base: int, distancia_min: int) -> bool:
  return len(codigo) <= base ** (longitud - distancia_min + 1)

def esMDS(codigo: list, longitud: int, base: int, distancia_min: int) -> bool:
  return len(codigo) == base ** (longitud - distancia_min + 1)

def crear_codigo(longitud: int, base: int, dimension: int, matriz: list[list]) -> list:
  """
  Crea un código a partir de una matriz generadora.

  Args:
    longitud (int): La longitud de las palabras del código.
    base (int): La base numérica del código.
    dimension (int): La dimensión del código.
    matriz (list[list]): La matriz generadora del código.

  Returns:
    list: El código generado a partir de la matriz generadora.
  """
  palabras = [''.join(map(str, x)) for x in itertools.product(range(base), repeat=longitud)]
  codigo = []
  for palabra in palabras:
    palabra_codificada = ''
    for i in range(dimension):
      suma = 0
      for j in range(longitud):
        suma += int(palabra[j]) * matriz[i][j]
      palabra_codificada += str(suma % base)
    codigo.append(palabra_codificada)
  return codigo