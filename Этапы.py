import datetime

number_stages = int(input('Сколько всего будет этапов: ')) # количество этапов
time_stage = int(input('Введите время сколько будет длиться один этап (в минутах): ')) # время этапа
transition_time = int(input('Введите время на переход (в минутах): ')) # время не переход
time_what = input('Во сколько начало (в формате 12:00): ')

skl = 0

hour, minute = time_what.split(':')
hour, minute = int(hour), int(minute)

x = datetime.timedelta(hours=hour, minutes=minute)

y = x + datetime.timedelta(minutes=time_stage)

if transition_time == 1:
    skl = 'минута'
elif transition_time % 10 == 2 or transition_time % 10 == 3 or transition_time % 10 == 4 or  transition_time in [2,3,4]:
    skl = 'минуты'
else:
    skl = 'минут'

for i in range(1, number_stages + 1):
    if i == 1:
        print(f'Этап {i}| С {x} до {y}| Переход {transition_time} {skl}')
        y = x + datetime.timedelta(minutes=transition_time) + datetime.timedelta(minutes=time_stage)
    else:
        x = y
        y = x + datetime.timedelta(minutes=time_stage) + datetime.timedelta(minutes=transition_time)
        print(f'Этап {i}| С {x} до {y - datetime.timedelta(minutes=transition_time)}| Переход {transition_time} {skl}')


