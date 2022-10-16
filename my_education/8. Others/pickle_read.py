import pickle

c = None

with open(r'C:\Users\aliye\Desktop\tests\game_state.bin', 'rb') as file:
    c = pickle.load(file)

print(c.health)
print(c.__dict__)
