# break and continue: also notice the placement

for i in range (1,12):
    if(i==3):
        print("skipped 3")
        continue
        
    print( "5 X ",i, "=",5*i)
    if (i==10):
        break
        print("break applied")
    
print("Thank you!")


