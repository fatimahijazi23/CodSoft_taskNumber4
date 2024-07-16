import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors Game")  #title of the window
        self.root.configure(bg="white")
        
        self.choices = ['Rock', 'Paper', 'Scissors']#possible choices
        
        self.frame = tk.Frame(root, bg="white")
        self.frame.pack(pady=20)
        
        self.label = tk.Label(self.frame, text="Choose your move:", font=('Arial', 24), bg="white")
        self.label.grid(row=0, column=0, columnspan=3)
        
        button_font = ('Arial', 18)
        button_padding = 20

        # Make a button for Rock and set its command to playGame with Rock
        self.rockButton = tk.Button(self.frame, text="Rock", font=button_font, padx=button_padding, pady=button_padding, command=lambda: self.playGame("Rock"), bg="pink")
        self.rockButton.grid(row=1, column=0)
        
        self.paperButton = tk.Button(self.frame, text="Paper", font=button_font, padx=button_padding, pady=button_padding, command=lambda: self.playGame("Paper"), bg="pink")
        self.paperButton.grid(row=1, column=1)
        
        self.scissorsButton = tk.Button(self.frame, text="Scissors", font=button_font, padx=button_padding, pady=button_padding, command=lambda: self.playGame("Scissors"), bg="pink")
        self.scissorsButton.grid(row=1, column=2)
        
        self.resultLabel = tk.Label(root, text="", font=('Arial', 35), bg="white")
        self.resultLabel.pack(pady=20)
        
    def playGame(self, user_choice):
        computerChoice = random.choice(self.choices)
        result = self.determineWinner(user_choice, computerChoice)
        self.resultLabel.config(text=f"You chose: {user_choice}\nComputer chose: {computerChoice}\nResult: {result}")
    
    def determineWinner(self, user_choice, computerChoice):
        if user_choice == computerChoice:
            return "It's a tie!"
        elif (user_choice == "Rock" and computerChoice == "Scissors") or \
             (user_choice == "Paper" and computerChoice == "Rock") or \
             (user_choice == "Scissors" and computerChoice == "Paper"):
            return "You won!"
        else:
            return "You lost!"

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissors(root)
    root.mainloop()
