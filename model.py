import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

# Data latih
data_latih = {
    'Ukuran_Rumah': [100, 150, 200, 120, 180, 250, 90, 160, 130, 220],
    'Jumlah_Kamar': [2, 3, 4, 2, 3, 5, 1, 3, 2, 4],
    'Lokasi': ['Jakarta', 'Bandung', 'Jakarta', 'Depok', 'Bandung', 'Jakarta', 'Bogor', 'Jakarta', 'Depok', 'Bandung'],
    'Harga': [1200000000, 1500000000, 2500000000, 1300000000, 1800000000, 3000000000, 1000000000, 2000000000, 1400000000, 2200000000]
}
df_latih = pd.DataFrame(data_latih)

# Data uji
data_uji = {
    'Ukuran_Rumah': [140, 170, 110, 200],
    'Jumlah_Kamar': [3, 3, 2, 4],
    'Lokasi': ['Jakarta', 'Bandung', 'Depok', 'Bogor']
}
df_uji = pd.DataFrame(data_uji)

# Encode kolom 'Lokasi'
le = LabelEncoder()
df_latih['Lokasi'] = le.fit_transform(df_latih['Lokasi'])
df_uji['Lokasi'] = le.transform(df_uji['Lokasi'])

# Pisahkan fitur (X) dan target (y)
X_latih = df_latih[['Ukuran_Rumah', 'Jumlah_Kamar', 'Lokasi']]
y_latih = df_latih['Harga']
X_uji = df_uji[['Ukuran_Rumah', 'Jumlah_Kamar', 'Lokasi']]

# Buat dan latih model
model = LinearRegression()
model.fit(X_latih, y_latih)

# Prediksi harga
prediksi_harga = model.predict(X_uji)
for i, harga in enumerate(prediksi_harga):
    print(f"Prediksi Harga Rumah {i+1}: Rp {int(harga):,}")