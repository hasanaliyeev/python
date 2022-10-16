import pickle
import my_pickles

with open(r'C:\Users\aliye\Desktop\tests\game_state.bin', 'w+b') as file:
    pickle.dump(my_pickles.c, file)
