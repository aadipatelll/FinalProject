import tkinter as tk
import csv
# def update_square():
#     global current_color
#     try:
#         row = next(reader)
#         for value in row:
#             print(current_color)
#             current_color = "green" if value == '1' else "blue"
#             square.config(bg=current_color)
#             root.update()  
#             root.after(1500)  # 1.5s
#     except StopIteration:
#         pass
# file_path = "random_data.csv"
# csvfile = open(file_path, newline='')
# reader = csv.reader(csvfile)


def animate():
    global x_position, counter, total_time_label
    canvas.delete("stickman")

    canvas.create_oval(x_position, 150, x_position + 20, 170, fill="black", tags="stickman")  # Head
    canvas.create_line(x_position + 10, 170, x_position + 10, 200, fill="black", tags="stickman")  # Body
    canvas.create_line(x_position + 10, 200, x_position, 230, fill="black", tags="stickman")  # Left leg
    canvas.create_line(x_position + 10, 200, x_position + 20, 230, fill="black", tags="stickman")  # Right leg
    canvas.create_line(x_position + 10, 180, x_position, 190, fill="black", tags="stickman")  # Left arm
    canvas.create_line(x_position + 10, 180, x_position + 20, 190, fill="black", tags="stickman")  # Right arm

    x_position += 1  
    if x_position > 500:  #end
        x_position = 0

    counter += 1
    total_time_label.config(text=f"Total Time: {counter * 0.01:.2f} seconds")  #Counter

    root.after(10, animate)  #in ms


root = tk.Tk()
root.title("292 Project")

canvas = tk.Canvas(root, width=500, height=300, bg="white")
canvas.pack()

x_position = 0  # Initial x-coordinate of stickman

counter = 0
total_time_label = tk.Label(root, text="Total Time: 0.00 seconds")
total_time_label.pack()
animate()  # Start the animation



screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")



title_label = tk.Label(root, text="ELEC 292 Project", font=("Helvetica", 24))
title_label.pack(pady=20)
description_label = tk.Label(root, text="Green running blue jumping", font=("Helvetica", 12))
description_label.pack()

root.mainloop()
