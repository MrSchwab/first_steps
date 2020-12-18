# Pirple Course - Homework #9
# Classes

#class class_name:

#    def __init__(self):
#        self.Attribute = 0

#    def another_function(self):
#        Action(s)


# Lecture 1: Introduction to classes

class Team:
    def __init__(self, name = "Name", origin = "Origin"):
        self.team_name = name
        self.team_origin = origin

    def define_team_name(self,name):
        self.team_name = name

    def define_team_origin(self,Origin):
        self.team_origin = Origin

#class inheritance_class_name(parent_class):
#    def __init__(self,input1,input2):
#        parent_class.__init__(self)
#        self.attribute1 = input1
#        self.attribute2 = input2

#    def another_method(self):
#        action(s)

class Player(Team):
    def __init__(self,player_name,player_points,team_name,team_origin):
        Team.__init__(self,team_name,team_origin)
        self.player_name = player_name
        self.player_points = player_points

    def scored_point(self):
        self.player_points += 1

    def set_name(self,name):
        self.player_name = name

    def __str__(self):
        return self.player_name + " has socred: " + str(self.player_points) + " points."

player1 = Player("Sid",0,"Sharks","Chicago")

print(player1.player_name)
print(player1.player_points)

player1.define_team_name("Sharks")

print(player1.team_name)
print(player1.team_origin)

player1.scored_point()
print(player1.player_points)

player1.set_name("Lee")
print(player1.player_name)
print(player1)

team1 = Team("Tigers","Chicago")
team2 = Team("Hawks","New York")
team3 = Team()

print(team1.team_name)

team1.define_team_name("Dolphins")

print(team1.team_name)
print(team1.team_origin)

print(team2.team_name)
print(team2.team_origin)

print(team3.team_name)
print(team3.team_origin)


