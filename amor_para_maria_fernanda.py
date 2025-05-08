import streamlit as st
import time

# Configuración de la app
st.set_page_config(page_title="Para mi chula", page_icon="💖")

# Título
st.title("Para mi chula")
st.subheader("Una carta digital con todo mi cariño - Guillermo Andrés")

# Mensaje inicial
with st.spinner('Escribiéndote algo bonito...'):
    time.sleep(2)

st.success("Te dedico este espacio solo a ti.")
st.balloons()

# Mostrar imagen
st.image("EF6CF4CB-6CFD-46AE-AF24-E365AEDFB88F.jpeg", caption="Tú y yo. El mejor equipo.", use_column_width=True)

# Poesía con markdown
st.markdown("""
### ✨ ¿Por qué te amo, mi chula?
- Porque tu sonrisa ilumina hasta los días más oscuros.
- Porque tus abrazos tienen el poder de calmar mi alma.
- Porque contigo todo tiene sentido.
- Porque eres mi regalo favorito de Dios.

""")

# Botón sorpresa
if st.button("Haz clic si eres la más hermosa"):
    st.write("Sabía que eras tú. ¡Mi chula hermosa, única e irreemplazable!")

# Canción favorita
st.markdown("**Escuchemos nuestra canción juntos:**")
st.markdown("[Die With A Smile - Bruno Mars (Spotify)](https://open.spotify.com/track/1f8Pfy7sy3bzw1niT2YboF)")

# Despedida
st.write("---")
st.markdown("Creado con amor por **Guillermo Andrés**")
