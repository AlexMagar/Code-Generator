import qrcode

# generate QR code 
# meassage as "Hello world"
qr = qrcode.make("Hello World")

# save QR code as image in PNG format
qr.save('MyQRcode.png')