"""
Aplicación principal del chatbot con FastAPI y OpenAI
"""

import os
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import openai
from .utils import build_messages, clean_response

# Cargar variables de entorno
load_dotenv()

# Configuración
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# Puedes usar gpt-4 si tienes acceso
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-3.5-turbo")

if not OPENAI_API_KEY:
    raise ValueError(
        "OPENAI_API_KEY no encontrada en las variables de entorno")

# Configurar OpenAI
openai.api_key = OPENAI_API_KEY

# Inicializar FastAPI
app = FastAPI(
    title="Chatbot INGE LEAN SAS",
    description="Chatbot para atención al cliente de INGE LEAN SAS usando OpenAI",
    version="1.0.0"
)

# Configurar CORS para permitir requests desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especifica los dominios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montar archivos estáticos (HTML, CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    """Endpoint de prueba"""
    return {"message": "Chatbot INGE LEAN SAS está funcionando con OpenAI!"}


@app.post("/chat")
async def chat(request: Request):
    """
    Endpoint principal para el chat
    Recibe una pregunta y devuelve una respuesta usando OpenAI
    """
    try:
        # Obtener datos del request
        data = await request.json()
        user_question = data.get("pregunta", "").strip()

        if not user_question:
            return JSONResponse(
                content={"error": "Por favor, escribe una pregunta"},
                status_code=400
            )

        # Construir los mensajes para OpenAI
        messages = build_messages(user_question)

        try:
            # Llamar a la API de OpenAI
            response = openai.ChatCompletion.create(
                model=MODEL_NAME,
                messages=messages,
                max_tokens=200,
                temperature=0.3,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )

            # Extraer la respuesta
            answer = response.choices[0].message.content
            answer = clean_response(answer)

            if not answer:
                answer = "Lo siento, no pude generar una respuesta. Por favor, contacta a nuestro equipo para más información."

        except openai.error.RateLimitError:
            answer = "Lo siento, hemos alcanzado el límite de consultas. Por favor, intenta de nuevo en unos minutos."
        except openai.error.InvalidRequestError as e:
            print(f"Error de solicitud inválida: {e}")
            answer = "Lo siento, hubo un problema con tu consulta. Por favor, reformula tu pregunta."
        except openai.error.AuthenticationError:
            print("Error de autenticación con OpenAI")
            answer = "Lo siento, hay un problema de configuración. Por favor, contacta a nuestro equipo técnico."
        except Exception as api_error:
            print(f"Error en API de OpenAI: {api_error}")
            answer = "Lo siento, hay un problema técnico temporal. Por favor, contacta directamente a nuestro equipo."

        return JSONResponse(content={"respuesta": answer})

    except Exception as e:
        print(f"Error en endpoint /chat: {e}")
        return JSONResponse(
            content={"error": "Error interno del servidor"},
            status_code=500
        )


@app.get("/health")
async def health_check():
    """Endpoint para verificar el estado del servicio"""
    try:
        # Hacer una prueba simple con OpenAI
        test_response = openai.ChatCompletion.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": "test"}],
            max_tokens=5
        )
        openai_connected = True
    except:
        openai_connected = False

    return {
        "status": "healthy",
        "openai_connected": openai_connected,
        "model": MODEL_NAME
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
