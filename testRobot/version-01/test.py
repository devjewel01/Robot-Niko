import re


txt = "The advice for humans"
x = re.search(".advice.*human", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")
