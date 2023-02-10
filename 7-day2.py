for num in range(1,21):
  #checking that number is divisible by both 3 and 5
  if(num%3==0 and num%5==0):
    print("FizzBuzz")
  #checking that number is divisible by 3
  elif(num%3 == 0):
    print("Fizz")
  #checking that number is divisible by 5
  elif(num%5 == 0):
    print("Buzz")
  #And if not divisible by either of them print num as it is
  else: 
    print(num)