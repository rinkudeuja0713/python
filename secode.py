# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode
message= str(input("Do you want to code or decode? \n Type c to code and d to decode "))
if (message=="c"): 
    msg= str(input("type your message"))
    
    user_input = msg.split()
    for word in user_input:
        if len(word)>=3:
            r1="dph"
            r2="lod"
            print(r1+word[1:]+word[0]+r2)
        else:
            print(word[::-1])
elif (message == "d"):
    msg2=str(input("type your message to decode"))
    user_input2=msg2.split()
    for word2 in user_input2:
        if len(word2)>= 3:
            word3= word2[3:-3]
            print(word3[-1]+word3[:-1])
        else:
            print(word2[::-1])

  
