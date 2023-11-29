## list
w_ans = 0
c_ans = 0
total = 0
q = ["1.what is the capital of india","2.what is the national bird","3.What is the national animal","4.What is the national game","5.Who is our prime minister","6.Who is kohli","7.How many members in the cricket team","8.who invented iphone","9.Who invented gravity","10.Who invented bulb"]
ans = ["delhi","peacock","tiger","hockey","modi","cricketer","11","steve jobs","newton","edison"]
for x in q:
    print(x)
    y = input("Enter the answer: ").lower()
    if y in ans:
        print("Correct answer")
        c_ans+=1
    else:
        print("Wrong answer")
        w_ans+=1
    total+=1
print(f"\nTotal Questions: {total}")
print(f"Correct Answers: {c_ans}")
print(f"Wrong Answers: {w_ans}")
if c_ans >= 8:
    print("passed quiz")
else:
    print("Failed quiz")


'''list = [1,5,6,4,8,9,0]
#list.append(10)
#list.pop()
#list.insert(2,20)
#list.sort()
#r = len(list)
#list.extend([40,50,60,70])
#list.reverse()
print(list)'''

