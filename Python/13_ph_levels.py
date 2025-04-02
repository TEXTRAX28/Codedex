ph_level = int(input("What is the pH level?: "))

if ph_level > 7:
  print("Basic")
elif ph_level < 7:
  print("Acidic")
else:
  print("Neutral")
