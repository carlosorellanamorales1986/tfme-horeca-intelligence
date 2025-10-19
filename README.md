TFME-HORECA-INTELLIGENCE

Sistema de Inteligencia Comercial para el Sector HORECA mediante scrapping Críticas de Tripadvisor Apify y análisis de oportunidades de negocio con DeepSeek AI.

📋 Tabla de Contenidos

    🎯 Overview

    🚀 Características Principales

    🏗️ Arquitectura del Sistema

    📦 Instalación

    ⚙️ Configuración

    📊 Flujo de Trabajo

    📁 Estructura del Proyecto

    🎮 Uso del Sistema

    📈 Resultados y Métricas

    🔧 Tecnologías Utilizadas

    🤝 Contribución

    📄 Licencia

🎯 Overview

TFME-HORECA-INTELLIGENCE es un sistema completo de análisis de inteligencia comercial para el sector HORECA (Hoteles, Restaurantes, Cafeterías) que transforma críticas negativas de Tripadvisor en oportunidades de negocio accionables mediante el uso de DeepSeek AI.


💡 Problema que Resuelve
Los establecimientos HORECA reciben cientos de críticas en plataformas como Tripadvisor, pero extraer insights accionables de estas críticas es un proceso manual, lento y subjetivo. Este sistema automatiza:

    🔍 Detección de problemas recurrentes

    🏷️ Clasificación automática de tipos de queja

    💡 Generación de oportunidades comerciales específicas

    📊 Agregación por establecimiento y temporalidad

🚀 Características Principales
1. Scraping Inteligente 🤖

    Extracción automatizada de restaurantes y críticas de Tripadvisor

    Sistema de actualización incremental para evitar duplicados

    Manejo robusto de errores y rate limiting

2. Procesamiento con IA 🧠

    Traducción automática a español de críticas en otros idiomas

    Clasificación de quejas en 20 categorías estandarizadas

    Resumen automático de problemáticas principales

3. Generación de Oportunidades 💼

    Detección de patrones recurrentes en críticas

    Propuestas comerciales específicas y accionables

    Agrupación por establecimiento y temporalidad

4. Base de Datos Centralizada 🗃️

    Almacenamiento estructurado de todos los datos

    Relaciones entre restaurantes, críticas y oportunidades

    Consultas SQL optimizadas para análisis

🏗️ Arquitectura del Sistema
Módulos Principales

    01_apify_scrape_restaurants.ipynb - Scraping de datos de restaurantes

    02_apify_scrape_reviews.ipynb - Scraping de críticas por restaurante

    03_deepseek_reviews_processing.ipynb - Procesamiento y clasificación con IA

    04_deepseek_oportunity_generator.ipynb - Generación de oportunidades comerciales

📦 Instalación
Prerrequisitos

    Python 3.8 o superior

    API Key de DeepSeek

    Cuenta de Apify (opcional, para scraping)

Instalación Rápida


# Clonar el repositorio
git clone https://github.com/tu-usuario/tfme-horeca-intelligence.git
cd tfme-horeca-intelligence

# Instalar dependencias
pip install -r requirements.txt

# O usar el script de instalación automática
python install.py

Dependencias Principales
txt

pandas>=1.5.0
requests>=2.28.0
apify-client>=1.0.0
numpy>=1.21.0

⚙️ Configuración
1. Archivo de Configuración

Crear config.py en la raíz del proyecto:
python

# config.py
DEEPSEEK_API_KEY = "sk-tu-api-key-de-deepseek"
DB_PATH = "tfm_database.db"
APIFY_API_KEY = "tu-api-key-de-apify"  # Opcional

2. Obtención de API Keys

    DeepSeek: https://platform.deepseek.com/api_keys

    Apify: https://console.apify.com/account/integrations (opcional)

📊 Flujo de Trabajo
Ejecución Completa del Sistema


# 1. Scraping de restaurantes
jupyter notebook 01_apify_scraping_restaurantes.ipynb

# 2. Scraping de críticas  
jupyter notebook 02_apify_scraping_reviews.ipynb

# 3. Procesamiento con IA
jupyter notebook 03_deepseek_procesamiento_reviews.ipynb

# 4. Generación de oportunidades
jupyter notebook 04_deepseek_generacion_oportunidades.ipynb

Flujo Paso a Paso

    📈 Scraping Inicial

        Obtención de lista de restaurantes de una ciudad

        Extracción de metadatos (nombre, dirección, rating, etc.)

    📝 Recolección de Críticas

        Scraping de críticas negativas (<3 estrellas)

        Filtrado por últimos 3 meses

        Almacenamiento estructurado

    🤖 Procesamiento con IA

        Traducción a español si es necesario

        Clasificación en categorías de queja

        Resumen automático de problemáticas

    💡 Generación de Oportunidades

        Agrupación por restaurante

        Análisis de patrones recurrentes

        Propuestas comerciales específicas

📁 Estructura del Proyecto


tfme-horeca-intelligence/
├── 📓 01_apify_scraping_restaurantes.ipynb
├── 📓 02_apify_scraping_reviews.ipynb
├── 📓 03_deepseek_procesamiento_reviews.ipynb
├── 📓 04_deepseek_generacion_oportunidades.ipynb
├── 📁 src/
│   └── 📁 utils/
│       └── 🐍 database.py
├── ⚙️ config.py
├── 📋 requirements.txt
├── 🔧 install.py
└── 📄 README.md

Base de Datos

Tabla Restaurantes
sql

id, nombre, direccion, telefono, posicion_ranking, tipo_cocina, rango_precio, tripadvisor_id, localizacion, email, latitud, longitud, website, rango_precio, platos, tripadvisor_web, fecha_insercion, fecha_actualizacion, fecha_escaneo_reviews, conteo_rating_1 conteo_rating_2, conteo_rating_3, conteo_rating_4, conteo_rating_5

Tabla Reviews
sql

id, restaurante_id, tripadvisor_id, review_id, titulo, contenido, rating, idioma, 
titulo_es, contenido_es, factores_queja, fecha_publicacion, fecha_experiencia, tipo_viaje, usuario, usuario_id, contribuciones_usuario, votos_utiles, respuesta_empresa, subratings, fotos, fecha_insercion

Tabla Oportunidades
sql

id, tripadvisor_id, reviews_utilizadas, problematicas_detectadas, 
oportunidades, fecha_insercion

🎮 Uso del Sistema
Ejemplo de Ejecución
python

# El sistema se ejecuta mediante notebooks Jupyter
# Cada notebook tiene celdas marcadas para ejecución secuencial

# 1. Configurar API keys en config.py
# 2. Ejecutar celdas en orden numerado
# 3. Ver resultados en la base de datos

Salidas del Sistema

    📊 Dashboard de Restaurantes

        328 restaurantes procesados

        278 críticas en español, 50 en otros idiomas

    📈 Análisis de Quejas

        20 categorías de problemas detectados

        Distribución por tipo de queja

    💼 Reportes de Oportunidades

        Oportunidades comerciales por establecimiento

        Propuestas específicas basadas en problemáticas reales

📈 Resultados y Métricas
Estadísticas del Sistema
Métrica	Valor	Descripción
🏪 Restaurantes	328	Total procesados
📝 Reviews	328+	Críticas analizadas
🌎 Idiomas	7	Soporte multidioma
🏷️ Categorías	20	Tipos de queja detectados
⏱️ Tiempo Procesamiento	~2s/review	Velocidad promedio

Categorías de Queja Detectadas

[
    "servicio_lento", "mal_servicio", "precio_elevado", "calidad_comida_mala",
    "comida_fria", "comida_poco_cocinada", "limpieza_mala", "ambiente_malo",
    "tiempo_espera_excesivo", "reservas_problemas", "bebidas_malas", 
    "ubicacion_mala", "ruido_excesivo", "espacio_insuficiente", 
    "presentacion_mala", "variedad_escasa", "cantidad_insuficiente",
    "horario_inadecuado", "staff_maleducado", "atencion_mesas_mala"
]

🔧 Tecnologías Utilizadas
🤖 Inteligencia Artificial

    DeepSeek API - Procesamiento de lenguaje natural

    Traducción automática - Soporte multidioma

    Clasificación de texto - Categorización de quejas

🕸️ Web Scraping

    Apify - Scraping estructurado de Tripadvisor

    Requests - Comunicación con APIs

💾 Almacenamiento de Datos

    SQLite3 - Base de datos relacional

    Pandas - Procesamiento y análisis de datos

📊 Análisis y Visualización

    Jupyter Notebooks - Desarrollo interactivo

    Python 3.8+ - Lenguaje de programación

🤝 Contribución

Las contribuciones son bienvenidas. Por favor:

    Fork el proyecto

    Crea una rama para tu feature (git checkout -b feature/AmazingFeature)

    Commit tus cambios (git commit -m 'Add some AmazingFeature')

    Push a la rama (git push origin feature/AmazingFeature)

    Abre un Pull Request

📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo LICENSE para detalles.
👥 Autor

Carlos Orellana - [TFM Master Data Science]
🙏 Agradecimientos

    DeepSeek por el acceso a su API de IA

    Apify por las herramientas de scraping

    Tripadvisor como fuente de datos (para uso académico)


¿Preguntas? ✉️ [carlosorellanamorales1986@gmail.com]
