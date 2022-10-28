print("Welcome to the Affirmations Generator!")
print()
print("I will ask you a few questions just to get to know you then generate an affirmation to pump you up for the day.")
print()
name = input("Name: ")
print()
print("Hi", name.upper()+".")
day = input("What day is it today?: ")
print()
song = input("What is your favorite song? ")
print()
if day.lower() == "monday":
  weekend = input("How was your weekend? Please enter 'bad' or 'good' ")
  print()
  if weekend.strip().trim().lower() == "good":
    print("To maintain the good mood from the weekend, go ahead and listen to",song,"be productive and at the end of the day have something to celebrate that you achieved today.")
    print()
  elif weekend.strip().trim().lower() == "bad":
    print("To get rid of the large emotional shift from the weekend, go ahead and listen to",song,"be productive and at the end of the day have something to celebrate that you achieved today.")
    print()
  else:
    print("Listen to",song,"be productive and at the end of the day have something to celebrate that you achieved today.")
  print()
elif day.lower() == "tuesday":
  print("Tuesdays are terrific! Zone in by listening to", song,"and be your terrific self!")
  print()
elif day.lower() == "wednesday":
  print("It's a Wacky Wednesday! Go ahead to do something fun while listening to", song)
  print()  
elif day.lower() == "thursday":
  print("Thursdays are fabulous! Get ready to be fabulous while listening to",song)
  print()
elif day.lower() == "friday":
  print("Fridays are fantastic! Be your fantastic self while listening to", song)
  print()  
elif day.lower() == "saturday":
  print("Saturdays are stupendious! Be your amazing self while listening to", song, "and do amazing things today.")
  print()
elif day.lower() == "sunday":
  print("Sundays are peaceful! Zone into your serene self while listening to", song)
  print()
else:
  print("Oops! Looks like you entered an invalid day.", name+".", "Please, kindly start over.")