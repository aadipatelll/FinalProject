import tkinter as tk
import time

def draw_stickman(x, y):
    head = canvas.create_oval(x - 10, y - 30, x + 10, y - 50, fill="black")
    body = canvas.create_line(x, y - 30, x, y + 10, fill="black")
    left_leg = canvas.create_line(x, y + 10, x - 5, y + 20, fill="black")
    right_leg = canvas.create_line(x, y + 10, x + 5, y + 20, fill="black")
    left_arm = canvas.create_line(x, y - 20, x - 10, y - 10, fill="black")
    right_arm = canvas.create_line(x, y - 20, x + 10, y - 10, fill="black")
    return head, body, left_leg, right_leg, left_arm, right_arm

def walk_stickman():
    global x_position, total_time

    # Number of steps and speed of the animation
    num_steps = 20  # Adjust the number of steps for the desired duration
    animation_speed = 0.025  # Adjust the animation speed for the desired speed

    while total_time < 5:
        for i in range(num_steps):
            x_position += 5
            total_time += animation_speed
            time_label.config(text=f"Time: {total_time:.2f}s")  # Update the time label
            update_stickman_position()
            time.sleep(animation_speed)

        for i in range(num_steps):
            x_position -= 5
            total_time += animation_speed
            time_label.config(text=f"Time: {total_time:.2f}s")  # Update the time label
            update_stickman_position()
            time.sleep(animation_speed)
    total_time=0

def jump_stickman():
    global y_position, total_time

    # Number of steps and speed of the animation
    num_steps = 20  # Adjust the number of steps for the desired duration
    animation_speed = 0.025  # Adjust the animation speed for the desired speed

    while total_time < 5:
        for i in range(num_steps):
            y_position -= 5
            total_time += animation_speed
            time_label.config(text=f"Time: {total_time:.2f}s")  # Update the time label
            update_stickman_position()
            time.sleep(animation_speed)

        for i in range(num_steps):
            y_position += 5
            total_time += animation_speed
            time_label.config(text=f"Time: {total_time:.2f}s")  # Update the time label
            update_stickman_position()
            time.sleep(animation_speed)
    total_time=0


def update_stickman_position():
    canvas.coords(stickman[0], x_position - 10, y_position - 30, x_position + 10, y_position - 50)
    canvas.coords(stickman[1], x_position, y_position - 30, x_position, y_position + 10)
    canvas.coords(stickman[2], x_position, y_position + 10, x_position - 5, y_position + 20)
    canvas.coords(stickman[3], x_position, y_position + 10, x_position + 5, y_position + 20)
    canvas.coords(stickman[4], x_position, y_position - 20, x_position - 10, y_position - 10)
    canvas.coords(stickman[5], x_position, y_position - 20, x_position + 10, y_position - 10)
    root.update()


root = tk.Tk()
root.title("292 Project")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

x_position = 50
y_position = 150
total_time = 0

canvas = tk.Canvas(root, width=500, height=300, bg="white")
canvas.pack()

title_label = tk.Label(root, text="ELEC 292 Project", font=("Helvetica", 24))
title_label.pack(pady=20)

time_label = tk.Label(root, text=f"Time: {total_time:.2f}s", font=("Helvetica", 16))
time_label.pack()

stickman = draw_stickman(x_position, y_position)

# Run the animations for a fixed number of iterations
for _ in range(10):  # Change 10 to the desired number of iterations
    walk_stickman()
    jump_stickman()


root.mainloop()
