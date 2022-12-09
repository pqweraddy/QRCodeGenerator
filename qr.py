# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 09:47:10 2022
@author: Paddy
install qrcode pillow pysimplegui
"""

import PySimpleGUI as sg
import qrcode
import webbrowser
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import VerticalBarsDrawer,RoundedModuleDrawer,HorizontalBarsDrawer,SquareModuleDrawer,GappedSquareModuleDrawer,CircleModuleDrawer
qr = qrcode.QRCode( #設定qrcode參數
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

sg.theme('Dark') #視窗主題設為黑色

layout1 = [ #主選單
          [sg.Text('Select Type', size=(20, 1), justification='center')],
          [sg.B('Hyperlink', 
           size=(10, 1),key='toweb',enable_events=True,button_color='red'),
           sg.B('Contacts',
           size=(10, 1),key='tovcard',enable_events=True,button_color='red')],
          [sg.B('Text', 
           size=(10, 1),key='totext',enable_events=True,button_color='red'),
           sg.B('View Author',
           size=(10, 1),key='view',enable_events=True,button_color='gray')],
          [sg.Exit()],
    ]

layout2 = [ #vcard選單
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
        [sg.Text('Choose Your Style', size=(40, 1), justification='center')],
        [sg.Radio('Default','stylev',key='stylev_default',default=True,size=(10,1)),
         sg.Radio('小方格','stylev',key='stylev_2',default=False,size=(10,1)),
         sg.Radio('圓點','stylev',key='stylev_3',default=False,size=(10,1))],
        [sg.Radio('圓角方格','stylev',key='stylev_4',default=False,size=(10,1)),
         sg.Radio('直線','stylev',key='stylev_5',default=False,size=(10,1)),
         sg.Radio('橫線','stylev',key='stylev_6',default=False,size=(10,1)),],
        [sg.Text("Select Logo: "), sg.FileBrowse(key="v_in")],
        [sg.B('Generate',size=(20, 1),key='vcok',enable_events=True,button_color='red'),
         sg.B('Cancel',size=(10, 1),key='cancel2',enable_events=True,button_color='gray')]
    ]

layout3 = [ #web選單
        [sg.Text('Input Your Website', size=(40, 1), justification='center')],
        [sg.Text('Website', size=(10, 1)),sg.I(size=(30,1),key='web',default_text="https://")],
        [sg.Text('Choose Your Style', size=(40, 1), justification='center')],
        [sg.Radio('Default','stylew',key='stylew_default',default=True,size=(10,1)),
         sg.Radio('小方格','stylew',key='stylew_2',default=False,size=(10,1)),
         sg.Radio('圓點','stylew',key='stylew_3',default=False,size=(10,1))],
        [sg.Radio('圓角方格','stylew',key='stylew_4',default=False,size=(10,1)),
         sg.Radio('直線','stylew',key='stylew_5',default=False,size=(10,1)),
         sg.Radio('橫線','stylew',key='stylew_6',default=False,size=(10,1)),],
        [sg.Text("Select Logo: "), sg.FileBrowse(key="w_in")],
        [sg.B('Generate',size=(20, 1),key='webok',enable_events=True,button_color='red'),
         sg.B('Cancel',size=(10, 1),key='cancel3',enable_events=True,button_color='gray')]
    ]
layout4 = [ #text選單
        [sg.Text('Input Your Text', size=(40, 1), justification='center')],
        [sg.Text('Text', size=(10, 1)),sg.I(size=(30,1),key='text')],
        [sg.Text('Choose Your Style', size=(40, 1), justification='center')],
        [sg.Radio('Default','stylet',key='stylet_default',default=True,size=(10,1)),
         sg.Radio('小方格','stylet',key='stylet_2',default=False,size=(10,1)),
         sg.Radio('圓點','stylet',key='stylet_3',default=False,size=(10,1))],
        [sg.Radio('圓角方格','stylet',key='stylet_4',default=False,size=(10,1)),
         sg.Radio('直線','stylet',key='stylet_5',default=False,size=(10,1)),
         sg.Radio('橫線','stylet',key='stylet_6',default=False,size=(10,1)),],
        [sg.Text("Select Logo: "), sg.FileBrowse(key="t_in")],
        [sg.B('Generate',size=(20, 1),key='textok',enable_events=True,button_color='red'),
         sg.B('Cancel',size=(10, 1),key='cancel4',enable_events=True,button_color='gray')]
    ]


#初始設定只顯示主選單
layout = [[sg.Column(layout1, key='-COL1-'), sg.Column(layout2, visible=False, key='-COL2-'), 
           sg.Column(layout3, visible=False, key='-COL3-'), sg.Column(layout4, visible=False, key='-COL4-')],
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
    #控制各選單顯示或隱藏
    elif event == 'tovcard':
        window['-COL1-'].update(visible=False)
        window['-COL2-'].update(visible=True)
        
    elif event == 'toweb':
        window['-COL1-'].update(visible=False)
        window['-COL3-'].update(visible=True)
        
    elif event == 'totext':
        window['-COL1-'].update(visible=False)
        window['-COL4-'].update(visible=True)

    elif event == 'cancel2':
        window['-COL2-'].update(visible=False)
        window['-COL1-'].update(visible=True)

    elif event == 'cancel3':
        window['-COL3-'].update(visible=False)
        window['-COL1-'].update(visible=True)
        
    elif event == 'cancel4':
        window['-COL4-'].update(visible=False)
        window['-COL1-'].update(visible=True)
        
        
    elif event == 'view':
        webbrowser.open("https://youtu.be/dQw4w9WgXcQ")
        sg.popup("you got rickroll'd",title="lol")

    #製作超連結
    elif event == 'webok':
        web = values['web']; #讀取輸入值
        path = r"{}".format(values['w_in']); #嵌入圖片路徑
        qr.add_data(web)
        qr.make(fit=True)
        #選取樣式
        if values["stylew_default"] == True:
            img = qr.make_image(image_factory=StyledPilImage, module_drawer=SquareModuleDrawer(),embeded_image_path=path)
            img.save("web.png")
            img.show()
        elif values["stylew_2"] == True:
            img = qr.make_image(image_factory=StyledPilImage, module_drawer=GappedSquareModuleDrawer(),embeded_image_path=path)
            img.save("web.png")
            img.show()
        elif values["stylew_3"] == True:
            img = qr.make_image(image_factory=StyledPilImage, module_drawer=CircleModuleDrawer(),embeded_image_path=path)
            img.save("web.png")
            img.show()
        elif values["stylew_4"] == True:
            img = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer(),embeded_image_path=path)
            img.save("web.png")
            img.show()
        elif values["stylew_5"] == True:
            img = qr.make_image(image_factory=StyledPilImage, module_drawer=VerticalBarsDrawer(),embeded_image_path=path)
            img.save("web.png")
            img.show()
        elif values["stylew_6"] == True:
            img = qr.make_image(image_factory=StyledPilImage, module_drawer=HorizontalBarsDrawer(),embeded_image_path=path)
            img.save("web.png")
            img.show()
        window['-COL3-'].update(visible=False)
        window['-COL1-'].update(visible=True)

    #製作文字
    elif event == 'textok':
        web = values['text'];
        path = r"{}".format(values['t_in']);
        qr.add_data(web)
        qr.make(fit=True)
        if values["stylet_default"] == True:
            img = qr.make_image(image_factory=StyledPilImage, module_drawer=SquareModuleDrawer(),embeded_image_path=path)
            img.save("text.png")
            img.show()
        elif values["stylet_2"] == True:
            img = qr.make_image(image_factory=StyledPilImage, module_drawer=GappedSquareModuleDrawer(),embeded_image_path=path)
            img.save("text.png")
            img.show()
        elif values["stylet_3"] == True:
            img = qr.make_image(image_factory=StyledPilImage, module_drawer=CircleModuleDrawer(),embeded_image_path=path)
            img.save("text.png")
            img.show()
        elif values["stylet_4"] == True:
            img = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer(),embeded_image_path=path)
            img.save("text.png")
            img.show()
        elif values["stylet_5"] == True:
            img = qr.make_image(image_factory=StyledPilImage, module_drawer=VerticalBarsDrawer(),embeded_image_path=path)
            img.save("text.png")
            img.show()
        elif values["stylet_6"] == True:
            img = qr.make_image(image_factory=StyledPilImage, module_drawer=HorizontalBarsDrawer(),embeded_image_path=path)
            img.save("text.png")
            img.show()
        window['-COL4-'].update(visible=False)
        window['-COL1-'].update(visible=True)
    
    #製作vcard
    elif event == 'vcok':
        path = r"{}".format(values['v_in']);
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
        #vcard格式
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
        if values["stylev_default"] == True:
            img = qr.make_image(image_factory=StyledPilImage, module_drawer=SquareModuleDrawer(),embeded_image_path=path)
            img.save("contact.png")
            img.show()
        elif values["stylev_2"] == True:
            img = qr.make_image(image_factory=StyledPilImage, module_drawer=GappedSquareModuleDrawer(),embeded_image_path=path)
            img.save("contact.png")
            img.show()
        elif values["stylev_3"] == True:
            img = qr.make_image(image_factory=StyledPilImage, module_drawer=CircleModuleDrawer(),embeded_image_path=path)
            img.save("contact.png")
            img.show()
        elif values["stylev_4"] == True:
            img = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer(),embeded_image_path=path)
            img.save("contact.png")
            img.show()
        elif values["stylev_5"] == True:
            img = qr.make_image(image_factory=StyledPilImage, module_drawer=VerticalBarsDrawer(),embeded_image_path=path)
            img.save("contact.png")
            img.show()
        elif values["stylev_6"] == True:
            img = qr.make_image(image_factory=StyledPilImage, module_drawer=HorizontalBarsDrawer(),embeded_image_path=path)
            img.save("contact.png")
            img.show()
        window['-COL2-'].update(visible=False)
        window['-COL1-'].update(visible=True)
window.close()
