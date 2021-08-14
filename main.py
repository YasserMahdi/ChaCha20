from BL.generators.hardmard import hardmard
from BL.generators.threshold import threshold
from BL.classifier import classify
import BL.Input_handler.image as imghandler
import BL.Input_handler.text as texthandle
import os
import PIL.Image
import io
from Crypto.Random import get_random_bytes
from BL.ciphering import ChaCha
from multiprocessing import Pool
from BL.analyzer import analyzer

#key =os.urandom(32)
#nonce = os.urandom(12)
#cip = ChaCha20(key,nonce,1)


#x^32+x^7+x^3+x^2+1
#x^32+x^27+x^7+1
#hm=hardmard('x^22+x^7+x^3+x^2+1','x^22+x^7+x^7+1')


# function1,max_period1 = analyzer('x^12+x^7+x^4+x^3+1').convert_pol_to_bin()
# function2,max_period2 = analyzer('x^12+x^11+x^10+x^4+1').convert_pol_to_bin()
# bit_to_xor_s1 = [0,2,3,6,11]
# bit_to_xor_s2 = [0,3,9,10,11]


function1,max_period1 = analyzer('x^5+x^2+1').convert_pol_to_bin()
function2,max_period2 = analyzer('x^5+x^3+1').convert_pol_to_bin()
bit_to_xor_s1 = [0,1,4]
bit_to_xor_s2 = [0,2,4]

max_clock = (2 ** int(max_period1) - 1)
hm=hardmard(function1,function2,bit_to_xor_s1,bit_to_xor_s2,max_clock)
#
hm.start_key_streamming()


# function1,max_period1 = analyzer('x^7+x^3+1').convert_pol_to_bin()
# function2,max_period2 = analyzer('x^7+x^5+1').convert_pol_to_bin()
# function3,max_period3 = analyzer('x^7+x^6+1').convert_pol_to_bin()
# bit_to_xor = [0,2,4]
# max_clock = ((2 ** int(max_period1)) - 1) * ((2 ** int(max_period2))-1) * ((2 ** int(max_period3))-1)
#
# th = threshold(function1,function2,function3,bit_to_xor,max_clock)
# th.start_key_streamming()
x=0
input_path = r'C:\Users\yasse\PycharmProjects\dsc\BL\input\aex.txt'
output_path1 = r'C:\Users\yasse\PycharmProjects\dsc\BL\output\aexc.txt'
output_path2 = r'C:\Users\yasse\PycharmProjects\dsc\BL\output\aexd.txt'
file_name, file_extension = os.path.splitext(input_path)
file_extension = file_extension.replace('.','')
file_type = classify(file_extension)
# declaring an integer value
integer_val = 11000000000000000000001010001110
# converting int to bytes with length
# of the array as 2 and byter order as big
bytes_val = integer_val.to_bytes(32, 'big')
key = [0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0]


key =bytearray(key)
key = key[1:33]
nonce = get_random_bytes(12)
encryptor = ChaCha.ChaCha(key, nonce)

if (file_type == "imageFiles"):


    enc_img = encryptor.ImgEncrypt(imghandler.img_loader(input_path))
    imghandler.img_writter(output_path1,enc_img)



    res = encryptor.ImgDecrypt(imghandler.img_loader(output_path1))
    img_stream = io.BytesIO(res)
    img_file = PIL.Image.open(img_stream)
    img_file.save(output_path2)

    print(file_type)
elif (file_type == "textFiles"):
    plaintext = texthandle.ReadText(input_path)
    ciphertext = encryptor.encrypt(plaintext)
    # print(ciphertext)
    ciphertext = bytes(ciphertext)
    texthandle.WriteText(output_path1,ciphertext)


    ciphertext = texthandle.ReadText(output_path1)
    plaintext = encryptor.decrypt(ciphertext)
    texthandle.WriteText(output_path2,plaintext)

else:
    print("File Type Is " + file_type)

