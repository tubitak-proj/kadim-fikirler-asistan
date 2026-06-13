import streamlit as st

# Sayfa ayarları
st.set_page_config(
    page_title="Kadim Fikirler", 
    page_icon="✍", 
    layout="centered"
)

# Başlık ve Açıklama
st.title("✨ Kadim Sözler, Yeni Hikayeler")
st.subheader("BİLSEM Yaratıcı Yazarlık Asistanı")
st.markdown("Dünya sorunlarına kadim mirasımızla çözüm bulmaya hazır mısın? Seçimlerini yap ve hikayene başla!")

# Sütunları oluşturma
col1, col2 = st.columns(2)

with col1:
    deger = st.selectbox("Kök Değer Seçiniz:", 
                        ["Yardımseverlik", "Saygı", "Adalet", "Sorumluluk", "Dürüstlük", "Sabır"])
    miras = st.selectbox("Kültürel Miras:", 
                        ["İmece Geleneği", "Ebru Sanatı", "Ahi Teşkilatı", "Bitki Bilgeliği", "Nasreddin Hoca", "Kündekari"])
    ska = st.selectbox("BM Kalkınma Hedefi:", [
        "SKA 17: Ortaklıklar",
        "SKA 14: Sudaki Yaşam",
        "SKA 8: İnsana Yakışır İş",
        "SKA 12: Sorumlu Tüketim",
        "SKA 13: İklim Eylemi"
    ])

with col2:
    tur = st.selectbox("Metin Türü:", ["Mektup", "Distopik Öykü", "Masal", "Günlük"])
    yas = st.selectbox("Yaş Grubu Hedefi:", ["9-11 Yaş", "12-14 Yaş", "15-18 Yaş"])

st.divider()

# İlham Kıvılcımı Butonu
if st.button("🚀 İlham Kıvılcımı Üret", use_container_width=True, type="primary"):
    if tur == "Mektup":
        giris = "Sevgili Gelecek,"
    elif tur == "Günlük":
        giris = "Sevgili Günlük,"
    elif tur == "Masal":
        giris = "Evvel zaman içinde, insanların doğayı unuttuğu bir çağda,"
    else:
        giris = "Gökyüzünün rengi o gün bir başkaydı."
    
    metin = f"""{giris} 
Bugün dünyanın karşı karşıya kaldığı **'{ska}'** krizini çok düşündüm. 
Çözüm aslında sandığımızdan çok daha yakın; atalarımızın **'{miras}'** kültüründe 
ve içimizdeki **'{deger}'** duygusunda gizli. 

Eğer biz bu değeri teknolojiyle birleştirirsek..."""

    st.success("İşte Hikayenin Başlangıcı! Sıra Sende...")
    st.info(metin)
    
    # Ekstra: Devamını yazmak için alan
    st.text_area("Hikayeni buradan devam ettirebilirsin:", height=200)
