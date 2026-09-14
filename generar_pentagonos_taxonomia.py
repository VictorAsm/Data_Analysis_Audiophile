import os
import numpy as np
import matplotlib.pyplot as plt

output_dir = "taxonomy_pentagons"
os.makedirs(output_dir, exist_ok=True)

tribes_data = {
    "audiofilo_senior": {
        "color": "#E76F51", 
        "values": [0.90, 0.93, 0.90, 0.98, 0.85]
    },
    "hibrido_romantico": {
        "color": "#E9C46A", 
        "values": [1, 0.60, 0.45, 0.40, 0.45]
    },
    "consumidor_estetico": {
        "color": "#F4A261", 
        "values": [0.25, 0.98, 0.40, 0.40, 0.98]
    },
    "streamer_casual": {
        "color": "#3D5A80", 
        "values": [0, 1, 1, 0, 1]
    }
}

for key, data in tribes_data.items():
    fig = plt.figure(figsize=(7, 7.5), dpi=300)
    ax = fig.add_subplot(111, polar=True)
    N = 5
    
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]
    
    values = data["values"]
    values += values[:1]
    
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    
    ax.grid(False)
    ax.yaxis.grid(False)
    ax.xaxis.grid(False)
    ax.spines['polar'].set_visible(False)
    
    # 1. Grilla pentagonal del fondo usando el color de la tribu con opacidad reducida
    grid_levels = [0.25, 0.50, 0.75, 1.0]
    for r in grid_levels:
        grid_angles = angles
        grid_r = [r] * len(grid_angles)
        ax.plot(grid_angles, grid_r, color=data["color"], linewidth=1.0, linestyle="solid", alpha=0.4)
    
    # 2. Radios desde el centro usando el color de la tribu
    for a in angles[:-1]:
        ax.plot([a, a], [0, 1.0], color=data["color"], linewidth=1.2, alpha=0.4)
    
    # Polígono principal de la tribu
    ax.plot(angles, values, color=data["color"], linewidth=3.2, linestyle='solid', zorder=4)
    
    # 3. Puntos sin borde blanco (edgecolors toma el mismo color de la tribu)
    ax.scatter(angles[:-1], values[:-1], color=data["color"], s=90, zorder=5, edgecolors=data["color"], linewidth=2)
    
    plt.xticks([])
    plt.yticks([])
    plt.ylim(0, 1.15)
    
    label_offset = 1.12
    
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)
    
    plt.tight_layout()
    out_path = f"{output_dir}/taxonomia_pentagono_{key}.png"
    
    plt.savefig(out_path, transparent=True, bbox_inches='tight')
    plt.close()

print("PERFECT_PENTAGONS_GENERATED")