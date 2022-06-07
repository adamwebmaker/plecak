
def knapSackBF(c,weight,val,n): #brute force rekurencyjny

    if n==0 or c == 0: #jesli nie ma juz kolejnych elementow lub nic wiecej sie nie zmiesci do plecaka
        return 0        #zwracamy 0

    if weight[n-1] > c: # jesli waga elementu jest wieksza od obecnej pojemnosci plecaka (zmniejsza sie ona wraz z rekurencja)
        return knapSackBF(c,weight,val,n-1)     #przechodzimy do kolejnego elementu

    else:                                                           #w przeciwnym wypadku
        res1 = val[n-1]+knapSackBF(c-weight[n-1],weight,val,n-1)    #dodajemy element do plecaka i szukamy dalej wedlug rekurencji maksymalnej sumy wartości kolejnych elementów
        res2 = knapSackBF(c,weight,val,n-1)                         #nie dodajemy obecnego elementu i szukamy maksymalnej sumy wartości kolejnych elementów
        return max(res1,res2)                               #wybieramy najwieksza sume i zwracamy ją w góre rekurencji


def knapSackDP(c,weight,val,n):
    tab = [[0 for x in range(c+1)] for x in range(n+1)]     #tworzymy tablice samych zer

    for i in range(n+1):
        for j in range(c+1):
            if weight[i-1] > j:         #jesli waga jest wieksza od obecnej kolumny
                tab[i][j]=tab[i-1][j]   # przepisujemy wartosc z góry
            else:
                res1 = tab[i-1][j]
                res2 = val[i-1]+tab[i-1][j-weight[i-1]]     #bierzemy wartosc obecnego elementu, oraz dodajemy ja do wartości elementu z wiersza wyżej i kolumny pomniejszonej o wage obecnego elementu
                tab[i][j]=max(res1,res2)

    return tab[n][c]


f = open("dane.txt", "r")

val = []
weight = []

c = int(f.readline())
n = int(f.readline())
for x in f:
    x = x.split()
    val.append(int(x[0]))
    weight.append(int(x[1]))

print("Brute force:")
print(knapSackBF(c,weight,val,len(val)))
print("\nDynamic programing:")
print(knapSackDP(c,weight,val,len(val)))



