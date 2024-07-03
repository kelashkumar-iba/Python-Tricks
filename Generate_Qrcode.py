import qrcode

qr_img = qrcode.make("www.linkedin.com/in/eh")

qr_img.save("QR-Code-Image.jpg")