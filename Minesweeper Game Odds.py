while True:
    # main program
    while True:
        gems = input(f'\nHow many gems do you want? (Max 24, Min 1): ')

        try:
            gems = int(gems)
        except ValueError:
            break

        if gems not in range(1, 25):
            print(f'{gems} is outside the range, please choose another number.')
            break

        total = 1
        for i in range(gems):
            top = gems - i
            bottom = 25 - i

            gem_odds = top/bottom
            total = total * gem_odds

            odds = "{:,.2f}".format(1/total)
            print(f'The odds of choosing {i + 1} gems is 1 in {odds}')