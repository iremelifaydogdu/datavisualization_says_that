#Veri Görselleşirme: Matplotlib & Seaborn

#matplotlib

#Kategorik : sütun grafik. Seaborn içindeki Countplot,matplotlib içindeki Barplot.
#Sayısal değişken : histogram, boxplot. (dağılım gösterir boxplot aykırı değerleri de gösterir.)

#Kategorik değişken görselleştirme

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sympy.physics.control.control_plots import matplotlib

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df=sns.load_dataset("titanic")
df.head()

df["sex"].value_counts().plot(kind="bar")
plt.show(block=True)

pip install matplotlib

#Sayısal Değişken Görselleştirme
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df=sns.load_dataset("titanic")
df.head()
plt.hist(df["age"])
plt.show(block=True)

plt.boxplot(df["fare"])
plt.show(block=True)


#Matplotlib Özellikleri: Katmanlı bir şekilde veri görselleştirme imkanı sunar. Bir katmanda bir görsel bir katmanda ayrı bir görsel bir katmanda title diğer katmanda eksenlerin bilgisini verme
 import numpy as np
 import pandas as pd
 import matplotlib.pyplot as plt
 pd.set_option('display.max_columns',None)
 pd.set_option('display.width', 500)
#plot: veriyi görselleştirme aracı

x=np.array([1,8])
y=np.array([0,150])
plt.plot(x,y, 'o') #ik numpy arrayini görselleştiriyorsun
plt.show(block=True)
#grafik çıkınca kapatmadan başka bir kod çalıştırınca grafiğin üzerine atar

#marker: işaretleyici özelliği

y=np.array([13,28,11,100])
#y noktalarına içi dolu daire koymak yani bir markerla işaretlemek
plt.plot(y,marker='o')
plt.show(block=True)

plt.plot(y,marker='*')
plt.show(block=True)

markers= ['o', '*', '.', ',', 'x', '+', 'P', 's', 'O', 'D', 'd', 'p', 'H', 'h'],

#Line: Çizgi oluşturmak

y = np.array([13,28,11,100])
plt.plot(y, linestyle="dotted", color='r')
plt.show(block=True)

plt.plot(y, linestyle="dashed")
plt.show(block=True)

plt.plot(y, linestyle="dashdot")
plt.show(block=True)


#Multiple Lines
x=np.array([23,18,31,10])
y=np.array([13,28,11,100])
plt.plot(x)
plt.plot(y)
plt.show(block=True)

#Labels: etiketler
x=np.array([80,85,90,95,100])
y=np.array([240,250,260,270,280])
plt.plot(x,y)
#Başlık
plt.title("Bu ana başlık")

plt.xlabel("X ekseni isimlendirmesi")
plt.ylabel("Y ekseni isimledirmesi")


plt.grid() #arka tarafa ızgara koymak
plt.show(block=True) #plt.show bir şekilde gerekli unutma


#Subplots: Birden fazla görselin gösterilmesi

#plot 1

x=np.array([80,85,90,95,100,105,110,115,120,125])
y=np.array([240,250,260,270,280,290,300,310,320,330])
plt.subplot(1,3,1)
plt.title("1")
plt.plot(x,y)




x=np.array([80,85,90,95,100,105,110,115,120,125])
y=np.array([240,250,260,270,280,290,300,310,320,330])
plt.subplot(1,3,2)
plt.title("2")
plt.plot(x,y)



x=np.array([80,85,90,95,100,105,110,115,120,125])
y=np.array([240,250,260,270,280,290,300,310,320,330])
plt.subplot(1,3,3)
plt.title("3")
plt.plot(x,y)
plt.show(block=True)

#Seaborn ile veri görselleştirme: yüksek seviye daha az çaba daha fazla iş

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
df= sns.load_dataset("tips")
df.head()

#kategorik değişken sözel türde olmasa bile sözel ifadeyi temsil eden değişenlerdi, sütun grafikle temsil ediliyordu.


df["sex"].value_counts()
sns.countplot(x=df["sex"],data=df)
plt.show()


#Sayısal Değişken Görselleştirme : kutugrafik ya da histogram


sns.boxplot(x=df["total_bill"])
plt.show()

df["total_bill"].hist()
plt.show()


#1 value_count, countplot.  2 histogram.  3 boxplot.


