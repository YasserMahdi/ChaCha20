

def img_loader(input_path):
    with open(input_path, 'rb') as img_file:
        img_data = img_file.read()
    return  img_data

def img_writter(output_path,enc_img):
    with open(output_path, 'wb') as enc_file:
        enc_file.write(enc_img)

