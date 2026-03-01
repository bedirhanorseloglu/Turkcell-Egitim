# Numpy'deki tek boyutlu dizinin özelleştirilmiş ve geliştirilmiş hali.
import pandas as pd
import numpy as np
from numpy import random
seri1 = pd.Series([88,65,12,57,91])     # değerler indisleriyle beraber tutuluyor.
print(seri1)    

print("============")

seri1 = pd.Series([88,65,12,57,91])
print(type(seri1))

print("============")

seri1 = pd.Series([88,65,12,57,91])
print(seri1.axes)       # indis bilgilerine ulaşabiliyoruz.

print("============")

seri1 = pd.Series([88,65,12,57,91])
print(seri1.dtype)      # elemanların tipine ulaştık.

print("============")

seri1 = pd.Series([88,65,12,57,91])
print(seri1.size)   # serinin boyutuna ulaştık.

print("============")

seri1 = pd.Series([88,65,12,57,91])
print(seri1.values)     # serinin değerlerine ulaştık.

print("============")

seri1 = pd.Series([88,65,12,57,91])
print(seri1.head(3))    # baştan ilk x elemanlara ulaştık.

print("============")

seri1 = pd.Series([88,65,12,57,91])
print(seri1.tail(2))    # sondan ilk x elemana ulaştık.

print("============")

# İndex İsimlendirme
seri1 = pd.Series([88,65,12,57,91] , index=[99,98,97,96,95])
print(seri1)

print("============")

seri1 = pd.Series([88,65,12,57,91] , index=["a","b","c","d","e"])
print(seri1)

print("============")

seri1 = pd.Series([88,65,12,57,91] , index=["a","b","c","d","e"])
print("'a' indexindeki eleman:" , seri1["a"])   # index ile seriye erişim
print("'a' indexinden 'd' indexine kadarki elemanlar:\n" , seri1["a" : "d"])

print("============")

# Dictionary (Sözlük) tipinde seri oluşturma
seri2 = pd.Series({"reg" : 10 , "log" : 11 , "cart" : 12})
print(seri2)

print("============")

sozluk1 = {
    "reg" : 10 , 
    "log" : 11 , 
    "cart" : 12
}

seri2 = pd.Series(sozluk1)
print(seri2)

print("============")

# İki seriyi birleştirerek yeni seri oluşturduk.
toplam1 = pd.concat([seri1 , seri2])
print(toplam1)

print("============")

# np.array'den seri oluşturduk.
a = np.array([12,65,18,94,84])
seri3 = pd.Series(a)
print(seri3)

print("============")

seri4 = pd.Series([121,200,15,99] , index= ["reg" , "log" , "cart" , "ref"])
print("Seri:\n " , seri4)
print("Serinin indexleri: " , seri4.index)
print("Serinin ayrı ayrı key-value değerleri (itemleri): " , list(seri4.items()))

print("============")

# ELeman Sorgulama
print("reg" in seri4)
print("a" in seri4)

print("============")

# Eleman Değiştirme
seri4 = pd.Series([121,200,15,99] , index= ["reg" , "log" , "cart" , "ref"])
seri4["reg"] = 777
print(seri4)

print("============")

print(seri4["reg":"cart"])

print("============")

# DataFrame Oluşturma
liste1 = [45,32,64,91,73]
dataFrame1 = pd.DataFrame(liste1 , columns=["değişkenİsmi"])
print(dataFrame1)

print("============")

m = np.arange(1,10).reshape((3,3))
dataFrameM = pd.DataFrame(m , columns=["var1" , "var2" , "var3"])
print(dataFrameM)

print("============")

# Sütun isimlerini değiştirme
m = np.arange(1,10).reshape((3,3))
dataFrameM = pd.DataFrame(m , columns=["var1" , "var2" , "var3"])
print("Sütün isimleri: " , dataFrameM.columns)

dataFrameM.columns = ("deg1" , "deg2" , "deg3")
print("Değiştirdiğim sütun isimleri ve tablosu: " , dataFrameM.columns)
print("\n")
print(dataFrameM)

print("============")

print("Tipi: " , type(dataFrameM))
print("İndex bilgileri: " , dataFrameM.axes)
print("Boyut bilgisi: " , dataFrameM.shape)
print("Boyutu:" , dataFrameM.size)
print("Değerleri:\n " , dataFrameM.values)
print("Değerlerinin tipi: " , type(dataFrameM.values))

print("============")

dizi1 = np.array([51,66,12,3621])
df2 = pd.DataFrame(dizi1 , columns=[0])
print(df2)

print("============")

# Eleman İşlemleri
s1 = np.random.randint(10 , size=5)
s2 = np.random.randint(10 , size=5)
s3 = np.random.randint(10 , size=5)

dict1 = {
    "var1" : s1,
    "var2" : s2,
    "var3" : s3,
}

df3 = pd.DataFrame(dict1)
print(df3)
df3.index = ["satır1" , "satır2" , "satır3" , "satır4" , "satır5"]
print(df3)

print("============")

print(df3["satır2":"satır4"])

print("============")

# Silme
df3.drop("satır1" , axis=0)     # drop metoduyla bu şekilde sildiğinde asıl dataframe'den silmiş olmuyorsun. O satır hala dataframe'de | axis = 0 -> x ekseni  
print(df3)

print("============")

print(df3)
df3.drop("satır1" , axis=0 , inplace=True)  # drop metoduna "inplace" değerini true olarak girersek kalıcı olarak silmiş oluruz.
print(df3)

print("============")

l = ["satır2" , "satır3"]   
df3.drop(l , axis=0 , inplace=True)    # Çoklu satır sildik.
print(df3)

print("============")

# Çoklu sütun sorgulama
l2 = ["var1" , "var2" , "var5"]
for x in l2:
    print(x in df3)

print("============")

# Eldeki sütunları kullanarak yeni sütun oluşturduk.
df3["var4"]= df3["var1"] * df3["var2"]  # var4 sütunu oluşturduk ve bunun değerlerine var1/var2 'nin sonuçlarını atadık
print(df3)

print("============")

# Sütun sildik. Tek fark y ekseninde silme yaptığımız için axis = 1 yaptık.
df3.drop("var4" , axis=1 )
print(df3)

print("============")

# Çoklu sütun sildik.
l3 = ["var3" , "var4"]
df3.drop(l3 , axis=1 , inplace=True)
print(df3)

print("============")

# EN SIK KARŞILAŞABİLCEĞİMİZ HATALARI İNCELEDİK (Gözlem ve Değişken Seçimi)(loc ve iloc)
# loc -> tanımlandığı şekliyle indeksleme-seçme yapmak için kullanılır. ([0,3] -> 0,1,2,3 indislerini yazdırır.) (spesik bir değişken ismi getirteceksek "loc" kullanmalıyız.)
# iloc -> alışık olduğumuz indeksleme mantığıyla seçim yapar. ([0,3] -> 0,1,2 indislerini yazdırır.)
m = np.random.randint(1,30 , size=(10,3))
df4 = pd.DataFrame(m , columns=["var1" , "var2" , "var3"])
print(df4)

print("============")

print(df4.loc[0:3])  # -> 3 dahil

print("============")

print(df4.iloc[0:3])    # -> 3 dahil değil

print("============")

print("0.satır 0. sütundaki eleman: " , df4.iloc[0,0])

print("============")

print("3 satır 2 sütun getirme:\n" , df4.iloc[:3 , :2])   # Virgülden önce: almak istediğin satırların aralığı ; Virgülden sonra: almak istedğin sütunların aralığı

print("============")

print("4 satır ve var3 sütununu getirme:\n" , df4.loc[0:3 , "var3"])    # spesik bir değişken ismi getirteceksek "loc" kullanmalıyız. burada iloc kullansaydık hata alırdık. Hata almamak için:

print("============")

print("Spesik bir değişken ismi getirteceksek ve iloc kullanmak istiyorsak:\n " , df4.iloc[0:3]["var3"])

print("============")

# Koşullu Eleman İşlemleri
m = np.random.randint(1,30 , size=(10,3))
df5 = pd.DataFrame(m , columns=["var1" , "var2" , "var3"])
print(df5)
print(df5.var1 > 15)

print("============")

print([(df5.var1 > 15) & (df5.var3 < 5)])

print("============")

print(df5.loc [(df5.var1 > 15) , ["var1" , "var2"]])    # spesik bir değişken ismi getirteceksek "loc" kullanmalıyız. !!!!!!!!!!!!!!
#  print(df5.loc [(df5.var1 > 15) , ["var1" , "var2"]])  =  print(df5[(df5.var1 > 15)][["var1" , "var2"]])

print("============")

# Birleştirme (Join) İşlemi
m = np.random.randint(1,30 , size=(5,3))
df6 = pd.DataFrame(m , columns=["var1" , "var2" , "var3"])
print(df6)

df6_1 = df6 + 99

print(pd.concat([df6 , df6_1])) # Çıktısında indexler 0 1 2 3 4 ; 0 1 2 3 4 diye gidiyor bu hatayı gidermek için pd.concat'ın üstüne geldiğimizde "ignore_index" değerinin varsayılan olarak false aldığını görüyoru.

print("============")

print(pd.concat([df6 , df6_1] , ignore_index=True))

print("============")

df6_1.columns = ["var1" , "var2" , "deg"]

print(pd.concat([df6 , df6_1] , join="inner"))  # Birleştirmek istediğim df'lerin sütun isimleri birbirinden farklıysa birleştirirken hata verecektir. Bu yöntemde iki df'in kesişimlerini birleştirdik.

print("============")

# İleri Birleştirme İşlemleri 
# a) Birebir Birleştirme
df7 = pd.DataFrame(
    {
        "calisanlar" : ["Ali" , "Veli" , "Ayse" , "Fatma"],
        "grup" : ["Muhasebe" , "Muhendislik" , "İK" , "Tıp"]
    }
)

df8 = pd.DataFrame(
    {
        "calisanlar" : ["Ali" , "Veli" , "Ayse" , "Fatma"],
        "ilkGiris" : [2010 , 2009 , 2014 , 2019]
    }
)

print(pd.merge(df7 , df8 , on="calisanlar"))  # Görüldüğü gibi "calisanlar" ortak olduğundan "merge" metoduyla birebir bir birleştirme yaptık.
# on="calisanlar" diye belirterek calisanlara göre birleştirme yaptık. Yapmasaydık da tek ortak noktası orası olduğu için yine aynı şey olacaktı. 
 
print("============")

# b) Çoktan Teke Birleştirme (Üstteki birleştirmeyi tek bir değişkene toplayıp bir birleştirme daha ekledik)
df9 = pd.merge(df7 , df8 , on="calisanlar")
df10 = pd.DataFrame(
    {
        "grup" : ["Muhasebe" , "Muhendislik" , "İK" , "Tıp"],
        "mudur" : ["Caner" , "Mustafa" , "Berkcan" , "Veysel"]
    }
)

print(pd.merge(df9 , df10))   #  on="grup" a göre birleştirdi çünkü ortak değer o 

print("============")

# c) Çoktan Çoka Birleştirme
df12 = pd.DataFrame(
    {
        "grup" : ["Muhasebe" , "Muhendislik" , "İK" , "Tıp"],
        "yetenekler" : ["Excel" , "Matematik" , "Beden Dili" , "Biyoloji"]
    }
)
print(pd.merge(df7 , df12))

print("============")

# Toplulaştırma !!!!!!!
"""
count()   first()   last() mean()    median()  
min()     max()     std ()    var()   sum()
"""
import seaborn as sns   # bu kütüphane içinde hazır yüklü datasetler var.
df = sns.load_dataset("planets")
print(df.head())

print("Mass verisinin ortalaması:" , df["mass"].mean())
print("Mass verisinin min değeri:" , df["mass"].min())
print("Mass verisinin max değeri:" , df["mass"].max())
print("Mass verisinin standart sapma değeri:" , df["mass"].std())

print("============")

print(df.describe())    # -> df dataframe'in count, mean, std, min, max değerlerini tek seferde görebiliyoruz.

print("============")

print(df.describe().T)  # Üsttekinin Transpozesini aldık.

print("============")

print(df.dropna().describe().T)   # dropna() yöntemi, eksik değerlere sahip olan satırları veya sütunları kaldırarak veri temizliği yapmanızı sağlar. Bunu yaptıktan sonra değerleri göster dedik burada.

print("============")

# Gruplama İşlemleri !!!!
# Gruplama işlemlerinden sonra genel olarak toplama işlemleri gelir(kullanılır).
df = pd.DataFrame(
    {
        "gruplar" : ["A","B","C","A","B","C"],
        "veri" : [10,11,52,23,43,55]
    }
    )

print(df.groupby("gruplar"))    # "groupby" metodu ile içine yazdığımız key'leri grupladık.

print("============")

print("A,B,C'nin ortalamaları:\n" , df.groupby("gruplar").mean())
print("A,B,C'nin toplamları:\n" , df.groupby("gruplar").sum())

print("============")

df = sns.load_dataset("planets")
print(df.head())
print(df.groupby("method")["orbital_period"].mean())

print("============")

print(df.groupby("method")["mass"].mean())

print("============")

print(df.groupby("method")["distance"].describe())

print("============")

# İleri Toplulaştırma İşlemleri (aggregate , filter , transform , apply)
# a) Aggregate
df = pd.DataFrame(
    {
        "gruplar" : ["A","B","C","A","B","C"],
        "değişken1" : [10,23,33,22,11,99],
        "değişken2" : [100,253,333,262,111,969]
    }
)

print(df.groupby("gruplar").mean())

print("============")

print(df.groupby("gruplar").aggregate(["min" , np.median , np.std]))   # özellikle istediğimiz özellikleri görmek için yaptık.
# pandas'ın içinde yer alan fonksiyonları kullanmak istersek tırnak içi, tırnak olmadan fark etmez. Ama pandas dışından bir özelliği istiyorsak tırnak kullanmadan yazarız.

print("============")

print(df.groupby("gruplar").aggregate({"değişken1":"min" , "değişken2":"max"}))    # değişken1'den bir özellik, değişken2'den başka bir özellik görüntülemek istedik.

print("============")

# b) Filter
df = pd.DataFrame(
    {
        "gruplar" : ["A","B","C","A","B","C"],
        "değişken1" : [10,23,33,22,11,99],
        "değişken2" : [100,253,333,262,111,969]
    }
)

def filtreFonksiyonu(x):
    return x["değişken1"].std() > 9

print(df.groupby("gruplar").filter(filtreFonksiyonu))


# c) Transform
df = pd.DataFrame(
    {
        "gruplar" : ["A","B","C","A","B","C"],
        "değişken1" : [10,23,33,22,11,99],
        "değişken2" : [100,253,333,262,111,969]
    }
)

# 1. Yol
df_a = df.iloc[: , 1:3]    # "gruplar değişkenini kullanmayacağım için onu çıkarttım."
print(df_a.transform(lambda x : (x-x.mean()) / x.std()))   #  transform() metodu, DataFrame veya Series üzerinde gruplama ve dönüşüm işlemleri yapmak için kullanılır.
                                                           # x'değişkenler yani gezilecek sütunlar.
print("============")

# 2. yol
df['dönüşüm_değişken1'] = df.groupby('gruplar')['değişken1'].transform(lambda x: (x - x.mean()) / x.std())
df['dönüşüm_değişken2'] = df.groupby('gruplar')['değişken2'].transform(lambda x: (x - x.mean()) / x.std())
# dönüşüm_değişken1 ve dönüşüm_değişken2 adıdna 2 tane yeni sütün oluşturduk ve transform işlemlerini yaprak dataframe'e ekledik.

print(df)

print("============")

# d) Apply
df = pd.DataFrame(
    {
        "değişken1" : [10,23,33,22,11,99],
        "değişken2" : [100,253,333,262,111,969]
    }
)

print(df.apply(np.sum))
print(df.apply(np.mean))

print("============")

df = pd.DataFrame(
    {
        "gruplar" : ["A","B","C","A","B","C"],
        "değişken1" : [10,23,33,22,11,99],
        "değişken2" : [100,253,333,262,111,969]
    }
)

print(df.groupby("gruplar").apply(np.sum))
print(df.groupby("gruplar").apply(np.mean))

print("============")

# Pivot Tablolar (groubby'ın çok boyutlu versiyonu olarak düşün)
import seaborn as sns
titanic = sns.load_dataset("titanic")
print(titanic.head())

print("============")

print(titanic.groupby("sex")["survived"].mean())    # sex -> neye göre gruplayayım , survived -> neyi gruplayayım

print("============")

print(titanic.groupby("sex")[["survived"]].mean())  # survived'ı iki köşeli paranteze alarak dataframe oluşturduk.

print("============")

print(titanic.groupby(["sex" , "class"])["survived"].aggregate("mean").unstack())  # cinsiyetlerin uçuş sınıfına göre hayatta kalanların ortalaması , unstack okunmayı kolaylaştırıyor.

print("============")

# pivot_table İle Pivot Tablo Oluşturma (Kolay Yol)
print(titanic.pivot_table("survived" , index="sex" , columns="class"))

print("============")

# Dış Kaynaklı Veri Okuma
# a) Csv Okuma
print(pd.read_csv("pandas dışarıdan veri alma\ornekcsv.csv" , sep=";"))

print("============")

# b) Txt Okuma
print(pd.read_csv("pandas dışarıdan veri alma\ornekcsv.csv" , sep=";"))

print("============")

# c) Excel Okuma
print(pd.read_excel("pandas dışarıdan veri alma\ornekx.xlsx"))

print("============")

df = pd.read_excel("pandas dışarıdan veri alma\ornekx.xlsx") # üsttekinin sütun isimlerini değişeceğim.
df.columns = ["Ankara" , "Bursa" , "Ceyhan"]
print(df)

print("============")

