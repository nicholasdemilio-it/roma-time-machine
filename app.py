import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="Roma Time Machine - Colosseo")

st.title("🏛️ Roma Time Machine: Colosseo")
st.caption("Confronto interattivo: Oggi (Street View) vs Ricostruzione Imperiale (80 d.C.)")

# Parametri e narrazione AI
col1, col2 = st.columns([3, 1])

with col2:
    st.subheader("🎙️ Guida Storica AI")
    st.info(
        "«Sei nell'anno 80 d.C. L'imperatore Tito ha appena inaugurato l'Anfiteatro Flavio. "
        "Oltre 50.000 spettatori riempiono le gradinate in travertino protetti dal grande velario rosso.»"
    )
    st.markdown("---")
    st.metric(label="Stato Ricostruzione", value="Epoca Flavia")
    st.button("🔊 Ascolta Narrazione Vocale")

with col1:
    # Componente interattivo Slider Prima / Dopo
    viewer_code = """
    <div style="position: relative; width: 100%; height: 580px; overflow: hidden; border-radius: 12px; box-shadow: 0 8px 24px rgba(0,0,0,0.3); font-family: sans-serif;">
      <!-- Layer Passato (Ricostruzione Storica) -->
      <img id="ancient-img" 
           src="https://images.unsplash.com/photo-1552832230-c0197dd311b5?q=80&w=1600&auto=format&fit=crop" 
           style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover;" />

      <!-- Layer Oggi (Street View / Rovine attuali) -->
      <div id="modern-container" style="position: absolute; top: 0; left: 0; width: 50%; height: 100%; overflow: hidden; border-right: 3px solid #f39c12;">
        <img src="https://images.unsplash.com/photo-1543429776-2782fc8e1acd?q=80&w=1600&auto=format&fit=crop" 
             style="position: absolute; top: 0; left: 0; width: 100vw; max-width: none; height: 100%; object-fit: cover;" />
      </div>

      <!-- Cursore Slider -->
      <input type="range" min="0" max="100" value="50" id="slider" 
             style="position: absolute; bottom: 25px; left: 10%; width: 80%; z-index: 10; accent-color: #f39c12; cursor: pointer;">
      
      <!-- Etichette -->
      <div style="position: absolute; top: 15px; left: 15px; background: rgba(0,0,0,0.7); color: #fff; padding: 6px 12px; border-radius: 4px; font-size: 13px; font-weight: bold;">
        OGGI
      </div>
      <div style="position: absolute; top: 15px; right: 15px; background: rgba(0,0,0,0.7); color: #f39c12; padding: 6px 12px; border-radius: 4px; font-size: 13px; font-weight: bold;">
        80 d.C.
      </div>
    </div>

    <script>
      const slider = document.getElementById('slider');
      const modernContainer = document.getElementById('modern-container');
      slider.addEventListener('input', (e) => {
        modernContainer.style.width = e.target.value + '%';
      });
    </script>
    """
    components.html(viewer_code, height=600)
