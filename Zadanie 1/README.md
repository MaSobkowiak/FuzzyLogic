Zaprogramuj w dowolnym języku programowania funkcję wyliczającą wartości funkcji przynależności zbioru rozmytego podanego parametrycznie:

tzn funkcję: double fp(double a, double b, double c) która zwraca wartość funkcji przynależności z przedziału [0,1] i jest zdefiniowana przez parametry a, b. c

np. Zbiór rozmyty młody człowiek=fp(20,20,40)

Wskazówki:

Trójkątna funkcja przynależności powinna być definiowana trzema parametrami a, b, c

Jeżeli a=b - patrz fp1.jpg
Jeżeli b=c - patrz fp2.jpg
W przeciwnym przypadku - patrz fp3.jpg

Na potrzeby zamodelowania zbioru rozmytego można wykorzystać wzór na prostą przechodzącą przez dwa punkty (xa, ya) i (xb, yb):  y - ya = (yb - ya)/(xb-xa) * (x-xa).