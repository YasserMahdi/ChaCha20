
def ReadText(input_path):
    with open(input_path, 'rb') as f:
        data = f.read()
    return data
def WriteText(output_path, data):
    with open(output_path, "wb") as f:
        # cipher = ciphertext.decode('utf-8')
        # print(cipher)
        f.write(data)

def key_stream_reader(path):
    keystream_array = []
    with open(path) as my_file:
        for line in my_file:
            keystream_array.append(line)
        return keystream_array

