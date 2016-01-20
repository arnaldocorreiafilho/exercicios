


def palindromo(s):
    temp = "".join(reversed(s))
    return temp == s


def reverse(s):
    temps = ""
    contador = len(s)-1
    while(contador >= 0):
        temps = temps + s[contador]
        contador = contador - 1
    return  temps
def palindromo2(s):
    temps = reverse(s)
    contador = 0
    while(contador < len(temps)):

        if(not(s[contador]==temps[contador])):
            return False
        contador = contador + 1
    return True