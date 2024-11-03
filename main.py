#Names: Hailey Clark and Lexi Nguyen (Lab 7, Group 4)
#Date: 03/12/24
#Description: A program that decrypts or encrypts messages and saving it to a file. 


import atbashcipher
import caesercipher
import check_input


def main():

  rep = 1
  while rep == 1:
    # Printing main menu
    print()
    print("-*-:Secret Decoder Ring:-*-")
    print()

    # Allowing user to decide to decrypt or encrypt a message
    print("1. Encrypt \n2. Decrypt \n")
    user_input = check_input.get_int_range("Number: ", 1, 2)
    print()
  
    if user_input == 1: # If the user chooses to encrypt

      #Allowing user to decide their encryption type
      print("Enter Encryption Type: \n1. Atbash \n2. Caeser \n")
      print()
      user_choice = check_input.get_int_range("Number: ", 1, 2)

      #If the user chooses to encrypt with atbash
      if user_choice == 1:  
        #Get user's message 
        user_message = input("Enter Message: ") 

        #Open file to write to
        file = open("message.txt", "w") 
        #Write encrypted message
        file.write(atbashcipher.AtbashCipher().encrypt_message(user_message))
        #Close file
        file.close() 
        
        print("Encrypted message saved to \"message.txt\"")
        print()
        
      #If the user chooses to encrypt with caeser
      else:
        #Getting user's message
        user_message = input("Enter Message: ") 

        #Getting user's shift value 
        user_shift = check_input.get_int_range("Shift Value: ", 0, 25) 

        #Open file to write to
        file = open("message.txt", "w") 
        #Write encrypted message
        file.write(caesercipher.CaeserCipher(user_shift).encrypt_message(user_message)) 
        #Close file
        file.close() 
        print("Encrypted message saved to \"message.txt\"")
        print()

    #If user chooses to decrypt
    else: 

      #Get user input for decryption type
      print("Enter Decryption Type: \n1. Atbash \n2. Caeser \n")
      print()
      user_choice = check_input.get_int_range("Number: ", 1, 2)

      #If the user chooses to decrypt using atbash
      if user_choice == 1: 
        #Open text file to read from
        file = open("message.txt", "r") 
        print("Reading encrpyted message from \"message.txt\"...")
        #Print out decrypted message from file
        print("Decrpyted message: ", atbashcipher.AtbashCipher().decrypt_message(file.read()))
        #Close file
        file.close() 
        print()
    
      #If the user chooses to decrypt using Caeser cipher
      else: 
        #Open file to read from 
        file = open("message.txt", "r") 
        message = file.read()
        #Asking for shift value
        user_shift = check_input.get_int_range("Shift Value: ", 0, 25)
        print("Reading encrpyted message from \"message.txt\"...")
        #Printing decrypted message
        print("Decrpyted message:", caesercipher.CaeserCipher(user_shift).decrypt_message(message))
        file.close()
        print()

    #Asking user if they want to repeat the program
    rep = check_input.get_int_range("Would you like to repeat the program? \n1. Yes \n2. No \nNumber: ", 1, 2)
    print()

    print("The -*-:Secret Decoder Ring:-*- shuts down...")
      
main()