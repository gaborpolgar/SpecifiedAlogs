from __future__ import unicode_literals
import random as rd
import timeit
import matplotlib.pyplot as plt

# Alprogramok, linearisKereses, feltolt, futasIdok

def linear_search(v, T):
    for i in range(0, len(v)):
        if v[i] == T:
            return i
    return -1

def feltolt(v, n, n_max):
    for i in range(0, n):
        v.append(rd.randint(1, n_max))

    return v

def futasIdok(futasSzam):
    nagySorozat.append(0)

    for i in range(0, futasSzam):

        egyFutas = []

        keresettElem = rd.randint(1, maxErtek)

        #nagySorozat[len(nagySorozat) - 1] = keresettElem

        start = timeit.default_timer()

        eredmeny = linear_search(nagySorozat, keresettElem)

        stop = timeit.default_timer()

        # Hat értéket tárolunk:

        # [futtatás sorszáma, elemek száma, maximális érték, eredmény(index), futásidő, eredmény (0,1)]

        egyFutas.append(i + 1)

        egyFutas.append(elemekSzama)

        egyFutas.append(maxErtek)

        egyFutas.append(eredmeny)

        egyFutas.append(stop - start)

        if eredmeny == -1:

            egyFutas.append(0)

        else:

            egyFutas.append(1)

        futasI.append(egyFutas)

    return futasI


# -    Egyszerű vizsgálat     -

# A sorozatot feltöltjük véletlen számokkal, és mérünk 5 futásidőt.

# A következő példában az elemeKszama 10_000_000, a maxErtek 1_000_000.


futasI = []

nagySorozat = []

elemekSzama = 10_000_000

maxErtek = 1_000_000

futtatasokSzama = 100

# A vektor feltöltése

feltolt(nagySorozat, elemekSzama, maxErtek)

nagySorozat.sort()
print(nagySorozat)


# Egyszerű vizsgálat

print("Egyszerű vizsgálat - Lineáris keresés")

print("Elemek száma: " + str(elemekSzama))

print("Maximális érték: " + str(maxErtek))

print("Futtatások száma: " + str(futtatasokSzama))

futasIdok(futtatasokSzama)

print("Eredmények:")

print(futasI)

futasIdokOsszegeHaTalalat = 0

futasIdokOsszegeHaNincsTalalat = 0

for i in range(0, futtatasokSzama):

    if futasI[i][5] == 1:

        futasIdokOsszegeHaTalalat += futasI[i][4]

    else:

        futasIdokOsszegeHaNincsTalalat += futasI[i][4]

print("A futásidők összege: " + str(futasIdokOsszegeHaTalalat) + " és átlaga: " + str(
    futasIdokOsszegeHaTalalat / futtatasokSzama) + " (ha volt találat) ")

# Ezekben a kereső biztos, hogy megvizsgálta az egész sorozatot!

print("A futásidők összege: " + str(futasIdokOsszegeHaNincsTalalat) + " és átlaga: " + str(
    futasIdokOsszegeHaNincsTalalat / futtatasokSzama) + " (ha nem volt találat) ")

# ------------------Grafikon készítése-------------------------------------


x = []

y_sec = []

y_msec = []

# Az x és az y tengelyek feltöltése

for i in range(0, len(futasI)):
    x.append(futasI[i][0])

    y_sec.append(futasI[i][4])

    y_msec.append(futasI[i][4] * 1000)

fig, axs = plt.subplots(1, 2)

fig.suptitle('Lineáris keresés vizsgálata')

axs[0].set_title('Futásidők(s)')

axs[0].scatter(x, y_sec, marker='o', color='red')

axs[1].set_title('Futásidők(ms)')

axs[1].scatter(x, y_msec, marker='o', color='green')

axs[0].set(xlabel='Futás', ylabel='s')

axs[1].set(xlabel='Futás', ylabel='ms')

plt.show()
