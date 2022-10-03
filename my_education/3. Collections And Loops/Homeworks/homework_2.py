sticks = 10
while True:
    player1 = int(input('First player: '))
    sticks -= player1
    print(f'Stick counts: {sticks}')
    if sticks == 0:
        print('Win Player 2')
        break
    player2 = int(input('Second player: '))
    sticks -= player2
    print(f'Stick counts: {sticks}')
    if sticks <= 0:
        print('Win Player 1')
        break
