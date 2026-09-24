import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="Roma Time Machine - Colosseo")

st.title("🏛️ Roma Time Machine: Colosseo")
st.caption("Trascina il cursore: Colosseo Oggi vs Ricostruzione Imperiale (80 d.C.)")

col1, col2 = st.columns([3, 1])

with col2:
    st.subheader("🎙️ Guida Storica AI")
    st.info(
        "«Anno 80 d.C. L'anfiteatro Flavio risplende nei suoi marmi travertini completi. "
        "50.000 cittadini assistono ai cento giorni di giochi voluti dall'imperatore Tito.»"
    )
    st.markdown("---")
    st.metric(label="Epoca Storica", value="80 d.C. (Flavi)")
    st.metric(label="Stato Struttura", value="Integra al 100%")
    
    st.markdown("---")
    st.subheader("🎟️ Sblocca Roma Antica")
    st.button("Acquista Tour Completo (€4.99)")

with col1:
    viewer_code = """
    <div style="position: relative; width: 100%; height: 560px; overflow: hidden; border-radius: 12px; box-shadow: 0 8px 24px rgba(0,0,0,0.4); font-family: sans-serif; background: #000;">
      
      <!-- LAYER PASSATO: Ricostruzione Storica Roma Antica (Arena integra) -->
      <img id="ancient-img" 
           src="https://images.unsplash.com/photo-1552832230-c0197dd311b5?q=80&w=1600&auto=format&fit=crop" 
           style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover;" />

      <!-- LAYER OGGI: Colosseo Attuale (Rovine) -->
      <div id="modern-container" style="position: absolute; top: 0; left: 0; width: 50%; height: 100%; overflow: hidden; border-right: 4px solid #f39c12; z-index: 2;">
        <img src="https://images.unsplash.com/photo-1543429776-2782fc8e1acd?q=80&w=1600&auto=format&fit=crop" 
             style="position: absolute; top: 0; left: 0; width: 100vw; max-width: none; height: 100%; object-fit: cover;" />
      </div>

      <!-- SLIDER DI SCORRIMENTO -->
      <input type="range" min="0" max="100" value="50" id="slider" 
             style="position: absolute; bottom: 25px; left: 10%; width: 80%; z-index: 10; accent-color: #f39c12; cursor: pointer; height: 8px;">
      
      <!-- ETICHETTE HUD -->
      <div style="position: absolute; top: 18px; left: 18px; background: rgba(0,0,0,0.75); color: #fff; padding: 6px 14px; border-radius: 6px; font-size: 13px; font-weight: bold; z-index: 5;">
        OGGI (Rovine)
      </div>
      <div style="position: absolute; top: 18px; right: 18px; background: rgba(0,0,0,0.75); color: #f39c12; padding: 6px 14px; border-radius: 6px; font-size: 13px; font-weight: bold; z-index: 5;">
        80 d.C. (Imperiale)
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
    components.html(viewer_code, height=580)
