import turtle
import pandas

scr = turtle.Screen()
scr.title('States Game')
img = 'blank_states_img.gif'
scr.addshape(img)
guesses = []
wrong = []

turtle.shape(img)

while len(guesses)  <50:
    answer = scr.textinput(title=f"{len(guesses)}/50", prompt="What's another state's name?")
    if answer == 'exit' or answer == 'Exit':
        break
    elif answer == str:
        answer.title()
    df = pandas.read_csv('50_states.csv')
    state_list =df.state.to_list()

   


    if answer in state_list:
        print('Correct')
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_row = df[df.state== answer]
        t.goto(int(state_row.x), int(state_row.y))
        t.write(answer)
        guesses.append(answer)

    else:
        wrong.append(answer)


export = pandas.DataFrame(wrong)
export.to_csv('states_to_learn.csv')

#turtle.mainloop()
scr.exitonclick()


