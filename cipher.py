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
    def __init__(self):
        # TODO: Insert anything you need for your cipher here
        # self._minimum_value = '_'
        # self._maximum_value = '^'
        # self._alphabet_size = ord(self._maximum_value) \
                            # -ord(self._minimum_value) + 1
        # self.alphabet_index = [str(i//10 + 1) +str(i%10 +1) for i in range(len(self._alphabet_size))]
        self.encrypt_dictionary = {}
        self.decrypt_dictionary = {}
        self.column = 10 
        self.row = 10 
        # print(alphabet_index)
        # plaintext= ''
        # ciphertext = ''
    def encrypt(self, plaintext, password):
        alphabet_size = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-=`~!@#$%^&*()_+\|{}[]:;',./<>?ñáéíúóü"
        ascii_password = 0
        for letter in password: 
            ascii_password = ord(letter) + ascii_password
        shift = ascii_password % 100
        starting_letter = alphabet_size[shift]   
        print(alphabet_size)
        print(starting_letter)

        for row in range(0,self.row):
            for col in range(0,self.column):
            if self.current < max:
                self.encrypt_dictionary[f"{r}{col}"] = alphabet
        for letter in alphabet_size:
            self.encrypt_dictionary[]

        # i = ''
        # for l in range(len(plaintext[i])):
        #     if plaintext[i] in alphabet_index:
        #         ciphertext += alphabet_index[alphabet_size.index(plaintext[i])]
        #     else:
        #         ciphertext += plaintext[i]

        # return ciphertext
            
        # print (alphabet_index)
    # def password_to_key(alphabet_size):
    #     password_ascii = ord(self.alphabet_size)

    # def _index_from_character(self, letter):
    #     if letter > self._maximum_value or letter < self._minimum_value:
    #         return 0
    #     return ord(letter) - ord(self._value_minimum)

    # def _character_from_index(self, index_from_character):
    #     if index_from_character>= 0 and index_from_character< self._size_alphabet:
    #         return chr(index_from_character+ ord(self._value_minimum))
    #     return ' '

    # def _offset_from_password(self, password):
    #     offset_key= 0
    #     for c in password:
    #         offset_key+= self._index_from_character(c)
    #     return offset_key % self._alphabet_size
        
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

    # ##########################################################################
    # # GET PSEUDOCODE
    # # Returns the pseudocode as a string to be used by the caller
    # ##########################################################################
    # def get_pseudocode(self):
    #     # TODO: This function should return your psuedocode, neatly formatted

    #     # The encrypt pseudocode
    #     pc = "insert the encryption pseudocode\n"

    #     # The decrypt pseudocode
    #     pc += "insert the decryption pseudocode\n"

    #     return pc

    ##########################################################################
    # ENCRYPT
    # TODO: ADD description
    ##########################################################################
    # def encrypt(self, plaintext, password):
    #     ciphertext = plaintext
    #     # TODO - Add your code here

    #     # Trial code done here

    #     # plaintext = input("Please enter you message here: ")
    #     # if plaintext == "":
    #     #     plaintext = "I am just \"plain\" text ~ 12345."
    #     # password = input("Please enter your password: ")
    #     # if password == "":
    #     #     password = "P@55w0rd!"
    #     #     print(f"Default password: {password}") 
    #     #     encrypted = cipher.encrypt(plaintext, password)

    #     #working code
    #     # ciphertext = ""
        
    #     # # find a Caesar password from a textual password
    #     # offset_key = self._offset_from_password(password)
    #     # assert offset_key >= 0 and offset_key < self._size_alphabet

    #     # # convert the plaintext one character at a time
    #     # for p in plaintext:
    #     #     # convert the character into an index we can work with
    #     #     index_from_character = self._index_from_character(p)
            
    #     #     # perform the shift
    #     #     index_from_character += offset_key

    #     #     # make sure it is within range
    #     #     index_from_character %= self._size_alphabet
    #     #     assert index_from_character >= 0 and index_from_character < self._size_alphabet

    #     #     # send the index into the ciphertext
    #     #     ciphertext += self._character_from_index(index_from_character)

    #     return ciphertext

    ##########################################################################
    # DECRYPT
    # TODO: ADD description
    ##########################################################################
    def decrypt(self, ciphertext, password):
        plaintext = ciphertext
        # TODO - Add your code here

        # Trial code done here

    #     password = input("Please enter your password: ")
    # if password == "":
    #     password = "P@55w0rd!"
    #     print(f"Default password: {password}") 

        # working code
        plaintext = ""
        
        # find a Caesar password from a textual password
        offset_key = self._offset_from_password(password)
        assert offset_key >= 0 and offset_key < self._size_alphabet

        # make the offset backwards
        offset_key = self._size_alphabet - offset_key
        assert offset_key >= 0 and offset_key < self._size_alphabet

        # convert the ciphertext one character at a time
        for p in ciphertext:
            # convert the character into an index we can work with
            index_from_character = self._index_from_character(p)
            
            # perform the shift
            index_from_character += offset_key

            # make sure it is within range
            index_from_character %= self._size_alphabet
            assert index_from_character >= 0 and index_from_character < self._size_alphabet

            # send the index into the ciphertext
            plaintext += self._character_from_index(index_from_character)
        return plaintext