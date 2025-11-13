import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('nilai_siswa.csv', sep=",")
data.info()
data.head()
data.describe()
print(data)

print("Rata-rata:", data ['Nilai'].mean())
print("Median:", data ['Nilai'].median())
print("Modus:", data ['Nilai'].mode()[0])

data.groupby('Mapel') ['Nilai'].agg(['max','min'])
rata = data.groupby('Mapel') ['Nilai'].mean()
rata.plot(kind='bar')
plt.title('Rata-Rata Nilai per Mapel')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai Rata-Rata')
plt.show()

sns.boxplot (x='Mapel', y='Nilai', data=data)
plt.title('Sebaran Nilai per Mata Pelajaran')
plt.show()

