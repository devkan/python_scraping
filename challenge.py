class Players:
  def __init__(self, name, team):
    self.name = name
    self.xp = 1000
    self.team = team

  def introduce(self):
    print(f"Hello, I'm {self.name}, and my team is {self.team}")


class Team:
  def __init__(self, team_name):
    self.team = team_name
    self.players = [] # empty list

  def add_player(self, name):
    new_player = Players(name, self.team) #클래스의 새 인스턴스를 생성
    self.players.append(new_player) #이 인스턴스를 다시 self.players의 리스트에 추가
    # 그래서 밑의 for문의 player가 introduce()메쏘드 접근이 가능하게 되는 것이다.

  def del_player(self, name):
    for player in self.players:
      if player.name == name:
        self.players.remove(player)
        break

  def show_player(self):
    for player in self.players:
      player.introduce()


team_x = Team("X")
team_x.add_player("kan")
team_x.add_player("sin")

team_y = Team("Y")
team_y.add_player("min")

team_x.show_player()
team_y.show_player()

team_x.del_player("sin")
team_x.show_player()
