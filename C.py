import itertools
import nufhe

# def get_cloud_key_dump_from_public():
# 	read_file = open('cloud_key', 'rb')
# 	data = read_file.read()
# 	return data

def compare_encrypted_bits(context, ciphertext1, ciphertext2, cloud_key):
    if len(ciphertext1.a) != len(ciphertext2.a):
        return False
    else:
        vm = context.make_virtual_machine(cloud_key)
        result = vm.gate_xor(ciphertext1, ciphertext2)
        return result

context = nufhe.Context()

cloud_key_dump = open('cloud_key', 'rb').read()
ciphertext1_dump = open('ciphertext1', 'rb').read()
ciphertext2_dump = open('ciphertext2', 'rb').read()

ctx1 = context.load_ciphertext(ciphertext1_dump)
ctx2 = context.load_ciphertext(ciphertext2_dump)
cl_key = context.load_cloud_key(cloud_key_dump)

aresame_enc = compare_encrypted_bits(context, ctx1, ctx2, cl_key)
aresame_enc_dump = aresame_enc.dumps()


with open('encrypted_compute', 'wb') as file:
    file.write(aresame_enc_dump)
