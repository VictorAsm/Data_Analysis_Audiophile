import matplotlib.pyplot as plt
import numpy as np
import random

# 1. Generar valores aleatorios ordenados
valores = sorted([12.5, 25, 37.5, 50, 62.5, 75, 87.5, 100])  # Ejemplo de valores ordenados
x = np.arange(len(valores))

# 2. Configurar el tamaño de la figura
fig, ax = plt.subplots(figsize=(2, 6))

# 3. Dibujar las barras
# zorder=3 asegura que las barras se dibujen POR ENCIMA de la grilla
bars = ax.bar(x, valores, color='#5D8AA8', width=0.9, zorder=3)

# 4. Configurar las líneas laterales (izquierda y derecha sólidas)
ax.spines['left'].set_color('gray')
ax.spines['left'].set_linewidth(0.5)
ax.spines['right'].set_color('gray')
ax.spines['right'].set_linewidth(0.5)

# Ocultar las líneas sólidas superior e inferior (la grilla hará el trabajo ahí)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# 5. Forzar la cantidad de líneas horizontales para el "cuadriculado"
# Esto crea líneas a distancias iguales (ej. 5 líneas)
ax.set_yticks(np.linspace(0, max(valores) + 20, 6))

# 6. Activar la grilla horizontal detrás de las barras
# linestyle='--' crea la línea con espacios que mencionaste
# zorder=0 la empuja al fondo
ax.grid(axis='y', color='gray', linestyle='--', linewidth=0.5, alpha=0.5, zorder=0)

# 7. Ocultar los textos de los números y las marquitas de los ejes
ax.set_yticklabels([])
ax.set_xticks([])
ax.tick_params(axis='y', length=0) # Oculta la rayita del número pero mantiene la grilla

# 8. Fondo transparente
ax.patch.set_alpha(0.0)
fig.patch.set_alpha(0.0)

# 9. Ajustar márgenes
plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)

# 10. Guardar como barras.png
plt.savefig('barras.png', transparent=True, dpi=300, bbox_inches='tight')

# Mostrar en pantalla
plt.show()