def genjil(nomorList):
    if (nomorList % 2) != 0:
        return 'Ganjil'
    else:
        return 'Genap'

ListNomor = list(map(int,
    input("\nEnter the numbers : ").strip().split()))

answer = print(str(list(map(genjil,ListNomor))))
         