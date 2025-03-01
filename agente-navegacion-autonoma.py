import tkinter as tk
import random
import heapq

# Configuración del entorno
maze_size = 24  # Aumentamos el tamaño del laberinto
tile_size = 25  # Reducimos el tamaño de los cuadros para que quepa en la pantalla

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Derecha, Izquierda, Abajo, Arriba

class AutonomousNavigationAgent:
    def __init__(self, canvas):
        self.canvas = canvas
        self.grid_size = maze_size
        self.start = (0, 0)
        self.goal = (maze_size - 1, maze_size - 1)
        self.walls = self.generate_walls()
        self.draw_environment()
        self.agent = self.canvas.create_oval(self.start[0] * tile_size + 5, self.start[1] * tile_size + 5,
                                             (self.start[0] + 1) * tile_size - 5, (self.start[1] + 1) * tile_size - 5,
                                             fill="blue")
        self.find_shortest_path()
    
    def generate_walls(self):
        walls = set()
        for _ in range(100):  # Más paredes para mayor dificultad
            walls.add((random.randint(0, maze_size - 1), random.randint(0, maze_size - 1)))
        walls.discard(self.start)
        walls.discard(self.goal)
        return walls
    
    def draw_environment(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                color = "white" if (i, j) not in self.walls else "black"
                self.canvas.create_rectangle(i * tile_size, j * tile_size, (i + 1) * tile_size, (j + 1) * tile_size, fill=color, outline="gray")
        self.canvas.create_rectangle(self.goal[0] * tile_size, self.goal[1] * tile_size, 
                                     (self.goal[0] + 1) * tile_size, (self.goal[1] + 1) * tile_size, fill="green")
    
    def find_shortest_path(self):
        def heuristic(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        
        open_set = []
        heapq.heappush(open_set, (0, self.start))
        came_from = {}
        cost_so_far = {self.start: 0}
        
        while open_set:
            _, current = heapq.heappop(open_set)
            
            if current == self.goal:
                break
            
            for dx, dy in directions:
                next_pos = (current[0] + dx, current[1] + dy)
                if 0 <= next_pos[0] < maze_size and 0 <= next_pos[1] < maze_size and next_pos not in self.walls:
                    new_cost = cost_so_far[current] + 1
                    if next_pos not in cost_so_far or new_cost < cost_so_far[next_pos]:
                        cost_so_far[next_pos] = new_cost
                        priority = new_cost + heuristic(self.goal, next_pos)
                        heapq.heappush(open_set, (priority, next_pos))
                        came_from[next_pos] = current
        
        path = []
        current = self.goal
        while current != self.start:
            path.append(current)
            current = came_from.get(current, self.start)
        path.reverse()
        
        self.follow_path(path)
    
    def follow_path(self, path):
        for i, step in enumerate(path):
            self.canvas.after(i * 100, self.move_agent, step)
    
    def move_agent(self, position):
        self.canvas.create_rectangle(position[0] * tile_size, position[1] * tile_size, 
                                     (position[0] + 1) * tile_size, (position[1] + 1) * tile_size, fill="lightblue")
        self.canvas.coords(self.agent, position[0] * tile_size + 5, position[1] * tile_size + 5, 
                           (position[0] + 1) * tile_size - 5, (position[1] + 1) * tile_size - 5)

def restart():
    canvas.delete("all")
    global agent
    agent = AutonomousNavigationAgent(canvas)

# Crear ventana
root = tk.Tk()
root.title("Agente de Navegación Autónoma")

canvas = tk.Canvas(root, width=maze_size * tile_size, height=maze_size * tile_size)
canvas.pack()

btn_restart = tk.Button(root, text="Reiniciar", command=restart)
btn_restart.pack()

# Crear y ejecutar el agente
agent = AutonomousNavigationAgent(canvas)
root.mainloop()
