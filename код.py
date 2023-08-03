money = int(input("Введите сумму, которую планируете положить под проценты: "))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

TKB = round(((per_cent['ТКБ']) * (money/100)), 2)
SKB = round(((per_cent['СКБ']) * (money/100)), 2)
VTB = round(((per_cent['ВТБ']) * (money/100)), 2)
SBER = round(((per_cent['СБЕР']) * (money/100)), 2)
deposit = [TKB, SKB, VTB, SBER]

print("Накопленные средства за год вклада в каждом из банков:", deposit)
print("Максимальная сумма, которую вы можете заработать за год: ", max(deposit))