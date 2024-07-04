import qrcode

qr_img = qrcode.make("www.linkedin.com/in/ke")

qr_img.save("QR-Code-Image.jpg")