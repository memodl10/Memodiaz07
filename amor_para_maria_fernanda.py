import streamlit as st
import time

# Configuración de la página
st.set_page_config(page_title="Para mi chula", page_icon="💖", layout="centered")

# Título
st.title("Para mi chula")
st.subheader("Una carta digital con todo mi cariño – Guillermo Andrés")

# Mensaje inicial
with st.spinner('Escribiéndote algo bonito...'):
    time.sleep(2)

st.success("Te dedico este espacio solo a ti.")
st.markdown("<h1 style='text-align: center;'>💖💖💖</h1>", unsafe_allow_html=True)

# Imagen romántica
st.image("foto_chula.jpeg", caption="Tú y yo, mi chula hermosa.", use_column_width=True)

# Poema romántico
st.markdown("""
### ✨ ¿Por qué te quiero, chula?
- Porque tu sonrisa ilumina hasta los días más oscuros.
- Porque tus abrazos calman mi alma.
- Porque contigo todo tiene sentido.
- Porque eres mi regalo favorito de Dios.
""")

# Efecto de corazones flotando (simulado)
for _ in range(10):
    st.markdown("<p style='text-align: center; font-size: 24px;'>❤️ 💕 💖 💘 💗 💞</p>", unsafe_allow_html=True)
    time.sleep(0.1)

# Botón sorpresa
if st.button("Haz clic si eres la más hermosa"):
    st.write("Sabía que eras tú. ¡Mi chula hermosa, única en el mundo!")

# Canción favorita (Bruno Mars - Die With a Smile)
st.markdown("""
### **Nuestra canción**
Escúchala conmigo:

<iframe width="100%" height="315" src="https://www.youtube.com/embed/IeNMzGfTL40?autoplay=0" 
frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>
""", unsafe_allow_html=True)
