import PySimpleGUI as sg

def create_window(theme):
    sg.theme(theme)
    sg.set_options(font = 'Calibri 20')
    layout = [
        [sg.Text('Nummer', justification = 'center', expand_x = True, right_click_menu = theme_menu, key = '-TEXT-', pad = (10,20))],
        [sg.Button('Clear'), sg.Button('Enter')],
        [sg.Button(7) ,sg.Button(8),sg.Button(9),sg.Button('*', expand_x = True)],
        [sg.Button(4),sg.Button(5),sg.Button(6),sg.Button('/', expand_x = True)], 
        [sg.Button(1),sg.Button(2),sg.Button(3),sg.Button('-', expand_x = True)],  
        [sg.Button(0, expand_x = True),sg.Button('.'),sg.Button('+')],
        [sg.Button("Color",right_click_menu = theme_menu, expand_x = True,)]       
            ]

    return sg.Window('Calculator', layout)

theme_menu = ['menu',['LightBlue','DarkBlue','DarkGreen','random']]
window = create_window('LightGreen')
current_num = []
full_operation = []



while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event in theme_menu[1]:
        window.close()
        window = create_window(event)



    if event in ['0','1','2','3','4','5','6','7','8','9','.']:
        current_num.append(event)
        num_string = ''.join(current_num)
        window['-TEXT-'].update(num_string)

    if event in ['+','-','/','*']:
        full_operation.append(''.join(current_num))
        current_num = []
        full_operation.append(event)
        window['-TEXT-'].update('')


    if event == 'Enter':
        full_operation.append(''.join(current_num))
        result = eval(' '.join(full_operation)) 
        window['-TEXT-'].update(result)
        full_operation = []



    if event  == 'Clear':
        current_num = []
        full_operation = []
        window['-TEXT-'].update('')

window.close()
