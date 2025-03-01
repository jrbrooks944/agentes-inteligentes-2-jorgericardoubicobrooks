import tkinter as tk
import random

# Configuración del entorno
tile_size = 50
width, height = 10, 10  # Tamaño del grid
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Derecha, Izquierda, Abajo, Arriba

class PatrolAgent:
    def __init__(self, canvas, grid_size):
        self.canvas = canvas
        self.grid_size = grid_size
        self.x, self.y = 1, 1  # Posición inicial
        self.direction = random.choice(directions)  # Dirección inicial
        self.obstacles = [(random.randint(2, grid_size - 2), random.randint(2, grid_size - 2)) for _ in range(5)]
        self.draw_environment()
        self.agent = self.canvas.create_rectangle(self.x * tile_size, self.y * tile_size, 
                                                  (self.x + 1) * tile_size, (self.y + 1) * tile_size, fill="blue")
        self.patrol()

    def draw_environment(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                self.canvas.create_rectangle(i * tile_size, j * tile_size, (i + 1) * tile_size, (j + 1) * tile_size, outline="gray")
        for obs in self.obstacles:
            self.canvas.create_rectangle(obs[0] * tile_size, obs[1] * tile_size, (obs[0] + 1) * tile_size, (obs[1] + 1) * tile_size, fill="red")

    def patrol(self):
        new_x = self.x + self.direction[0]
        new_y = self.y + self.direction[1]

        if (new_x, new_y) in self.obstacles or not (0 <= new_x < self.grid_size and 0 <= new_y < self.grid_size):
            self.direction = random.choice(directions)  # Cambia de dirección al azar
        else:
            self.x, self.y = new_x, new_y

        self.canvas.coords(self.agent, self.x * tile_size, self.y * tile_size, (self.x + 1) * tile_size, (self.y + 1) * tile_size)
        self.canvas.after(500, self.patrol)  # Mueve al agente cada 500ms

# Crear ventana
root = tk.Tk()
root.title("Agente de Patrullaje")
canvas = tk.Canvas(root, width=width * tile_size, height=height * tile_size)
canvas.pack()

# Crear y ejecutar el agente
agent = PatrolAgent(canvas, width)
root.mainloop()
