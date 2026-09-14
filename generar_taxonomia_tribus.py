import os
import shutil
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------
# 1. GENERACIÓN DEL DATASET SINTÉTICO (5,000 PERFILES DE CONSUMO)
# ------------------------------------------------------------------------------
np.random.seed(42)
n_usuarios = 5000
regiones = ["Japón", "Norteamérica", "Europa", "Latinoamérica", "Resto del Mundo"]
prob_regiones = [0.15, 0.35, 0.30, 0.12, 0.08]

usuarios_data = []
for i in range(n_usuarios):
    region = np.random.choice(regiones, p=prob_regiones)
    rand_tribu = np.random.rand()

    if rand_tribu < 0.30:
        tribu = "Audiófilo Senior"
        edad = np.random.normal(55, 8)
        gasto_streaming = np.random.normal(10, 3)
        gasto_vinilos = np.random.normal(110, 20) if region in ["Japón", "Europa"] else np.random.normal(85, 15)
        gasto_cds = np.random.normal(60, 15) if region == "Japón" else np.random.normal(25, 10)
        gasto_cassettes = np.random.normal(10, 3)
        compras_bandcamp = np.random.normal(8, 3)
        conexion_emocional = np.random.normal(9, 0.8)
        fidelidad_equipo = 2
    elif rand_tribu < 0.55:
        tribu = "Híbrido Romántico"
        edad = np.random.normal(25, 4)
        gasto_streaming = np.random.normal(15, 2)
        gasto_vinilos = np.random.normal(50, 12)
        gasto_cds = np.random.normal(10, 4)
        gasto_cassettes = np.random.normal(25, 6) if region == "Europa" else np.random.normal(15, 5)
        compras_bandcamp = np.random.normal(12, 4)
        conexion_emocional = np.random.normal(8.5, 0.9)
        fidelidad_equipo = np.random.choice([1, 2], p=[0.70, 0.30])
    elif rand_tribu < 0.75:
        tribu = "Consumidor Estético"
        edad = np.random.normal(21, 3)
        gasto_streaming = np.random.normal(15, 1.5)
        gasto_vinilos = np.random.normal(40, 10)
        gasto_cds = np.random.normal(2, 1)
        gasto_cassettes = np.random.normal(12, 4)
        compras_bandcamp = np.random.normal(2, 1)
        conexion_emocional = np.random.normal(5, 1.2)
        fidelidad_equipo = 0
    else:
        tribu = "Streamer Casual"
        edad = np.random.normal(32, 10)
        gasto_streaming = np.random.normal(22, 3)
        gasto_vinilos = np.random.normal(1, 1)
        gasto_cds = np.random.normal(1, 1)
        gasto_cassettes = 0
        compras_bandcamp = 0
        conexion_emocional = np.random.normal(2, 1.0)
        fidelidad_equipo = 1

    usuarios_data.append({
        "edad": np.clip(int(edad), 18, 75),
        "region": region,
        "gasto_streaming": max(0, gasto_streaming),
        "gasto_vinilos": max(0, gasto_vinilos),
        "gasto_cds": max(0, gasto_cds),
        "gasto_cassettes": max(0, gasto_cassettes),
        "compras_bandcamp": max(0, compras_bandcamp),
        "fidelidad_equipo": fidelidad_equipo,
        "conexion_emocional": np.clip(conexion_emocional, 1, 10),
        "tribu_real": tribu
    })

df_usuarios = pd.DataFrame(usuarios_data)

# Configuración de Paleta Cromática Exacta del Notebook
colores_tribu = {
    "Audiófilo Senior": "#E76F51",    # Terracota
    "Híbrido Romántico": "#E9C46A",   # Ámbar
    "Consumidor Estético": "#F4A261", # Coral
    "Streamer Casual": "#264653"     # Azul/Teal
}

output_dir = "taxonomy_export"
os.makedirs(output_dir, exist_ok=False)

# ------------------------------------------------------------------------------
# 2. GRÁFICO 1: STAR GLYPHS - MATRIZ DIAGNÓSTICA 2X2 (DIAPOSITIVA SLIDE 4)
# ------------------------------------------------------------------------------
radar_features = ["gasto_streaming", "gasto_vinilos", "gasto_cds", "gasto_cassettes", "compras_bandcamp", "conexion_emocional"]
labels = ["Gasto\nStreaming", "Gasto\nVinilos", "Gasto\nCDs", "Gasto\nCassettes", "Compras\nBandcamp", "Conexión\nEmocional"]
num_vars = len(radar_features)

df_radar_data = df_usuarios.copy()
for col in radar_features:
    min_v = df_radar_data[col].min()
    max_v = df_radar_data[col].max()
    df_radar_data[col] = (df_radar_data[col] - min_v) / (max_v - min_v) if max_v > min_v else 0

angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, axes = plt.subplots(2, 2, figsize=(12, 10.5), subplot_kw=dict(polar=True), dpi=300)
fig.patch.set_facecolor('#0F172A')

tribus_grid = [
    ("Audiófilo Senior", 0, 0, "Alta fidelidad, gasto masivo en vinilos,\ndescubrimiento en disquerías físicas."),
    ("Híbrido Romántico", 0, 1, "Altísimo apego emocional, apoyo en Bandcamp,\ndescubre en digital pero compra en físico."),
    ("Consumidor Estético", 1, 0, "Tocadiscos de maletín, música como objeto de moda,\nalta compra de vinilos por estética."),
    ("Streamer Casual", 1, 1, "Nula conexión con formatos físicos,\nportabilidad total, inmediatez algorítmica.")
]

for tribu, r, c, desc in tribus_grid:
    ax = axes[r, c]
    ax.set_facecolor('#1E293B')
    color = colores_tribu[tribu]
    values = df_radar_data[df_radar_data["tribu_real"] == tribu][radar_features].median().tolist()
    values += values[:1]
    
    ax.plot(angles, values, color=color, linewidth=2.8)
    ax.fill(angles, values, color=color, alpha=0.35)
    
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, color='#E2E8F0', fontsize=8.5, fontweight='bold')
    ax.tick_params(colors='#64748B', labelsize=7)
    ax.grid(color='#334155', linestyle='--', linewidth=0.7)
    ax.spines['polar'].set_color('#475569')
    ax.set_ylim(0, 1)
    
    ax.set_title(tribu, color=color, fontsize=15, fontweight='bold', pad=15)
    ax.text(0.5, -0.22, desc, transform=ax.transAxes, ha='center', va='top', color='#94A3B8', fontsize=8.5, style='italic')

plt.suptitle("Matriz Diagnóstica de las Cuatro Tribus de Consumo", color='#F8FAFC', fontsize=18, fontweight='bold', y=0.98)
plt.tight_layout()
plt.subplots_adjust(hspace=0.45, wspace=0.35, top=0.90)
plt.savefig(f"{output_dir}/01_taxonomia_matriz_2x2_tribus.png", facecolor='#0F172A', bbox_inches='tight')
plt.close()

# ------------------------------------------------------------------------------
# 3. GRÁFICO 2: PCA GLYPH PLOT (MAPPING BERTIN - EN PLANO REDUCIDO)
# ------------------------------------------------------------------------------
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

feature_cols = ["edad", "gasto_streaming", "gasto_vinilos", "gasto_cds", "gasto_cassettes", "compras_bandcamp", "fidelidad_equipo", "conexion_emocional"]
X_scaled = StandardScaler().fit_transform(df_usuarios[feature_cols])
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
df_usuarios["pca_1"] = X_pca[:, 0]
df_usuarios["pca_2"] = X_pca[:, 1]

df_sample = df_usuarios.sample(400, random_state=42).copy()

fig, ax = plt.subplots(figsize=(11, 6), dpi=300)
fig.patch.set_facecolor('#0F172A')
ax.set_facecolor('#1E293B')

shape_map = {0: 'o', 1: 's', 2: 'D'} # 0=Maletín(Círculo), 1=Standard(Cuadrado), 2=HiFi(Diamante)

for tribu, color in colores_tribu.items():
    df_sub = df_sample[df_sample["tribu_real"] == tribu]
    for eq_val, shape in shape_map.items():
        df_sub_eq = df_sub[df_sub["fidelidad_equipo"] == eq_val]
        if len(df_sub_eq) > 0:
            sizes = df_sub_eq["conexion_emocional"] * 18
            ax.scatter(
                df_sub_eq["pca_1"], df_sub_eq["pca_2"],
                c=color, marker=shape, s=sizes, alpha=0.75,
                edgecolors='#0F172A', linewidths=0.5
            )

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#334155')
ax.spines['bottom'].set_color('#334155')
ax.tick_params(colors='#94A3B8', labelsize=9)
ax.grid(color='#334155', linestyle='--', linewidth=0.5, alpha=0.7)

ax.set_xlabel("Componente Principal 1 (PC1 - Varianza Explicada)", color='#F8FAFC', fontsize=11, fontweight='bold')
ax.set_ylabel("Componente Principal 2 (PC2)", color='#F8FAFC', fontsize=11, fontweight='bold')
ax.set_title("PCA Glyph Plot: Identificando Tribus en el Ruido Multidimensional", color='#F8FAFC', fontsize=15, fontweight='bold', pad=15)

# Leyendas personalizadas
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], marker='o', color='w', label='Audiófilo Senior', markerfacecolor='#E76F51', markersize=9),
    Line2D([0], [0], marker='o', color='w', label='Híbrido Romántico', markerfacecolor='#E9C46A', markersize=9),
    Line2D([0], [0], marker='o', color='w', label='Consumidor Estético', markerfacecolor='#F4A261', markersize=9),
    Line2D([0], [0], marker='o', color='w', label='Streamer Casual', markerfacecolor='#264653', markersize=9),
    Line2D([0], [0], color='w', label='---'),
    Line2D([0], [0], marker='o', color='w', label='Círculo: Maletín / Casual', markerfacecolor='#94A3B8', markersize=8),
    Line2D([0], [0], marker='s', color='w', label='Cuadrado: Equipo Estándar', markerfacecolor='#94A3B8', markersize=8),
    Line2D([0], [0], marker='D', color='w', label='Diamante: Hi-Fi Dedicado', markerfacecolor='#94A3B8', markersize=8)
]
leg = ax.legend(handles=legend_elements, loc='upper left', frameon=True, facecolor='#0F172A', edgecolor='#334155', fontsize=8.5)
for text in leg.get_texts():
    text.set_color('#F8FAFC')

plt.tight_layout()
plt.savefig(f"{output_dir}/02_taxonomia_pca_glyph_plot.png", facecolor='#0F172A', bbox_inches='tight')
plt.close()

# ------------------------------------------------------------------------------
# 4. GRÁFICO 3: COMPOSICIÓN DE MERCADO LOCAL POR REGIÓN CULTURAL
# ------------------------------------------------------------------------------
df_region = df_usuarios.groupby(["region", "tribu_real"]).size().unstack(fill_value=0)
df_region_pct = df_region.div(df_region.sum(axis=1), axis=0) * 100

fig, ax = plt.subplots(figsize=(10, 5), dpi=300)
fig.patch.set_facecolor('#0F172A')
ax.set_facecolor('#1E293B')

order_tribus = ["Audiófilo Senior", "Híbrido Romántico", "Consumidor Estético", "Streamer Casual"]
df_region_pct = df_region_pct[order_tribus]

bottom = np.zeros(len(df_region_pct))
for tribu in order_tribus:
    values = df_region_pct[tribu].values
    ax.barh(df_region_pct.index, values, left=bottom, label=tribu, color=colores_tribu[tribu], height=0.55)
    bottom += values

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#334155')
ax.spines['bottom'].set_color('#334155')
ax.tick_params(colors='#F8FAFC', labelsize=10)
ax.xaxis.grid(True, color='#334155', linestyle='--', linewidth=0.5)

ax.set_xlabel("Porcentaje del Mercado Local (%)", color='#F8FAFC', fontsize=11, fontweight='bold')
ax.set_ylabel("Región Cultural", color='#F8FAFC', fontsize=11, fontweight='bold')
ax.set_title("Composición Generacional y de Consumo por Región Cultural", color='#F8FAFC', fontsize=15, fontweight='bold', pad=15)

leg = ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.18), ncol=4, frameon=False)
for text in leg.get_texts():
    text.set_color('#F8FAFC')
    text.set_fontsize(9.5)

plt.tight_layout()
plt.savefig(f"{output_dir}/03_taxonomia_composicion_region.png", facecolor='#0F172A', bbox_inches='tight')
plt.close()

print("ALL_TAXONOMY_PLOTS_GENERATED_SUCCESSFULLY")
