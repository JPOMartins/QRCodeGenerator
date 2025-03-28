import qrcode

def generate_qr_code(url, output_file):
    if not output_file.lower().endswith(".png"):
        output_file += ".png"
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)

def main():
    url = input("Enter the URL: ")
    output_file = input("Enter the output file name: ")

    generate_qr_code(url, output_file)
    print(f"QR Code generated and saved as {output_file}")
    print("Welcome to the QR Code Generator!")

if __name__ == "__main__":
    main()