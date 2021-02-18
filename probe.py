from datetime import datetime

user_id = 1488

a = "15"
print(isinstance(a, int))

user_input_command = input()
if user_input_command == 'create_conf':
    print('Укажи количество созданных конфигураций:')
    user_input_work = int(input())
    if user_input_work <= 0:
        print('Введено значение <= 0')
    else:
        print('create_conf:', user_input_work, '\nuser_id:', user_id, '\ndatetime:', datetime.now())
else:
    if user_input_command == 'change_conf':
        print('Укажи количество измененных конфигураций:')
        user_input_work = int(input())
        if user_input_work <= 0:
            print('Введено значение <= 0')
        else:
            print('create_conf:', user_input_work, '\nuser_id:', user_id, '\ndatetime:', datetime.now())
    else:
        print('Хорошо подумай, прежде чем мне такое писать')




