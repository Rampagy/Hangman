from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
import random



class HangmanGame(Widget):
    display_word = StringProperty()
    wrong_guess = 0
    correct_guess = 0
    
    def FindHangmanWord(self):
        afile = 'Dictionary.txt'

        # find number of lines in file
        with open(afile) as f:
            for i, l in enumerate(f):
                pass

        # grab a random line and return it
        randNum = random.randrange(i+1)
        with open(afile) as f:
            for i, line in enumerate(f):
                if i+1 >= randNum:
                    return line[:len(line)-1]
                    break
        return None

    def check_in_word(self, btn):
        count = 0;
        for i, letter in enumerate(hangman_word):
            if btn.text == letter.upper():
                self.display_word = self.display_word[:i*2] + btn.text + self.display_word[i*2+1:]
                self.correct_guess+=1
                count += 1
                
                if self.correct_guess >= len(hangman_word):
                    print('GAME OVER, YOU WIN')
                
        if count == 0:
            # count wrong guess
            self.wrong_guess+=1
            if self.wrong_guess >= 6:
                print('GAME OVER, YOU LOSE!')

        
        btn.disabled = True # True is synonymous with 1


    def init_display_word(self, word):
        tmp_display_word = ''
        for letter in word:
            tmp_display_word += '_ '
        self.display_word = tmp_display_word[:len(tmp_display_word)-1]

class HangmanApp(App):
    def build(self):
        game = HangmanGame()
        game.init_display_word(hangman_word)
        return game



if __name__ == "__main__":
    hangman_word = HangmanGame().FindHangmanWord()
    HangmanApp().run()


