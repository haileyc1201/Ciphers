import cipher


class AtbashCipher(cipher.Cipher):

  def __init__(self):
    #Calls the superclass constructor
    super().__init__() 

    #Initializes cipher bet as the reversed alphabet
    self._cipherbet = ['Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']


  
  
  def _encrypt_letter(self, letter) -> str:
    '''Encrypts a letter using the cipherbet'''
    #Appends through alphabet
    for i in range(0, len(self._alphabet)): 
      #If the letter is found
      if letter == self._alphabet[i]: 
        #Return the cipherbet letter at the same index
        return self._cipherbet[i] 
    #If the letter is not found in the alphabet, raise an index error
    raise IndexError("Letter not found in alphabet") 


  
  def _decrypt_letter(self, letter) -> str:
    '''Decrypts a letter using the cipherbet'''
    
    #Appends through cipherbet
    for i in range(0, len(self._cipherbet)): 
      #If the letter is found
      if letter == self._cipherbet[i]: 
        #Return the alphabet letter at the same index
        return self._alphabet[i] 

    #If the letter is not found in the cipherbet, raise an index error
    raise IndexError("Letter not found in cipherbet") 

