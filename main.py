import random
import math
import time
import statistics 

functions=['sin','cos','tan','csc','sec','cot']

times=[]
accuracy=[]

#dict for converting inputs to values
answers={
  "1":1,
  "-1":-1,
  "s2/2":0.70710678118,
  "-s2/2":-0.70710678118,
  "s3/2":0.86602540378,
  "-s3/2":-0.86602540378,
  "2s3/3":1.15470053838,
  "-2s3/3":-1.15470053838,
  "s3":1.73205080757,
  "-s3":-1.73205080757,
  "s3/3":0.57735026919,
  "-s3/3":-0.57735026919,
  "2":2,
  "-2":-2,
  "s2":1.41421356237,
  "-s2":-1.41421356237,
  "1/2":0.5,
  "-1/2":-0.5,
  "0":0,
}

def getProblem():
  #making sure fraction can't be simplified (aka can't be smth like 4π/6)
  good=False
  while good==False:
    function=random.choice(functions)
    denominator=random.choice([1,2,3,4,6])
    max=denominator*2
    numerator=random.randrange(1,max,1)
    if numerator!=1 and denominator!=1:
      if numerator==denominator:
        continue
      elif math.gcd(numerator,denominator)!=1:
        continue
      else:
        good=True
    else:
      good=True
  #making formatting good
  if numerator==1 and denominator==1:
    problem=f"{function} π"
  elif numerator==1:
    problem=problem=f"{function} π/{denominator}"
  elif denominator==1: 
    problem=f"{function} {numerator}π"
  else:
    problem=f"{function} {numerator}π/{denominator}"
  angle=(numerator*math.pi)/denominator
  #special answer for undefined functions
  if problem=='tan 3π/2' or problem=='tan π/2' or problem=='cot π' or problem=='csc π' or problem=='sec π/2' or problem=='sec 3π/2':
    answer='undefined'
  #finding value of problems
  elif function=='sin':
    answer=math.sin(angle)
  elif function=='cos':
    answer=math.cos(angle)
  elif function=='tan':
    answer=math.tan(angle)
  elif function=='csc':
    answer=1/math.sin(angle)
  elif function=='sec':
    answer=1/math.cos(angle)
  elif function=='cot':
    answer=1/math.tan(angle)
  return {'problem':problem, 'answer':answer}

print('Use s in place of square root')
print("Enter 'end' to end session")
while True:
  right=True #variable to check if answer is accurate, used for calculating accuracy
  thing=getProblem()
  print(thing['problem'])
  startingTime=time.time() #used for calculating time to solve
  while True:
    yourAnswer=str(input(''))
    if yourAnswer in answers.keys() or yourAnswer=="undefined" or yourAnswer=="end":
      break
    else:
      print("That is not a valid answer")
  if yourAnswer=="end": #ending session
    break
  elif thing['answer']==yourAnswer: #used if right answer is undefined
    print('right')
  elif yourAnswer=="undefined": #used if you input undefined but the answer isn't that 
    for number in answers: #converting decimal value to fractions
      if math.isclose(answers[number],thing['answer']):
        rightAnswer=number
    print(f"The right answer was {rightAnswer}")
    right=False
  elif thing['answer']==1.83697019872103e-16 or thing['answer']==-1.83697019872103e-16 or thing['answer']==-1.2246467991473532e-16 or thing['answer']==6.123233995736766e-17 or thing['answer']==-6.123233995736766e-17 or thing['answer']==1.2246467991473532e-16 and yourAnswer=='0': #this is bc math.isclose is a bitch and I didn't think of comparing the difference 
    print('right')
  elif thing['answer']==1.83697019872103e-16 or thing['answer']==-1.83697019872103e-16 or thing['answer']==-1.2246467991473532e-16 or thing['answer']==1.2246467991473532e-16 or thing['answer']==6.123233995736766e-17 or thing['answer']==-6.123233995736766e-17 and yourAnswer!=0: #same thing
    print('The right answer is 0')
    right=False
  elif thing['answer']=='undefined' and yourAnswer!='undefined': 
    print('The right answer is undefined')
    right=False
  elif math.isclose(thing['answer'],answers[yourAnswer]): #checking if right 
    print('right')
  else:
    for number in answers: #converting decimal value to fractions
      if math.isclose(answers[number],thing['answer']):
        rightAnswer=number
    print(f"The right answer is {rightAnswer}")
    right=False
  endingTime=time.time()
  times.append(endingTime-startingTime)
  accuracy.append(right)

print(f"{round(statistics.mean(times),2)} was your mean time")
print(f"{round(statistics.median(times),2)} was your median time")
amountRight=0
for x in accuracy:
  if x:
    amountRight+=1
print(f"{round(amountRight/len(accuracy), 2)} was your accuracy")
