import tkinter as tk
import random

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Game")
        self.cards = list(range(1, 9)) * 2
        random.shuffle(self.cards)
        self.buttons = []
        self.first = None
        self.second = None
        self.turn_count = 0
        self.colors = ["red", "blue", "green", "orange", "purple", "brown", "pink", "cyan"]
        
        self.turn_label = tk.Label(self.root, text=f"Turns: {self.turn_count}", font=("Helvetica", 14))
        self.turn_label.grid(row=4, column=0, columnspan=4)
        
        self.create_widgets()
    
    def create_widgets(self):
        for i in range(4):
            row = []
            for j in range(4):
                button = tk.Button(self.root, width=10, height=5, font=("Helvetica", 24, "bold"),
                                   command=lambda i=i, j=j: self.on_click(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)
    
    def on_click(self, i, j):
        if self.first and self.second:
            return
        
        if self.first == (i, j):  # 同じカードをクリックした場合は無視する
            return
        
        card_value = self.cards[i * 4 + j]
        color = self.colors[card_value - 1]
        
        # カードがクリックされる前は灰色の背景に灰色の数字を表示し、クリックされた後は白色の背景にカラフルな数字を表示する
        self.buttons[i][j].config(text="", state="disabled", bg="gray", disabledforeground="gray")
        self.root.after(500, lambda: self.buttons[i][j].config(text=str(card_value), bg="white", disabledforeground=color))
        
        if not self.first:
            self.first = (i, j)
        elif not self.second:
            self.second = (i, j)
            self.turn_count += 1
            self.turn_label.config(text=f"Turns: {self.turn_count}")
            self.root.after(1000, self.check_match)
    
    def check_match(self):
        first_card = self.cards[self.first[0] * 4 + self.first[1]]
        second_card = self.cards[self.second[0] * 4 + self.second[1]]
        
        if first_card == second_card:
            self.buttons[self.first[0]][self.first[1]].config(bg="light green")
            self.buttons[self.second[0]][self.second[1]].config(bg="light green")
        else:
            self.buttons[self.first[0]][self.first[1]].config(text="", state="normal", bg="gray")
            self.buttons[self.second[0]][self.second[1]].config(text="", state="normal", bg="gray")
        
        self.first = None
        self.second = None

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()
