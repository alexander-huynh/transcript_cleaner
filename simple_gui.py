import tkinter as tk

def show_text():
    # Get the text from the entry widget
    entered_text = entry.get()
    # Update the label with the entered text
    label_result.config(text=f"You entered: {entered_text}")

# Create the main window
window = tk.Tk()
window.title("Simple GUI")

# Create and place widgets
label_prompt = tk.Label(window, text="Enter some text:")
label_prompt.pack(pady=5)

entry = tk.Entry(window)
entry.pack(pady=5)

button_show = tk.Button(window, text="Show Text", command=show_text)
button_show.pack(pady=5)

label_result = tk.Label(window, text="")
label_result.pack(pady=5)

# Run the application
window.mainloop()
