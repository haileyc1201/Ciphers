
# Importing Abstract Base Classes (ABC)
import abc 

class Cipher(abc.ABC):

  def __init__(self):
    
    #Initializing alphabet as a list containing all letters in the alphabet
    self._alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


  #Get private variable _alphabet using a decorator
  @property 
  def get_alphabet (self):
    '''returns alphabet'''
    return self._alphabet


  def encrypt_message (self, msg):
    '''receives an unencrypted message and returns the encrypted message'''

    #Setting message to uppercase
    message = msg.upper() 
    #Initializing new message
    new_message = "" 

    #Iterating through each character in message
    for letter in message: 
       #If character is in the alphabet
      if letter in self._alphabet:
        #Encrypt letter and append to new message
        new_message += self._encrypt_letter(letter) 

      #If the character is not in the alphabet
      else: 
        #Append character
        new_message += letter 

    #Return new message
    return new_message 
        
      

  def decrypt_message (self, msg) -> str:
    '''receives an encrypted message and returns the decrypted message'''

    #Setting message to uppercase
    message = msg.upper() 
    #Initializing new message
    new_message = "" 

    #Iterating through each character in message
    for letter in message: 
      #If character is in the alphabet
      if letter in self._alphabet : 
        #Decrypt letter and append to new message
        new_message += self._decrypt_letter(letter) 

      #If the character is not in the alphabet
      else: 
        #Append character
        new_message += letter 

    #Return new message
    return new_message 



  
  #Decorator for abstract methods to be overwritten by subclasses
  @abc.abstractmethod
  def _encrypt_letter (self, letter) -> str:
    '''overwritten by subclasses to encrypt single letters'''
    pass

  @abc.abstractmethod
  def _decrypt_letter (self, letter) -> str:
    '''overwritten by subclasses to decrypt a single letter'''
    pass

  
  