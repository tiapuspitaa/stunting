import subprocess
import sys

# Fungsi untuk memastikan library terinstal melalui requirements.txt
def install_requirements():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    except subprocess.CalledProcessError as e:
        print(f"Error installing requirements: {e}")
        sys.exit(1)

# Pastikan semua library terinstal sebelum diimpor
install_requirements()

# Impor library setelah instalasi
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Fungsi untuk membaca dan memproses data
@st.cache_data
def load_data():
    # Ganti path ini dengan file dataset Anda
    file_path = "stunting2.csv"  # Sesuaikan dengan file Anda
    data = pd.read_csv(file_path)
    return data

# Judul aplikasi
st.title("Analisis Data Stunting")

# Load data
data = load_data()

# Menampilkan tabel data
st.subheader("Dataset")
st.write(data)

# Analisis deskriptif
st.subheader("Analisis Deskriptif")
st.write(data.describe())

# Visualisasi Matplotlib - Distribusi Gender
st.subheader("Distribusi Gender")
fig, ax = plt.subplots()
data["Gender"].value_counts().plot(kind='bar', ax=ax, color=['blue', 'orange'])
ax.set_title("Distribusi Gender")
ax.set_xlabel("Gender")
ax.set_ylabel("Jumlah")
st.pyplot(fig)

# Visualisasi Matplotlib - Distribusi Stunting
st.subheader("Distribusi Stunting")
fig, ax = plt.subplots()
data["Stunting"].value_counts().plot(kind='bar', ax=ax, color=['green', 'red'])
ax.set_title("Distribusi Stunting")
ax.set_xlabel("Stunting")
ax.set_ylabel("Jumlah")
st.pyplot(fig)

# Visualisasi Seaborn - Heatmap Korelasi
st.subheader("Korelasi Antar Variabel")
fig, ax = plt.subplots()
numeric_data = data.select_dtypes(include=["number"])
sns.heatmap(numeric_data.corr(), annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
ax.set_title("Korelasi Antar Kolom")
st.pyplot(fig)

# Filter Data Berdasarkan Umur
st.subheader("Filter Data Berdasarkan Umur")
filter_value = st.slider("Pilih Umur Minimum:", int(data["Age"].min()), int(data["Age"].max()))
filtered_data = data[data["Age"] >= filter_value]
st.write(filtered_data)

# Chart Streamlit - Berat Badan
st.subheader("Distribusi Berat Badan")
st.bar_chart(data["Body Weight"])
