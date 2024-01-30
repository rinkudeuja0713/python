# create a program capable of displaying questions to users like KBC
# use list datatype to store the questions and their answers
# display the final amount the person is taking hime after playing the game

user = str(input("Hello! Welcome to KBC. Are you ready to play?\n Yes No\n"))
if (user == "yes" or user == "okay" or user =="ok"):
  
    print("Heres your first question:\n What is the capital city of Nepal?\n")
    list1= ["A.Bhaktapur ", "B.Kathmandu ", "C.Pokhara ", "D.Birgunj"]
    print(list1)
    ans1=str(input("Select and type the correct option\n"))
    if (ans1=="B" or ans1=="b"):
        print("Correct Answer!\n You've won 500\n")
       
    else:
        print("sorry, that is incorrect")
    
    print("Heres your second question:\n What is height of Mt.Everest?\n")
    list2= ["A.9989 ", "B.4899 ", "C.8848 ", "D.8898"]
    print(list2)
    ans2=str(input("Select and type the correct option\n"))
    if (ans2=="C" or ans2=="c"):
        print("Correct Answer!\n You've won 500\n")
        
    else:
        print("sorry, that is incorrect")

    print("Heres your third question:\n Who discovered gravity?\n")
    list3= ["A.Sir Isaac Newton", "B.Albert Einstein ", "C.Mary Curie", "D.Mahatma Gandhi"]
    print(list3)
    ans3=str(input("Select and type the correct option\n"))
    if (ans3=="A" or ans3=="a"):
        print("Correct Answer!\n You've won 500\n")
    else:
        print("sorry, that is incorrect")
    
    print("Heres your last question:\n Which triangle has all sides equal?\n")
    list4= ["A.Equivalent triangle ", "B.Isosceles triangle", "C.Equilateral Triangle ", "D.Equal Triangle"]
    print(list4)
    ans4=str(input("Select and type the correct option\n"))
    if (ans4=="C" or ans4=="c"):
        print("Correct Answer!\n You've won 500\n")
    else:
        print("sorry, that is incorrect")
    



