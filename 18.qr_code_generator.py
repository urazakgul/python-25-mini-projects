# Bu proje, kullanıcıların paylaşmak ve tarayabilecekleri QR kodları oluşturabilecekleri bir program oluşturmayı içerir.
# (This project involves creating a program that generates QR codes for the user to share and scan.)

import qrcode

data = "https://twitter.com/urazdev"
img = qrcode.make(data)
img.show()