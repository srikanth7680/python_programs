## break statement
'''for x in range(7):
    if x == 5:
        break
    else:
        print(x)

## continue statement
for x in range(7):
    if x == 5:
        continue
    else:
        print(x)
## pass statement
for x in range(7):
    if x == 5:
        pass
    print(x)'''

### Quiz Application
total_marks = 25
c_ans = 0
w_ans = 0
q = input("what is the capital city of india: ").lower()
if q == "delhi":
    print("Correct Answer")
    c_ans+= 1
else:
    print("Wrong answer")
    w_ans+= 1
q = input("What is the national bird: ").lower()
if q == "peacock":
    print("correct answer")
    c_ans+=1
else:
    print("Wrong answer")
    w_ans+= 1
q = input("What is the national anthem: ").lower()
if q == "janaganamana":
    print("correct answer")
    c_ans+=1
else:
    print("Wrong answer")
    w_ans+= 1
q = input("What is the national animal: ").lower()
if q == "tiger":
    print("correct answer")
    c_ans+=1
else:
    print("Wrong answer")
    w_ans+= 1
q = input("What is the national game: ").lower()
if q == "hockey":
    print("correct answer")
    c_ans+=1
else:
    print("Wrong answer")
    w_ans+= 1
q = input("Who is our prime minister: ").lower()
if q == "modi":
    print("correct answer")
    c_ans+=1
else:
    print("Wrong answer")
    w_ans+= 1
q = input("Who is kohli: ").lower()
if q == "cricketer":
    print("correct answer")
    c_ans+=1
else:
    print("Wrong answer")
    w_ans+= 1
q = input("How many members in the cricket team: ").lower()
if q == "11":
    print("correct answer")
    c_ans+=1
else:
    print("Wrong answer")
    w_ans+= 1
q = input("who invented iphone: ").lower()
if q == "steve jobs":
    print("correct answer")
    c_ans+=1
else:
    print("Wrong answer")
    w_ans+= 1
q = input("Who invented gravity: ").lower()
if q == "newton":
    print("correct answer")
    c_ans+=1
else:
    print("Wrong answer")
    w_ans+= 1
q = input("Who invented bulb: ").lower()
if q == "edison":
    print("correct answer")
    c_ans+=1
else:
    print("Wrong answer")
    w_ans+= 1
q = input("Who invented facebook: ").lower()
if q == "mark":
    print("correct answer")
    c_ans+=1
else:
    print("Wrong answer")
    w_ans+= 1
q = input("who invented twitter: ").lower()
if q == "elon musk":
    print("correct answer")
    c_ans+=1
else:
    print("Wrong answer")
    w_ans+= 1
q = input("who owned meta : ").lower()
if q == "mark":
    print("correct answer")
    c_ans+=1
else:
    print("Wrong answer")
    w_ans+= 1
q = input("which country is the highest population in the world: ").lower()
if q == "india":
    print("correct answer")
    c_ans+=1
else:
    print("Wrong answer")
    w_ans+= 1
q = input("who invented zero: ").lower()
if q == "aryabatta":
    print("correct answer")
    c_ans+=1
else:
    print("Wrong answer")
    w_ans+= 1
q = input("How many alphabets: ").lower()
if q == "26":
    print("correct answer")
    c_ans+=1
else:
    print("Wrong answer")
    w_ans+= 1
q = input("How many numbers are there in the world: ").lower()
if q == "infinite":
    print("correct answer")
    c_ans+=1
else:
    print("Wrong answer")
    w_ans+= 1
q = input("Who made the film Intersteller: ").lower()
if q == "christopher nolan":
    print("correct answer")
    c_ans+=1
else:
    print("Wrong answer")
    w_ans+= 1
q = input("who is the CEO of google: ").lower()
if q == "sundarpichai":
    print("correct answer")
    c_ans+=1
else:
    print("Wrong answer")
    w_ans+= 1
q = input("Who is mike tyson: ").lower()
if q == "boxer":
    print("correct answer")
    c_ans+=1
else:
    print("Wrong answer")
    w_ans+= 1
q = input("Who is jordon: ").lower()
if q == "basketball legend":
    print("correct answer")
    c_ans+=1
else:
    print("Wrong answer")
    w_ans+= 1
q = input("What is our national language: ").lower()
if q == "hindi":
    print("correct answer")
    c_ans+=1
else:
    print("Wrong answer")
    w_ans+= 1
q = input("Who won the FIFO worldcup : ").lower()
if q == "argentina":
    print("correct answer")
    c_ans+=1
else:
    print("Wrong answer")
    w_ans+= 1
q = input("who is father of nation: ").lower()
if q == "gandhi":
    print("correct answer")
    c_ans+=1
else:
    print("Wrong answer")
    w_ans+= 1

if c_ans == total_marks:
    print("passed in quiz")
elif w_ans <= 20:
    print("fail in the quiz")
elif w_ans == total_marks:
    print("fail in the quiz")
elif c_ans > 20:
    print("Passed in the quiz")

