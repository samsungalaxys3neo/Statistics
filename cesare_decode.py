# Decodifica Cesare senza testo originale
# Algoritmo: Frequenza delle lettere (assume che la lettera più frequente nel testo cifrato corrisponda alla 'E' italiana)

import string
from collections import Counter

def cesare_decode(ciphertext):
    # Solo lettere maiuscole
    text = ''.join(c for c in ciphertext.upper() if c in string.ascii_uppercase)
    if not text:
        return "Testo cifrato non valido."
    # Conta le frequenze
    freq = Counter(text)
    if not freq:
        return "Testo cifrato non valido."
    # Trova la lettera più frequente
    most_common = freq.most_common(1)[0][0]
    # In italiano, la lettera più frequente è 'E'
    key = (ord(most_common) - ord('E')) % 26
    # Decodifica
    decoded = []
    for c in ciphertext:
        if c.isupper():
            decoded.append(chr((ord(c) - 65 - key) % 26 + 65))
        elif c.islower():
            decoded.append(chr((ord(c) - 97 - key) % 26 + 97))
        else:
            decoded.append(c)
    return ''.join(decoded)

if __name__ == "__main__":
    # Esempio di utilizzo
    encrypted = input("Inserisci il testo cifrato Cesare: ")
    print("Testo decodificato:")
    print(cesare_decode(encrypted))
