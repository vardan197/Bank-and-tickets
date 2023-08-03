ticket_count = int(input('Какое количество билетов вы хотите приобрести? '))
cost = 0

for guest in range(1, ticket_count + 1):
    print('Введите возраст', guest, 'посетителя: ', end='')
    age = int(input())

    if age > 25:
        cost += 1390

    elif 18 <= age <= 25:
        cost += 990

    else:
        cost += 0

if ticket_count > 3:
    cost = cost - cost * 10 / 100

print('Общая сумма к оплате: ', cost, 'рублей')
