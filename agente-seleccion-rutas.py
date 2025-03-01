import tkinter as tk
import random

# Configuración del entorno
tile_size = 50
width, height = 10, 10  # Tamaño del grid
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Derecha, Izquierda, Abajo, Arriba

class RouteSelectionAgent:
    def __init__(self, canvas, grid_size):
        self.canvas = canvas
        self.grid_size = grid_size
        self.x, self.y = 0, 0  # Posición inicial
        self.rewards = self.generate_rewards()
        self.obstacles = [(random.randint(2, grid_size - 2), random.randint(2, grid_size - 2)) for _ in range(5)]
        self.draw_environment()
        self.agent = self.canvas.create_rectangle(self.x * tile_size, self.y * tile_size, 
                                                  (self.x + 1) * tile_size, (self.y + 1) * tile_size, fill="blue")
        self.find_best_path()
    
    def generate_rewards(self):
        return [[random.randint(1, 10) for _ in range(self.grid_size)] for _ in range(self.grid_size)]
    
    def draw_environment(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                color = "white" if (i, j) not in self.obstacles else "red"
                self.canvas.create_rectangle(i * tile_size, j * tile_size, (i + 1) * tile_size, (j + 1) * tile_size, fill=color, outline="gray")
                self.canvas.create_text(i * tile_size + 25, j * tile_size + 25, text=str(self.rewards[i][j]), font=("Arial", 12))
    
    def find_best_path(self):
        path = []
        while (self.x, self.y) != (self.grid_size - 1, self.grid_size - 1):
            path.append((self.x, self.y))
            best_move = None
            best_reward = -1
            for dx, dy in directions:
                nx, ny = self.x + dx, self.y + dy
                if 0 <= nx < self.grid_size and 0 <= ny < self.grid_size and (nx, ny) not in self.obstacles and (nx, ny) not in path:
                    if self.rewards[nx][ny] > best_reward:
                        best_reward = self.rewards[nx][ny]
                        best_move = (nx, ny)
            if best_move:
                self.x, self.y = best_move
                self.canvas.create_rectangle(self.x * tile_size, self.y * tile_size, (self.x + 1) * tile_size, (self.y + 1) * tile_size, fill="lightblue")
                self.canvas.coords(self.agent, self.x * tile_size, self.y * tile_size, (self.x + 1) * tile_size, (self.y + 1) * tile_size)
            else:
                break  # Si no hay movimientos válidos, se detiene
            self.canvas.update()
            self.canvas.after(500)
        print("Ruta óptima recorrida:", path)

# Crear ventana
root = tk.Tk()
root.title("Agente de Selección de Rutas")
canvas = tk.Canvas(root, width=width * tile_size, height=height * tile_size)
canvas.pack()

# Crear y ejecutar el agente
agent = RouteSelectionAgent(canvas, width)
root.mainloop()
