#There are many steps to make this code work as a caesar cipher
#The first step is the easiest , yet to understand is very important.
#text = input("Enter the text to encrypt or decrypt: ")
#order_key = input("Enter the encryption key: ")
 #Notice that my key is shorter than the text above , so i will need to make this repeatedly encrypted around these words to make it fully encrypted.
#shift = 3
#I will be using the letters in the alphabet , there wont be scii code which will be more mathematical. 
#alphabet = 'abcdefghijklmnoqrstuvwxyz'
#For now you will needd to find the position each of your character will be in the alphabet. Using learned comma
#index = alphabet.find(text[0].lower())#Before the char funct , you can do this
#This way you can officially calling the index variable( the number of it ) and make the comma works.
#The reason why it shows h is clearly , text[0] means the first character of the text. And H is the at number 7 in the alphabet.
#indexed_letter = ''#Makes it a value
#char = ' '#Makes it a value
#print(shifted)
#This is making more sense now right? 7 +3 = 10 , by adding +3 in the shifted variable you got a new encrypted code , but not yet ! Youre only debugging the numbers , not the letters.
#Now you need to make some iteration in order to make this easier to code
#add a funct by using def. indent all the lines after that.
def Magicman(wording , neutralize_key , revenue = 1 ):
    key_index = 0 #Starting off with the core principle  , adding 0 adds a starting point.
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    indexed_letter = ''
    for words in wording.lower():
        if not words.isalpha():
            indexed_letter += words #This makes it obvious that youre trying to put an exception for space. This is just the first step for an else clause.
            #Now , add an else caulse , you see why the console encrypt your space as c? simply its because 0 + 3 = 3 , and 3 = c in alphabet.
        else: #Find the right word to encode 
            #it worked ! you put an exception for your space and now its gone. What a relief. But what now? Change your plain text into a different text.It will show that you are now out of range , your scope for your alphabetic letters are in range of 10 , and it goes past it. Now make it a loop of only letters that are >10.
            key_word = neutralize_key[key_index %len(neutralize_key)]
            neutral_word = alphabet.index(key_word) #Define the neutralizing and the encrypted letter
            key_index += 1 #You are encrypting your key. So we need to know your index. Adding 1 makes your letter keeps you from encrypting continously differ from the first letter. E.g: a + 1 = b and so on.
            #Add % 26 to indexed , to divide it , you will have : 26 : 25 = quotient 1.
            index = alphabet.find(words) #2 index because inside the for comma you need to declare another var. Because its INSIDE.
            indexed = (index + neutral_word * revenue ) %len(alphabet) #This will make it easier than:                    #(index + shift) % 26            #By adding this index comma you will now be able to see the num of the index of char by the comma .find(). So to encrypt both num and letters.
            indexed_letter += alphabet[indexed]#Indexed_letter means that you add 10 to your alphabet. The indexed means 7 + 3 , it didnt add directly to your alphabet yet.
        #print('letter:' , words , 'indexed_letter:' , indexed_letter) #It comes to a point where you now know how to make the console print the line that you wanted. You can replace the name (new_char) to a different name whatever you favor it.
    return indexed_letter
def NoMoreBloodShed(wording ,neutralize_key):
    return Magicman(wording , neutralize_key)
def NoMoreMassacre(wording , neutralize_key):
    return Magicman(wording , neutralize_key , -1)
# Interactable part
text = input("Enter the text to encrypt or decrypt: ")
order_key = input("Enter the encryption key: ")
mode = input("Type 'e' to encrypt or 'd' to decrypt: ").strip().lower()
print(f"DEBUG: mode = '{mode}'")
if mode == 'e':
    result = NoMoreBloodShed(text, order_key)
    print(f'\nEncrypted text: {result}')
elif mode == 'd':
    result = NoMoreMassacre(text, order_key)
    print(f'\nDecrypted text: {result}')
else:
    print("Invalid option. Please type 'e' or 'd'.")
    
#growth = Magicman(text , order_key)
#decipher = Magicman(growth , order_key) #Make sure you got your revenue multiplied. Why? Its math. Period. -1(anything + anything) = + (-1 x anything + anything)
#growth = NoMoreBloodShed(text , order_key)
#decipher= NoMoreMassacre(text, order_key)
#print(growth)
#print(decipher)
#print(f'\n indexed_text: {text}')
#print(f'\n key: {order_key}')
#print(f'\n deciphered text: {decipher}\n')


            #print(char , index)#print(char, index) # You can print 2 variables to make it next eachother , delighting right?   
            #Now make an if func.(you need to make it at the beggining of your for )
            #print (char == ' ') #This operator makes char equality to a space , you cant use one = because char is in interger , to clarify it will makes char = char EQUAL a space. And this will compare and make the expressions either true of false.
#print(growth)    
#Important take : Every letter that you encrypt will be encrypt with the same specified neutralize number or whatever it is , just use a vigenere function lmao. Way simpler  
#Why do you need to make indexed_l += alphabet[indexed]? ,<=> Encrypt the message even if its not in the alphabet. E.g: a space.
#Remember: Operator	Meaning
#==	Equal
#!=	Not equal
#>	Greater than
#<	Less than
#>=	Greater than or equal to
#<=	Less than or equal to