# Aaron Rasmussen
# CS 406
# Prof. Guyer
# April 5, 2024
#
# LED Interface
#############################################################################################################################################################

import PySimpleGUI as sg

# Define the layout of main program
layout = [
    [sg.Text("Enter your phrases to be displayed:")],
    [sg.Text('Phrase 1:'),sg.InputText(key='phrase1')],
    [sg.Text('Phrase 2:'), sg.InputText(key='phrase2')],
    [sg.Text('Phrase 3:'),sg.InputText(key='phrase3')],
    [sg.Text('Phrase 4:'), sg.InputText(key='phrase4')],
    [sg.Text('Phrase 5:'),sg.InputText(key='phrase5')],
    [sg.Text('Phrase 6:'), sg.InputText(key='phrase6')],
    [sg.Button("SUBMIT")],
    [sg.Button("Exit")]
]

# Create GUI window
window = sg.Window("LED Message Display", layout, size=(500, 500), keep_on_top=False)

#Variable Declarations:
p_one = None
p_two = None
p_three = None
p_four = None
p_five = None
p_six = None

# Infinite loop to continuously react to events, exits when window closed or button pressed
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event == "SUBMIT":
        p_one = values['phrase1']
        p_two = values['phrase2']
        p_three = values['phrase3']
        p_four = values['phrase4']
        p_five = values['phrase5']
        p_six = values['phrase6']
        print('Phrase1: ', p_one)
        print('Phrase2: ', p_two)
        print('Phrase3: ', p_three)
        print('Phrase4: ', p_four)
        print('Phrase5: ', p_five)
        print('Phrase6: ', p_six)


window.close()