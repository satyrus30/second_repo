
'''
Только что вышел новый фильм «Мстители»! В кассах кинотеатра много людей, стоящих в огромную очередь.
Каждый из них имеет один 100, 50или 25купюру. Билет на «Мстителей» стоит 25 dollars.

Вася сейчас работает клерком. Он хочет продать билет каждому человеку в этой очереди.

Может ли Вася продать билет каждому и отдать сдачу, если у него изначально нет денег
и он продает билеты строго в порядке очереди?

Вернитесь YES, если Вася сможет продать билет каждому и отдать сдачу с имеющимися у него в
данный момент купюрами. В противном случае вернитесь NO.
'''


def tickets(turn):
    wallet_list = []

    # следующий человек с купюрой в очереди
    def select_people(turn, i=0):
        return turn[i]

    #  кошелек Васи
    def wallet(wallet_info, new_item_wallet):
        wallet_info.append(new_item_wallet)
        return wallet_info

    i = 0
    if turn[i] != 25:
        return 'NO'
    else:
        wallet_list = wallet(wallet_list, select_people(turn))
        turn.remove(turn[i])

    while i < len(turn):
        if select_people(turn, i) == 50 and wallet_list.count(25) >= 1:
            wallet_list.remove(25)
            wallet(wallet_list, turn.pop(i))
        elif select_people(turn, i) == 100 and wallet_list.count(25) == 3:
            turn.pop(i)
            for y in wallet_list:
                wallet_list.remove(y)
        elif select_people(turn, i) == 100 and wallet_list.count(50) >= 1 and wallet_list.count(25) >= 1:
            wallet_list.remove(50)
            wallet_list.remove(25)
            turn.pop(i)
        elif select_people(turn, i) == 25:
            wallet(wallet_list, turn.pop(i))
        else:
            return 'NO'

    if i == len(turn):
        return 'YES'

