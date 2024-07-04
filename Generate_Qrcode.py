import qrcode

qr_img = qrcode.make("www.linkedin.com/in/kelas")

qr_img.save("QR-Code-Image.jpg")