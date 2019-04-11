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

def get_secret_key_from_A():
	read_file = open('secret_key', 'rb')
	data = read_file.read()
	return data

ctx = nufhe.Context()

secret_key = ctx.load_secret_key( get_secret_key_from_A() )

bits2 = word_to_8_bit_binary("david")

ciphertext2 = ctx.encrypt(secret_key, bits2)
ciphertext2_dump = ciphertext2.dumps()

with open('ciphertext2', 'wb') as file:
    file.write(ciphertext2_dump)
