import qrcode

def read_text(file_path):
    with open(file_path,"r") as file:
        text = file.read()   
    return text

file_path = "/home/aashish/Documents/Python Training Class/message.txt"
text_message = read_text(file_path)
qr = qrcode.QRCode()
qr.add_data(text_message)
qr.make(fit=True)
img = qr.make_image(fill_color="blue",back_color="white")
img.save("QR.png")
print("Succes")