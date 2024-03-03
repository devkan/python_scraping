##################################
# method
##################################

# variable 뒤에 붙는 함수를 method라 부룬다.. name.upper() 처럼
# 데이타와 결합한 함수라 보면 된다.

name = "kan"
print(name.upper())
print(name.endswith("n"))
print(name.replace("k","h"))

##################################
# list
##################################
print("list....................")

days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri"]
print(days_of_week)
print(days_of_week.count("Wed")) # result : 1, Wed 데이타가 몇개인지 카운트하는 것임

print(days_of_week[2]) # result : Wed
print(days_of_week[-1]) #result : Fri

days_of_week.append("Sat")
print(days_of_week)

days_of_week.remove("Fri")
print(days_of_week)

days_of_week.reverse()
print(days_of_week) # days_of_week.reverse()

print(days_of_week.reverse()) # None을 출력함. 
# reverse()자체 return값이 없어서 바로 print 찍으면 none이 출력되는 것임
# 즉, reverse를 사용하면 역순으로 만들기는 하지만, 리턴값이 없다보니 print 하면 None이 나오는 것음

days_of_week.clear()
print(days_of_week) # result : []


##################################
# Tuples (변경 불가한 데이타), 변경시에는 list를 사용하면 된다.
##################################
print("Tuples....................")
days = ("Mon", "Tue", "Wed") #()는 튜블, []는 리스트
print(days[1])


##################################
# Dicts 
##################################
print("Dicts....................")

player = {
  'name' : 'kan',
  'age' : 20,
  'alive' : True,
  'food' : ["🍕", "🍔"], # 딕셔너리에 리스트를 넣을수 있다.
  'tuple' : ('a'), # 딕셔너리에 튜플을 넣을수 있다.
  'tuple2' : days # 딕셔너리에 튜플을 넣을수 있다.
}

print(player) # {'name': 'kan', 'age': 20, 'alive': True}
print(player.get('age')) # 20
print(player.get('food')) # ['🍕', '🍔']
print(player['food']) # ['🍕', '🍔']

player.pop('age') # age를 삭제함
print(player) # {'name': 'kan', 'alive': True, 'food': ['🍕', '🍔']}
player['job'] = "developer"
print(player) # {'name': 'kan', 'alive': True, 'food': ['🍕', '🍔'], 'job': 'developer'}

player['food'].append("🍜")
print(player.get('food')) # ['🍕', '🍔', '🍜']
