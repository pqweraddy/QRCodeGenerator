import qrcode

a=int(input("輸入你要轉換qrcode的格式,網址:1, 聯絡人:2:"))

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