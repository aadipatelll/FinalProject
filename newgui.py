import tkinter as tk
from tkinter i
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import csv

root = tk.Tk()
root.title("292 Project")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")


title_label = tk.Label(root, text="ELEC 292 Project", font=("Helvetica", 24))
title_label.pack(pady=20)

# Create a figure and axis for the plot
fig, ax = plt.subplots()

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

def read():
    filename = "./HDF5/test_features_predictions.csv"

    # Read CSV file
    x = []
    y = []
    x_counter = 0  
    with open(filename, "r") as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            if row[-1] == '1':
                y.append(1)
                x.append(x_counter)
                x += 5
            elif row[-1] == '0':
                y.append(0)
                x.append(x_counter)
                x_counter += 5

    ax.clear()
    ax.scatter(x, y)
    ax.plot(x, y, color='red', linestyle='--') 
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Jumping (1=yes 0=no)')
    ax.set_title('Running / Jumping')
    canvas.draw()

read()

root.mainloop()
