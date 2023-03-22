import turtle as t
#importing turtle and naming it t so I dont have to write out hangman each time 
from random import choice
#importing a random choice generator for the word bank


def draw_background():
    t.setup(500, 800)
    t.title('Hangman')
    t.pu()
    t.setpos(-100, -200)
    t.seth(0)
    t.pd()
    t.forward(200)

def draw_head():
    t.pu()
    t.setpos(0, 0)
    t.pd()
    t.circle(10)

def draw_body():
    t.pu()
    t.setpos(0, 0)
    t.pd()
    t.seth(270)
    t.forward(100)

def draw_unfinished():
    pass  # Not yet implemented

def draw_left_arm():
    t.pu()
    t.setpos(0, -20)
    t.pd()
    t.seth(225)
    t.forward(45)

def draw_right_arm():
    t.pu()
    t.setpos(0, -20)
    t.pd()
    t.seth(315)
    t.forward(45)

def draw_left_leg():
    t.pu()
    t.setpos(0,-100)
    t.pd()
    t.seth(225)
    t.forward(60)

def draw_right_leg():
    t.pu()
    t.setpos(0,-100)
    t.pd()
    t.seth(315)
    t.forward(60)
##For each one of the parts of the hang man, a function is made that sets the turtle at the location of the start of the line, and then I used the "Seth" function to turn 
##the turtle to face whever it needs to for that line.


word = choice('word fire freind monitor lebeda phone time until yesterday it was good day telephone napkin face thirteen flowers walls flag lamp post curtain compact disk protein bar bubble tea energy workout gym door handle frame books box fan drawer hangman'.split())
correct: set[str] = set()
wrong: set[str] = set()
MAX_GUESSES = 7
num_guesses = 0

draw_functions = [draw_head, draw_body, draw_left_arm, draw_right_arm, draw_left_leg, draw_right_leg] * (7 - 1)

draw_background()

while num_guesses < MAX_GUESSES:
    print(MAX_GUESSES - num_guesses, 'guesses left')
    clue = [letter if letter in correct else '-' for letter in word]
    print(' '.join(clue))
    if wrong:
        print('Wrong:', ' '.join(sorted(list(wrong))))

    guess = input('Guess? ')
    num_guesses += 1

    if guess == word:
        print('Right!')
        break
    if len(guess) > 1:
        print('Wrong')
    else:
        if guess in correct or guess in wrong:
            print('You already guessed that')
        else:
            if guess in word:
                print('Right')
                correct.add(guess)
            else:
                print('Wrong')
                wrong.add(guess)
                draw_functions[len(wrong) - 1]()