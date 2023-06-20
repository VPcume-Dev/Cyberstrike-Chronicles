import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Game Settings")

# Create variables to store chosen difficulty and music preference
chosen_difficulty = tk.StringVar()
chosen_music_preference = tk.StringVar()
chosen_difficulty.set("Normal")  # Set the default difficulty to "Normal"

# Function to display the chosen mode
def display_chosen_mode():
    difficulty = chosen_difficulty.get()
    music_preference = chosen_music_preference.get()
    mode_label.config(text=f"Your mode is: {difficulty} with {music_preference} music.")

# Create a frame to hold the buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

# Create the difficulty buttons
hard_button = tk.Button(button_frame, text="Hard", command=lambda: set_difficulty("Hard"), font=("Arial", 16))
normal_button = tk.Button(button_frame, text="Normal", command=lambda: set_difficulty("Normal"), font=("Arial", 16))
easy_button = tk.Button(button_frame, text="Easy", command=lambda: set_difficulty("Easy"), font=("Arial", 16))

# Create the music preference buttons
music_button = tk.Button(button_frame, text="Music", command=lambda: set_music_preference("Music"), font=("Arial", 16))
no_music_button = tk.Button(button_frame, text="No Music", command=lambda: set_music_preference("No Music"), font=("Arial", 16))

# Create a frame to hold the mode label
label_frame = tk.Frame(root)
label_frame.pack(pady=10)

# Create the mode label
mode_label = tk.Label(label_frame, text="Your mode is: ", font=("Arial", 18, "bold"))

# Create a button to display the chosen mode
display_button = tk.Button(root, text="Display Mode", command=display_chosen_mode, font=("Arial", 16))

# Function to handle difficulty button clicks
def set_difficulty(difficulty):
    chosen_difficulty.set(difficulty)

# Function to handle music button clicks
def set_music_preference(music_preference):
    chosen_music_preference.set(music_preference)

# Place the buttons in the frame
hard_button.grid(row=0, column=0, padx=10)
normal_button.grid(row=0, column=1, padx=10)
easy_button.grid(row=0, column=2, padx=10)
music_button.grid(row=1, column=0, padx=10)
no_music_button.grid(row=1, column=1, padx=10)
mode_label.pack()
display_button.pack(pady=20)

# Run the main event loop
root.mainloop()
