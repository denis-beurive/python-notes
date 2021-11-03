import qrcode

qr: qrcode.main.QRCode = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data('Some data')
qr.make(fit=True)

img: qrcode.image = qr.make_image(fill_color="black", back_color="white")
img.save("some_file.png")