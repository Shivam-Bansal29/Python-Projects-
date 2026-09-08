money=0
x=input(" Enter Your Name : ")
print(f" Welcome to the game {x}\n")#here i usse f-string method looks more
print(" 🛑 Press 0 to quit the game \n\n")# cleaner than printing("wlcm togame,x,\n")
questions=[
    {"que": "What is the capital of India ?",
        "ans": "a. Delhi    b.Chandigarh\nc.goa    d. mumbai" ,"correct": "a",
     "prize": 1000},# here in dictinory I also store money won and correct answer

    {"que": "Who is the PM of India ",
     "ans": "a. Narinder Modi b. Dropti murmu\nc.Rahul Gandhi   d.Neerav Modi",
     "correct" : "a" , "prize": 10000 },

    {"que":"Which is the largest state of India on basis of area",
     "ans": "a.Gujarat    b.Maharashtra \nc.Punjab    d.Rajasthan ",
      "correct": "d" , "prize": 50000 },

    { "que":"Who is the fisrt president of India",
      "ans": "a.Jawaharlal Nehru  b.RajendraPrasad\nc.Dr.Radhakrishnan d.Mahatma Gandhi",
    "correct": "b" , "prize": 100000 },

    {"que":"Which is the largest river of India",
        "ans":"a.Kaveri     b.Godawari \nc.Ganga     d.Yammuna ",
      "correct": "a" , "prize": 500000 },

]# I make list of dictinary which are separatd by (,) here at 0 index of list there
# is question 1 and index 1 of list there is question 2

for y in questions:# by this it will give items of 0 index and store in y and
        #same for index 1,2,3,4
    print(y["que"],"\n")#by this it will print que of index 0 as here y gaves 0 index
    print(y["ans"],"\n")# by this ans
    answer=input("enter the option :").lower()# by lower()option is converted 
                                            # into lowercase
    if answer =="0":
        print("\nYou Chosse to exit the game ")
        break
    elif answer == y["correct"]:# this chek corect part of 1st question and
                                    #chek is answer==to thing written in correct or not
        print("\nWeldone!! your answer is right")
        money+=y["prize"]#If user selects correct option  increase the money by prize 
        # wriiten in dictinaory 
        print(" You win ", money,"\n")
    else:
        print(f"\n Your answer is wrong ,\n Right answer is {y["correct"]}\n  Game is over now")
        break
    
 
print(" you won",money)
        
            
        
