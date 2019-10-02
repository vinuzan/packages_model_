import os #functional module
#lests create a module to encrypt and decrypt a file.

def encrypt(file):
    encode = os.fsencode(file)
    return encoded_file
    #enecrypt some file
    #return dsif rncrypted file

def decrypt(file):
    decoded_file = os.fsdecode(file)
    return decoded_file