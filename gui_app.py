import tkinter as tk
from tkinter import messagebox
import subprocess
import sys

class SCEQuestionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SCE Question")
        self.root.geometry("400x200")
        self.root.configure(bg='#f0f0f0')
        
        # Center the window on screen
        self.center_window()
        
        # Create main frame
        main_frame = tk.Frame(root, bg='#f0f0f0')
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Question label
        self.question_label = tk.Label(
            main_frame, 
            text="Do you like SCE?", 
            font=('Arial', 18, 'bold'),
            bg='#f0f0f0',
            fg='#333333'
        )
        self.question_label.pack(pady=(0, 30))
        
        # Button frame
        button_frame = tk.Frame(main_frame, bg='#f0f0f0')
        button_frame.pack()
        
        # Yes button
        yes_button = tk.Button(
            button_frame,
            text="Yes",
            font=('Arial', 16, 'bold'),
            bg='#4CAF50',
            fg='black',
            width=6,
            height=1,
            command=self.yes_clicked,
            cursor='hand2',
            relief='raised',
            bd=3,
            highlightbackground='#333333',
            highlightthickness=2
        )
        yes_button.pack(side='left', padx=10)
        
        # No button
        no_button = tk.Button(
            button_frame,
            text="No",
            font=('Arial', 16, 'bold'),
            bg='#f44336',
            fg='black',
            width=6,
            height=1,
            command=self.no_clicked,
            cursor='hand2',
            relief='raised',
            bd=3,
            highlightbackground='#333333',
            highlightthickness=2
        )
        no_button.pack(side='left', padx=10)
        
    def center_window(self):
        """Center the window on the screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def yes_clicked(self):
        """Handle Yes button click"""
        # Change the question text to "Good"
        self.question_label.config(text="Good", fg='#4CAF50')
        # Wait 1 second then quit
        self.root.after(1000, self.root.quit)
        
    def no_clicked(self):
        """Handle No button click"""
        # Change the question text to "Wrong Answer."
        self.question_label.config(text="Wrong Answer.", fg='#f44336')
        # Wait 1 second then quit and run main.py
        self.root.after(1000, self.quit_and_run_main)
        
    def quit_and_run_main(self):
        """Quit the GUI and run main.py"""
        self.root.quit()
        try:
            subprocess.Popen([sys.executable, "main.py"])
        except Exception as e:
            print(f"Error running main.py: {e}")

def main_gui():
    """Main function to run the GUI application"""
    root = tk.Tk()
    app = SCEQuestionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main_gui()
