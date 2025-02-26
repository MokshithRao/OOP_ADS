class Person:
    def __init__(self, name, games=None) -> None:
        self.name = name
        self.games = games

    def add_game(self, game):
        if game not in self.games:
            self.games.append(game)
    
    def remove_game(self, game):
        for i in self.games:
            # print(i)
            if i == game:
                self.games.remove(game)
    

    def get_favorite_games(self):
        # for i in self.games:
        return self.games
    
    def get_name(self):
        return self.name


    def __str__(self):
        return f"Person(name={self.name}, games={self.games})"




class SocialNetwork:
    def __init__(self) -> None:
        self.person = None
        self.users = []

    def add_user(self, user):
        for i in self.users:
            if i.get_name() == user.get_name():
                print(f"User with name {user.get_name()} already exists.")
                return
        self.users.append(user)
                
    
    
        # for i in self.users:
        #     print(i.name, i.games)


    def remove_user(self, name):
        for i in self.users:
            if i.get_name() == name:
                self.users.remove(i)
                if self.person == i:
                    self.person = None
                return
        print(f"User with name {name} not found.")

    
    def get_user(self, name):
        for i in self.users:
            if i.get_name() == name:
                return i
        # print(f"User {name} is not in the network.")
        return None
            
    def update_person(self, person):
        for i in self.users:
            if i.get_name() == person.get_name():
                self.person = i
                return
        print(f"User {person.get_name()} is not in the network.")
    


    def get_users_who_like(self, game):
        likes = []
        for i in self.users:
            if game in i.get_favorite_games():
                likes.append(i.get_name())
        return likes
    

    def __str__(self):
        s = ""
        for i in self.users:
            s+=str(i)+", "
        s = s[:-2]
        return f"SocialNetwork(current person={self.person}, users=[{s}])"