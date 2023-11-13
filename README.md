# Python 專題 - QR Code 產生器
## 主題發想
專題

## 預計規劃
1. QR Code 產生器
2. 圖形GUI介面
3. vCard 格式
## 參考範例
https://www.qr-code-generator.com/

## Start

### QR Code 程式碼簡介
python 本身有內建 QR Code 函式庫，安裝方法如下：
```
pip install qrcode
```
在程式中輸入：
```python=
import qrcode
img = qrcode.make('Some data here') #欲轉換為qrcode的內容
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png") #設定儲存檔名
```
執行程式，即可生成QR Code 圖檔，並儲存於該程式檔所屬資料夾中。

---

### vCard 格式

vCard是電子名片的文件格式標準
## 流程
首先我們先使用文字介面(Console Application)製作簡易QR Code 產生器，程式碼如下：
```python=
import qrcode

a=int(input("輸入你要轉換qrcode的格式/n網址:1, 聯絡人:2:"))

if(a==1):
    b=input("輸入你要轉換的網址:")
    img = qrcode.make(b)
    type(img)  # qrcode.image.pil.PilImage
    img.save("some_file.png")
    img.show()
elif (a==2):
    fn=input("first name:")
    ln=input("last name:")
    tel=input("tel:")
    email=input("email:")
    
    
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
```
### 測試
![](https://i.imgur.com/iSXdk6s.png)

執行程式後，會跳出文字介面選單，輸入1或2決定要製作何種格式的QR Code。上圖以製作超連結 QR Code 為例。

![](https://i.imgur.com/dViaMmi.png)


![](https://i.imgur.com/uPLb2U3.png)

![](https://i.imgur.com/QcWQ1pW.png)

![](https://i.imgur.com/tDLppme.png)
掃描結果
![](https://i.imgur.com/iBaYfxe.png)

---
## 轉換圖形頁面(GUI)
### PySimpleGUI
https://www.pysimplegui.org/en/latest/

```python=
import PySimpleGUI as sg

sg.theme('DarkAmber')   # 顏色主題
# 該視窗(layout)所有物件
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# 叫出視窗
window = sg.Window('Window Title', layout)
# 重複迴圈以獲取按鍵指示
while True:
    event, values = window.read()
    # 如果關閉視窗或按下"Cancel"
    if event == sg.WIN_CLOSED or event == 'Cancel': 
        break
    print('You entered ', values[0])

window.close()
```
![](https://i.imgur.com/rkq7eRa.png)
### something useful 

```python=6
layout1 = [ ]
layout2 = []
layout3 = []

layout = [[sg.Column(layout1, key='-COL1-'), 
           sg.Column(layout2, visible=False, key='-COL2-'),
           sg.Column(layout3, visible=False, key='-COL3')],]


# 視窗顯示
window = sg.Window('QR Code Generator', layout)
str = ""

# 消息循環
while True:
    event, values = window.read()
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
```
### 測試

![](https://i.imgur.com/NNIPgG2.png)

![](https://i.imgur.com/pn1RZ50.png)

![](https://i.imgur.com/vpD5nHu.png)

---
## 新增個性化選項
### 格子點樣式
python qrcode 函式庫有提供下列數種自定義qrcode樣式：

| 造型名稱             | 說明     |
| -------------------- | -------- |
| SquareModuleDrawer()|預設方格|
|GappedSquareModuleDrawer()|	小方格
|CircleModuleDrawer()	|圓點
|RoundedModuleDrawer()	|圓角方格
|VerticalBarsDrawer()	|直線
|HorizontalBarsDrawer()	|橫線

![](https://i.imgur.com/RhR2tLL.png)

```python
img = qr.make_image(image_factory=StyledPilImage, module_drawer=SquareModuleDrawer())
#於module_drawer中輸入你要的樣式
```
### QR Code 中央放置圖片
```python
img = qr.make_image(image_factory=StyledPilImage,embeded_image_path='sample.jpg')
#在 path 中輸入圖片路徑
```

### 程式實作
![](https://i.imgur.com/oyv64Oj.png)
![](https://i.imgur.com/SlBWiJz.png)

![](https://i.imgur.com/Cksmvu5.png)
![](https://i.imgur.com/qXktlcf.png)
![](https://i.imgur.com/XIN4RKK.png)

---
## 打包成exe檔
### autopytoexe
```
pip install auto-py-to-exe
```
![](https://i.imgur.com/w9PVrO8.png)

## 成品分享

[qrcode.exe](https://drive.google.com/file/d/1VrU4hV_vsyduRWFkR1MFj3QHTPcWdkam/view?usp=share_link)

## 後記
![](https://i.imgur.com/4dktBm8.png)

![](https://i.imgur.com/EI2AIpg.png)

## References

https://www.learnwithshin.com/post/%E5%88%A9%E7%94%A8python%E5%81%9A%E5%87%BAqr-code
https://www.qr-code-generator.com/solutions/vcard-qr-code/
https://vocus.cc/article/627bc705fd8978000146162a

https://steam.oxxostudio.tw/category/python/example/qrcode.html

使用PySimpleGUI
https://sa123.cc/b4kr4yclg4eicbe1gpp9.html
https://stackoverflow.com/questions/59500558/how-to-display-different-layouts-based-on-button-clicks-in-pysimple-gui-persis

## Credit
主題發想 : 李育烜
程式實作 : 李育烜
圖形設計 : 李育烜
debug : 李育烜 
## Contacts
email: pqweraddy@gmail.com
github: [@pqweraddy](https://github.com/pqweraddy)
Facebook: [李育烜](https://www.facebook.com/paddyyslee/) [李墊尺](https://www.facebook.com/batterylee87)
Instagram: [@paddyyslee](https://instagram.com/paddyyslee)
