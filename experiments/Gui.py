import tkinter as tk
from tkinter import messagebox

# Function to handle button clicks
def play_game():
    messagebox.showinfo("Play", "Starting the game!")

def show_game_details():
    messagebox.showinfo("Game Details", "Game details here.")

def show_game_settings():
    import settings.py

def quit_game():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Cyberstrike Chronicles")

# Configure window size and position
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = int(screen_width / 2)
window_height = int(screen_height / 2)
window_x = int((screen_width - window_width) / 2)
window_y = int((screen_height - window_height) / 2)
root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
root.minsize(400, 200)

# Create a frame to hold the title and buttons
frame = tk.Frame(root)
frame.pack(pady=20)

# Create the title label
title_label = tk.Label(frame, text="Cyberstrike Chronicles", font=("Arial", 24, "bold"))
title_label.pack(pady=(0, 20))

# Create the buttons
play_button = tk.Button(frame, text="Play", command=play_game, font=("Arial", 20))
game_details_button = tk.Button(frame, text="Game Details", command=show_game_details, font=("Arial", 20))
game_settings_button = tk.Button(frame, text="Game Settings", command=show_game_settings, font=("Arial", 20))
quit_button = tk.Button(frame, text="Quit", command=quit_game, font=("Arial", 20))

# Place the buttons in the frame
play_button.pack(pady=10)
game_details_button.pack(pady=10)
game_settings_button.pack(pady=10)
quit_button.pack(pady=10)

# Run the main event loop
root.mainloop()