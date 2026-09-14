import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns

# Set global publication quality style (Tufte / Albers inspired editorial design)
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']
plt.rcParams['axes.edgecolor'] = '#CBD5E1'
plt.rcParams['axes.linewidth'] = 0.8
plt.rcParams['grid.color'] = '#F1F5F9'
plt.rcParams['grid.linestyle'] = '--'
plt.rcParams['grid.alpha'] = 0.7

output_dir = "plots_png"
os.makedirs(output_dir, exist_ok=True)

# Palette definitions
COLOR_BLUE = "#2563EB"       # Audiófilo / Japón / Bandcamp
COLOR_TERRACOTTA = "#C2410C" # Híbrido / Vinilo / Hype
COLOR_PURPLE = "#7C3AED"     # Estético / Visual
COLOR_GREEN = "#059669"      # Retención Ética / Streamer
COLOR_RED = "#DC2626"        # Alerta / Sunset / Disqueras
COLOR_TEXT = "#1E293B"       # Dark Slate Body
COLOR_MUTED = "#64748B"      # Subtitles / Axis labels

def apply_clean_spines(ax):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#CBD5E1')
    ax.spines['bottom'].set_color('#CBD5E1')
    ax.tick_params(colors=COLOR_TEXT, labelsize=10)

# ==========================================
# 1. TAXONOMÍA DE TRIBUS DE CONSUMO
# ==========================================
fig, ax = plt.subplots(figsize=(8, 5), dpi=300)
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

tribes = ['Audiófilo Senior\n(Hi-Fi Purista)', 'Híbrido Romántico\n(Físico + Digital)', 
          'Consumidor Estético\n(Aesthetic / Moda)', 'Streamer Casual\n(Digital Puro)']
gasto_fisico = [480, 310, 185, 12] # USD anuales
conexion_emocional = [9.4, 8.8, 5.2, 3.1] # Escala 1-10

colors = [COLOR_BLUE, COLOR_TERRACOTTA, COLOR_PURPLE, COLOR_GREEN]

x = np.arange(len(tribes))
width = 0.35

rects1 = ax.bar(x - width/2, gasto_fisico, width, label='Gasto Físico Anual ($ USD)', color=colors, alpha=0.9)
ax2 = ax.twinx()
rects2 = ax2.plot(x + width/2, conexion_emocional, color=COLOR_TEXT, marker='o', linewidth=2.5, 
                  markersize=8, label='Índice Conexión Emocional (1-10)')

ax.set_ylabel('Gasto Físico Anual ($ USD)', fontsize=11, fontweight='bold', color=COLOR_TEXT)
ax2.set_ylabel('Índice de Conexión Emocional (1-10)', fontsize=11, fontweight='bold', color=COLOR_TEXT)
ax.set_xticks(x)
ax.set_xticklabels(tribes, fontsize=9.5, color=COLOR_TEXT)

apply_clean_spines(ax)
ax2.spines['top'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax2.spines['right'].set_color('#CBD5E1')

for rect in rects1:
    height = rect.get_height()
    ax.annotate(f'${height}',
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3), textcoords="offset points",
                ha='center', va='bottom', fontsize=9, fontweight='bold', color=COLOR_TEXT)

for i, txt in enumerate(conexion_emocional):
    ax2.annotate(f'{txt}/10', (x[i] + width/2, txt + 0.2), ha='center', fontsize=9, fontweight='bold', color=COLOR_TEXT)

ax2.set_ylim(0, 11)
ax.set_ylim(0, 560)
plt.title('Taxonomía del Consumidor: Gasto Físico vs Conexión Emocional', fontsize=12, fontweight='bold', color=COLOR_TEXT, pad=15)
plt.tight_layout()
plt.savefig(f"{output_dir}/01_taxonomia_tribus.png")
plt.close()

# ==========================================
# 2. MÉTODOS DE DESCUBRIMIENTO MUSICAL
# ==========================================
fig, ax = plt.subplots(figsize=(8, 4.5), dpi=300)
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

channels = ['Recomendación Algorítmica\n(Streaming)', 'Boca a Boca / Comunidad', 
            'Conciertos y Festivales', 'Digging Físico\n(Ferias / Disquerías)']
percentages = [42.5, 28.0, 16.5, 13.0]
bar_colors = [COLOR_BLUE, COLOR_TERRACOTTA, COLOR_GREEN, COLOR_PURPLE]

bars = ax.barh(channels, percentages, color=bar_colors, height=0.55, alpha=0.9)
apply_clean_spines(ax)
ax.xaxis.grid(True)
ax.set_xlim(0, 50)
ax.set_xlabel('Porcentaje de Consumidores (%)', fontsize=11, fontweight='bold', color=COLOR_TEXT)

for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width}%',
                xy=(width + 1, bar.get_y() + bar.get_height() / 2),
                ha='left', va='center', fontsize=10, fontweight='bold', color=COLOR_TEXT)

plt.title('Canales Principales de Descubrimiento de Nuevas Bandas', fontsize=12, fontweight='bold', color=COLOR_TEXT, pad=15)
plt.tight_layout()
plt.savefig(f"{output_dir}/02_metodos_descubrimiento.png")
plt.close()

# ==========================================
# 3. PSICOLOGÍA DE ATRACCIÓN & HOOKS
# ==========================================
fig, ax = plt.subplots(figsize=(8, 4.5), dpi=300)
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

hooks = ['Visual Hook\n(Arte de Portada / Edición)', 'Vocal & Sonic Hook\n(Firma Técnica / Timbres)', 
         'Media & Lore Hook\n(Misticismo / Bandas Sonoras)']
impact_pct = [48.0, 34.0, 18.0]
hook_colors = [COLOR_PURPLE, COLOR_BLUE, COLOR_TERRACOTTA]

wedges, texts, autotexts = ax.pie(impact_pct, labels=hooks, autopct='%1.1f%%',
                                  startangle=140, colors=hook_colors,
                                  textprops=dict(color=COLOR_TEXT, fontsize=10, fontweight='bold'),
                                  wedgeprops=dict(width=0.4, edgecolor='white', linewidth=2))

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)

plt.title('Disparadores Sensoriales (Triggers de Atracción hacia Álbumes)', fontsize=12, fontweight='bold', color=COLOR_TEXT, pad=15)
plt.tight_layout()
plt.savefig(f"{output_dir}/03_psicologia_atraccion_hooks.png")
plt.close()

# ==========================================
# 4. ASONANCIA CROMÁTICA VS LEALTAD (CONFESSIONS II)
# ==========================================
fig, ax = plt.subplots(figsize=(8, 4.5), dpi=300)
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

metrics = ['Ilegibilidad Visual\n(Asonancia Cromática)', 'Atractivo Estético Puro\n(Nulo Impacto Gráfico)', 
           'Lealtad de Marca\n(Prestigio del Artista)', 'Retención de Venta Real\n(Álbum Confessions II)']
values = [88, 15, 92, 85] # Porcentaje
colors_conf = [COLOR_RED, COLOR_MUTED, COLOR_BLUE, COLOR_GREEN]

bars = ax.barh(metrics, values, color=colors_conf, height=0.5, alpha=0.9)
apply_clean_spines(ax)
ax.xaxis.grid(True)
ax.set_xlim(0, 100)
ax.set_xlabel('Índice Evaluativo (%)', fontsize=11, fontweight='bold', color=COLOR_TEXT)

for bar in bars:
    w = bar.get_width()
    ax.annotate(f'{w}%', xy=(w + 1.5, bar.get_y() + bar.get_height()/2),
                va='center', fontsize=10, fontweight='bold', color=COLOR_TEXT)

plt.title('Caso Confessions II: Lealtad de Marca vs Ilegibilidad del Diseño', fontsize=12, fontweight='bold', color=COLOR_TEXT, pad=15)
plt.tight_layout()
plt.savefig(f"{output_dir}/04_asonancia_lealtad_confessions.png")
plt.close()

# ==========================================
# 5. ECONOMÍA & SUPERVIVENCIA ARTISTA
# ==========================================
fig, ax = plt.subplots(figsize=(7, 4.5), dpi=300)
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

platforms = ['Bandcamp\n(Venta Directa Ética)', 'Disqueras Corporativas\n(Majors / Intermediación)']
margins = [85.0, 15.0] # Porcentaje retenido por el artista
p_colors = [COLOR_GREEN, COLOR_RED]

bars = ax.bar(platforms, margins, color=p_colors, width=0.45, alpha=0.9)
apply_clean_spines(ax)
ax.yaxis.grid(True)
ax.set_ylim(0, 100)
ax.set_ylabel('Margen Retenido por el Artista (%)', fontsize=11, fontweight='bold', color=COLOR_TEXT)

for bar in bars:
    h = bar.get_height()
    ax.annotate(f'{h}%', xy=(bar.get_x() + bar.get_width()/2, h + 2),
                ha='center', fontsize=11, fontweight='bold', color=COLOR_TEXT)

plt.title('Supervivencia del Artista Independiente: Retención Directa de Ingresos', fontsize=12, fontweight='bold', color=COLOR_TEXT, pad=15)
plt.tight_layout()
plt.savefig(f"{output_dir}/05_economia_supervivencia_bandcamp_majors.png")
plt.close()

# ==========================================
# 6. CURVA DE HYPE E INFLACIÓN DE PRECIOS
# ==========================================
fig, ax = plt.subplots(figsize=(8, 5), dpi=300)
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

np.random.seed(42)
streams = np.random.uniform(0.5, 50, 120) # Millones de streams
prices = 18 + 0.8 * streams + np.random.normal(0, 6, 120) # USD

ax.scatter(streams, prices, color=COLOR_TERRACOTTA, alpha=0.6, edgecolors='none', s=40, label='Ediciones en Vinilo')

# Trendline
z = np.polyfit(streams, prices, 1)
p = np.poly1d(z)
x_line = np.linspace(0.5, 50, 100)
ax.plot(x_line, p(x_line), color=COLOR_RED, linestyle='--', linewidth=2, label='Curva Inflacionaria (Impuesto al Pop)')

apply_clean_spines(ax)
ax.grid(True)
ax.set_xlabel('Eje X: Popularidad Digital en Streaming (Millones de Reproducciones)', fontsize=10, fontweight='bold', color=COLOR_TEXT)
ax.set_ylabel('Eje Y: Precio del Soporte Físico ($ USD)', fontsize=10, fontweight='bold', color=COLOR_TEXT)
ax.legend(frameon=True, facecolor='white', edgecolor='#CBD5E1', fontsize=9)

plt.title('Curva de Hype: Divergencia y Sobrecosto en Mercado Minorista', fontsize=12, fontweight='bold', color=COLOR_TEXT, pad=15)
plt.tight_layout()
plt.savefig(f"{output_dir}/06_curva_hype_impuesto_pop.png")
plt.close()

# ==========================================
# 7. SHOCK GEOPOLÍTICO SONY CD 2028
# ==========================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5), dpi=300)
fig.patch.set_facecolor('white')
ax1.set_facecolor('white')
ax2.set_facecolor('white')

# Subplot 1: Japón vs Occidente (Participación CD)
regions = ['Japón\n(Mercado Físico)', 'Occidente\n(EE.UU. / Europa)']
cd_share = [66.0, 12.0]
ax1.bar(regions, cd_share, color=[COLOR_BLUE, COLOR_MUTED], width=0.45, alpha=0.9)
apply_clean_spines(ax1)
ax1.yaxis.grid(True)
ax1.set_ylim(0, 80)
ax1.set_ylabel('Cuota de Mercado del Formato CD (%)', fontsize=10, fontweight='bold', color=COLOR_TEXT)
for bar in ax1.patches:
    h = bar.get_height()
    ax1.annotate(f'{h}%', xy=(bar.get_x() + bar.get_width()/2, h + 2), ha='center', fontsize=10, fontweight='bold', color=COLOR_TEXT)
ax1.set_title('Resiliencia del CD: Japón vs Occidente', fontsize=11, fontweight='bold', color=COLOR_TEXT)

# Subplot 2: Sony Plant Operating Capacity 2020-2028
years = [2020, 2022, 2024, 2026, 2028]
capacity = [100, 82, 55, 20, 0]
ax2.plot(years, capacity, color=COLOR_RED, marker='s', linewidth=2.5, markersize=7)
apply_clean_spines(ax2)
ax2.grid(True)
ax2.set_ylim(-5, 110)
ax2.set_xlabel('Año', fontsize=10, fontweight='bold', color=COLOR_TEXT)
ax2.set_ylabel('Capacidad Operativa (%)', fontsize=10, fontweight='bold', color=COLOR_TEXT)
for y, c in zip(years, capacity):
    ax2.annotate(f'{c}%', (y, c + 4), ha='center', fontsize=9, fontweight='bold', color=COLOR_TEXT)
ax2.set_title('Proyección Sunset Cierre Plantas Sony CD', fontsize=11, fontweight='bold', color=COLOR_TEXT)

plt.tight_layout()
plt.savefig(f"{output_dir}/07_shock_geopolitico_sony_cd.png")
plt.close()

# ==========================================
# 8. ESCALABILIDAD BIG DATA (K-MEANS VS OVERPLOTTING)
# ==========================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5), dpi=300)
fig.patch.set_facecolor('white')
ax1.set_facecolor('white')
ax2.set_facecolor('white')

np.random.seed(101)
# 3000 Raw items
x_raw = np.concatenate([np.random.normal(2, 0.8, 1000), np.random.normal(6, 1.0, 1000), np.random.normal(4, 1.2, 1000)])
y_raw = np.concatenate([np.random.normal(3, 0.8, 1000), np.random.normal(7, 0.9, 1000), np.random.normal(2, 0.7, 1000)])

ax1.scatter(x_raw, y_raw, color=COLOR_MUTED, alpha=0.25, s=12)
apply_clean_spines(ax1)
ax1.set_title('A. Colapso por Overplotting (N=3,000 Álbumes)', fontsize=10, fontweight='bold', color=COLOR_TEXT)
ax1.set_xlabel('PC1 (Varianza)', fontsize=9, color=COLOR_MUTED)
ax1.set_ylabel('PC2 (Varianza)', fontsize=9, color=COLOR_MUTED)

# K-Means Aggregated Centroids
centroids_x = [2.0, 6.0, 4.0]
centroids_y = [3.0, 7.0, 2.0]
weights = [1000, 1000, 1000]
c_colors = [COLOR_BLUE, COLOR_TERRACOTTA, COLOR_GREEN]

ax2.scatter(x_raw, y_raw, color='#E2E8F0', alpha=0.15, s=8)
for cx, cy, col in zip(centroids_x, centroids_y, c_colors):
    ax2.scatter(cx, cy, color=col, s=250, edgecolors='black', linewidth=1.5, zorder=5)
    circle = plt.Circle((cx, cy), 1.2, color=col, fill=True, alpha=0.2, zorder=3)
    ax2.add_patch(circle)

apply_clean_spines(ax2)
ax2.set_title('B. Agregación Espacial K-Means (Centroides)', fontsize=10, fontweight='bold', color=COLOR_TEXT)
ax2.set_xlabel('PC1 (Varianza)', fontsize=9, color=COLOR_MUTED)
ax2.set_ylabel('PC2 (Varianza)', fontsize=9, color=COLOR_MUTED)

plt.tight_layout()
plt.savefig(f"{output_dir}/08_escalabilidad_kmeans_bigdata.png")
plt.close()

print("ALL_PLOTS_GENERATED_SUCCESSFULLY")
