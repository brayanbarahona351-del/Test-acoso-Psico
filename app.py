import streamlit as st
import time

st.set_page_config(
    page_title="Prevención de Acoso", 
    page_icon="🧠", 
    layout="centered"
)

# --- 🧠 SÍMBOLO DE PSICOLOGÍA ---
st.image(
    "https://p1.hiclipart.com/preview/845/460/60/"
    "simbolo-da-psicologia-psychology-symbol-black-text-png-clipart.jpg", 
    width=120
)

st.title("🚨 Test de Prevención de Acoso Sexual")
st.write("**Policía Nacional de Honduras**")
st.write("---")
st.write(
    "Este cuestionario es una herramienta de autoevaluación anónima "
    "para identificar conductas de riesgo, promover el respeto al "
    "consentimiento y garantizar un ambiente laboral seguro."
)

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
    
    col1, col2, col3 = st
