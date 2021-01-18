import PySimpleGUI as sg

def main():
    layout = [[sg.Text('0.0000', size=(15, 1), font=('Helvetica', 18), text_color='black', key='_DISPLAY_')],
          [sg.Text('Last Operation')],
          [sg.Button('(',size=(7,2)), sg.Button(')',size=(7,2)), sg.Button('c',size=(7,2)), sg.Button('«',size=(7,2))],
          [sg.Button('7',size=(7,2)), sg.Button('8',size=(7,2)), sg.Button('9',size=(7,2)), sg.Button('÷',size=(7,2))],
          [sg.Button('4',size=(7,2)), sg.Button('5',size=(7,2)), sg.Button('6',size=(7,2)), sg.Button('x',size=(7,2))],
          [sg.Button('1',size=(7,2)), sg.Button('2',size=(7,2)), sg.Button('3',size=(7,2)), sg.Button('-',size=(7,2))],
          [sg.Button('.',size=(7,2)), sg.Button('0',size=(7,2)), sg.Button('=',size=(7,2)), sg.Button('+',size=(7,2))]]
    window = sg.Window("My Calculator", layout=layout, size=(350, 320)).read()

    # while True:
    #     event, values = window.read()
    #     if event is None:
    #         break
    #     if event in ['0','1','2','3','4','5,','6','7','8','9']:
    #         number_click(event)

if __name__ == '__main__':
    main()
