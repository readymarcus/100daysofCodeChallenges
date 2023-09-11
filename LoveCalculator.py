print("Welcome to the Love Calculator")
name1 = input(str("What's your name?"))
name2 = input("What is their name?")\

nameone = name1.lower()
nametwo = name2.lower()

tcount = 0
lcount = 0

for i in nameone:
    if i == 't':
        tcount = tcount + 1
for i in nameone:
    if i == 'r':
        tcount = tcount + 1
for i in nameone:
     if i == 'u':
         tcount = tcount + 1
for i in nameone:
     if i == 'e':
         tcount = tcount + 1
for i in nametwo:
    if i == 'l':
        lcount = lcount + 1
for i in nametwo:
    if i == 'o':
        lcount = lcount + 1
for i in nametwo:
    if i == 'v':
        lcount = lcount + 1
for i in nametwo:
    if i == 'e':
        lcount = lcount + 1

love = tcount + lcount

if love <= 10:
    print("Your score is: " + str(love) + ", you go together like coke and mentos")
elif love >= 90:
    print ("Your scorfe is: " + str(love) + "you go together like coke and mentos")
elif love >= 40 and love <= 50:
    print ("Your score is: " + str(love) + "...You're alright ")
else:
    print ("Your score is: " + str(love))