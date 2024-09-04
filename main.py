import random as rd
import PySimpleGUI as sg
import string

class PasswordGenerator:
    def __init__(self):
        sg.theme('DarkBlue18')
        layout = [
            [sg.Text('Site/Software', size=(15, 1)), sg.Input(key='site', size=(20, 1))],
            [sg.Text('E-mail/User', size=(15, 1)), sg.Input(key='user', size=(20, 1))],
            [sg.Text('Number of characters'), 
             sg.Combo(values=list(range(1, 31)), key='total_chars', default_value=12, size=(5, 1))],
            [sg.Output(size=(32, 5))],
            [sg.Button('Generate Password')]
        ]
    
        self.janela = sg.Window('Password Generator', layout)

    def Start(self):
        while True:
            event, values = self.janela.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Generate Password':
                if self.validate_input(values):
                    self.generate_password(values)
                else:
                    sg.popup('Please fill in all fields and select a valid number of characters.')
    
        self.janela.close()

    def validate_input(self, values):
        return all(values[key] for key in ['site', 'user']) and values['total_chars']

    def generate_password(self, values):
        length = int(values['total_chars']) 
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(rd.choice(characters) for _ in range(length))
        print(password, flush=True)  
        self.save_password(password, values)

    def save_password(self, new_password, values):
        try:
            with open('passwords.txt', 'a') as archive:
                archive.write(f"Site/Software: {values['site']}, E-mail/User: {values['user']}, New Password: {new_password}\n")
            print('File has been saved!', flush=True) 
        except IOError as e:
            sg.popup(f'Error saving file: {e}')

gen = PasswordGenerator()
gen.Start()
