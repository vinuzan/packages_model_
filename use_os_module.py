from os_module import encrypt, decrypted

print(encrypt('README.md'))

x_files = encrypt('README.md')

print(x_files)

de_classified_x_files = decrypt(x_files)