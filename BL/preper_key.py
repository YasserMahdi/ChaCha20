def key_loader(keypath):
    with open(keypath, "r") as myfile:
        data = myfile.read()
        return data


def split(word):
    return [char for char in word]


datalist = []


def chunks(l, n):
    length = len(l)
    i = 0
    for i in range(0, length, n):

        tempstr = []
        for j in range(i, i + 256):
            if ((i + n) % length < 256):
                break
            else:
                tempstr.append(int(l[j]))
        datalist.append(tempstr)
    return datalist

# word = split(data)
# # Driver code
# chnk = chunks(word, 256)
# print(chnk)
#
# # x = chunks(data,256)
