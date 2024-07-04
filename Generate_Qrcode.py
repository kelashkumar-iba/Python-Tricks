import qrcode

qr_img = qrcode.make("www.linkedin.com/in/klh")

qr_img.save("QR-Code-Image.jpg")