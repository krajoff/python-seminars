def compress(file):
    with open(file, 'r', encoding ='utf-8') as text:
        inp_str = text.readline()
        ind = 0
        out_str = ''
        count = 1
        while ind < len(inp_str) - 1:
            if inp_str[ind] == inp_str[ind + 1]:
                count += 1
            else:
                if count == 1:
                    out_str += inp_str[ind]
                else:
                    out_str += str(count) + inp_str[ind]
                count = 1
            ind += 1
#        else:
#            out_str += str(count) + inp_str[ind]
    print(out_str)

compress('input.txt')


def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1
    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding

print(rle_encode('AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB'))


prev_char=''