print("****WELCOME TO KBC GAME****")
question_list = [
"How many continents are there?",
"What is the capital of India?",
"NG mei kaun se course padhaya jaata hai?",
"who founded microsoft?"
]

options_list = [

["Four", "Nine", "Seven", "Eight"],
["Chandigarh", "Bhopal", "Chennai", "Delhi"],
["Software Engineering", "Counseling", "Tourism", "Agriculture"],
["elon musk","jeff","mark","bill gates"]
]


solution_list = [3, 4, 1,2]
answer_list=[
             ["1.four","3.seven"],
             ["2.bhopal","4.delhi"],
             ["1.softwere engineering","3.agriculture"],
             ["2.jeff","4.bill gates"]]
print("******KAUN BANEGA CROREPATI  (KBC)********")
i=0
s=0
count=0
while i<len(question_list):
    print(question_list[i])
    a=0
    b=0
    while a<len(options_list[i]):
        k=options_list[i][a]
        print(a+1,k)
        a+=1
    num=input("DO YOU WANT 50-50 LIFE LINE")
    if num=="yes":
        print("accept")
        if count<1:
            print(answer_list[b])
            num1=int(input("enter the answer:-"))
            if num1==solution_list[i]:
                s+=1
                print("your answer is correct")
                print("you win Rs/",s)
            else:
                print("incorrect answer")
                print("you win Rs/",s)
                break
            count+=20000
        else:
            print("you already use lifeline")
            num2=int(input("enter the your answer:-"))
            if num2==solution_list[i]:
                print("congrats your answer is right")
                s+=100
                print("you win Rs/",s)
            else:
                print("your answer is wrong")
                print("you win Rs/",s)
                break  
    else:
        pass
        k=int(input("enter your answer"))
        if k==solution_list[i]:
            print("right answer")
            s+=10000
            print("you win Rs/",s)
        else:
            print("your answer is worng")
            print("you win rss/",s)
            break
    i=i+1
print("congratulations...your participated in KBC game")
print("you win Rs/",s)
print("thankyou for particapting.....")    























            
        
        



