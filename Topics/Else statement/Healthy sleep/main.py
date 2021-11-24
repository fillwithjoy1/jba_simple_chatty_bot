sleep_deficiency_marker = int(input())
sleep_excess_marker = int(input())
current_sleep = int(input())

if sleep_deficiency_marker <= current_sleep <= sleep_excess_marker:
    print('Normal')
elif sleep_deficiency_marker >= current_sleep:
    print('Deficiency')
elif current_sleep >= sleep_excess_marker:
    print('Excess')