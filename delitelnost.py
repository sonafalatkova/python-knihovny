"""Vypišme si čísla z nějakého rozsahu na základě jejich dělitelnosti dvěma čísly.

Zkuste z nějakého rozsahu čísel vypsat čísla, která jsou dělitelná 3 i 4 současně.
Zkuste z nějakého rozsahu čísel vypsat čísla, která jsou dělitelná 5 nebo 6. Stačí vypsat text: "Číslo je dělitelné 5 nebo 6."""

for cislo in range(1,31):
    if cislo%3 == 0 and cislo%4 == 0:
        print(f'Číslo', cislo, 'je dělitelné 3 a 4.')

for cislo in range(1,101):
    if cislo%5 == 0 and cislo%6 == 0:
        print(f'Číslo', cislo, 'je dělitelné 5 a 6.')

