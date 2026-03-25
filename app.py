import streamlit as st
import time

st.set_page_config(page_title="Prevención de Acoso", page_icon="🧠", layout="centered")

# --- 🧠 SÍMBOLO DE PSICOLOGÍA ---
st.image("https://p1.hiclipart.com/preview/845/460/60/simbolo-da-psicologia-psychology-symbol-black-text-png-clipart.jpg", width=120)

st.title("🚨 Test de Prevención de Acoso Sexual")
st.write("**Policía Nacional de Honduras**")
st.write("---")
st.write(
    "Este cuestionario es una herramienta de autoevaluación anónima "
    "para identificar conductas de riesgo, promover el respeto al consentimiento "
    "y garantizar un ambiente laboral seguro. Responde con honestidad."
)

# --- 📱 BARRA LATERAL (SIDEBAR) ---
with st.sidebar:
    st.header("📞 Canales de Denuncia")
    st.write("Si eres víctima o testigo de acoso, no te quedes callado. Reporta a:")
    st.info("**Inspectoría General:** Denuncia presencial en tu UMEP.")
    st.warning("**DIDADPOL:** 104 (Línea gratuita de denuncias)")
    st.write("---")
    st.error("El acoso sexual y laboral son faltas graves y delitos penales.")

# --- 📝 DICCIONARIO DE PREGUNTAS (12) ---
# He acortado las líneas para que no den error al copiar
preguntas = [
    {
        "area": "🛡️ ÁREA 1: Límites Físicos y Ciberacoso",
        "p": "Es costumbre saludar con beso, pero una agente nueva se incomoda y retrocede.", 
        "opts": [
            "Le digo que no sea 'creída' y la abrazo igual.", 
            "Respeto su espacio de inmediato y la saludo de palabra o con la mano.", 
            "Me ofendo y le digo a los demás que es una maleducada."
        ],
        "correcta": 1
    },
    {
        "area": None,
        "p": "Estás aburrido de madrugada en el portón y chateas con colegas.", 
        "opts": [
            "Me limito a conversar de temas generales o enviar memes no ofensivos.", 
            "Le escribo a una compañera preguntando qué hace en la cama (insinuaciones).", 
            "Mando un video pornográfico al chat privado de una agente 'por bromear'."
        ],
        "correcta": 0
    },
    {
        "area": None,
        "p": "Consigues el número de una agente que te gusta en el grupo oficial de WhatsApp.", 
        "opts": [
            "Le escribo en su día libre de forma insistente para salir.", 
            "Le mando fotos mías sin camisa para ver 'si hay química'.", 
            "Respeto que es un grupo de trabajo y uso su número solo para temas operativos."
        ],
        "correcta": 2
    },
    {
        "area": "⚖️ ÁREA 2: Abuso de Poder",
        "p": "Eres jefe de turno y te atrae mucho un/a subalterna/o bajo tu mando.", 
        "opts": [
            "Le ofrezco el fin de semana libre si acepta salir a cenar conmigo.", 
            "Mantengo estricta distancia profesional; mi rango no es para conseguir citas.", 
            "Le pongo los turnos más pesados hasta que me haga caso."
        ],
        "correcta": 1
    },
    {
        "area": None,
        "p": "Un compañero de la escala básica te debe un favor por cubrirle un turno.", 
        "opts": [
            "Le insinúo que me pague con 'cariño', dejándose abrazar o dándome un beso.", 
            "Le digo que si no sale conmigo, le reportaré al superior.", 
            "Le digo que no se preocupe, el apoyo entre compañeros es fundamental."
        ],
        "correcta": 2
    },
    {
        "area": None,
        "p": "Entrevistas a una ciudadana víctima de un robo y te parece muy atractiva.", 
        "opts": [
            "Tomo su número del expediente y le escribo en la noche para coquetearle.", 
            "Le ofrezco darle prioridad a su caso si acepta tomarse un café conmigo.", 
            "Realizo el procedimiento con total respeto y protejo sus datos."
        ],
        "correcta": 2
    },
    {
        "area": "🗣️ ÁREA 3: Ambiente Laboral Hostil",
        "p": "En la comida haces un comentario sexual y una compañera dice que la incomodaste.", 
        "opts": [
            "Pido disculpas sinceras, reconozco mi error y no lo vuelvo a hacer.", 
            "Me burlo de ella frente a los demás por 'no aguantar casaca'.", 
            "Le digo que en la Policía tiene que aprender a aguantar el ambiente pesado."
        ],
        "correcta": 0
    },
    {
        "area": None,
        "p": "Tus compañeros muestran fotos íntimas filtradas de la exnovia de un agente.", 
        "opts": [
            "Me río y les pido que me pasen las fotos por WhatsApp para guardarlas.", 
            "Les exijo que borren eso; difundir material íntimo es un delito.", 
            "Las veo un rato, pero me quedo callado para no tener problemas con el grupo."
        ],
        "correcta": 1
    },
    {
        "area": None,
        "p": "Escuchas el rumor de que un/a oficial ascendió porque 'se acuesta con el jefe'.", 
        "opts": [
            "Detengo la plática; difamar reduciendo el trabajo a favores sexuales es acoso.", 
            "Me quedo escuchando para averiguar si es cierto.", 
            "Se lo voy a contar de inmediato a mi compañero de patrulla."
        ],
        "correcta": 0
    },
    {
        "area": "🛑 ÁREA 4: Cultura del Consentimiento",
        "p": "Invitas a salir a un colega y te dice claramente: 'No me interesa'.", 
        "opts": [
            "Le sigo insistiendo en los pasillos diciéndole que se hace de rogar.", 
            "Acepto su respuesta con madurez a la primera y no vuelvo a tocar el tema.", 
            "Me enojo y le aplico la 'ley del hielo' durante los turnos."
        ],
        "correcta": 1
    },
    {
        "area": None,
        "p": "Alguien te rechazó una cita. Días después te toca cubrirle en un operativo.", 
        "opts": [
            "Hago mi trabajo con el mismo nivel de profesionalismo y lealtad de siempre.", 
            "Hago mi trabajo a medias para que vea 'lo que se pierde'.", 
            "Aprovecho el estrés del operativo para tirarle indirectas por su rechazo."
        ],
        "correcta": 0
    },
    {
        "area": None,
        "p": "Un superior hace comentarios morbosos sobre el cuerpo de una compañera nueva.", 
        "opts": [
            "Le digo a la compañera que mejor no diga nada para evitar un 'castigo'.", 
            "Me uno a los comentarios para quedar bien con el superior.", 
            "Animo a la compañera a denunciar y me ofrezco como testigo."
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
    
    res = st.radio(f"**{i+1}. {item['p']}**", item['opts'], key=f"pregunta_{i}")
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
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.metric(label="Tu Puntuación Obtenida", value=f"{puntos} / 12", delta=f"{porcentaje}% de compatibilidad")
    
    st.markdown("### 📊 Ubicación en la Escala Ética")
    
    posicion = (puntos / 12) * 100
    
    # Textos HTML separados estrictamente con (+) para evitar errores de salto de línea
    html_grafica = (
        "<div style='width:100%;background-color:#ddd;border-radius:5px;position:relative;height:35px;margin-top:10px;'>"
        "<div style='width:66.6%;background-color:#ff4b4b;height:100%;border-radius:5px 0 0 5px;position:absolute;left:0;top:0;display:flex;align-items:center;justify-content:center;color:white;font-weight:bold;font-size:12px;'>RIESGO</div>"
        "<div style='width:25%;background-color:#ffaa00;height:100%;position:absolute;left:66.6%;top:0;display:flex;align-items:center;justify-content:center;color:white;font-weight:bold;font-size:12px;'>ALERTA</div>"
        "<div style='width:8.4%;background-color:#28a745;height:100%;border-radius:0 5px 5px 0;position:absolute;left:91.
