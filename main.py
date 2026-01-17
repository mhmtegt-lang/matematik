import streamlit as st
import time

# Sayfa tasarımı
st.set_page_config(page_title="Zıplayan Virgül", layout="centered")

# Görsel stil ayarları
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: white; }
    .digit-card {
        background-color: white; color: #0d1117;
        border-radius: 10px; padding: 15px;
        font-size: 50px; font-weight: bold;
        text-align: center; margin: 5px;
        display: inline-block; width: 70px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.5);
    }
    .comma-style {
        font-size: 60px; color: #ff4b4b;
        font-weight: bold; margin: 0 10px;
        display: inline-block;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🔢 Ondalık Sayılar: Virgülün Yolculuğu")

# Giriş Alanları
col1, col2 = st.columns(2)
with col1:
    sayi_input = st.text_input("Bir sayı girin (Virgüllü):", "3,456")
with col2:
    carpan = st.selectbox("Çarpanı seçin:", [10, 100, 1000])

# Sayı kartlarının yerinde değişeceği alan
placeholder = st.empty()

if st.button("Hareketi Başlat! ✨"):
    # Matematiksel işlem için virgülü noktaya çevir
    sayi_str = sayi_input.replace(',', '.')
    if '.' not in sayi_str: sayi_str += '.0'
    liste = list(sayi_str)
    adim_sayisi = len(str(carpan)) - 1
    
    for i in range(adim_sayisi + 1):
        with placeholder.container():
            # Sayıyı kartlar halinde tek satırda göster
            html_content = '<div style="display: flex; justify-content: center; align-items: center; flex-wrap: wrap;">'
            for char in liste:
                if char == '.':
                    html_content += '<div class="comma-style">,</div>'
                else:
                    html_content += f'<div class="digit-card">{char}</div>'
            html_content += '</div>'
            st.markdown(html_content, unsafe_allow_html=True)
            
            if i < adim_sayisi:
                st.info(f"Adım {i+1}: Virgül bir sağa zıplıyor...")
                # Virgül kaydırma mantığı
                idx = liste.index('.')
                if idx == len(liste) - 1:
                    liste.pop(idx); liste.append('0'); liste.append('.')
                else:
                    liste[idx], liste[idx+1] = liste[idx+1], liste[idx]
                time.sleep(1.5)
            else:
                sonuc = "".join(liste).replace('.', ',').rstrip(',')
                st.success(f"İşlem Tamamlandı! Sonuç: {sonuc}")
                st.balloons()
