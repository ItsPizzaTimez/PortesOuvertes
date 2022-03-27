import qrcode

data = input('Mettez votre lien juste ici : ')
color_scan = input('Mettez votre couleur juste ici en anglais(important) pour les traits : ')
color_background = input('Mettez votre couleur juste ici en anglais(important) pour le fond du QRcode : ')

qrcode = qrcode.QRCode(
    version=3,
    box_size=3,
    border=5
)

qrcode.add_data(data)

img =  qrcode.make_image(fill_color=color_scan, back_color=color_background)

img.show('Ton super QRcode')