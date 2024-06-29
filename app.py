import streamlit as st

menu = ["Home"]
choice = st.sidebar.selectbox("Menu", menu)

# Pilihan halaman
if choice == "Home":
    st.title('Produk Skincare Dan Kosmetik Yang Sering Dibeli Oleh Konsumen Pada Toko Indah Store')
    # Gambar header
    st.image("wardah.jpg", use_column_width=True)
    # Konten deskriptif dengan styling
    st.markdown(
        """
        <p style="text-align: justify; font-size: 18px; line-height: 1.6; color: #333;">
       Skincare adalah serangkaian praktik dan produk yang digunakan untuk merawat dan menjaga kesehatan kulit. Tujuan utama dari skincare adalah menjaga kulit tetap sehat, bersih, terhidrasi, dan terlindungi dari faktor-faktor lingkungan yang dapat merusak kulit seperti sinar matahari, polusi, dan radikal bebas. 
        </p>
        """, unsafe_allow_html=True
    )
    st.markdown(
        """
        <p style="text-align: justify; font-size: 18px; line-height: 1.6; color: #333;">
        Kosmetik adalah produk yang digunakan untuk meningkatkan atau mengubah penampilan wajah, tubuh, atau rambut. Kosmetik mencakup berbagai produk seperti makeup, pewarna rambut, parfum, dan produk perawatan pribadi lainnya. 
        </p>
        """, unsafe_allow_html=True
    )

    st.markdown(
        """
        <p style="text-align: justify; font-size: 18px; line-height: 1.6; color: #333;">
        Toko Indah Store beralamat di Jl. Cibatu, Nagrak, Kec. Cisaat, Kabupaten Sukabumi, Jawa Barat 43152
        </p>
        """, unsafe_allow_html=True
    )

    st.write(
                 """
        <p style="text-align: justify; font-size: 18px; line-height: 1.6; color: #333;">
         Berikut merupakan gambar dari output Itemset Frekuensi Tinggi:
                     </p>
        """, unsafe_allow_html=True
    )

    image_path = 'skarlet.jpg'  # Ganti dengan path gambar Anda
    st.image(image_path, caption='Scarlett', use_column_width=True)

    st.write(
                 """
        <p style="text-align: justify; font-size: 18px; line-height: 1.6; color: #333;">
         Body Lotion Jolly Scarlett dan Body Lotion Losion Scarlett merupakan produk dengan Frekuensi Tinggi.
                     </p>
        """, unsafe_allow_html=True
    )

    st.write(
                 """
        <p style="text-align: justify; font-size: 18px; line-height: 1.6; color: #333;">
         Berikut merupakan produk yang paling sering dibeli secara bersamaan 
                     </p>
        """, unsafe_allow_html=True
    )
    image_path = 'mybelline.jpg'  # Ganti dengan path gambar Anda
    st.image(image_path, caption='Maybelline', use_column_width=True)

    st.write(
                 """
        <p style="text-align: justify; font-size: 18px; line-height: 1.6; color: #333;">
         Eyeliner Gel Maybelline dan Mascara Waterproof Maybelline merupakan produk yang sering dibeli secara bersamaan, dengan arti jika konsumen membeli Eyeliner Gel Maybelline maka konsumen juga akan membeli Mascara Waterproof Maybelline. Dari produk ini perusahaan dapat menyusun tata letak barang sesuai barang yang sering dibeli oleh konsumen.
                     </p>
        """, unsafe_allow_html=True
    )

    st.write(
                 """
        <p style="text-align: justify; font-size: 18px; line-height: 1.6; color: #333;">
         Berikut adalah produk yang sering dibeli dari data transaksi 2023 :
                     </p>
        """, unsafe_allow_html=True
    )

    image_path = 'maybelline.jpg'  # Ganti dengan path gambar Anda
    st.image(image_path, caption='', use_column_width=True)
    
    image_path = 'check.jpg'  # Ganti dengan path gambar Anda
    st.image(image_path, caption='', use_column_width=True)

    image_path = 'sabun.jpg'  # Ganti dengan path gambar Anda
    st.image(image_path, caption='', use_column_width=True)

    st.write(
                 """
        <p style="text-align: justify; font-size: 18px; line-height: 1.6; color: #333;">
         Body Lotion Jolly Scarlett,Eyeliner Gel Maybelline dan Lip Tint Red Wardah, produk ini merupakan produk dengan jumlah transaksi paling banyak atau produk yang paling sering dibeli oleh konsumen. Dari produk yang sering dibeli perusahaan dapat menyusun promosi produk kepada setiap konsumen.
                     </p>
        """, unsafe_allow_html=True
    )
    

