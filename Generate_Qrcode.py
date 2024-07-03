import qrcode
qr_img = qrcode.make("www.linkedin.com/in/kelash")

qr_img.save("qr-img.jpg")