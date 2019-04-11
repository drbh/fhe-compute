import nufhe

context = nufhe.Context()

result_dump = open('encrypted_compute', 'rb').read()
secret_key_dump = open('secret_key', 'rb').read()

results = context.load_ciphertext(result_dump)
secret_key = context.load_secret_key(secret_key_dump)

result_bits = context.decrypt(secret_key, results)
passed = not any(result_bits)
print(passed)
