import PySimpleGUI as sg
import qrcode

sg.theme('LightGreen')


layout1 = [
          [sg.Text('choose how you want to be', size=(40, 1), justification='left')],
          [sg.B('Hyperlink', 
           size=(10, 1),key='text',enable_events=True,button_color='red')],
          [sg.B('Contacts',
           size=(10, 1),key='vcard',enable_events=True,button_color='red')],
          [sg.Exit()],

    ]
layout2 = [
        [sg.Text('Input Your Information', size=(40, 1), justification='center')],
        [sg.Text('First Name', size=(10, 1)),sg.InputText(size=(30,1),key='fn')],
        [sg.Text('Last Name', size=(10, 1)),sg.Input(size=(30,1),key='ln')],
        [sg.Text('Telephone', size=(10, 1)),sg.I(size=(30,1),key='tel')],
        [sg.Text('email', size=(10, 1)),sg.I(size=(30,1),key='email')],
        [sg.B('Generate',
         size=(10, 1),key='vcok',enable_events=True,button_color='red')]
    ]

layout3 = [
        [sg.Text('Website', size=(10, 1)),sg.I(size=(30,1),key='web',default_text="https://")],
        [sg.B('Generate',
         size=(10, 1),key='webok',enable_events=True,button_color='red')]
    ]

layout = [[sg.Column(layout1, key='-COL1-'), sg.Column(layout2, visible=False, key='-COL2-'), sg.Column(layout3, visible=False, key='-COL3-')],
          [sg.Text('A Paddy Lee Production', size=(40, 1), justification='center')]]




# 視窗顯示
window = sg.Window('QR Code Generator', layout)
str = ""

# 消息循环
while True:
    event, values = window.read()
    # print(event,values)
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break
    elif event == 'text':
        window[f'-COL1-'].update(visible=False)
        window[f'-COL3-'].update(visible=True)
        
        
    elif event == 'vcard':
        window[f'-COL1-'].update(visible=False)
        window[f'-COL2-'].update(visible=True)
            
    elif event == 'webok':
        web = values['web'];
        img = qrcode.make(web)
        type(img)  # qrcode.image.pil.PilImage
        img.save("some_file.png")
        img.show()

        window[f'-COL3-'].update(visible=False)
        window[f'-COL1-'].update(visible=True)
        
    elif event == 'vcok':
        fn = values['fn']
        ln = values['ln']
        tel = values['tel']
        email = values['email']
        
        
        template = """
BEGIN:VCARD
VERSION:3.0
N:{};{}
FN:{} {}
TEL;CELL:{}
EMAIL;WORK;INTERNET:{}
END:VCARD
""".format(ln,fn,fn,ln,tel,email)
        img = qrcode.make(template)
        type(img)  # qrcode.image.pil.PilImage
        img.save("some_file.png")
        img.show()
        
        window[f'-COL2-'].update(visible=False)
        window[f'-COL1-'].update(visible=True)
        
window.close()