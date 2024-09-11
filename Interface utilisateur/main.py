# Python : Tkinter

from root import *
photo_label = ttk.Label(root, text="Python", font=("Arial", 12)).pack()

photo = tk.PhotoImage(file="./assets/Python.png")
ttk.Label( root, image=photo, compound='top').pack()

root.mainloop()