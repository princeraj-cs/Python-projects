import random
import tkinter as tk
from tkinter import messagebox

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "You Lose, opponent has blackjack"
    elif u_score == 0:
        return "You Win with a blackjack!"
    elif c_score > 21:
        return "Opponent went over. You Win!"
    elif u_score > 21:
        return "You went over. You Lose"
    elif u_score > c_score:
        return "You Win!"
    else:
        return "You Lose"

class BlackjackGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack Game")
        self.root.geometry("600x500")
        self.root.configure(bg="#0e5e0e")
        
        self.user_cards = []
        self.computer_cards = []
        
        # Title
        self.title_label = tk.Label(root, text="♠ BLACKJACK ♣", 
                                    font=("Arial", 28, "bold"), 
                                    bg="#0e5e0e", fg="white")
        self.title_label.pack(pady=20)
        
        # Computer section
        self.computer_frame = tk.Frame(root, bg="#0e5e0e")
        self.computer_frame.pack(pady=10)
        
        self.computer_label = tk.Label(self.computer_frame, text="Dealer's Cards:", 
                                       font=("Arial", 14), 
                                       bg="#0e5e0e", fg="white")
        self.computer_label.pack()
        
        self.computer_cards_label = tk.Label(self.computer_frame, text="", 
                                             font=("Arial", 18, "bold"), 
                                             bg="#0e5e0e", fg="yellow")
        self.computer_cards_label.pack()
        
        self.computer_score_label = tk.Label(self.computer_frame, text="", 
                                             font=("Arial", 12), 
                                             bg="#0e5e0e", fg="white")
        self.computer_score_label.pack()
        
        # Separator
        tk.Label(root, text="━" * 50, bg="#0e5e0e", fg="white").pack(pady=10)
        
        # User section
        self.user_frame = tk.Frame(root, bg="#0e5e0e")
        self.user_frame.pack(pady=10)
        
        self.user_label = tk.Label(self.user_frame, text="Your Cards:", 
                                   font=("Arial", 14), 
                                   bg="#0e5e0e", fg="white")
        self.user_label.pack()
        
        self.user_cards_label = tk.Label(self.user_frame, text="", 
                                         font=("Arial", 18, "bold"), 
                                         bg="#0e5e0e", fg="lightblue")
        self.user_cards_label.pack()
        
        self.user_score_label = tk.Label(self.user_frame, text="", 
                                         font=("Arial", 12), 
                                         bg="#0e5e0e", fg="white")
        self.user_score_label.pack()
        
        # Result label
        self.result_label = tk.Label(root, text="", 
                                     font=("Arial", 16, "bold"), 
                                     bg="#0e5e0e", fg="orange")
        self.result_label.pack(pady=15)
        
        # Buttons
        self.button_frame = tk.Frame(root, bg="#0e5e0e")
        self.button_frame.pack(pady=20)
        
        self.hit_button = tk.Button(self.button_frame, text="HIT", 
                                    font=("Arial", 14, "bold"), 
                                    bg="#4CAF50", fg="white", 
                                    width=10, command=self.hit)
        self.hit_button.grid(row=0, column=0, padx=10)
        
        self.stand_button = tk.Button(self.button_frame, text="STAND", 
                                      font=("Arial", 14, "bold"), 
                                      bg="#f44336", fg="white", 
                                      width=10, command=self.stand)
        self.stand_button.grid(row=0, column=1, padx=10)
        
        self.new_game_button = tk.Button(self.button_frame, text="NEW GAME", 
                                         font=("Arial", 14, "bold"), 
                                         bg="#2196F3", fg="white", 
                                         width=22, command=self.new_game)
        self.new_game_button.grid(row=1, column=0, columnspan=2, pady=10)
        
        # Start first game
        self.new_game()
    
    def new_game(self):
        """Start a new game"""
        self.user_cards = []
        self.computer_cards = []
        self.result_label.config(text="")
        
        # Deal initial cards
        for _ in range(2):
            self.user_cards.append(deal_card())
            self.computer_cards.append(deal_card())
        
        self.hit_button.config(state=tk.NORMAL)
        self.stand_button.config(state=tk.NORMAL)
        
        self.update_display(show_all_dealer_cards=False)
        
        # Check for immediate blackjack
        user_score = calculate_score(self.user_cards)
        computer_score = calculate_score(self.computer_cards)
        
        if user_score == 0 or computer_score == 0:
            self.end_game()
    
    def hit(self):
        """Player draws another card"""
        self.user_cards.append(deal_card())
        user_score = calculate_score(self.user_cards)
        
        self.update_display(show_all_dealer_cards=False)
        
        if user_score > 21 or user_score == 0:
            self.end_game()
    
    def stand(self):
        """Player stands, dealer's turn"""
        self.end_game()
    
    def end_game(self):
        """End the game and show results"""
        # Dealer draws cards
        computer_score = calculate_score(self.computer_cards)
        while computer_score != 0 and computer_score < 17:
            self.computer_cards.append(deal_card())
            computer_score = calculate_score(self.computer_cards)
        
        user_score = calculate_score(self.user_cards)
        
        # Show all cards
        self.update_display(show_all_dealer_cards=True)
        
        # Show result
        result = compare(user_score, computer_score)
        self.result_label.config(text=result)
        
        # Disable buttons
        self.hit_button.config(state=tk.DISABLED)
        self.stand_button.config(state=tk.DISABLED)
    
    def update_display(self, show_all_dealer_cards=False):
        """Update the display with current cards and scores"""
        user_score = calculate_score(self.user_cards)
        computer_score = calculate_score(self.computer_cards)
        
        # Update user display
        self.user_cards_label.config(text=f"{self.user_cards}")
        if user_score == 0:
            self.user_score_label.config(text="BLACKJACK!")
        else:
            self.user_score_label.config(text=f"Score: {user_score}")
        
        # Update computer display
        if show_all_dealer_cards:
            self.computer_cards_label.config(text=f"{self.computer_cards}")
            if computer_score == 0:
                self.computer_score_label.config(text="BLACKJACK!")
            else:
                self.computer_score_label.config(text=f"Score: {computer_score}")
        else:
            self.computer_cards_label.config(text=f"[{self.computer_cards[0]}, ?]")
            self.computer_score_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = BlackjackGUI(root)
    root.mainloop()
