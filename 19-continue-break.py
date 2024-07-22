#i=int(input("Enter your Floor Number:"))
i=14
floor=0
for floor in range(0,1000):
  floor=floor+1
  if(floor==13):
    print("\n There's no 13th Floor \n")
    continue
  print(f"You're in {floor} floor")
  if(floor==21):
    print("You're in top floor")
    break
# else("Please get down")