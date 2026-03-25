import streamlit as st
import time

st.set_page_config(page_title="Prevención de Acoso", page_icon="🧠", layout="centered")

# --- 🧠 SÍMBOLO DE PSICOLOGÍA ---
st.image("https://p1.hiclipart.com/preview/845/460/60/simbolo-da-psicologia-psychology-symbol-black-text-png-clipart.jpg", width=120)

st.title("🚨 Test de Prevención de Acoso Sexual")
st.write("**Policía Nacional de Honduras**")
st.write("---")
st.write("Este cuestionario es una herramienta de autoevaluación anónima para identificar conductas de riesgo, promover el respeto al consentimiento y garantizar un ambiente laboral seguro.")

# --- 📱 BARRA LATERAL (SIDEBAR) ---
with st.sidebar:
    st.header("📞 Canales de Denuncia")
    st.write("Si eres víctima de acoso, no te quedes callado:")
    st.info("**Inspectoría General:** Denuncia presencial en tu UMEP.")
    st.warning("**DIDADPOL:** 104 (Línea gratuita de denuncias)")
    st.write("---")
    st.error("El acoso sexual y laboral son delitos penales.")

# --- 📝 DICCIONARIO DE PREGUNTAS (12) ---
preguntas = [
    {
        "area": "🛡️ ÁREA 1: Límites Físicos y Ciberacoso",
        "p": "Es costumbre saludar de beso, pero una agente retrocede.", 
        "opts": [
            "Le digo que no sea 'creída' y la abrazo igual.", 
            "Respeto su espacio y la saludo de palabra.", 
            "Me ofendo y digo a los demás que es maleducada."
        ],
        "correcta": 1
    },
    {
        "area": None,
        "p": "Estás aburrido de madrugada y chateas con colegas.", 
        "opts": [
            "Me limito a conversar y enviar memes no ofensivos.", 
            "Escribo a una compañera con insinuaciones sexuales.", 
            "Mando un video pornográfico al chat privado."
        ],
        "correcta": 0
    },
    {
        "area": None,
        "p": "Consigues el número de una agente que te gusta en WhatsApp.", 
        "opts": [
            "Le escribo en su día libre insistiendo para salir.", 
            "Le mando fotos mías sin camisa.", 
            "Uso su número solo para temas operativos."
        ],
        "correcta": 2
    },
    {
        "area": "⚖️ ÁREA 2: Abuso de Poder",
        "p": "Eres jefe y te atrae un subalterno bajo tu mando.", 
        "opts": [
            "Le ofrezco el fin de semana libre si sale conmigo.", 
            "Mantengo distancia; mi rango no es para conseguir citas.", 
            "Le pongo los turnos más pesados hasta que me haga caso."
        ],
        "correcta": 1
    },
    {
        "area": None,
        "p": "Un compañero te debe un favor por cubrirle un turno.", 
        "opts": [
            "Le insinúo que me pague dejándose abrazar.", 
            "Le digo que si no sale conmigo, le reportaré.", 
            "Le digo que el apoyo entre compañeros es fundamental."
        ],
        "correcta": 2
    },
    {
        "area": None,
        "p": "Entrevistas a una ciudadana víctima de robo muy atractiva.", 
        "opts": [
            "Tomo su número del expediente para coquetearle.", 
            "Le ofrezco prioridad en su caso si toma un café conmigo.", 
            "Realizo el procedimiento con total respeto a sus datos."
        ],
        "correcta": 2
    },
    {
        "area": "🗣️ ÁREA 3: Ambiente Laboral Hostil",
        "p": "Haces un comentario sexual y una compañera se incomoda.", 
        "opts": [
            "Pido disculpas sinceras y no lo vuelvo a hacer.", 
            "Me burlo de ella por 'no aguantar casaca'.", 
            "Le digo que aprenda a aguantar el ambiente pesado."
        ],
        "correcta": 0
    },
    {
        "area": None,
        "p": "Tus compañeros muestran fotos íntimas filtradas de una exnovia.", 
        "opts": [
            "Me río y pido que me pasen las fotos para guardarlas.", 
            "Les exijo que borren eso; difundirlas es un delito.", 
            "Las veo, pero me quedo callado para no tener problemas."
        ],
        "correcta": 1
    },
    {
        "area": None,
        "p": "Escuchas que alguien ascendió porque 'se acuesta con el jefe'.", 
        "opts": [
            "Detengo la plática; difamar así es acoso.", 
            "Me quedo escuchando para averiguar si es cierto.", 
            "Se lo cuento de inmediato a mi compañero de patrulla."
        ],
        "correcta": 0
    },
    {
        "area": "🛑 ÁREA 4: Cultura del Consentimiento",
        "p": "Invitas a salir a un colega y te dice: 'No me interesa'.", 
        "opts": [
            "Le sigo insistiendo diciéndole que se hace de rogar.", 
            "Acepto su respuesta con madurez y no toco el tema.", 
            "Me enojo y le aplico la 'ley del hielo' en los turnos."
        ],
        "correcta": 1
    },
    {
        "area": None,
        "p": "Alguien te rechazó. Días después te toca cubrirle la espalda.", 
        "opts": [
            "Hago mi trabajo con profesionalismo y lealtad.", 
            "Hago mi trabajo a medias para que vea lo que se pierde.", 
            "Aprovecho el operativo para tirarle indirectas."
        ],
        "correcta": 0
    },
    {
        "area": None,
        "p": "Un superior hace comentarios morbosos sobre una compañera nueva.", 
        "opts": [
            "Le digo a ella que calle para evitar un castigo.", 
            "Me uno a los comentarios para quedar bien.", 
            "Animo a la compañera a denunciar y soy su testigo."
        ],
        "correcta": 2
    }
]

respuestas = []

# --- 🚀 MOSTRAR PREGUNTAS ---
for i, item in enumerate(preguntas):
    if item["area"]:
        st.write("---")
        st.subheader(item["area"])
    
    res = st.radio(f"**{i+1}. {item['p']}**", item['opts'], key=f"q_{i}")
    respuestas.append(res)

st.write("---")

# --- 📊 EVALUACIÓN ---
if st.button("Evaluar mis respuestas", type="primary"):
    puntos = 0
    for i, res in enumerate(respuestas):
        if res == preguntas[i]['opts'][preguntas[i]['correcta']]:
            puntos += 1
            
    st.divider()
    
    porcentaje = int((puntos / 12) * 100)
    texto_carga = "Analizando tu perfil..."
    barra_progreso = st.progress(0, text=texto_carga)
    
    if porcentaje > 0:
        for i in range(porcentaje):
            time.sleep(0.01)
            barra_progreso.progress(i + 1, text=f"{texto_carga} {i+1}%")
    else:
        time.sleep(1)
        
    barra_progreso.empty()
    
    # ¡Esta es la línea que se te había borrado a la mitad!
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.metric(label="Tu Puntuación Obtenida", value=f"{puntos} / 12", delta=f"{porcentaje}% de compatibilidad")
    
    st.markdown("### 📊 Ubicación en la Escala Ética")
    
    posicion = (puntos / 12) * 100
    
    html_grafica = (
        "<div style='width:100%; background-color:#ddd; border-radius:5px; position:relative; height:35px; margin-top:10px;'>"
        "<div style='width:66.6%; background-color:#ff4b4b; height:100%; border-radius:5px 0 0 5px; position:absolute; left:0; top:0; display:flex; align-items:center; justify-content:center; color:white; font-weight:bold; font-size:12px;'>RIESGO</div>"
        "<div style='width:25%; background-color:#ffaa00; height:100%; position:absolute; left:66.6%; top:0; display:flex; align-items:center; justify-content:center; color:white; font-weight:bold; font-size:12px;'>ALERTA</div>"
        "<div style='width:8.4%; background-color:#28a745; height:100%; border-radius:0 5px 5px 0; position:absolute; left:91.6%; top:0; display:flex; align-items:center; justify-content:center; color:white; font-weight:bold; font-size:12px;'>ÓPTIMO</div>"
        f"<div style='position:absolute; left:calc({posicion}% - 10px); top:-20px; font-size:20px;'>⬇️</div>"
        "</div>"
        "<div style='display:flex; justify-content:space-between; font-size:12px; color:#555; padding-top:2px;'>"
        "<span>0 pts</span><span>8 pts</span><span>11 pts</span><span>12 pts</span>"
        "</div>"
    )
    
    st.markdown(html_grafica, unsafe_allow_html=True)
    st.write("---")
    
    st.markdown("### 📋 Tu Diagnóstico y Consejos")

    texto_alto = "🌟 **12 pts: ÉTICA INTACHABLE** \n\nEntiendes el respeto y promueves un ambiente seguro."
    consejo_alto = "**💡 Consejo:** ¡Sigue así! Sé un agente de cambio y corrige a tus compañeros si ves acoso."

    texto_medio = "⚠️ **9 a 11 pts: ALERTA DE RIESGO** \n\nEstás normalizando acciones que constituyen acoso."
    consejo_medio = "**💡 Consejo:** Reflexiona sobre las 'bromas'. Mantén una postura profesional siempre."

    texto_bajo = "🚨 **8 pts o menos: RIESGO ALTO** \n\nTus respuestas reflejan hostigamiento y abuso graves."
    consejo_bajo = "**💡 URGENTE:** Detén cualquier insinuación. El rango no te da derecho a favores."

    if puntos == 12:
        st.balloons()
        col_img, col_txt = st.columns([1, 3])
        with col_img:
            st.markdown("<h1 style='text-align:center;font-size:80px;'>👮‍♂️✨</h1>", unsafe_allow_html=True)
        with col_txt:
            st.success(f"🎯 **¡TÚ ESTÁS AQUÍ!** \n\n {texto_alto}")
            st.info(consejo_alto)
            
    elif puntos >= 9:
        st.snow()
        col_img, col_txt = st.columns([1, 3])
        with col_img:
            st.markdown("<h1 style='text-align:center;font-size:80px;'>👮‍♂️🤔</h1>", unsafe_allow_html=True)
        with col_txt:
            st.warning(f"🎯 **PRESTA ATENCIÓN** \n\n {texto_medio}")
            st.warning(consejo_medio)
            
    else:
        st.toast('🚨 ¡ALERTA DE RIESGO!', icon='🚨')
        col_img, col_txt = st.columns([1, 3])
        with col_img:
            st.markdown("<h1 style='text-align:center;font-size:80px;'>👮‍♂️🛑</h1>", unsafe_allow_html=True)
