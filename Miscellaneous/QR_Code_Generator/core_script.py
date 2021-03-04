

import  qrcode
import qrcode.image.svg

#Use_Case_1
qr_code=qrcode.make("https://goo.gl/maps/XsY9KJqRtgxLjAsd8")
qr_code.save("Maps_Location.png") #Google_Maps_Lcoation

#Use_Case_2
qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=15,border=3)
qr.add_data("https://github.com/Tech-Knight-Danny/Proof-of-Concepts")  #Github Link
qr.make(fit=True)
qr_img=qr.make_image(fill_color="red",back_color="white")
qr_img.save("Github_QR_Code")

#Use_Case_3
factory=qrcode.image.svg.SvgPathImage #Scalable Vector Graphics
svg_img=qrcode.make("Hey there, this a random set of strings to demonstrate a QR code's use! ", image_factory=factory)
svg_img.save("QR_SVG.svg") #SVGs are used to scale an image up and down as needed without losing any quality, making it a great choice for responsive web design
