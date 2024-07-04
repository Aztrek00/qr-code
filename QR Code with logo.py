import qrcode
from PIL import Image  # Import the correct class from Pillow

# Create the QR code with desired settings
qr = qrcode.QRCode(
    version=1,  # Adjust version for complexity (1 is smallest)
    box_size=10,  # Pixel size for each box in the QR code
    border=2  # White border width around the QR code
)

# Add the data to the QR code (replace with your desired URL)
qr.add_data("https://www.youtube.com/@CodeWithYu")

# Generate the QR code image
qr_img = qr.make_image(fill_color='red', back_color='white')

# Open and resize the logo (combined into one step)
logo = Image.open("./pngwing.com.png").resize((75, 50), Image.LANCZOS).convert("RGBA")

# Calculate the center coordinates for pasting
offset = ((qr_img.size[0] - 75) // 2, (qr_img.size[1] - 50) // 2)

# Paste the logo onto the QR code image
qr_img.paste(logo, offset)

# Save the final image
qr_img.save("qr_with_logo.png")
