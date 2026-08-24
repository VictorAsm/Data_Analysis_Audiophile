# 🎧 Visual Analytics de la Melomanía: El Ecosistema del Consumo Analógico y la Supervivencia del Artista

Este proyecto presenta un pipeline analítico y visual interactivo de extremo a extremo que estudia las dinámicas de consumo musical contemporáneas, abarcando desde la **tensión generacional en la era del renacimiento físico** hasta el **impacto socioeconómico directo sobre la supervivencia del creador de música**. 

A través del modelado matemático y un robusto diseño de información, demostramos cómo el fenómeno del "hype" estético, las asimetrías geopolíticas de manufactura y decisiones de la industria (como el cese de producción de CDs de Sony para 2028) afectan de manera dispar a artistas independientes, de nivel medio y multinacionales.

---

## 📐 Framework de Diseño de Información (Tamara Munzner)

Para asegurar el rigor científico del proyecto, las visualizaciones fueron construidas bajo el framework de cinco niveles de Tamara Munzner:

### 1. ¿Por qué se visualiza? (Why: Motivación y Tareas)
*   **Motivación:** El streaming democratizó el alcance masivo pero precarizó críticamente el ingreso del artista. En paralelo, el soporte físico (vinilo, cassette, CD) experimenta un resurgimiento impulsado por la moda visual antes que por la calidad de audio, deformando la cadena de valor.
*   **Tareas de Análisis Visual:**
    *   **Identificar y Clasificar:** Segmentar la audiencia general en tribus de melómanos según su firma psicográfica y demográfica.
    *   **Exponer la Distorsión:** Analizar la burbuja de precios inflada por la demanda estética en formatos físicos.
    *   **Trazar el Flujo de Sostén:** Mapear cómo la psicología de atracción inicial (portadas, *lore*, sonido) se traduce en decisiones éticas de compra directa (Bandcamp) que sostienen las carreras de creadores pequeños frente a las grandes disqueras (*Majors*).

### 2. ¿Qué se visualiza? (What: Descripción del Dataset)
El pipeline procesa tres conjuntos de datos enriquecidos:
*   **Dataset de Consumidores ($N=5,000$):** Perfiles multivariados que registran variables demográficas (edad, región) y cuantitativas de gasto físico por formato, volumen de streaming, uso de plataformas de apoyo (Bandcamp), nivel de equipamiento técnico y escala afectiva de conexión emocional.
*   **Catálogo Comercial ($N=300$):** Álbumes de vinilo, CD y cassette lanzados por artistas reales, cruzando su volumen de popularidad en streaming con su demanda estética y sus fluctuaciones asimétricas de precio en el mercado minorista.
*   **Censo de Creadores ($N=30$):** Perfiles de artistas segmentados por tres polos geográficos (Japón, EE.UU., Europa) y cuatro estratos de la industria (Megastar, Rising Star, Mid-Tier, Indie Puro en Bandcamp) para medir sus costos logísticos y su vulnerabilidad financiera.

### 3. ¿Para quién? (To Whom & Context)
Visualizaciones pensadas para **analistas de la industria musical, managers culturales, investigadores de la sociología del consumo y artistas independientes** en su búsqueda de viabilidad de auto-gestión física y digital.

### 4. ¿Cómo? (How: Justificación de Elecciones de Diseño Visual)
*   **Semiótica de Jacques Bertin:** El *PCA Glyph Plot* utiliza posición espacial (PC1 y PC2) para proyectar similitudes demográficas, color para identificar cualitativamente la tribu, tamaño para codificar la conexión emocional y forma de marcador para el nivel de equipamiento técnico, maximizando el canal perceptivo en un solo plano.
*   **Interacción del Color de Josef Albers:** El *Diagrama de Sankey* aplica transiciones en canales RGBA con opacidades suaves (15% a 30%) que se corresponden con el color afectivo de la cohorte de destino, eliminando el "efecto espagueti" y guiando el ojo del lector sin fatiga.
*   **Maximización del Data-to-Ink Ratio (Edward Tufte):** El gráfico de barras geográficas y el gráfico de barras del *Shock CD Sony 2028* han sido desprovistos de bordes decorativos, grillas redundantes y ruido estético para asegurar que los datos hablen por sí mismos con un alto contraste sobre fondo oscuro.
*   **Evitar Saturación y Hairball:** Sustituimos el clásico gráfico de Categorías Paralelas en la Sección de Psicología del Melómano por un **Sunburst Chart concéntrico e interactivo** que organiza radialmente el flujo multidimensional sin solapamiento de líneas.

---

## 🎨 Galería de Casos de Estudio Reales Incorporados

El Jupyter Notebook cuenta con un análisis crítico-editorial apoyado por una galería interactiva en HTML que renderiza las portadas de los siguientes álbumes:

*   **Ado (*Kyogen*):** El magnetismo de las portadas ilustradas con estética anime oscura como imán de adquisición física inmediato para nuevas generaciones.
*   **Gorillaz (*Demon Days*):** El paralelismo histórico y visual con el mítico retrato a cuatro sombras de *With The Beatles*.
*   **Ariana Grande (*eternal sunshine*):** Simpleza visual, estética limpia y demostración de rango de firma vocal que consagra la fidelidad del oyente.
*   **Linkin Park (*Hybrid Theory*):** El descubrimiento de bandas a través de medios transmedia (bandas sonoras en el cine como *Transformers*).
*   **Mayhem (*De Mysteriis Dom Sathanas*):** El morbo y el coleccionismo físico alimentados por el misterio y el trágico *lore* (historia interna) de la escena extrema noruega.
*   **La Paradoja de Madonna (*Confessions on a Dance Floor*):** Análisis de **Asonancia Cromática Extrema y Lealtad de Marca**. Demostramos cómo la inmensa fama y prestigio de Madonna logran anular un diseño cromático sofocante de nula legibilidad visual (letras rojas sobre vinilo rosa saturado), convalidando la compra de todos modos.

---

## 📂 Catálogo de Visualizaciones Exportadas (`/plots`)

Todos los gráficos dinámicos han sido exportados como archivos `.html` interactivos que conservan las animaciones, linked brushing y filtros al abrirse en cualquier navegador. Las gráficas estáticas se exportaron en `.png` de alta definición:

1.  `fig_01_coordenadas_paralelas.html`: Mapa multidimensional de densidad de flujos de gasto.
2.  `fig_02_pca_glyp_plot.html`: Proyección en el espacio reducido de las variables de Bertin.
3.  `fig_03_sankey_flow.html`: Transiciones afectivas de descubrimiento y motivación (RGBA).
4.  `fig_04_radar_glyphs.html`: Huellas dactilares polares y comparativas de cada tribu de consumo.
5.  `fig_05_composicion_regional.png`: Distribución de mercados locales limpia al estilo Edward Tufte.
6.  `fig_06_burbuja_precios_box.html`: Box plots interactivos que exponen la inflación en el soporte físico.
7.  `fig_07_curva_hype_scatter.html`: Dispersión de la demanda estéticamente inflada frente al streaming.
8.  `fig_08_matriz_supervivencia_artistas.html`: El rol protector de Bandcamp frente a intermediarios corporativos.
9.  `fig_09_shock_cd_sony.html`: El impacto financiero regional ante la muerte definitiva del CD en 2028.
10. `fig_10_triggers_sunburst.html`: El flujo psicográfico concéntrico de disparadores sensoriales.

---

## 🚀 Instrucciones de Ejecución

El repositorio incluye dos utilitarios de Python automatizados para reconstruir el entorno localmente de forma inmediata:

Este proyecto fue desarrollado en el marco de la Winter School de Visual Analytics como trabajo final de graduación de excelencia técnica y teórica.
***
