from PIL import Image

def open_image(file_path):
    return Image.open(file_path)

    
def get_pixel_values(image, row):
    return [image.getpixel((x, row))[2] for x in range(image.width)]

def extract_binary_data(pixel_values):
    return ''.join(map(str, pixel_values))

def decode_binary_string(binary_string):
    return ''.join(chr(int(binary_string[i*8:i*8+8], 2)) for i in range(len(binary_string)//8))

def main():
    image_path = 'hard_version.png'
    image = open_image(image_path)

    row_to_extract = 0
    pixel_values = get_pixel_values(image, row_to_extract)
    binary_data = extract_binary_data(pixel_values)
    res = ''.join(binary_data[x] for x in range(1, len(binary_data), 2))
    decoded_message = decode_binary_string(res)

    print(decoded_message)

if __name__ == "__main__":
    main()
