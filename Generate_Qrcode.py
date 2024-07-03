import qrcode

qr_img = qrcode.make("www.linkedin.com/in/kelah")

qr_img.save("QR-Code-Image.jpg")