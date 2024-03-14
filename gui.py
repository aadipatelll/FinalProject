import tkinter as tk
import csv

def update_square():
    global current_color
    try:
        row = next(reader)
        for value in row:
            print(current_color)
            current_color = "green" if value == '1' else "blue"
            square.config(bg=current_color)
            root.update()  
            root.after(1500)  # 1.5s
    except StopIteration:
        pass

root = tk.Tk()
root.title("CSV File Reader")


# hello

file_path = "random_data.csv"
csvfile = open(file_path, newline='')
reader = csv.reader(csvfile)
label = tk.Label(root, text="Green running, Blue Jumping")
label.pack()
current_color = "blue"
square = tk.Frame(root, width=300, height=300, bg=current_color, highlightbackground="black", highlightthickness=1)
square.pack()

update_square()

root.mainloop()

csvfile.close()
