import qrcode

# generate QR code 
# meassage as "Hello world"
#qr = qrcode.make("Hello World")

# save QR code as image in PNG format
#qr.save('MyQRcode.png')

# qr code with web link 

# define size of qr code
qr = qrcode.QRCode(
    version=1.0,
    box_size=10,
    border=10
)

link = 'linkedin.com/in/laxman-magar-002b05147'
qr.add_data(link)
qr.make(fit=True)
img = qr.make_image()
img.save('LaxmanLinkedIn.png')