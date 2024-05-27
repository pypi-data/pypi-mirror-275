import random
class janken:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.win_list = [["scissors"], ["rock"], ["paper"]]
        self.init_choices = ['rock', 'paper', 'scissors']
        self.init_win_list = [["scissors"], ["rock"], ["paper"]]

    def all_reset(self):
        self.choices = self.init_choices
        self.win_list = self.init_win_list
    
    def delete_gesture(self,name):
        if name not in self.choices: 
            print("It dosen't exist")
            return None
        del self.choices[self.choices.index(name)]
        del self.win_list[self.choices.index(name)]

    def check_gesuture(self, name):
        if name not in self.choices: 
            print("It dosen't exist")
            return None
        print(self.choices[self.choices.index(name)])
        print(self.win_list[self.choices.index(name)])

    def get_computer_choice(self):
        """Randomly select the computer's choice"""
        return random.choice(self.choices)

    def get_user_choice(self):
        """Get the user's choice"""
        choice = input("Enter a choice (rock, paper, scissors, or your custom gesture): ").lower()
        while choice not in self.choices:
            choice = input("Enter a choice (rock, paper, scissors, or your custom gesture): ").lower()
        return choice

    def determine_winner(self, user_choice, computer_choice):
        """Determine the winner of the game"""
        if computer_choice in self.win_list[self.choices.index(user_choice)]:
            return "You win!"
        elif user_choice in self.win_list[self.choices.index(computer_choice)]:
            return "You lose"
        elif user_choice not in self.choices:
                return "Invalid choice. Please try again."
        else:
            return "It's a tie!"


    def add_custom_gesture_interactive(self):
        
        print("If you make a mistake, input 'reset'")
        name = input("Tell me the gesture name!! : ").lower()
        if name in [self.choices]:
            print("It already exist")
            add_custom_gesture()
            return None
        if name == 'reset': return None
        
        win = ""
        win_ls = []
        print("if you want to finish adding, input 'ok'")
        while True:
            win = input("What can the gesture win to? : ").lower()
            if win == 'reset': return None
            if win == 'ok': break
            if win in self.choices:
                win_ls.append(win)
            else:
                print("It doesn't exist")
                continue
        
        lose = ""
        lose_ls = []
        print("if you want to finish adding, input 'ok'")
        while True:
            lose = input("What can the gesture lose to? : ").lower()
            if lose == 'reset': return None
            if lose == 'ok': break
            if lose in win_ls:
                print('It can already lose to ',name)
                continue
            elif lose in self.choices:
                lose_ls.append(lose)
            else:
                print("That doesn't exist")
                continue

        self.choices.append(name)
        self.win_list.append(win_ls)
        for l in lose_ls:
            self.win_list[self.choices.index(l)].append(name)

    def add_custom_gesture(self, name, win=[], lose=[]):
        self.choices.append(name)
        self.win_list.append(win)
        for l in lose:
            self.win_list[self.choices.index(l)].append(name)

# play the game
    def play_game(self):
        """Play the game of Rock, Paper, Scissors with custom gestures"""
        
        while True:
            user_choice = self.get_user_choice()
            computer_choice = self.get_computer_choice()
            result = self.determine_winner(user_choice, computer_choice)
            if result != "It's a tie!":
                break
            print('enemy choice ',computer_choice)
            print(result)
        print('enemy choice ',computer_choice)
        print(result)
