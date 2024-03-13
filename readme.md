# Proyecto de Codificación N-aria

Este proyecto implementa varias funciones para trabajar con códigos n-arios, incluyendo la generación de esferas de códigos y el empaquetamiento esférico.

## Funciones

### distanciaHamming(code_Word_1: str, code_word_2: str) -> int

Calcula la distancia de Hamming entre dos palabras de código. Devuelve -1 si las palabras de código tienen longitudes diferentes.

### esfera(codigo: str, n: int, t: int) -> List[str]

Genera una esfera de radio t en un código n-ario. La esfera es una lista de todas las palabras de código que están a una distancia de Hamming de hasta t desde la palabra de código dada.

### empaquetamiento_esferico(n: int, longitud: int, t: int) -> List[str]

Realiza el empaquetamiento esférico de un código. El empaquetamiento esférico es una lista de palabras de código tal que cada palabra de código está a una distancia de Hamming de al menos t+1 de todas las otras palabras de código en el paquete.

## Cómo usar

Para usar estas funciones, simplemente importe el archivo `main.py` en su código Python y llame a las funciones como se muestra en los ejemplos de uso a continuación:

```python
import main

# Calcular la distancia de Hamming entre dos palabras de código
distancia = main.distanciaHamming('1010', '1001')
print(distancia)  # Imprime: 2

# Generar una esfera de radio 1 en un código binario
esfera = main.esfera('1010', 2, 1)
print(esfera)  # Imprime: ['1010', '0010', '1110', '1000', '1020', '1011', '1012']

# Realizar el empaquetamiento esférico de un código binario de longitud 4 con t = 1
paquete = main.empaquetamiento_esferico(2, 4, 1)
print(paquete)  # Imprime: ['0000', '0011', '0101', '0110', '1001', '1010', '1100', '1111']
```

## Contribuir

Las contribuciones son bienvenidas. Por favor, abra un problema para discutir la contribución antes de hacer un pull request.

## Licencia

Este proyecto está licenciado bajo los términos de la licencia MIT.