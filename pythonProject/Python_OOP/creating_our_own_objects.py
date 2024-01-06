class PlayerCharacter:
    def __init__(self, name=None, age=0):  # dunder method -> similar to constructor from java
        self.name = name
        self.age = age
    # the self keyword -> refers to the player character -> the instance
    def run(self):
        print('run')
        return 'Done'

player1 = PlayerCharacter("Luis", 21)
print(f"Player One: {player1.name} \n", f"Age: {player1.age}")
player2 = PlayerCharacter("Lucy", 50)
