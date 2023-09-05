movieList = set(input("Masukkan 5 movie kesukaan anda yang dipisahkan dengan koma: ").split(','))
movieListTeman = set(input("Masukkan 5 movie kesukaan teman anda yang dipisahkan dengan koma: ").split(','))

movieListSama = movieList.intersection(movieListTeman)
counterSama = len(movieListSama)
persentase = ( counterSama / len(movieList) ) * 100
print(f"Kesukaan movie kalian yang sama sebesar {persentase}%")