
import tkinter as tk
from tkinter import ttk

def click_calculateButton():
    spd = float( spdText.get() )    # get speed driven from the speed textfield
    time = float( timeText.get() )        # get time driven in minutes from the time textfield
    dist = spd * time / 60                # do the math!
    distText.set( round(dist,1) )         # display the output

def command_exitButton():
    root.destroy()

# create root window
root = tk.Tk()
root.title("Distance Calculator")
root.geometry("280x150")    # size of window

# create frame and add it to the root window
frame = ttk.Frame(root, padding="10 10 10 10")
frame.pack(fill=tk.BOTH, expand=True)

# create labels and textfields
ttk.Label(frame, text="Time Driven (minutes):").grid(column=0, row=0, padx=5, pady=5, sticky=tk.E)  # display label in grid
timeText = tk.StringVar()
ttk.Entry(frame, width=25, textvariable=timeText).grid(column=1, row=0)

ttk.Label(frame, text="Speed:").grid(column=0, row=1, padx=5, pady=5, sticky=tk.E)
spdText = tk.StringVar()
ttk.Entry(frame, width=25, textvariable=spdText).grid(column=1, row=1)

# create a button and add it to the window
ttk.Button(frame, text="Calculate", command=click_calculateButton).grid(column=0, row=2, padx=5, pady=5, sticky=tk.E)
ttk.Button(frame, text="Exit", command=command_exitButton).grid(column=1, row=2, padx=5, pady=5, sticky=tk.W)

ttk.Label(frame, text="Distance:").grid(column=0, row=3, padx=5, pady=5, sticky=tk.E)
distText = tk.StringVar()
distEntry = ttk.Entry(frame, width=25, textvariable=distText, state="readonly").grid(column=1, row=3) # notice readonly!
