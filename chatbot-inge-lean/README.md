# Chatbot INGE LEAN SAS con OpenAI

Chatbot inteligente para atención al cliente de INGE LEAN SAS, desarrollado con FastAPI y OpenAI GPT.

## 🚀 Características

- ✅ Responde preguntas frecuentes sobre servicios, ubicación, horarios, etc.
- ✅ Interfaz web moderna y responsive
- ✅ API REST con FastAPI
- ✅ Integración con OpenAI GPT-3.5/GPT-4
- ✅ Manejo de errores robusto
- ✅ Indicador de estado en tiempo real

## 📋 Requisitos

- Python 3.8+
- Cuenta en OpenAI con API key
- Navegador web moderno

## 🛠️ Instalación

### 1. Preparar el entorno

```bash
# Extraer el ZIP y navegar al directorio
cd chatbot-inge-lean

# Crear entorno virtual (recomendado)
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Configurar OpenAI

1. Ve a [OpenAI API Keys](https://platform.openai.com/api-keys)
2. Crea una nueva API key
3. Copia el archivo `.env.example` a `.env`
4. Edita `.env` y agrega tu API key:

```env
OPENAI_API_KEY=sk-tu_clave_real_aqui
MODEL_NAME=gpt-3.5-turbo
```

### 4. Ejecutar la aplicación

```bash
# Opción 1: Usando el script incluido
python run.py

# Opción 2: Usando uvicorn directamente
uvicorn app.main:app --reload
```

### 5. Usar el chatbot

Abre tu navegador en: `http://localhost:8000/static/index.html`

## 📁 Estructura del proyecto

```
chatbot-inge-lean/
├── app/
│   ├── __init__.py      # Inicialización del paquete
│   ├── main.py          # Aplicación principal FastAPI
│   ├── faq.py           # Preguntas frecuentes
│   └── utils.py         # Funciones auxiliares
├── static/
│   └── index.html       # Frontend web moderno
├── .env.example         # Ejemplo de variables de entorno
├── requirements.txt     # Dependencias
├── run.py              # Script de ejecución fácil
└── README.md           # Este archivo
```

## 🔧 Personalización

### Modificar las FAQ

Edita el archivo `app/faq.py` para agregar, quitar o modificar preguntas:

```python
FAQ = [
    {
        "q": "¿Nueva pregunta?",
        "a": "Nueva respuesta aquí."
    },
    # ... más preguntas
]
```

### Cambiar el modelo de OpenAI

En tu archivo `.env`:

```env
# Para GPT-4 (si tienes acceso)
MODEL_NAME=gpt-4

# Para GPT-3.5 Turbo (más económico)
MODEL_NAME=gpt-3.5-turbo
```

### Personalizar la interfaz

Edita `static/index.html` para cambiar:
- Colores y estilos CSS
- Textos y mensajes
- Logo de la empresa

## 🔍 Endpoints de la API

- `GET /` - Endpoint de prueba
- `POST /chat` - Endpoint principal para el chat
- `GET /health` - Verificación del estado del servicio
- `GET /docs` - Documentación automática de la API

## 💰 Costos de OpenAI

- **GPT-3.5 Turbo**: ~$0.002 por 1K tokens
- **GPT-4**: ~$0.03 por 1K tokens

Para un chatbot de FAQ, GPT-3.5 Turbo es suficiente y más económico.

## 🚀 Despliegue en producción

### Variables de entorno importantes:

```env
OPENAI_API_KEY=tu_clave_real
MODEL_NAME=gpt-3.5-turbo
DEBUG=False
```

### Consideraciones:

- Configura CORS apropiadamente
- Implementa rate limiting
- Usa HTTPS
- Monitorea el uso de la API de OpenAI

## 🔧 Solución de problemas

### Error: "OPENAI_API_KEY no encontrada"
- Verifica que el archivo `.env` existe
- Verifica que la API key es correcta
- Reinicia la aplicación

### Error: "RateLimitError"
- Has excedido tu cuota de OpenAI
- Verifica tu plan en OpenAI
- Espera unos minutos e intenta de nuevo

### Error: "AuthenticationError"
- Tu API key es inválida
- Verifica que la copiaste correctamente
- Genera una nueva API key en OpenAI

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Notas importantes

- ⚠️ **Nunca subas tu archivo `.env` a repositorios públicos**
- 💡 Monitorea tu uso de la API de OpenAI regularmente
- 🔒 En producción, usa variables de entorno del servidor
- 📊 Considera implementar logging para analizar las consultas

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.

## 👨‍💻 Autor

Desarrollado como proyecto académico para análisis y desarrollo de software.

---

¿Necesitas ayuda? Revisa la [documentación de OpenAI](https://platform.openai.com/docs) o crea un issue en el repositorio.
