# import tkinter as tk
# import random

# # Configuración del entorno
# tile_size = 50
# width, height = 10, 10  # Tamaño del grid
# directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Derecha, Izquierda, Abajo, Arriba

# class ExplorerAgent:
#     def __init__(self, canvas, grid_size):
#         self.canvas = canvas
#         self.grid_size = grid_size
#         self.x, self.y = 1, 1  # Posición inicial
#         self.visited = set()  # Memoria interna de áreas exploradas
#         self.visited.add((self.x, self.y))
#         self.obstacles = [(random.randint(2, grid_size - 2), random.randint(2, grid_size - 2)) for _ in range(5)]
#         self.draw_environment()
#         self.agent = self.canvas.create_rectangle(self.x * tile_size, self.y * tile_size, 
#                                                   (self.x + 1) * tile_size, (self.y + 1) * tile_size, fill="blue")
#         self.explore()

#     def draw_environment(self):
#         for i in range(self.grid_size):
#             for j in range(self.grid_size):
#                 self.canvas.create_rectangle(i * tile_size, j * tile_size, (i + 1) * tile_size, (j + 1) * tile_size, outline="gray")
#         for obs in self.obstacles:
#             self.canvas.create_rectangle(obs[0] * tile_size, obs[1] * tile_size, (obs[0] + 1) * tile_size, (obs[1] + 1) * tile_size, fill="red")

#     def explore(self):
#         possible_moves = [(self.x + dx, self.y + dy) for dx, dy in directions]
#         valid_moves = [move for move in possible_moves if self.is_valid(move)]

#         if valid_moves:
#             self.x, self.y = random.choice(valid_moves)
#             self.visited.add((self.x, self.y))

#         self.canvas.coords(self.agent, self.x * tile_size, self.y * tile_size, (self.x + 1) * tile_size, (self.y + 1) * tile_size)
#         self.canvas.after(500, self.explore)

#     def is_valid(self, move):
#         x, y = move
#         return (0 <= x < self.grid_size and 0 <= y < self.grid_size and
#                 move not in self.obstacles and move not in self.visited)

# # Crear ventana
# root = tk.Tk()
# root.title("Agente Explorador")
# canvas = tk.Canvas(root, width=width * tile_size, height=height * tile_size)
# canvas.pack()

# # Crear y ejecutar el agente
# agent = ExplorerAgent(canvas, width)
# root.mainloop()




# import tkinter as tk
# import random

# # Configuración del entorno
# tile_size = 50
# width, height = 10, 10  # Tamaño del grid
# directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Derecha, Izquierda, Abajo, Arriba

# class ExplorerAgent:
#     def __init__(self, canvas, grid_size):
#         self.canvas = canvas
#         self.grid_size = grid_size
#         self.x, self.y = 1, 1  # Posición inicial
#         self.visited = set()  # Memoria interna de áreas exploradas
#         self.visited.add((self.x, self.y))
#         self.obstacles = [(random.randint(2, grid_size - 2), random.randint(2, grid_size - 2)) for _ in range(5)]
#         self.draw_environment()
#         self.agent = self.canvas.create_rectangle(self.x * tile_size, self.y * tile_size, 
#                                                   (self.x + 1) * tile_size, (self.y + 1) * tile_size, fill="blue")
#         self.explore()

#     def draw_environment(self):
#         for i in range(self.grid_size):
#             for j in range(self.grid_size):
#                 self.canvas.create_rectangle(i * tile_size, j * tile_size, (i + 1) * tile_size, (j + 1) * tile_size, outline="gray")
#         for obs in self.obstacles:
#             self.canvas.create_rectangle(obs[0] * tile_size, obs[1] * tile_size, (obs[0] + 1) * tile_size, (obs[1] + 1) * tile_size, fill="red")

#     def explore(self):
#         possible_moves = [(self.x + dx, self.y + dy) for dx, dy in directions]
#         valid_moves = [move for move in possible_moves if self.is_valid(move)]

#         if valid_moves:
#             self.x, self.y = random.choice(valid_moves)
#             self.visited.add((self.x, self.y))
#             self.canvas.create_rectangle(self.x * tile_size, self.y * tile_size, (self.x + 1) * tile_size, (self.y + 1) * tile_size, fill="lightblue")

#         self.canvas.coords(self.agent, self.x * tile_size, self.y * tile_size, (self.x + 1) * tile_size, (self.y + 1) * tile_size)
#         self.canvas.after(500, self.explore)

#     def is_valid(self, move):
#         x, y = move
#         return (0 <= x < self.grid_size and 0 <= y < self.grid_size and
#                 move not in self.obstacles and move not in self.visited)

# # Crear ventana
# root = tk.Tk()
# root.title("Agente Explorador")
# canvas = tk.Canvas(root, width=width * tile_size, height=height * tile_size)
# canvas.pack()

# # Crear y ejecutar el agente
# agent = ExplorerAgent(canvas, width)
# root.mainloop()










import tkinter as tk
import random

# Configuración del entorno
tile_size = 50
width, height = 10, 10  # Tamaño del grid
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Derecha, Izquierda, Abajo, Arriba

class ExplorerAgent:
    def __init__(self, canvas, grid_size):
        self.canvas = canvas
        self.grid_size = grid_size
        self.x, self.y = 1, 1  # Posición inicial
        self.visited = set()  # Memoria interna de áreas exploradas
        self.visited.add((self.x, self.y))
        self.obstacles = [(random.randint(2, grid_size - 2), random.randint(2, grid_size - 2)) for _ in range(5)]
        self.draw_environment()
        self.agent = self.canvas.create_oval(self.x * tile_size + 10, self.y * tile_size + 10, 
                                             (self.x + 1) * tile_size - 10, (self.y + 1) * tile_size - 10, 
                                             fill="blue")
        self.explore()

    def draw_environment(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                self.canvas.create_rectangle(i * tile_size, j * tile_size, (i + 1) * tile_size, (j + 1) * tile_size, outline="gray")
        for obs in self.obstacles:
            self.canvas.create_rectangle(obs[0] * tile_size, obs[1] * tile_size, (obs[0] + 1) * tile_size, (obs[1] + 1) * tile_size, fill="red")

    def explore(self):
        possible_moves = [(self.x + dx, self.y + dy) for dx, dy in directions]
        valid_moves = [move for move in possible_moves if self.is_valid(move)]

        if valid_moves:
            self.x, self.y = random.choice(valid_moves)
            self.visited.add((self.x, self.y))
            self.canvas.create_rectangle(self.x * tile_size, self.y * tile_size, (self.x + 1) * tile_size, (self.y + 1) * tile_size, fill="lightblue")

        self.canvas.coords(self.agent, self.x * tile_size + 10, self.y * tile_size + 10, 
                           (self.x + 1) * tile_size - 10, (self.y + 1) * tile_size - 10)
        self.canvas.after(500, self.explore)

    def is_valid(self, move):
        x, y = move
        return (0 <= x < self.grid_size and 0 <= y < self.grid_size and
                move not in self.obstacles and move not in self.visited)

# Crear ventana
root = tk.Tk()
root.title("Agente Explorador")
canvas = tk.Canvas(root, width=width * tile_size, height=height * tile_size)
canvas.pack()

# Crear y ejecutar el agente
agent = ExplorerAgent(canvas, width)
root.mainloop()