##############################################################################
# COMPONENT:
#    CIPHER01
# Author:
#    <Jeff Pitcher>
# Summary:
#    Implement your cipher here. You can view 'example.py' to see the
#    completed Caesar Cipher example.
##############################################################################


##############################################################################
# CIPHER
##############################################################################
class Cipher:
    #     # TODO: Insert anything you need for your cipher here
    def encrypt(self, plaintext, password):
        column = 10
        row = 10
        max = 100
        encrypt_dictionary = {}
        alphabet_size = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-=`~!@#$%^&*()_+\\|{}[]:;',./<>?ñáéíú\" "
        ascii_password = 0

        for letter in password: 
            ascii_password = ord(letter) + ascii_password
        shift = ascii_password % 100
        starting_letter = alphabet_size[shift]   
        current = shift

        for r in range(0,row):
            for c in range(0,column):   
                if current < max:
                    encrypt_dictionary[alphabet_size[current]] = f"{r}{c}"
                    shift += 1
                elif current >= max:
                    encrypt_dictionary[alphabet_size[current - max]] = f"{r}{c}"
                current += 1

        encrypted = ''
        encrypted_with_commas= ''
        for letter in plaintext:
            encrypted += f"{encrypt_dictionary[letter]}"
        for letter in plaintext:
            encrypted_with_commas += f"{encrypt_dictionary[letter]},"
        encrypted_with_commas = encrypted_with_commas[:-1]

        print(encrypted_with_commas)
        return encrypted_with_commas 

    def decrypt(self, ciphertext, password):
        encrypted_list = ciphertext.split(',')
        column = 10 
        row = 10 
        max = 100
        decrypt_dictionary = {}
        alphabet_size = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-=`~!@#$%^&*()_+\\|{}[]:;',./<>?ñáéíú\" "
        ascii_password = 0
        for letter in password: 
            ascii_password = ord(letter) + ascii_password
        shift = ascii_password % 100
        current = shift

        for r in range(0,row):
            for c in range(0,column):   
                if current < max:
                    decrypt_dictionary[f"{r}{c}"] = alphabet_size[current] 
                    shift += 1
                elif current >= max:
                    decrypt_dictionary[f"{r}{c}"] = alphabet_size[current - max]

                current += 1

        decrypted = ''
        for letter in encrypted_list:
            decrypted += f"{decrypt_dictionary[letter]}"
        
        return decrypted
        
    def get_author(self):
        # TODO: Return your name
        return "Jeff Pitcher"

    def get_cipher_name(self):
        # TODO: Return the cipher name
        return "Polybius Square Cipher"
        

    ##########################################################################
    # GET CIPHER CITATION
    # Returns the citation from which we learned about the cipher
    ##########################################################################
    def get_cipher_citation(self):
        # TODO: This function should return your citation(s)
        s = "practicalcryptography.com (2022), " \
            "\" practical cryptography - Polybius Square Cipher\', \n retrieved: " \
            "http://practicalcryptography.com/ciphers/classical-era/polybius-square/"
        return s

    ##########################################################################
    # GET PSEUDOCODE
    # Returns the pseudocode as a string to be used by the caller
    ##########################################################################
    def get_pseudocode(self):
        # TODO: This function should return your psuedocode, neatly formatted

        # The encrypt pseudocode
        pc = "below is the encryption pseudocode\n"\
            " \n"\
            "columns = 5\n"\
            "rows = 5\n"\
            "max = 25\n"\
            "start = 5\n"\
            "current = start\n"\
            " \n"\
            "for letter in password:\n"\
            "  start += ord(letter) % 25\n"\
            " \n"\
            "encryption = {}\n"\
            "alphabet = 'abcdefghijklmnopqrstuvwxy'\n"\
            " \n"\
            "for r in range(0,rows):\n"\
            "  for col in range(0,columns):\n"\
            "    # print(col)\n"\
            "    if current < max:\n"\
            "      encryption[alphabet[current]] = f'{r}{col}'\n"\
            "      start += 1\n"\
            "    elif current > max:\n"\
            "      encryption[alphabet[current - max]] = f'{r}{col}'\n"\
            " \n"\
            "    current += 1\n"\
            " \n"\
            "print(encryption)\n"\
            " \n"\
            "encryptedMessage = ''\n"\
            "for letter in plaintext:\n"\
            "  encryptedMessage += f'{encryption[letter]} '\n"\
            " \n"\
            "print(encryptedMessage)\n"\
            "return ciphertext\n"\

        # The decrypt pseudocode
        pc += "below is the decryption pseudocode\n"\
            " \n"\
            "columns = 5\n"\
            "rows = 5\n"\
            "max = 25\n"\
            "start = 5\n"\
            "current = start\n"\
            " \n"\
            "for letter in password:\n"\
            "  start += ord(letter) % 25\n"\
            " \n"\
            "decryption = {}\n"\
            "alphabet = 'abcdefghijklmnopqrstuvwxy'\n"\
            " \n"\
            "for r in range(0,rows):\n"\
            "  for col in range(0,columns):\n"\
            "    # print(col)\n"\
            "    if current < max:\n"\
            "      decryption[f'{r}{col}'] = alphabet[current]\n"\
            "      start += 1\n"\
            "    elif current > max:\n"\
            "      decryption[f'r}{col}'] = alphabet[current - max]\n"\
            " \n"\
            "    current += 1\n"\
            " \n"\
            "print(decryption)\n"\
            "decryptedMessage = ''\n"\
            " \n"\
            "for letter in ciphertext:\n"\
            "  decryptedMessage += f'{decryption[letter]}'\n"\
            " \n"\
            "print(encryptedMessage)\n"\
            "return plaintext\n"\

        return pc
    