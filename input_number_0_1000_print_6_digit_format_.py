#ask user to input a number between 0 and 1000
while True:
  number = int(input("Enter a number between 0 and 1000:"))
  if number < 0 or number > 1000:
    print("Enter numbers 0 - 1000 only.")
    continue
#print the number in 6 digit format
  else:
    print(f"Output: {number:06d}")
