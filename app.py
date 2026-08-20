import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# ==========================================
# 1. GENERACIÓN DEL DATASET ROBUSTO (N=5000)
# ==========================================
np.random.seed(42)
n_usuarios = 5000
regiones = ["Japón", "Norteamérica", "Europa", "Latinoamérica", "Resto del Mundo"]
prob_regiones = [0.15, 0.35, 0.30, 0.12, 0.08]

usuarios_data = []
for i in range(n_usuarios):
    region = np.random.choice(regiones, p=prob_regiones)
    rand_tribu = np.random.rand()
    
    if rand_tribu < 0.30: # Audiófilo Senior
        edad = np.random.normal(55, 8)
        gasto_streaming = np.random.normal(10, 3)
        gasto_vinilos = np.random.normal(110, 20) if region in ["Japón", "Europa"] else np.random.normal(85, 15)
        gasto_cds = np.random.normal(60, 15) if region == "Japón" else np.random.normal(25, 10)
        gasto_cassettes = np.random.normal(10, 3)
        cant_vinilos = np.random.normal(190, 45)
        cant_cds = np.random.normal(150, 35)
        cant_cassettes = np.random.normal(20, 8)
        fidelidad_equipo = 2  # Hi-Fi
        conexion_emocional = np.random.normal(9, 0.8)
        compras_bandcamp = np.random.normal(8, 3)
        descubrimiento = np.random.choice(["Digging en Disquerías", "Recomendación boca a boca", "Radio y Medios"], p=[0.50, 0.35, 0.15])
        motivacion = "Disfrute Melómano / Calidad"
        tribu = "Audiófilo Senior"
    elif rand_tribu < 0.55: # Híbrido Romántico
        edad = np.random.normal(25, 4)
        gasto_streaming = np.random.normal(15, 2)
        gasto_vinilos = np.random.normal(50, 12)
        gasto_cds = np.random.normal(10, 4)
        gasto_cassettes = np.random.normal(25, 6) if region == "Europa" else np.random.normal(15, 5)
        cant_vinilos = np.random.normal(35, 12)
        cant_cds = np.random.normal(15, 6)
        cant_cassettes = np.random.normal(25, 10)
        fidelidad_equipo = np.random.choice([1, 2], p=[0.70, 0.30])
        conexion_emocional = np.random.normal(8.5, 0.9)
        compras_bandcamp = np.random.normal(12, 4)
        descubrimiento = "Algoritmos de Streaming"
        motivacion = "Disfrute Melómano / Calidad"
        tribu = "Híbrido Romántico"
    elif rand_tribu < 0.75: # Consumidor Estético
        edad = np.random.normal(21, 3)
        gasto_streaming = np.random.normal(15, 1.5)
        gasto_vinilos = np.random.normal(40, 10)
        gasto_cds = np.random.normal(2, 1)
        gasto_cassettes = np.random.normal(12, 4)
        cant_vinilos = np.random.normal(15, 5)
        cant_cds = np.random.normal(2, 1)
        cant_cassettes = np.random.normal(8, 3)
        fidelidad_equipo = 0  # Maletín
        conexion_emocional = np.random.normal(5, 1.2)
        compras_bandcamp = np.random.normal(2, 1)
        descubrimiento = np.random.choice(["Algoritmos de Streaming", "Recomendación boca a boca"], p=[0.80, 0.20])
        motivacion = "Estética / Moda (Aesthetic)"
        tribu = "Consumidor Estético"
    else: # Streamer Casual
        edad = np.random.normal(32, 10)
        gasto_streaming = np.random.normal(22, 3)
        gasto_vinilos = np.random.normal(1, 1)
        gasto_cds = np.random.normal(1, 1)
        gasto_cassettes = 0
        cant_vinilos = 0
        cant_cds = np.random.normal(1, 1)
        cant_cassettes = 0
        fidelidad_equipo = 1  # Estándar
        conexion_emocional = np.random.normal(2, 1.0)
        compras_bandcamp = 0
        descubrimiento = "Algoritmos de Streaming"
        motivacion = "Conveniencia / Inmediatez"
        tribu = "Streamer Casual"
        
    edad = np.clip(int(edad), 18, 75)
    gasto_streaming = max(0, gasto_streaming)
    gasto_vinilos = max(0, gasto_vinilos)
    gasto_cds = max(0, gasto_cds)
    gasto_cassettes = max(0, gasto_cassettes)
    cant_vinilos = max(0, int(cant_vinilos))
    cant_cds = max(0, int(cant_cds))
    cant_cassettes = max(0, int(cant_cassettes))
    compras_bandcamp = max(0, int(compras_bandcamp))
    conexion_emocional = np.clip(conexion_emocional, 1, 10)
    
    usuarios_data.append({
        "edad": edad, "region": region, "gasto_streaming": gasto_streaming,
        "gasto_vinilos": gasto_vinilos, "gasto_cds": gasto_cds, "gasto_cassettes": gasto_cassettes,
        "cant_vinilos": cant_vinilos, "cant_cds": cant_cds, "cant_cassettes": cant_cassettes,
        "compras_bandcamp": compras_bandcamp, "fidelidad_equipo": fidelidad_equipo,
        "conexion_emocional": conexion_emocional, "descubrimiento": descubrimiento,
        "motivacion": motivacion, "gasto_fisico_total": gasto_vinilos + gasto_cds + gasto_cassettes,
        "tribu_real": tribu
    })

df_usuarios = pd.DataFrame(usuarios_data)

# Pre-computamos el espacio PCA para que las coordenadas espaciales queden estables (Focus+Context)
feature_cols = ["edad", "gasto_streaming", "gasto_vinilos", "gasto_cds", "gasto_cassettes", 
                "cant_vinilos", "cant_cds", "cant_cassettes", "compras_bandcamp", "fidelidad_equipo", "conexion_emocional"]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df_usuarios[feature_cols])
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
df_usuarios["pca_1"] = X_pca[:, 0]
df_usuarios["pca_2"] = X_pca[:, 1]
df_usuarios["cluster"] = df_usuarios["tribu_real"].map({"Audiófilo Senior": 0, "Híbrido Romántico": 1, "Consumidor Estético": 2, "Streamer Casual": 3})

# Configuración estática de nodos de Sankey
ALL_SANKEY_NODES = [
    "Jóvenes (<30 años)", "Adultos Medios (30-45)", "Adultos Mayores (>45)",
    "Digging en Disquerías", "Recomendación boca a boca", "Radio y Medios", "Algoritmos de Streaming",
    "Disfrute Melómano / Calidad", "Estética / Moda (Aesthetic)", "Conveniencia / Inmediatez",
    "Audiófilo Senior", "Híbrido Romántico", "Consumidor Estético", "Streamer Casual"
]
NODE_MAP = {node: i for i, node in enumerate(ALL_SANKEY_NODES)}

# Colores del tema Albers Afectivos
colores_tribu = {
    "Audiófilo Senior": "#E76F51",      # Terracota
    "Híbrido Romántico": "#E9C46A",     # Ámbar/Oro viejo
    "Consumidor Estético": "#F4A261",    # Coral
    "Streamer Casual": "#264653"         # Azul calma
}

# ==========================================
# 2. INICIALIZACIÓN DE LA APP (TEMA CYBORG)
# ==========================================
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

app.layout = dbc.Container([
    # Banner Principal
    dbc.Row([
        dbc.Col(html.Div([
            html.H1("MELOMANÍA VISUAL ANALYTICS", className="text-center mt-4 mb-1 text-primary font-weight-bold"),
            html.H5("Análisis de Tensión Generacional, Conexión Emocional y Consumo de Música", className="text-center text-muted mb-4")
        ]), width=12)
    ]),
    
    # Panel de Filtros Laterales e Info
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("FILTROS ANALÍTICOS (Interacción en Tiempo Real)", className="font-weight-bold text-success"),
                dbc.CardBody([
                    # Filtro de Región
                    html.Label("Región Cultural:", className="font-weight-bold text-light mt-2"),
                    dcc.Dropdown(
                        id="region-filter",
                        options=[{"label": r, "value": r} for r in regiones] + [{"label": "Todas las regiones", "value": "Todas"}],
                        value="Todas",
                        clearable=False,
                        className="text-dark"
                    ),
                    
                    # Filtro de Edad
                    html.Label("Rango de Edad:", className="font-weight-bold text-light mt-4"),
                    dcc.RangeSlider(
                        id="edad-filter",
                        min=18, max=75, step=1,
                        value=[18, 75],
                        marks={18: '18a', 30: '30a', 45: '45a', 60: '60a', 75: '75a'},
                        tooltip={"always_visible": True, "placement": "bottom"}
                    ),
                    
                    # Filtro de Emoción
                    html.Label("Conexión Emocional Mínima (1 a 10):", className="font-weight-bold text-light mt-4"),
                    dcc.Slider(
                        id="emocion-filter",
                        min=1, max=10, step=0.5,
                        value=1.0,
                        marks={i: str(i) for i in range(1, 11)},
                        tooltip={"always_visible": True, "placement": "bottom"}
                    ),
                    
                    # Métrica de usuarios activos
                    html.Hr(style={"borderColor": "#303030"}),
                    html.Div([
                        html.H4("Usuarios Filtrados:", className="text-muted text-center mb-1"),
                        html.H2(id="user-count-badge", className="text-center text-warning font-weight-bold")
                    ], className="mt-3")
                ])
            ], className="mb-4")
        ], lg=3, md=4, xs=12),
        
        # Panel de Gráficos (Fila Superior)
        dbc.Col([
            dbc.Row([
                # PCA Glyph Plot
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("Proyección PCA: Glifos Multivariados (Foco + Contexto)", className="font-weight-bold text-primary"),
                        dbc.CardBody([
                            dcc.Graph(id="glyph-plot", style={"height": "400px"})
                        ])
                    ], className="mb-4")
                ], lg=7, md=12),
                
                # Star Glyphs / Radar
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("Star Glyphs: Firmas de Consumo Medianas", className="font-weight-bold text-primary"),
                        dbc.CardBody([
                            dcc.Graph(id="radar-plot", style={"height": "400px"})
                        ])
                    ], className="mb-4")
                ], lg=5, md=12)
            ]),
            
            # Panel de Gráficos (Fila Inferior)
            dbc.Row([
                # Sankey Flow
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("Sankey Flow: Trayectoria de Descubrimiento y Motivación", className="font-weight-bold text-primary"),
                        dbc.CardBody([
                            dcc.Graph(id="sankey-plot", style={"height": "350px"})
                        ])
                    ], className="mb-4")
                ], lg=6, md=12),
                
                # Coordenadas Paralelas
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("Coordenadas Paralelas (Correlaciones Multidimensionales)", className="font-weight-bold text-primary"),
                        dbc.CardBody([
                            dcc.Graph(id="parallel-plot", style={"height": "350px"})
                        ])
                    ], className="mb-4")
                ], lg=6, md=12)
            ])
        ], lg=9, md=8, xs=12)
    ])
], fluid=True, style={"backgroundColor": "#121214", "minHeight": "100vh"})

# ==========================================
# 3. CALLBACK DE CONTROL INTERACTIVO DE DATOS
# ==========================================
@app.callback(
    [Output("glyph-plot", "figure"),
     Output("radar-plot", "figure"),
     Output("sankey-plot", "figure"),
     Output("parallel-plot", "figure"),
     Output("user-count-badge", "children")],
    [Input("region-filter", "value"),
     Input("edad-filter", "value"),
     Input("emocion-filter", "value")]
)
def update_dashboard(region, edad_rango, min_emocion):
    # Filtrado dinámico de datos (Foco)
    df_filtered = df_usuarios.copy()
    if region != "Todas":
        df_filtered = df_filtered[df_filtered["region"] == region]
    df_filtered = df_filtered[
        (df_filtered["edad"] >= edad_rango[0]) & 
        (df_filtered["edad"] <= edad_rango[1]) &
        (df_filtered["conexion_emocional"] >= min_emocion)
    ]
    
    cant_usuarios = f"{len(df_filtered):,} / 5,000"
    
    # --------------------------------------------------
    # GRÁFICO 1: PCA Glyph Plot (Foco + Contexto)
    # --------------------------------------------------
    # Para mantener el contexto, mostramos todos los usuarios de fondo en gris semitransparente
    fig_glyph = go.Figure()
    
    # Contexto (Atenuado de fondo)
    fig_glyph.add_trace(go.Scatter(
        x=df_usuarios["pca_1"], y=df_usuarios["pca_2"],
        mode="markers",
        marker=dict(color="#222226", size=4, opacity=0.3),
        name="Población General",
        hoverinfo="skip"
    ))
    
    # Foco (Puntos Filtrados con Canales Visuales de Bertin)
    for tribu, color in colores_tribu.items():
        subset = df_filtered[df_filtered["tribu_real"] == tribu]
        if len(subset) > 0:
            fig_glyph.add_trace(go.Scatter(
                x=subset["pca_1"], y=subset["pca_2"],
                mode="markers",
                marker=dict(
                    color=color,
                    size=subset["conexion_emocional"] * 1.5, # Tamaño codifica emoción
                    line=dict(color="#121214", width=0.5)
                ),
                name=tribu,
                text=[f"Edad: {row['edad']}a | Región: {row['region']}<br>Físico: ${row['gasto_fisico_total']:.1f}/mes" for _, row in subset.iterrows()],
                hoverinfo="text"
            ))
            
    fig_glyph.update_layout(
        paper_bgcolor="#1E1E24", plot_bgcolor="#1E1E24",
        margin=dict(l=10, r=10, t=30, b=10),
        font=dict(color="#F4F1DE"),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, font=dict(size=9)),
        xaxis=dict(showgrid=True, gridcolor="#2D2D35", zerolinecolor="#2D2D35"),
        yaxis=dict(showgrid=True, gridcolor="#2D2D35", zerolinecolor="#2D2D35")
    )
    
    # --------------------------------------------------
    # GRÁFICO 2: Star Glyphs (Radar Chart)
    # --------------------------------------------------
    fig_radar = go.Figure()
    radar_features = ["gasto_streaming", "gasto_vinilos", "gasto_cds", "gasto_cassettes", "compras_bandcamp", "conexion_emocional"]
    df_radar_norm = df_usuarios.copy()
    
    # Normalizamos para escalas equivalentes
    for col in radar_features:
        df_radar_norm[col] = (df_radar_norm[col] - df_radar_norm[col].min()) / (df_radar_norm[col].max() - df_radar_norm[col].min())
    
    # Volvemos a filtrar el dataset normalizado
    if region != "Todas":
        df_radar_norm = df_radar_norm[df_radar_norm["region"] == region]
    df_radar_norm = df_radar_norm[
        (df_radar_norm["edad"] >= edad_rango[0]) & 
        (df_radar_norm["edad"] <= edad_rango[1]) &
        (df_radar_norm["conexion_emocional"] >= min_emocion)
    ]
    
    for tribu, color in colores_tribu.items():
        subset_tribu = df_radar_norm[df_radar_norm["tribu_real"] == tribu]
        if len(subset_tribu) > 0:
            mediana_tribu = subset_tribu[radar_features].median()
            valores_lista = mediana_tribu.tolist()
            
            fig_radar.add_trace(go.Scatterpolar(
                r=valores_lista + [valores_lista[0]],
                theta=[f.replace("_", " ").title() for f in radar_features] + [radar_features[0].replace("_", " ").title()],
                fill='toself',
                name=tribu,
                line=dict(color=color, width=2)
            ))
            
    fig_radar.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 1], gridcolor="#2D2D35", tickfont=dict(color="#A0A0A0", size=8)),
            angularaxis=dict(gridcolor="#2D2D35", tickfont=dict(color="#F4F1DE", size=9))
        ),
        paper_bgcolor="#1E1E24", plot_bgcolor="#1E1E24",
        margin=dict(l=40, r=40, t=40, b=10),
        font=dict(color="#F4F1DE"),
        showlegend=False
    )
    
    # --------------------------------------------------
    # GRÁFICO 3: Diagrama de Sankey (Flujo Generacional)
    # --------------------------------------------------
    if len(df_filtered) > 0:
        df_sankey = df_filtered.copy()
        df_sankey["rango_edad"] = pd.cut(
            df_sankey["edad"], 
            bins=[17, 30, 45, 76], 
            labels=["Jóvenes (<30 años)", "Adultos Medios (30-45)", "Adultos Mayores (>45)"]
        )
        
        flow1 = df_sankey.groupby(["rango_edad", "descubrimiento"]).size().reset_index(name="value")
        flow1.columns = ["source", "target", "value"]
        
        flow2 = df_sankey.groupby(["descubrimiento", "motivacion"]).size().reset_index(name="value")
        flow2.columns = ["source", "target", "value"]
        
        flow3 = df_sankey.groupby(["motivacion", "tribu_real"]).size().reset_index(name="value")
        flow3.columns = ["source", "target", "value"]
        
        flows = pd.concat([flow1, flow2, flow3])
        flows = flows[flows["value"] > 0]
        
        flows["source_idx"] = flows["source"].map(NODE_MAP)
        flows["target_idx"] = flows["target"].map(NODE_MAP)
        
        fig_sankey = go.Figure(data=[go.Sankey(
            node=dict(
                pad=12, thickness=15,
                line=dict(color="black", width=0.5),
                label=ALL_SANKEY_NODES,
                color="#3D5A80"
            ),
            link=dict(
                source=flows["source_idx"].tolist(),
                target=flows["target_idx"].tolist(),
                value=flows["value"].tolist(),
                color="rgba(244, 241, 222, 0.12)" # Flujos semitransparentes
            )
        )])
    else:
        fig_sankey = go.Figure()
        
    fig_sankey.update_layout(
        paper_bgcolor="#1E1E24",
        font=dict(color="#F4F1DE", size=10),
        margin=dict(l=10, r=10, t=20, b=10)
    )
    
    # --------------------------------------------------
    # GRÁFICO 4: Coordenadas Paralelas (Brushing Dinámico)
    # --------------------------------------------------
    if len(df_filtered) > 0:
        # Tomamos muestra de hasta 500 para rendimiento fluido
        df_sample_para = df_filtered.sample(min(500, len(df_filtered)), random_state=42)
        fig_parallel = px.parallel_coordinates(
            df_sample_para,
            dimensions=["edad", "gasto_streaming", "gasto_vinilos", "gasto_cassettes", "conexion_emocional", "fidelidad_equipo"],
            color="cluster",
            color_continuous_scale=[(0.0, "#E76F51"), (0.33, "#E9C46A"), (0.66, "#F4A261"), (1.0, "#264653")],
            labels={
                "edad": "Edad", "gasto_streaming": "Streaming ($)", "gasto_vinilos": "Vinilos ($)",
                "gasto_cassettes": "Cassettes ($)", "conexion_emocional": "Emoción", "fidelidad_equipo": "Equipo"
            }
        )
        fig_parallel.update_layout(
            paper_bgcolor="#1E1E24",
            font=dict(color="#F4F1DE", size=10),
            coloraxis_showscale=False,
            margin=dict(l=40, r=40, t=30, b=10)
        )
    else:
        fig_parallel = go.Figure()
        fig_parallel.update_layout(paper_bgcolor="#1E1E24", font=dict(color="#F4F1DE"))
        
    return fig_glyph, fig_radar, fig_sankey, fig_parallel, cant_usuarios

# ==========================================
# 4. EJECUCIÓN DEL SERVIDOR
# ==========================================
if __name__ == "__main__":
    app.run(debug=True)