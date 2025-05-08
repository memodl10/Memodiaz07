import streamlit as st
import time

# Configuración de la página
st.set_page_config(
    page_title="Para chula",
    page_icon="❤️",
    layout="centered"
)

# Título principal
st.title("Para chula")
st.subheader("Una carta digital con todo mi cariño – Guillermo Andrés")

# Mensaje inicial
with st.spinner("Escribiéndote algo bonito..."):
    time.sleep(2)

st.success("Te dedico este espacio solo a ti.")
st.markdown("<h2 style='text-align: center;'>❤️❤️❤️❤️❤️</h2>", unsafe_allow_html=True)

# Mostrar imagen
st.image("foto_chula.jpeg.JPG", use_column_width=True, caption="Tú y yo, chula hermosa.")

# Poema o dedicatoria
st.markdown("""
### ✨ ¿Por qué te quiero mucho, chula?
- Porque tu sonrisa ilumina hasta los días más oscuros.
- Porque tus abrazos tienen el poder de calmar mi alma.
- Porque contigo todo tiene sentido.
- Porque eres mi regalo favorito de Dios.
""")

# Botón sorpresa
if st.button("Haz clic si eres la más hermosa"):
    st.markdown("### ¡Sabía que eras tú! ¡Chula hermosa, única y favorita!")
    st.markdown("<h1 style='text-align: center;'>❤️</h1>", unsafe_allow_html=True)

# Enlace a la canción
st.markdown("""
### **Nuestra canción especial:**
[**Escuchemos "Die With a Smile" de Bruno Mars**](https://www.youtube.com/watch?v=dQw4w9WgXcQ)
""")

# Mensaje final
st.markdown("""
---
**Con todo mi cariño,  
Guillermo Andrés**  
❤️
""")
