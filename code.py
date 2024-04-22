import qrcode
from PIL import Image

def generate_qr_code(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=20,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # QR code ko display karne ke liye
    img.show()

    # QR code ko save karna
    img.save("C:\\Users\\mrahe\\Desktop\\tuesday_class\\flask\\internship.png")
    print("file save")

if __name__ == "__main__":
    website_link = "https://google.com"  # Aapka website ka link yahaan daalein
    generate_qr_code(website_link)
