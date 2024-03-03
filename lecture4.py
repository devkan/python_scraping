###########################
# class1
###########################

class Puppy:
  pass # 그냥 지나가라는것임

jindo = Puppy() # jindo가 puppy에 속해 있음을 알려주는 것임
print(jindo) # <__main__.Puppy object at 0x7f488f4672b0> jindo를 찍었는데, Puppy object라고 표기해줌.
# 즉, 객체로 인식하고 있다는 것임. 0x7f488f4672b0의 메모리에 있다고 알려주는 것이고..


###########################
# class2
###########################
print("class2.......................")

class Fruits:
  def __init__(self): # 생성자, 초기에 무조건 실행됨
    #print(self) # <__main__.Fruits object at 0x7fc695d1fe80>

    self.name = "apple"
    self.color = "red"
    self.taste = "sweet"


apple = Fruits()

print(apple) # <__main__.Fruits object at 0x7fc695d1fe80> gaga로 찍히는 거랑 메모리 주소가 같다.
# 즉, class 밑의 메소드들은 무조건 첫번째 인자는 자신이라는 것이다.

print(
  apple.name,
  apple.color,
  apple.taste
)


###########################
# class3
###########################
print("class3.......................")

# Person 클래스
class Person:
  def __init__(self, name, age, hobby):
    self.name = name
    self.age = age
    self.hobby = hobby

  def __str__(self):
    return f"__str__ is {self.name}, {self.age}\n"

  def haha(self):
    print("haha")
    
  def introduce(self):
    self.haha()
    print(f"My name is {self.name}, I'm {self.age} years old")


# person으로 부터 상속(inheritance) 받을때 이처럼 상속받을 클래스명을 적어주면 된다.
# super() 오타 조심.. 괄호

class Man(Person):
  def __init__(self, name, age, hobby):
    super().__init__(
      name, 
      age,
      hobby
    )
    self.is_game = "yap" # 각각의 property와 method를 가질수 있다.
    
  def game(self):
    print("very instresting!!")


class Woman(Person):
  def __init__(self, name, age, hobby):
    super().__init__(
      name, 
      age,
      hobby    
    )
    self.food = "good job" # 각각의 property와 method를 가질수 있다.
    self.skin = "ok" # 각각의 property와 method를 가질수 있다.

  def dress(self):
    print("very pretty!!")




kim = Person(
  name = "kim", 
  hobby = "reading",
  age = "20" # 키워드 지정시 위치가 변경되어도 된다.
)
print(kim.name, kim.age, kim.hobby) # kim 20 reading

kang = Person("kang", "21", "playing") # 제대로 데이타을 출력해 주지만, 위처럼 키워드를 사용해 지정하는 것이 좋다.
print(kang.name, kang.age, kang.hobby) # kim 20 reading

# print __str__
print(
  kim,
  kang
)
# __str__를 실행해서 데이타를 출력해주는 것임.

kim.introduce()
kang.introduce()

###########################
# inheritance
###########################
print("inheritance.......................")

Lee = Man(
  name = "Lee", 
  age = "20", 
  hobby = "work"
)

Hong = Woman(
  name = "Hong",
  age = "30",
  hobby = "shopping"
)

print(
  Lee,
  Hong
)

Lee.game() 
Hong.dress()
Lee.introduce() # 상속을 받지 때문에 super의 메소드에 접근이 가능하다.
Hong.introduce()
