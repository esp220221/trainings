print("Welcome to my computer quiz!")

playing = input("Do you want to play?(yes or no) ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("That's Correct!")
    score += 1
else:
    print("That's incorrect!")

answer = input("What does GPU? ")
if answer.lower() == "graphics processing unit":
    print("That's Correct!")
    score += 1
else:
    print("That's incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("That's Correct!")
    score += 1
else:
    print("That's incorrect!")

answer = input("What does PSU? ")
if answer.lower() == "power supply unit":
    print("That's Correct!")
    score += 1
else:
    print("That's incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str(score/4 * 100) + " %!")
