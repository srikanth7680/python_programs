## split() function
val = "Rama is going to school"
y = val.split()
for x in y:
    print(len(x))
## strip() function
a = "  Rama  "
print(a.strip())
##lstrip() function
b = "   Rama"
print(b.lstrip())
##rstrip() function
c = "Rama   "
print(c.rstrip())
##
d = "A R J U N"
for x in d:
    if x == " ":
        pass
    else:
        print(x,end="")
