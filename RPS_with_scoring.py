print("hello to the R,P,S game")
counter1=0
counter2=0
while True:
  p1=input("R,P,S? ")
  p2=input("R,P,S? ")
  if p1=="R" and p2=="R":
    print("draw")
  elif p1=="R" and p2=="P":
    print("p2 win")
    counter2 += 1
  elif p1=="R" and p2=="S":
    print("p1 win")
    counter1 += 1
  elif p1=="P" and p2=="R":
    print("p1 win")
    counter1 += 1
  elif p1=="P" and p2=="P":
    print("draw")
  elif p1=="P" and p2=="S":
    print("p2 win")
    counter2 += 1
  elif p1=="S" and p2=="R":
    print("p2 win")
    counter2 += 1
  elif p1=="S" and p2=="P":
    print("p1 win")
    counter1 += 1
  elif p1=="S" and p2=="S":
    print("draw")
  else:
    print("Please enter either R,P,S and make sure they are captial")
  print ("p1_score is",counter1)
  print ("p2_score is",counter2)
  if counter1==3 or counter2==3:
    print("thanks for playing")
    exit()
  else:
    continue
