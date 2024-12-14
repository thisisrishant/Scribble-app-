import tkinter as tk

class ScribbleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Scribble App")

        
        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        
        self.color = "black"
        self.brush_size = 3
        self.last_x, self.last_y = None, None

        
        self.canvas.bind("<Button-1>", self.start_drawing) 
        self.canvas.bind("<B1-Motion>", self.draw)  
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)  

        
        self.create_controls()

    def start_drawing(self, event):
        self.last_x, self.last_y = event.x, event.y

    def draw(self, event):
        if self.last_x and self.last_y:
            self.canvas.create_line(
                self.last_x, self.last_y, event.x, event.y,
                fill=self.color, width=self.brush_size, capstyle=tk.ROUND, smooth=True
            )
        self.last_x, self.last_y = event.x, event.y

    def stop_drawing(self, event):
        self.last_x, self.last_y = None, None

    def set_color(self, new_color):
        self.color = new_color

    def set_brush_size(self, new_size):
        self.brush_size = new_size

    def clear_canvas(self):
        self.canvas.delete("all")

    def create_controls(self):
        
        control_frame = tk.Frame(self.root, pady=5)
        control_frame.pack()

        
        colors = ["black", "red", "green", "blue", "yellow", "purple", "orange"]
        for color in colors:
            btn = tk.Button(control_frame, bg=color, width=2, command=lambda c=color: self.set_color(c))
            btn.pack(side=tk.LEFT, padx=2)

        
        brush_label = tk.Label(control_frame, text="Brush size:")
        brush_label.pack(side=tk.LEFT, padx=5)
        brush_slider = tk.Scale(control_frame, from_=1, to=20, orient=tk.HORIZONTAL, command=lambda s: self.set_brush_size(int(s)))
        brush_slider.set(self.brush_size)
        brush_slider.pack(side=tk.LEFT, padx=5)

        
        clear_button = tk.Button(control_frame, text="Clear", command=self.clear_canvas)
        clear_button.pack(side=tk.LEFT, padx=5)


if __name__ == "__main__":
    root = tk.Tk()
    app = ScribbleApp(root)
    root.mainloop()
