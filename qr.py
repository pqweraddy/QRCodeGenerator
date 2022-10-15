# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 20:33:53 2022

@author: Paddy
"""

import PySimpleGUI as sg
import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)

sg.theme('Dark')

layout1 = [
          [sg.Text('Select Type', size=(20, 1), justification='center')],
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
        [sg.Text('website', size=(10, 1)),sg.I(size=(30,1),key='url')],        
        [sg.Text('Street', size=(10, 1)),sg.I(size=(30,1),key='st')],
        [sg.Text('City', size=(10, 1)),sg.I(size=(12,1),key='city'), 
         sg.Text('ZIP Code', size=(8, 1)),sg.I(size=(7,1),key='zi')], 
        [sg.Text('State', size=(10, 1)),sg.I(size=(30,1),key='state')],
        [sg.Text('Country', size=(10, 1)),sg.I(size=(30,1),key='coun')],
        [sg.Text('choose your style', size=(40, 1), justification='center')],
        [sg.Radio('Default','style',key='stylev_default',default=True,size=(10,1)),
         sg.Radio('小方格','style',key='stylev_2',default=False,size=(10,1)),
         sg.Radio('圓點','style',key='stylev_3',default=False,size=(10,1))],
        [sg.Radio('圓角方格','style',key='stylev_4',default=False,size=(10,1)),
         sg.Radio('直線','style',key='stylev_5',default=False,size=(10,1)),
         sg.Radio('橫線','style',key='stylev_6',default=False,size=(10,1)),],
        [sg.B('Browser',
         size=(10, 1),key='vcard',enable_events=True)],
        [sg.B('Generate',size=(10, 1),key='vcok',enable_events=True,button_color='red'),
         sg.B('Cancel',size=(10, 1),key='cancel2',enable_events=True,button_color='gray')]
    ]

layout3 = [
        [sg.Text('Input Your Website', size=(40, 1), justification='center')],
        [sg.Text('Website', size=(10, 1)),sg.I(size=(30,1),key='web',default_text="https://")],
        [sg.Text('Choose Your Style', size=(40, 1), justification='center')],
        [sg.Radio('Default','style',key='stylew_default',default=True,size=(10,1)),
         sg.Radio('小方格','style',key='stylew_2',default=False,size=(10,1)),
         sg.Radio('圓點','style',key='stylew_3',default=False,size=(10,1))],
        [sg.Radio('圓角方格','style',key='stylew_4',default=False,size=(10,1)),
         sg.Radio('直線','style',key='stylew_5',default=False,size=(10,1)),
         sg.Radio('橫線','style',key='stylew_6',default=False,size=(10,1)),],
        [sg.B('Browser',
         size=(10, 1),key='vcard',enable_events=True)],
        [sg.B('Generate',size=(10, 1),key='webok',enable_events=True,button_color='red'),
         sg.B('Cancel',size=(10, 1),key='cancel3',enable_events=True,button_color='gray')]
    ]

layout = [[sg.Column(layout1, key='-COL1-'), sg.Column(layout2, visible=False, key='-COL2-'), sg.Column(layout3, visible=False, key='-COL3-')],
          [sg.Text('A Paddy Lee Production', size=(20, 1), justification='center')]]




# 視窗顯示
window = sg.Window('QR Code Generator', layout)
str = ""

# 事件循環
while True:
    web=""
    event, values = window.read()
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break
    elif event == 'text':
        window[f'-COL1-'].update(visible=False)
        window[f'-COL3-'].update(visible=True)
        
    elif event == 'cancel2':
        window[f'-COL2-'].update(visible=False)
        window[f'-COL1-'].update(visible=True)

    elif event == 'cancel3':
        window[f'-COL3-'].update(visible=False)
        window[f'-COL1-'].update(visible=True)
        
    elif event == 'vcard':
        window[f'-COL1-'].update(visible=False)
        window[f'-COL2-'].update(visible=True)
            
    elif event == 'webok':
        web = values['web'];
        qr.add_data(web)
        qr.make(fit=True)
<<<<<<< Updated upstream
        img = qr.make_image()
        #type(img)  # qrcode.image.pil.PilImage
        img.save("some_file.png")
        img.show()

        window[f'-COL3-'].update(visible=False)
        window[f'-COL1-'].update(visible=True)
=======
        if values["stylew_default"] == True:
            img = qr.make_image(image_factory=StyledPilImage, module_drawer=SquareModuleDrawer())
            img.save("some_file.png")
            img.show()
        elif values["stylew_2"] == True:
            img = qr.make_image(image_factory=StyledPilImage, module_drawer=GappedSquareModuleDrawer())
            img.save("some_file.png")
            img.show()
        elif values["stylew_3"] == True:
            img = qr.make_image(image_factory=StyledPilImage, module_drawer=CircleModuleDrawer())
            img.save("some_file.png")
            img.show()
        elif values["stylew_4"] == True:
            img = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
            img.save("some_file.png")
            img.show()
        elif values["stylew_5"] == True:
            img = qr.make_image(image_factory=StyledPilImage, module_drawer=VerticalBarsDrawer())
            img.save("some_file.png")
            img.show()
        elif values["stylew_6"] == True:
            img = qr.make_image(image_factory=StyledPilImage, module_drawer=HorizontalBarsDrawer())
            img.save("some_file.png")
            img.show()
        else:
            sg.popup("Please Select Your Style")
        window['-COL3-'].update(visible=False)
        window['-COL1-'].update(visible=True)
>>>>>>> Stashed changes
        
           # 要轉換成 QRCode 的文字
          # 根據參數製作為 QRCode 物件

      # 產生 QRCode 圖片
        
    elif event == 'vcok':
        fn = values['fn']
        ln = values['ln']
        tel = values['tel']
        st = values['st']
        city = values['city']
        state = values['state']
        coun = values['coun']
        email = values['email']
        url = values['url']
        zi = values['zi']
        
        template = """
BEGIN:VCARD
VERSION:3.0
N:{};{}
FN:{} {}
ADR:;;{};{};{};{};{}
TEL;CELL:{}
EMAIL;WORK;INTERNET:{}
URL:{}
END:VCARD
""".format(ln,fn,fn,ln,st,city,state,zi,coun,tel,email,url)
        qr.add_data(template)
        qr.make(fit=True)
<<<<<<< Updated upstream
        img = qr.make_image()
        #type(img)  # qrcode.image.pil.PilImage
        img.save("some_file.png")
        img.show()
        
        window[f'-COL2-'].update(visible=False)
        window[f'-COL1-'].update(visible=True)
=======
        if values["stylev_default"] == True:
            img = qr.make_image(image_factory=StyledPilImage, module_drawer=SquareModuleDrawer())
            img.save("some_file.png")
            img.show()
        elif values["stylev_2"] == True:
            img = qr.make_image(image_factory=StyledPilImage, module_drawer=GappedSquareModuleDrawer())
            img.save("some_file.png")
            img.show()
        elif values["stylev_3"] == True:
            img = qr.make_image(image_factory=StyledPilImage, module_drawer=CircleModuleDrawer())
            img.save("some_file.png")
            img.show()
        elif values["stylev_4"] == True:
            img = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
            img.save("some_file.png")
            img.show()
        elif values["stylev_5"] == True:
            img = qr.make_image(image_factory=StyledPilImage, module_drawer=VerticalBarsDrawer())
            img.save("some_file.png")
            img.show()
        elif values["stylev_6"] == True:
            img = qr.make_image(image_factory=StyledPilImage, module_drawer=HorizontalBarsDrawer())
            img.save("some_file.png")
            img.show()
        else:
            sg.popup("Please Select Your Style")
        window['-COL2-'].update(visible=False)
        window['-COL1-'].update(visible=True)
>>>>>>> Stashed changes
        
window.close()