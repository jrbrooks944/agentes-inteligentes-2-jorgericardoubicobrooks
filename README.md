# AGENTES INTELIGENTES 2

# Agente de Patrullaje (Reflejo Simple)

¿Qué sucede cuando ejecutas el código?
El agente comienza en la posición (1, 1) del grid.
Se mueve en una dirección aleatoria y revisa si se encuentra con un obstáculo o con los bordes del grid.
Si se encuentra con un obstáculo o llega al borde, cambia su dirección aleatoriamente y continúa patrullando.
Cada vez que el agente se mueve, se actualiza su posición en el canvas, lo que lo hace visible como un rectángulo azul que se mueve por la cuadrícula.
Este proceso de patrullaje continúa indefinidamente hasta que cierres la ventana.
Resumen:
Este código simula un agente que patrulla una cuadrícula de forma aleatoria, evitando obstáculos. Cada vez que se mueve, se actualiza su posición en una interfaz gráfica, y cambia de dirección si se encuentra con un obstáculo o el borde de la cuadrícula.


Agente Explorador de Mapas (Con Estado Interno)

¿Qué sucede cuando ejecutas el código?
El agente comienza en la posición (1, 1) y explora el entorno aleatoriamente.
En cada paso, se mueve a una celda adyacente válida (que no sea un obstáculo y no haya sido visitada previamente) y marca esa celda como visitada.
Las celdas visitadas se dibujan de color lightblue.
El agente sigue explorando el grid hasta que se cierra la ventana.
Resumen:
Este código simula un agente que explora un grid de manera aleatoria, evitando obstáculos y recordando las celdas que ya ha visitado. Cada movimiento del agente se muestra en una interfaz gráfica, y el agente continúa explorando mientras haya celdas válidas por descubrir.



# Agente de Navegación Autónoma (Basado en Metas)

¿Qué sucede cuando ejecutas el código?
El agente comienza en la celda (0, 0) y el objetivo está en la celda (23, 23).
Se generan 100 paredes aleatorias en el laberinto.
El algoritmo A* encuentra el camino más corto desde el inicio hasta el objetivo.
El agente sigue este camino, y su movimiento se dibuja en el canvas con un círculo azul.
Cuando el agente llega al objetivo, se detiene.
Si presionas el botón "Reiniciar", el laberinto y el agente se restablecen para empezar nuevamente.
Resumen:
Este código simula un agente autónomo que navega por un laberinto utilizando el algoritmo A* para encontrar el camino más corto hacia su objetivo, evitando obstáculos. Cada movimiento del agente se muestra en una interfaz gráfica, y puedes reiniciar el proceso cuando desees.


# Agente de Selección de Rutas (Basado en Utilidad)

Lo que sucede cuando ejecutas el código:
El agente comenzará en la posición (0, 0) y tratará de encontrar el camino más eficiente hacia la esquina inferior derecha del grid (23, 23).
El agente se mueve hacia las celdas con la mayor recompensa, mientras evita los obstáculos y no se mueve a las celdas que ya ha visitado.
La visualización gráfica en el canvas te permitirá ver el camino que sigue el agente, con cada celda marcada por su recompensa.
Si quieres empezar de nuevo, puedes presionar el botón "Reiniciar".
En resumen, el código simula un agente que busca un camino óptimo a través de un entorno con obstáculos y recompensas, y lo visualiza en una ventana gráfica.
