
def tentukan_olahraga(x):
    if x > 750 :
        print("Jumlah kalori: "+str(x)) 
        print("Jenis kalori: Lari")
        print("Waktu Olahraga: "+str((x/20)*2))
    elif x > 500 :
        print("Jumlah kalori: "+str(x)) 
        print("Jenis kalori: Badminton")
        print("Waktu Olahraga: "+str((x/20)*2))
    elif x < 500 :
        print("Jumlah kalori: "+str(x)) 
        print("Jenis kalori: Renang")
        print("Waktu Olahraga: "+str((x/20)*2))
    else :
        print ("Inputan salah")

print (tentukan_olahraga(751))
