import pyttsx3

eng=pyttsx3.init()
eng.setProperty("rate",110)

eng.say("Hello! What is your name?")
eng.runAndWait()
name=input("Name: ")

eng.say("What is your age?")
eng.runAndWait()
age=input("Age: ")

eng.say("What is your gender?")
eng.runAndWait()
gender=input("Gender(Male/Female): ")
sex="he" if gender.lower()=="male" else "she" if gender.lower()=="female" else "this person"

eng.say("What is your hometown?")
eng.runAndWait()
home=input("HomeTown: ")

eng.say("{} is {} years old and currently {} is living in {}".format(name,sex,age,home))
eng.runAndWait()

