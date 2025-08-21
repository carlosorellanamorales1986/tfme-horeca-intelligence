# TFM - HORECA Intelligence

Sistema de identificación de oportunidades comerciales para distribuidores HORECA mediante análisis de críticas negativas en restaurantes de Tripadvisor.

## Objetivo

Este proyecto desarrolla un pipeline de data mining para generar leads comerciales cualificados analizando las causas raíz de las críticas negativas en restaurantes de Girona (puestos 120-240 en Tripadvisor).

## Estructura del Proyecto

tfme-horeca-intelligence/
├── data/ # Datos
│ ├── raw/ # Datos sin procesar (no se sube a Git)
│ └── processed/ # Datos procesados (no se sube a Git)
├── docs/ # Memoria y documentación
├── src/ # Código fuente
│ ├── utils/ # Funciones auxiliares
│ ├── scrape_restaurants.py
│ ├── scrape_reviews.py
│ └── enrich_reviews.py
├── README.md
└── requirements.txt


## Instalación

1. Clona el repositorio:
git clone https://github.com/<tu_usuario>/tfme-horeca-intelligence.git

2. Instala las dependencias
pip install -r requirements.txt

## Uso
El pipeline se ejecuta en 3 pasos:

    1. Scraping de metadatos de restaurantes:
    python src/scrape_restaurants.py

    2. Scraping de reviews:
    python src/scrape_reviews.py

    3. Enriquecimiento con LLM:
    python src/enrich_reviews.py

## Resultados

Los datasets finales se generan en data/processed/:

    restaurantes_girona.csv
    reviews_negativas_enriquecidas.csv

## Herramientas

    Python 3.10
    Selenium & undetected-chromedriver
    Pandas
    DeepSeek API

## Contacto

Carlos Orellana - carlosorellanamorales1986@gmail.com