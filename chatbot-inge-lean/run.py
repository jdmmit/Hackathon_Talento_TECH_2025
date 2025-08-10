"""
Script para ejecutar el chatbot fácilmente
"""

import uvicorn
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

def main():
    print("🤖 Iniciando Chatbot INGE LEAN SAS con OpenAI...")
    print("=" * 60)

    # Verificar API key
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌ ERROR: OPENAI_API_KEY no encontrada!")
        print("📝 Por favor:")
        print("   1. Copia .env.example a .env")
        print("   2. Agrega tu API key de OpenAI")
        print("   3. Ejecuta de nuevo")
        return

    if api_key.startswith("sk-") and len(api_key) > 20:
        print("✅ API Key de OpenAI configurada correctamente")
    else:
        print("⚠️  ADVERTENCIA: La API key parece incorrecta")

    model = os.getenv("MODEL_NAME", "gpt-3.5-turbo")
    print(f"🧠 Modelo: {model}")

    print("🌐 URLs importantes:")
    print("   📱 Interfaz web: http://localhost:8000/static/index.html")
    print("   🔧 API docs: http://localhost:8000/docs")
    print("   ❤️  Health check: http://localhost:8000/health")
    print("=" * 60)
    print("❌ Para detener: Ctrl+C")
    print("🚀 Iniciando servidor...")

    try:
        uvicorn.run(
            "app.main:app",
            host="0.0.0.0",
            port=8000,
            reload=True,
            log_level="info"
        )
    except KeyboardInterrupt:
        print("\n👋 ¡Chatbot detenido! Hasta luego.")
    except Exception as e:
        print(f"\n❌ Error al iniciar: {e}")

if __name__ == "__main__":
    main()
