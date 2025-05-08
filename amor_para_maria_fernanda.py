import streamlit as st
import time

# Configuración de la app
st.set_page_config(page_title="Para mi chula", page_icon="💖")

# Título
st.title("Para mi chula")
st.subheader("Una carta digital con todo mi cariño – Guillermo Andrés")

# Mensaje inicial
with st.spinner('Escribiéndote algo bonito...'):
    time.sleep(2)
st.success("Te dedico este espacio solo a ti.")
st.balloons()

# Mostrar imagen
st.image("foto_chula.jpeg.JPG", caption="Tú y yo, mi chula hermosa.", use_column_width=True)

# Poesía con markdown
st.markdown("""
### ✨ ¿Por qué te quiero, mi chula?
- Porque tu sonrisa ilumina hasta los días más oscuros.
- Porque tus abrazos tienen el poder de calmar mi alma.
- Porque contigo todo tiene sentido.
- Porque eres mi regalo favorito de Dios.
""")

# Botón sorpresa
if st.button("Haz clic si eres la más hermosa"):
    st.write("Sabía que eras tú. ¡Mi chula hermosa, única e irrepetible!")

# Canción favorita
st.markdown("**Escuchemos nuestra canción juntos:**")
st.video("https://www.youtube.com/watch?v=UyMNC3C2EGc")  # Puedes reemplazarlo si tienes otro link

# Mensaje final
st.markdown("""
---

Gracias por existir, por hacerme reír y por dejarme quererte.

Con todo mi cariño,  
**Guillermo Andrés**
""")
