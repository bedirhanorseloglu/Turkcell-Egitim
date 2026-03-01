"""Dizi oluşturma"""
import numpy as np
dizi1 = np.array([1,2,3,4,5])
print(dizi1)

print("============")

dizi2 = np.array((1,2,3,4))     # tuple türünde bir dizi oluşturduk.
print(dizi2)

print("============")

"""Dizilerdeki Boyutlar"""
# Dizilerdeki bir boyut, bir dizi derinliği düzeyidir (iç içe geçmiş diziler).İç içe dizi: Öğeleri dizi olan dizilerdir.

dizi3 = np.array(42) # 0 boyutlu bir dizi
print(dizi3)

print("============")

dizi4 = np.array([1,2,3,4,5]) # 1 boyutlu bir dizi
print(dizi4)

print("============")

dizi5 = np.array([[1,2,3,4] , [5,6,7,8]])  # 2 boyutlu bir dizi. (Öğeleri olarak 1 boyutlu dizilere sahip bir diziye 2 boyutlu dizi denir.)
print(dizi5)

print("============")

dizi6 = np.array([[[1,2,3],[4,5,6]] , [[7,8,9] , [10,11,12]]]) # 3 boyutlu dizi. (Öğeleri olarak 2 boyutlu dizilere(matrisler) sahip bir diziye 3 boyutlu dizi denir.)
# Mor-> matris ; Mavi -> satırlar ; Sarı-> sütunlar
print(dizi6)

print("============")

# NumPy Arrays, dizinin kaç boyuta sahip olduğunu bize söyleyen bir tamsayı döndüren "ndim" özniteliğini sağlar.
a = np.array(42)
b = np.array([1,2,3])
c = np.array([[1,2,3]])
d = np.array([[[1,2,3] , [4,5,6]] , [[7,8,9] , [10,11,12]]])

print("A dizisinin boyutu: " , a.ndim)
print("B dizisinin boyutu: " , b.ndim)
print("C dizisinin boyutu: " , c.ndim)
print("D dizisinin boyutu: " , d.ndim)

print("============")

# Bir dizinin herhangi bir sayıda boyutu olabilir. Dizi oluşturulduğunda, ndmin argümanını kullanarak boyutların sayısını tanımlayabilirsiniz.
dizi6 = np.array([1,2,3,4,5] , ndmin=5)
print(dizi6)

print("============")

"""Dizi Öğelerine Erişim"""
dizi7 = np.array([54,85,45,62,94,56])   # 1 boyutlu dizide erişim.
print("Dizinin ilk elemanı: " , dizi7[0])
print("Dizinin ikinci elemanı: " , dizi7[1])
print("Dizinin üçüncü ve dördüncü elemanının toplamı: " , dizi7[2] + dizi7[3])

print("============")

dizi8 = np.array([[51,63,34,75] , [87,64,97,37]])   # 2 boyutlu dizide erişim.
print("1. sıradaki 2. eleman: " , dizi8[0,1])
print("2. sıradaki 4. eleman: " , dizi8[1,3])

print("============")

dizi9 = np.array([[[65,47,87,64] , [54,65,45,65]] , [[87,45,12,35] , [15,65,87,98]]])
print("1. satırın 2. dizisinin üçüncü elemanı: " , dizi9[0,1,2]) # ilk rakam kaçıncı mavi , ikinci mavinin kaçıncı sarısı , üçüncü rakam sarının kaçıncı elemanı.

print("============")

"""NumPy Dizi Dilimleme"""
dizi10 = np.array([54,57,98,65,12,34,91,4,15])  # 1 boyutlu dizide dilimleme.
print(dizi10[0:4])
print(dizi10[2:])
print(dizi10[:4])
print(dizi10[1:5:2])
print(dizi10[::2])

print("============")

dizi11 = np.array([[24,45,65,12,61,23] , [48,1,64,81,74,94]])
print(dizi11[1 , 1:3])  # 1. maviyi , 1'den 2'ye kadar dilimledik.   Virgülden öncesi maviyi sonrası elemanları temsil ediyor.
print(dizi11[0 , 1:3])  # 0. maviyi , 1'den 2'ye kadar dilimledik.
print(dizi11[0:2 , 2])  # 0. maviden 1. maviye kadar , 2. indistekini aldık.
print(dizi11[0:2 , 1:4])    # 0. maviden 1. maviye kadar , 1. elemandan 3.ye kadar dilimledik.

print("============")

"""NumPy Dizi Kopyası(copy) ve Görünüm(view)"""
dizi12 = np.array([4,48,65,17,35,94])
x = dizi12.copy()   # Kopya -> orijinal != kopya , kendi verisi yoktur.
dizi12[0] = 61

print("Orijinali: " , dizi12)
print("Kopyası: " , x)

print("============")

dizi12 = np.array([4,48,65,17,35,94])
y = dizi12.view()   # Görüntü -> orijinal = görüntü , kendi verisi vardır.
dizi12[0] = 61

print("Orijinali: " , dizi12)
print("Görüntüsü: " , y)

print("============")

# Bir dizinin kendi verilerine sahip olup olmadığını kontrol etmek için "base" özniteliğinin değerini yazdırın
dizi12 = np.array([4,48,65,17,35,94])
x = dizi12.copy()
y = dizi12.view()

print("Kendi verisi: " , x.base)
print("Kendi verisi: " , y.base)

print("============")

"""NumPy Dizi Şekli"""
# Bir dizinin şekli, her boyuttaki öğelerin sayısıdır (Kaça kaçlık matris?).
dizi13 = np.array([[1,2,3] , [3,4,5] , [6,7,8]])
print(dizi13.shape)

print("============")

dizi14 = np.array([[[1,2,3] , [4,5,6]] , [[7,8,9] , [10,11,12]]])
print(dizi14.shape)

print("============")

"""NumPy Dizisini Yeniden Şekillendirme"""
# Yeniden şekillendirme, bir dizinin şeklini değiştirmek anlamına gelir. Bir dizinin şekli, her boyuttaki öğelerin sayısıdır. Yeniden şekillendirerek boyutları ekleyebilir veya kaldırabilir veya her boyuttaki öğe sayısını değiştirebiliriz.
# 1 boyutu 2 boyutluya dönüştürme
dizi15 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
yeniDizi15 = dizi15.reshape(4,3)     # 4 satır 3 sütun yaptı
yeniDizi15_2 = dizi15.reshape(6,2)   # 6 satır 2 sütun yaptı
print(yeniDizi15)
print(yeniDizi15_2)

print("============")

# 1 boyutu 3 boyutluya dönüştürme
dizi15 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
yeniDizi15_3 = dizi15.reshape(3,2,2)    # 3 tane 2 satır 2 sütunluk yaptı.
yeniDizi15_4 = dizi15.reshape(2,3,2)    # 2 tane 3 satır 2 sütunluk yaptı
print(yeniDizi15_3)

print("============")

# Herhangi Bir Şekilde Yeniden Şekillendirebilir miyiz?
# Her iki şekilde de yeniden şekillendirme için gerekli unsurlar eşit olduğu sürece evet.
# 8 elemanlı bir 1B diziyi 2 sıra 2B dizide 4 elemana yeniden şekillendirebiliriz, ancak 3x3 = 9 eleman gerektireceği için onu 3 elemanlı 3 satır 2B diziye yeniden şekillendiremeyiz.

print("============")

# Dizileri düzleştirme -> reshape(-1)
# Düzleştirme dizisi, çok boyutlu bir diziyi 1 boyutlu bir diziye dönüştürmek anlamına gelir.

dizi16 = np.array([[1,2,3] , [4,5,6]])
yeniDizi16 = dizi16.reshape(-1)
print(yeniDizi16)

print("============")
"""NumPy Dizisi Iterators (Yineleme)"""
# Yineleme, öğelerden birer birer geçmek anlamına gelir. Numpy'de çok boyutlu dizilerle uğraşırken, bunu python'un temel for döngüsünü kullanarak yapabiliriz. 1 boyutlu bir dizide yinelenirsek, her öğeden birer birer geçecektir.
# 1 boyutluda yineleme
dizi17 = np.array([40,23,65,17,91])
for x in dizi17:
    print(x)

print("============")

# 2 boyutluda yineleme
dizi18 = np.array([[15,14,65,12] , [18,32,69,47]])
for x in dizi18:
    print(x)

print("============")

dizi18 = np.array([[15,14,65,12] , [18,32,69,47]])
for x in dizi18:
    for y in x:
        print(y)

print("============")

# 3 boyutlu dizide yineleme
dizi19 = np.array([[[14,16] , [98,61]] , [[1,97] , [64,53]]])
for x in dizi19:
    print(x)

print("============")

# elemanlarını tek tek yinelemnek istersek
for x in dizi19:
    for y in x:
        for z in y:
            print(z)

print("============")

# Bu tarz çok boyutlu bir dizinin elemanlarını tek tek yazdırmak için iç içe bir sürü for yerine kolay olarak "nditer" özniteliğini kullanıyoruz.
for x in np.nditer(dizi19):
    print(x)

print("============")

# Yineleme sırasında öğelerin veri tipini değiştirmek için "op_dtypes" argümanını kullanabilir ve beklenen veri tipini iletebiliriz.
# NumPy, öğenin yerinde veri türünü değiştirmez (öğenin dizide olduğu yerde), bu nedenle bu eylemi gerçekleştirmek için başka bir alana ihtiyaç duyar. 
# Bu fazladan alana tampon denir ve bunu nditer() içinde etkinleştirmek için "flags=['buffered']"

dizi20 = np.array([50,16,34])
for x in np.nditer(dizi20 , flags=["buffered"] , op_dtypes=["S"]):
    print(x)

print("============")

dizi21 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(dizi21[: , ::2]):    # virgülden önceki: mavilerin hepsini al, sonraki: 2'şer adımlayarak git
    print(x)

print("============")

# Bazen yineleme yaparken öğenin karşılık gelen indise ihtiyaç duyarız, bu kullanım durumları için "ndenumerate()" yöntemi kullanılabilir.
dizi22 = np.array([51,23,63])
for index , eleman in np.ndenumerate(dizi22):
    print(index , eleman)

print("============")

dizi22_1 = np.array([[12,36,47] , [87,94,14]])
for index , eleman in np.ndenumerate(dizi22_1):
    print(index , eleman)

print("============")

dizi22_2 = np.array([[[84,65,15] , [14,56,17]] , [[12,64,74] , [41,69,94]]])
for index , eleman in np.ndenumerate(dizi22_2):
    print(index , eleman)

print("============")

"""NumPy Join Array (Birleştirme Dizisi)"""
# Birleştirme, iki veya daha fazla dizinin içeriğini tek bir diziye koymak anlamına gelir.
# SQL'de tabloları bir anahtara göre birleştiririz, oysa NumPy'de dizileri eksenlere göre birleştiririz.
# Birleştirmek istediğimiz bir dizi dizisini eksenle birlikte "concatenate()" -> birleştirmek işlevine geçiriyoruz. Eksen açıkça geçilmezse 0 olarak alınır.

# 1 boyutlu dizide birleştirme
dizi23 = np.array([1,2,3])
dizi23_1 = np.array([4,5,6])

toplamDizi = np.concatenate((dizi23 , dizi23_1))
print("Birleşmiş hali:" , toplamDizi)

print("============")

# 2 boyutlu dizide birleştirme
dizi24 = np.array([[1,2,3] , [3,4,5]])
dizi24_1 = np.array([[4,5,6] , [7,8,9]])

toplamDizi2 = np.concatenate((dizi24 , dizi24_1))
print(toplamDizi2)

print("============")

# Stack, concatenate ile aynıdır, tek fark, stack'in yeni bir eksen boyunca yapılmasıdır.
# İki tane 1 boyutlu diziyi ikinci eksen boyunca birleştirebiliriz, bu da onları üst üste koymamıza neden olur, yani stack.
# Birleştirmek istediğimiz bir dizi dizisini eksenle birlikte stack() yöntemine geçiriyoruz. Eksen açıkça geçilmezse 0 olarak alınır.
dizi25 = np.array([1,2,3])
dizi25_1 = np.array([4,5,6])    
toplamDizi3 = np.stack((dizi25 , dizi25_1) , axis=0)    # Direkt birleştirdi sütun sütun -> axis = 0 ->  x ekseninde birleştirdi.
toplamDizi3_1 = np.stack((dizi25 , dizi25_1) , axis=1)    # Birleştirip transpozesini aldı. -> axis = 1 -> y ekseninde birleştirdi.
print(toplamDizi3)
print(toplamDizi3_1)

print("============")

# NumPy, bir yardımcı işlev sağlar: "hstack()", satırlar boyunca istiflemek için. 
dizi26 = np.array([1,2,3])
dizi26_1 = np.array([4,5,6])
toplamDizi4 = np.hstack((dizi26 , dizi26_1))    # -> hepsini tek satırda yazdı.
print(toplamDizi4)

print("============")

# NumPy bir yardımcı işlev sağlar: "vstack()" satırlar boyunca yığınlamak için.
dizi26 = np.array([1,2,3])
dizi26_1 = np.array([4,5,6])
toplamDizi5 = np.vstack((dizi26 , dizi26_1))    # -> axis = 0
print(toplamDizi5)

print("============")

# NumPy bir yardımcı işlev sağlar: derinlikle aynı olan yükseklik boyunca istifleme yapmak için "dstack()"
dizi26 = np.array([1,2,3])
dizi26_1 = np.array([4,5,6])
toplamDizi6 = np.dstack((dizi26 , dizi26_1)) # -> axis = 1
print(toplamDizi6)

print("============")

"""NumPy Splitting Array (NumPy Bölme Dizisi)"""
# Bölme, Birleştirme işleminin tersidir.
# Birleştirme, birden çok diziyi bir dizide birleştirir ve Bölme, bir diziyi birden çok diziye böler.
# Dizileri bölmek için "array_split()" kullanıyoruz, ona bölmek istediğimiz diziyi ve bölme sayısını iletiyoruz.
dizi27 = np.array([1,2,3,4,5,6])
yeniDizi27 = np.array_split(dizi27 , 3)
print(yeniDizi27)

print("============")

# Dizi gerekenden daha az öğeye sahipse, buna göre sondan ayarlanacaktır.
yeniDizi27_1 = np.array_split(dizi27 , 4)
print(yeniDizi27_1)

print("============")

# Bir diziyi 3 diziye bölerseniz, herhangi bir dizi öğesinde olduğu gibi sonuçtan bunlara erişebilirsiniz:
yeniDizi27_2 = np.array_split(dizi27 , 3)
print(yeniDizi27_2[0])
print(yeniDizi27_2[1])
print(yeniDizi27_2[2])

print("============")

# 2 boyutlu dizide bölme
dizi28 = np.array([[1,2,3] , [4,5,6] ,  [7,8,9] , [10,11,12]])
yeniDizi28 = np.array_split(dizi28 , 2)
print(yeniDizi28)

print("============")

dizi29 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
yeniDizi29 = np.array_split(dizi29 , 3 , axis=1)
print(yeniDizi29)   # -> 1 4 7 10 13 16 bir dizi, 2 5 8 11 14 17 bir dizi, 3 6 9 12 15 18 bir dizi. (her mavinin ilk elemanları bir dizi , ikinci elemanları bir dizi ...) 

print("============")

# Alternatif bir çözüm, hstack()'in karşısında "hsplit()" kullanmaktır.
dizi29 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
yeniDizi29_1 = np.hsplit(dizi29 , 3)
print(yeniDizi29_1)

print("============")

"""NumPy Searching Arrays (NumPy Arama Dizileri)"""
# Bir diziyi belirli bir değer için arayabilir ve eşleşen dizinleri döndürebilirsiniz.
# Bir dizi aramak için "where()" yöntemini kullanın.
dizi30 = np.array([1,2,3,4,5,4,4])
nerede = np.where(dizi30 == 4)
print(nerede) # -> Bu, 4 değerinin indeks 3, 5 ve 6'da mevcut olduğu anlamına gelir.

print("============")

dizi31 = np.array([1,2,3,4,5,6,7,8])
nerede2 = np.where(dizi31 % 2 == 0)
print(nerede2)

print("============")

# Dizide ikili arama gerçekleştiren ve arama sırasını korumak için belirtilen değerin girileceği dizini döndüren "searchsorted()" adlı bir yöntem vardır.
# Searchsorted() yönteminin sıralanmış dizilerde kullanıldığı varsayılır.
dizi32 = np.array([6,7,8,9])
nerede3 = np.searchsorted(dizi32 , 7)
print(nerede3)

print("============")

# Varsayılan olarak en soldaki dizin döndürülür, ancak bunun yerine en sağdaki dizini döndürmek için side='right' verebiliriz.
dizi32 = np.array([6,7,8,9])
nerede3_1 = np.searchsorted(dizi32 , 7 , side="right")
print(nerede3_1)

print("============")

dizi33 = np.array([1,3,5,9])
nerede4 = np.searchsorted(dizi33 , [2,4,6,7,8])
print(nerede4) #?????????????????????

print("============")

"""NumPy Sorting Arrays (NumPy Sıralama Dizileri)"""
# Sıralama, öğeleri düzgün bir sıraya koymak anlamına gelir.
# Sıralı dizi, sayısal veya alfabetik, artan veya azalan gibi öğelere karşılık gelen bir düzene sahip herhangi bir dizidir.
# NumPy ndarray nesnesi, belirtilen bir diziyi sıralayacak olan "sort()" adlı bir işleve sahiptir.
dizi34 = np.array([3,2,0,1])
print(np.sort(dizi34))

print("============")

dizi35 = np.array(["banana" , "cherry" , "apple"])
print(np.sort(dizi35))

print("============")

# 2 boyutluda sıralama
dizi36 = np.array([[3,1,2] , [6,5,4]])
print(np.sort(dizi36))

print("============")

"""NumPy Filter Array (NumPy Filtre Dizisi)"""
# Varolan bir diziden bazı öğeleri alıp bunlardan yeni bir dizi oluşturmaya filtreleme denir.
# NumPy'de, bir diziyi bir boole dizin listesi kullanarak filtrelersiniz.
# Bir boole dizin listesi, dizideki elemanlara karşılık gelen bir boolean listesidir.
# Bir dizindeki değer True ise, o öğe filtre uygulanmış dizide yer alır, bu dizindeki değer False ise, o öğe filtre uygulanmış diziden çıkarılır.
dizi37 = np.array([41,42,43,44])
x = [True , False , True , False]
yeniDizi37 = dizi37[x]
print(yeniDizi37)

print("============")

# Yukarıdaki örnekte, True ve False değerlerini sabit kodladık, ancak genel kullanım, koşullara dayalı bir filtre dizisi oluşturmaktır.
# Yalnızca 42'den yüksek değerleri döndürecek bir filtre dizisi oluşturun:
dizi37 = np.array([41,42,43,44])
filtreDizi = []
for eleman in dizi37:
    if eleman > 42:
        filtreDizi.append(True)
    
    else:
        filtreDizi.append(False)

yeniDizi37_1 = dizi37[filtreDizi]
print(yeniDizi37_1)

print("============")

# Yukarıdaki örnek, NumPy'de oldukça yaygın bir görevdir ve NumPy, bunun üstesinden gelmek için güzel bir yol sağlar.
# Durumumuzdaki yinelenebilir değişken yerine doğrudan diziyi değiştirebiliriz ve tam da beklediğimiz gibi çalışacaktır.
# Yalnızca 42'den yüksek değerleri döndürecek bir filtre dizisi oluşturun:
dizi37 = np.array([41,42,43,44])
filtreDizi2 = dizi37 > 42
yeniDizi37_2 = dizi37[filtreDizi2]
print(filtreDizi2)
print(yeniDizi37_2)

print("============")

"""Random Numbers in NumPy (NumPy'de Rastgele Sayılar)"""
from numpy import random
x = random.randint(100)
print(x)

print("============")

#Rastgele modülün "rand()" yöntemi, 0 ile 1 arasında rastgele bir kayan nokta döndürür.
x = random.rand()
print(x)

print("============")

# NumPy'de dizilerle çalışıyoruz ve rastgele diziler oluşturmak için yukarıdaki örneklerden iki yöntemi kullanabilirsiniz.
# "randint()" yöntemi, bir dizinin şeklini belirtebileceğiniz bir size parametresi alır.
x = random.randint(100 , size=5)
print(x)

print("============")

# Her satır 0'dan 100'e kadar 5 rasgele tamsayı içeren 3 satırlı bir 2-B dizi oluşturun:
x = random.randint(100 , size=(3,5))
print(x)

print("============")

# 5 rasgele ondalıklı sayı içeren bir 1 boyutlu dizi oluşturun:
x = random.rand(5)
print(x)

print("============")

# Her satır 5 rasgele sayı içeren 3 satırlı bir 2 boyutlu dizi oluşturun:
x = random.rand(3,5)
print(x)

print("============")

# choice() yöntemi, bir dizi değere dayalı olarak rastgele bir değer oluşturmanıza olanak tanır.
# choice() yöntemi, bir diziyi parametre olarak alır ve değerlerden birini rasgele döndürür.
x = random.choice([3,7,6,5])
print(x)

print("============")

# Dizinin şeklini belirtmek için bir size parametresi ekleyin.
x = random.choice([1,5,9,7] , size=(3,5))
print(x)

print("============")



