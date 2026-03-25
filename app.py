import streamlit as st
import time

st.set_page_config(page_title="Prevención de Acoso - Policía Nacional", page_icon="🧠", layout="centered")

# --- 🧠 SÍMBOLO DE PSICOLOGÍA ---
st.image("https://p1.hiclipart.com/preview/845/460/60/simbolo-da-psicologia-psychology-symbol-black-text-png-clipart.jpg", width=120)

st.title("🚨 Test de Prevención de Acoso Sexual y Límites Profesionales")
st.write("**Policía Nacional de Honduras**")
st.write("---")
st.write("Este cuestionario es una herramienta de autoevaluación anónima para identificar conductas de riesgo, promover el respeto al consentimiento y garantizar un ambiente laboral seguro en la institución. Responde con total honestidad.")

# --- 📱 BARRA LATERAL (SIDEBAR) PARA DENUNCIAS ---
with st.sidebar:
    st.header("📞 Canales de Denuncia")
    st.write("Si eres víctima o testigo de acoso sexual o laboral, no te quedes callado. Reporta a:")
    st.info("**Inspectoría General:** Denuncia presencial o por los canales oficiales de tu UMEP.")
    st.warning("**DIDADPOL:** 104 (Línea gratuita de denuncias)")
    st.write("---")
    st.error("Recuerda: El acoso sexual y laboral son faltas disciplinarias graves y delitos penales.")

# --- 📝 DICCIONARIO DE PREGUNTAS (12) ---
preguntas = [
    {
        "area": "🛡️ ÁREA 1: Límites Físicos y Ciberacoso",
        "p": "Es costumbre en tu unidad saludar con beso en la mejilla, pero notas que una agente de nuevo ingreso se incomoda y retrocede.", 
        "opts": [
            "Le digo que no sea 'creída' o 'delicada' y la abrazo igual para que se acostumbre.", 
            "Respeto su espacio de inmediato y paso a saludarla solo de palabra o con la mano.", 
            "Me ofendo y le digo a los demás compañeros que es una maleducada."
        ],
        "correcta": 1
    },
    {
        "area": None,
        "p": "Estás aburrido de madrugada cubriendo el portón de la UMEP/Jefatura y estás chateando con colegas.", 
        "opts": [
            "Me limito a conversar de temas generales o enviar memes que no sean ofensivos.", 
            "Le escribo a una compañera preguntándole qué está haciendo en la cama o insinuaciones de doble sentido.", 
            "Mando un sticker o video pornográfico al chat privado de una agente 'solo por bromear'."
        ],
        "correcta": 0
    },
    {
        "area": None,
        "p": "Consigues el número de una agente que te gusta en el grupo oficial de WhatsApp del batallón.", 
        "opts": [
            "Le escribo en su día libre ('franco') para invitarla a salir de forma insistente.", 
            "Le mando fotos mías sin camisa para ver 'si hay química'.", 
            "Respeto que es un grupo de trabajo y uso su número estrictamente para temas operativos."
        ],
        "correcta": 2
    },
    {
        "area": "⚖️ ÁREA 2: Abuso de Poder (Hostigamiento Quid Pro Quo)",
        "p": "Eres jefe de turno (o superior) y te atrae mucho un/a subalterna/o que está bajo tu mando directo.", 
        "opts": [
            "Le ofrezco darle el fin de semana libre o un mejor puesto si acepta salir a cenar conmigo.", 
            "Mantengo estricta distancia profesional; mi rango no es una herramienta para conseguir citas.", 
            "Le pongo los turnos más pesados o le llamo la atención sin razón hasta que me haga caso."
        ],
        "correcta": 1
    },
    {
        "area": None,
        "p": "Un compañero/a de la escala básica te debe un gran favor por haberle cubierto un turno festivo.", 
        "opts": [
            "Le insinúo que me pague el favor con 'cariño', dejándose abrazar o dándome un beso.", 
            "Le digo que si no sale conmigo, le reportaré al superior que faltó ese día.", 
            "Le digo que no se preocupe, el apoyo entre compañeros es fundamental y no pido nada a cambio."
        ],
        "correcta": 2
    },
    {
        "area": None,
        "p": "Estás haciendo una entrevista a una ciudadana que fue víctima de un robo y te parece muy atractiva.", 
        "opts": [
            "Tomo su número del expediente y le escribo en la noche para 'ver cómo sigue' y coquetearle.", 
            "Le ofrezco darle prioridad a su caso si acepta tomarse un café conmigo.", 
            "Realizo el procedimiento policial con total respeto y protejo la privacidad de sus datos."
        ],
        "correcta": 2
    },
    {
        "area": "🗣️ ÁREA 3: Ambiente Laboral Hostil y Complicidad",
        "p": "Durante el rancho (comida), haces un comentario sexual o en doble sentido y una compañera te dice que la incomodaste.", 
        "opts": [
            "Pido disculpas sinceras, reconozco mi error y no vuelvo a hacer comentarios de ese tipo.", 
            "Me burlo de ella frente a los demás por 'no aguantar casaca'.", 
            "Le digo que si está en la Policía tiene que aprender a aguantar el ambiente pesado."
        ],
        "correcta": 0
    },
    {
        "area": None,
        "p": "En el dormitorio de la posta, tus compañeros están mostrando fotos íntimas que se filtraron de la exnovia de un agente.", 
        "opts": [
            "Me río de la situación y les pido que me pasen las fotos por WhatsApp para guardarlas.", 
            "Les exijo que borren eso; les recuerdo que difundir material íntimo es un delito y una falta grave.", 
            "Las veo un rato, pero me quedo callado para no tener problemas con el grupo."
        ],
        "correcta": 1
    },
    {
        "area": None,
        "p": "Escuchas un rumor o 'chambre' fuerte afirmando que un/a oficial ascendió de puesto porque 'se acuesta con el jefe'.", 
        "opts": [
            "Detengo la plática; difamar el trabajo de una colega reduciéndolo a favores sexuales es acoso.", 
            "Me quedo escuchando con atención para saberme bien la historia y averiguar si es cierto.", 
            "Se lo voy a contar de inmediato a mi compañero de patrulla para que también sepa."
        ],
        "correcta": 0
    },
    {
        "area": "🛑 ÁREA 4: Cultura del Consentimiento y el Rechazo",
        "p": "Invitas a salir a un colega de tu misma promoción y te dice clara y directamente: 'No me interesa'.", 
        "opts": [
            "Le sigo insistiendo en los pasillos diciéndole que se está 'haciendo de rogar'.", 
            "Acepto su respuesta con madurez a la primera y no vuelvo a tocar el tema.", 
            "Me enojo, dejo de hablarle y le aplico la 'ley del hielo' durante los turnos."
        ],
        "correcta": 1
    },
    {
        "area": None,
        "p": "Alguien de tu batallón te rechazó una invitación a salir. Días después te toca cubrirle la espalda en un allanamiento u operativo.", 
        "opts": [
            "Hago mi trabajo con el mismo nivel de profesionalismo, vigilancia y lealtad de siempre.", 
            "Hago mi trabajo a medias o con desgano para que vea 'lo que se pierde'.", 
            "Aprovecho el estrés del operativo para tirarle indirectas o burlarme de su rechazo."
        ],
        "correcta": 0
    },
    {
        "area": None,
        "p": "Notas que un superior jerárquico está haciendo comentarios morbosos constantemente sobre el cuerpo de una compañera recién graduada del ITP.", 
        "opts": [
            "Le digo a la compañera que mejor no diga nada porque el superior la puede mandar a 'castigo'.", 
            "Me uno a los comentarios para quedar bien con el superior jerárquico.", 
            "Animo a la compañera a denunciar la situación y me ofrezco como testigo del hostigamiento."
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
    
    # Asignamos una key dinámica a cada radio button para poder reiniciarlos
    res = st.radio(f"**{i+1}. {item['p']}**", item['opts'], key=f"pregunta_{i}", index=None)
    respuestas.append(res)

st.write("---")

# --- 📊 EVALUACIÓN Y ANIMACIONES ---
if st.button("Evaluar mis respuestas", type="primary"):
    if None in respuestas:
        st.warning("⚠️ Por favor, responde las 12 preguntas para poder generar tu evaluación.")
    else:
        # Calculamos los puntos
        puntos = 0
        for i, res in enumerate(respuestas):
            indice_elegido = preguntas[i]['opts'].index(res)
            if indice_elegido == preguntas[i]['correcta']:
                puntos += 1
        
        st.divider()
        
        with st.spinner('Analizando tus respuestas...'):
            time.sleep(1.5)
            
        st.subheader(f"Tu puntuación: {puntos} de 12")
        st.markdown("### 📊 Escala de Calificación de Tolerancia Cero")
        
        # Textos fijos de los niveles
        texto_alto = "🌟 **12 puntos: PROFESIONALISMO Y ÉTICA INTACHABLE** \n\nEntiendes perfectamente qué es el acoso sexual, respetas el consentimiento y promueves un ambiente de trabajo seguro. Eres un policía íntegro y un ejemplo para la institución."
        texto_medio = "⚠️ **9 a 11 puntos: ALERTA DE COMPORTAMIENTOS NORMALIZADOS** \n\nCuidado. Estás justificando o normalizando acciones que constituyen acoso laboral o sexual (como los chistes, rumores o la insistencia). Necesitas revisar tus límites urgentes antes de cometer una falta disciplinaria grave."
        texto_bajo = "🚨 **8 puntos o menos: RIESGO ALTO DE COMETER ACOSO / DELITO** \n\n**Atención:** Tus respuestas reflejan comportamientos de hostigamiento, abuso de autoridad y falta de respeto graves. Estas acciones son causales de despido en la institución e incurren en delitos penales. Se recomienda buscar reeducación inmediata y cambiar estas actitudes."

        # --- LÓGICA DE VISUALIZACIÓN ---
        if puntos == 12:
            st.balloons()
            st.success(f"➡️ **¡TÚ ESTÁS AQUÍ!** \n\n {texto_alto}")
            st.write("---")
            st.markdown(texto_medio)
            st.markdown(texto_bajo)
            
        elif puntos >= 9:
            st.snow()
            st.markdown(texto_alto)
            st.write("---")
            st.warning(f"➡️ **¡TÚ ESTÁS AQUÍ!** \n\n {texto_medio}")
            st.write("---")
            st.markdown(texto_bajo)
            
        else:
            st.toast('🚨 ¡ALERTA DE RIESGO!', icon='🚨')
            time.sleep(0.5)
            st.toast('🛑 Revisa tus comportamientos urgentes', icon='🛑')
            
            st.markdown(texto_alto)
            st.markdown(texto_medio)
            st.write("---")
