"""
Funciones auxiliares para el chatbot
"""

from .faq import FAQ

def build_prompt(user_question: str) -> str:
    """
    Construye el prompt que se enviará a la API de OpenAI

    Args:
        user_question (str): La pregunta del usuario

    Returns:
        str: El prompt completo para la API
    """
    # Convertir las FAQ en texto legible
    faq_text = "\n".join([f"P: {item['q']}\nR: {item['a']}" for item in FAQ])

    # Construir el prompt completo
    prompt = (
        "Eres un asistente virtual de INGE LEAN SAS, una empresa de soluciones tecnológicas en el Eje Cafetero, Colombia. "
        "Responde de manera clara, amable y profesional a las preguntas de los clientes. "
        "Si la pregunta no está relacionada con las FAQ o con la empresa, responde: "
        "'Por favor, comunícate con nuestro equipo para más información específica.'\n\n"
        "PREGUNTAS FRECUENTES:\n"
        f"{faq_text}\n\n"
        f"Pregunta del usuario: {user_question}\n"
        "Respuesta:"
    )

    return prompt

def clean_response(response: str) -> str:
    """
    Limpia la respuesta de la API eliminando espacios extra y caracteres no deseados

    Args:
        response (str): Respuesta cruda de la API

    Returns:
        str: Respuesta limpia
    """
    return response.strip().replace('\n\n', '\n')

def build_messages(user_question: str) -> list:
    """
    Construye los mensajes para el formato de chat de OpenAI

    Args:
        user_question (str): La pregunta del usuario

    Returns:
        list: Lista de mensajes para la API de OpenAI
    """
    # Convertir las FAQ en texto legible
    faq_text = "\n".join([f"P: {item['q']}\nR: {item['a']}" for item in FAQ])

    system_message = (
        "Eres un asistente virtual de INGE LEAN SAS, una empresa de soluciones tecnológicas en el Eje Cafetero, Colombia. "
        "Responde de manera clara, amable y profesional a las preguntas de los clientes. "
        "Si la pregunta no está relacionada con las FAQ o con la empresa, responde: "
        "'Por favor, comunícate con nuestro equipo para más información específica.'\n\n"
        "PREGUNTAS FRECUENTES:\n"
        f"{faq_text}"
    )

    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_question}
    ]

    return messages
