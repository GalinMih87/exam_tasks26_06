exp_need_amount = float(input())
battle_number = int(input())
bat_total = 0
count = 0
condition = False

for bat in range(1, battle_number + 1):
    follow_lines = float(input())

    bat_total += follow_lines
    count += 1

    if bat % 3 == 0:
        bat_total = (follow_lines * 0.15) + bat_total

    if bat % 5 == 0:
        bat_total = bat_total - (follow_lines * 0.10)

    if bat % 15 == 0:
        bat_total = (follow_lines * 0.05) + bat_total

    if bat_total >= exp_need_amount:
        condition = True
        break

if condition:
    print(f"Player successfully collected his needed experience for {count} battles.")
else:
    deff = abs(bat_total - exp_need_amount)
    print(f"Player was not able to collect the needed experience, {deff:.2f} more needed.")