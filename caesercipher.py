import cipher


class CaeserCipher(cipher.Cipher):

  def __init__ (self, shift):
    '''Initializes shift and alphabet which are used to create cipherbet'''
    #Calls the superclass for alphabet
    super().__init__() 
    #Initializes cipherbet as an empty list
    self._cipherbet = [] 

    #Iterates through and appends the shifted alphabet to the cipherbet
    for i in range(len(self._alphabet)): 
      location = i + shift 
      if location >= 26:
        location -= 26
      self._cipherbet.append(self._alphabet[location])

    #Initializes shift as the shift value
    self._shift = shift 


  
  def _encrypt_letter(self, letter) -> str:
    '''Looks up letter location in alphabet, then returns letter for cipherbet'''
    #Iterates through alphabet
    for i in range(len(self._alphabet)): 
      #If letter is found
      if letter == self._alphabet[i]: 
        #Return the cipherbet letter at the same index
        return self._cipherbet[i] 
        
    #If the letter is not found in the alphabet, raise an index error
    raise IndexError("Letter not found in alphabet") 
    


  
  def _decrypt_letter(self, letter) -> str:
    '''Looks up letter location in cipherbet, then returns letter for alphabet'''
    #Iterates through cipherbet
    for i in range(len(self._cipherbet)): 
      #If letter is found
      if letter == self._cipherbet[i]: 
        #Return the alphabet letter at the same index
        return self._alphabet[i] 

    #If the letter is not found in the cipherbet, raise an index error
    raise IndexError("Letter not found in alphabet") 

  
  



    