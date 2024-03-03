
'''
True, False 는 이처럼 대문자로 시작해야 한다.
true, false 는 에러가 난다.
'''

####################################

def say_hello(name):
  print("hellow how r u?", name)

say_hello("kan")

#####################################

name = "kan"
age = "49"

print(f"hello I'm {name}, I have {age} years old") #hello I'm kan, I have 49 years old
print("hell I'm {name}, I have {age} years old") # hell I'm {name}, I have {age} years old
"""
{변수명} 으로 받아서 처리하려면 print 앞에 f를 꼭 붙여야 한다.
이는 f-스트링(f-string)이라고 불리면, f-스트링은 파이썬 3.6 버전부터 도입된 문자열 포매팅 기능으로, 
문자열 안에 중괄호 {}를 사용해 변수의 값을 직접 삽입할 수 있게 해 준다.
"""


def make_juice(fruit):
  return f"{fruit}"

def add_sugar(iced_juice):
  return f"{iced_juice} + sugar"

juice = make_juice("apple")
drink_juice = add_sugar(juice)
print(drink_juice)

#####################################

num = 10
if num > 20:
  print("20 over")
elif num >= 10 :
  print("10 over")
else:
  print("other num")
  
#####################################

age = input("How old are you? ") # 프롬프트에서 입력 받을때
input_age = int(age)

if input_age < 18:
  print("You can't drink")
elif input_age >= 18 and input_age <= 35:
  print("You drink beer!")
elif input_age == 60 or input_age == 70:
  print("Birthday party!")
else:
  print("go ahead!!")  
  
 
## while ###########################
distance = 0
while distance < 20:
  print("I'm running:", distance, "km")
  distance = distance + 1
  

## position argument ################
def plus(a, b):
  return a + b

plus(2, 3) # 5
"""
별도 키워드 없이 값을 지정하면 순서대로 들어가는 것이 position argument이다.

"""

## keyword argument ################
def minus(a, b, c, d, e):
  return a - b - c - d - e

minus(a=10, b=2, c=3, d=4, e=5) # -4
minus(c=10, b=2, a=3, e=5, d=4) # -18 # 순서가 바뀌어도 상관없다.
minus(10, 2, c=3, d=4, e=5) # 포지션 argument를 시작해서 keyword argument로 혼용해서 사용이 가능하다.
minus(a=10, b=2, c=3, 4, 5) #하지만 반대로 keyword argument를 시작해서 position argument로 혼용하면 오류가 난다.

    
  
## casino ##########################
# # https://docs.python.org/3/library/index.html 에서 library를 참조

from random import randint

print("Python Casino!!!")

computer_choice = randint(1, 50)
playing = True

while playing: 
  choice = int(input("Choose Number (1~50): "))
  
  if choice == computer_choice:
    print("You won!")
    playing = False
  elif choice > computer_choice:
    print("Lower!!")
  elif choice < computer_choice:
    print("Higher!!")
  
  