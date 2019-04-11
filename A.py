import itertools
import nufhe

def word_to_8_bit_binary(str2convert):
    chars_as_binary = [list(bin(ord(ch))[2:].zfill(8)) for ch in str2convert]
    asbin = list(itertools.chain(*chars_as_binary))
    results = list(map(int, asbin))
    return results

def _8_bit_binary_to_word(bit_list):
    n = 8
    string = "".join(list(map(str, bit_list)))
    splitup = [string[i:i+n] for i in range(0, len(string), n)]
    rebased = [chr(int(x, 2)) for x in splitup]
    return "".join(rebased)

ctx = nufhe.Context()
secret_key, cloud_key = ctx.make_key_pair()

bits1 = word_to_8_bit_binary("david")
ciphertext1 = ctx.encrypt(secret_key, bits1)

ciphertext1_dump = ciphertext1.dumps()
cloud_key_dump = cloud_key.dumps()
secret_key_dump = secret_key.dumps()

with open('ciphertext1', 'wb') as file:
    file.write(ciphertext1_dump)

with open('cloud_key', 'wb') as file:
    file.write(cloud_key_dump)

with open('secret_key', 'wb') as file:
    file.write(secret_key_dump)
