import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Membuat judul aplikasi dashboard
st.title('Dashboard: Korelasi dan Visualisasi Produk')

# Membuat DataFrame dari data yang diberikan
data = {
    "product_weight_g": [225.0, 1000.0, 154.0, 371.0, 625.0, 200.0, 18350.0, 900.0,
                         400.0, 600.0, 1100.0, 7150.0, 250.0, 600.0, 200.0,
                         800.0, 400.0, 900.0, 1700.0, 500.0, 2550.0,
                         800.0, 75.0, 500.0, 1800.0, 900.0, 3600.0,
                         300.0, 740.0, 3600.0],
    "product_dimension_cm3": [2240.0, 10800.0, 2430.0, 2704.0, 4420.0, 2090.0,
                              73920.0, 12800.0, 5967.0, 2040.0, 2560.0,
                              42750.0, 2023.0, 9724.0, 2023.0, 352.0,
                              2700.0, 12000.0, 10500.0, 2560.0, 31320.0,
                              4608.0, 1911.0, 3380.0, 12000.0, 12500.0,
                              43750.0, 2520.0, 3887.0, 32798.0],
    "product_category_name": ['perfumaria', 'artes', 'esporte_lazer', 'bebes',
                              'utilidades_domesticas', 'instrumentos_musicais',
                              'cool_stuff', 'moveis_decoracao', 'eletrodomesticos',
                              'brinquedos', 'cama_mesa_banho', 'bebes',
                              'instrumentos_musicais', 'moveis_decoracao',
                              'construcao_ferramentas_seguranca', 'esporte_lazer',
                              'perfumaria', 'informatica_acessorios',
                              'moveis_decoracao', 'cama_mesa_banho',
                              'moveis_decoracao', 'cama_mesa_banho',
                              'beleza_saude', 'bebes', 'moveis_decoracao',
                              'utilidades_domesticas', 'malas_acessorios',
                              'informatica_acessorios', 'informatica_acessorios',
                              'esporte_lazer']
}

df = pd.DataFrame(data)

# ---- Grafik 1: Heatmap Korelasi ----
# Menghitung korelasi
correlation_matrix = df[['product_weight_g', 'product_dimension_cm3']].corr()

# Mengatur ukuran gambar
plt.figure(figsize=(10, 8))

# Membuat heatmap
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f",
            linewidths=.5, cbar_kws={"shrink": .8})

# Menambahkan judul pada heatmap
plt.title('Correlation Between Product Weight and Product Dimension')

# Menampilkan heatmap di Streamlit
st.subheader("Korelasi Antara Berat Produk dan Dimensi Produk")
st.pyplot(plt)

# ---- Grafik 2: Scatter Plot ----
# Mengatur ukuran gambar
plt.figure(figsize=(12, 8))

# Membuat scatter plot
sns.scatterplot(data=df, x='product_weight_g', y='product_dimension_cm3',
                hue='product_category_name', palette='Set2', s=100)

# Menambahkan judul dan label sumbu
plt.title('Visualization of Product Weight and Dimension by Category', fontsize=16)
plt.xlabel('Product Weight (grams)', fontsize=14)
plt.ylabel('Product Dimension (cm³)', fontsize=14)
plt.legend(title='Product Category', bbox_to_anchor=(1.05, 1), loc='upper left')

# Menampilkan scatter plot di Streamlit
plt.grid()
plt.tight_layout()
st.subheader("Visualisasi Berat Produk dan Dimensi Berdasarkan Kategori")
st.pyplot(plt)


