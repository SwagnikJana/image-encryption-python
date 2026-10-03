from PIL import Image


def encrypt_decrypt_image(input_file, output_file, key):
    
    image = Image.open(input_file)

    
    image = image.convert("RGB")

    
    pixels = image.load()

    
    for x in range(image.width):
        for y in range(image.height):

            r, g, b = pixels[x, y]

            
            r = r ^ key
            g = g ^ key
            b = b ^ key

            
            pixels[x, y] = (r, g, b)

    
    image.save(output_file)

    print("Image processed successfully!")
    print("Saved as:", output_file)


print("===== IMAGE ENCRYPTION TOOL =====")
print("1. Encrypt Image")
print("2. Decrypt Image")

choice = input("Enter your choice (1 or 2): ")

input_file = input("Enter input image path: ")
output_file = input("Enter output image path: ")

key = int(input("Enter encryption key (0-255): "))

if key < 0 or key > 255:
    print("Key must be between 0 and 255.")
else:
    encrypt_decrypt_image(input_file, output_file, key)