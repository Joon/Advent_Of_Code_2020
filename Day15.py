numbers = [int(s) for s in "0,5,4,1,10,14,7".split(',')]
#numbers = [int(s) for s in "3,1,2".split(',')]

spoken_numbers = {}
last_said = 0

def say_number(said, turn):
    global last_said
    last_said = said
    if last_said in spoken_numbers.keys():
        spoken_numbers[last_said]['number_times_said'] += 1
        spoken_numbers[last_said]['last_said_at'].append(turn)
        return False
    else:
        spoken_numbers[said] = {'last_said_at': [turn], 'number_times_said': 1}
        return True

for i in range(len(numbers)):
    say_number(numbers[i], i + 1)

turn = len(spoken_numbers) + 1
last_said = numbers[len(numbers) - 1]
new_number = True
while turn <= 30000000:
    if turn % 1000000 == 0:
        print('.')
    if (new_number):
        new_number = say_number(0, turn)
    else:
        # the next number to speak is the difference between the turn number when it was last spoken 
        # and the turn number of the time it was most recently spoken before then 
        said_before = spoken_numbers[last_said]['last_said_at']
        before_1 = said_before[-2:][0]
        before_2 = said_before[-2:][1]
        turn_num = before_2 - before_1
        new_number = say_number(turn_num, turn)
    turn += 1

print(last_said)

#For example, suppose the starting numbers are 0,3,6:
#Turn 1: The 1st number spoken is a starting number, 0.
#Turn 2: The 2nd number spoken is a starting number, 3.
#Turn 3: The 3rd number spoken is a starting number, 6.
#Turn 4: Now, consider the last number spoken, 6. Since that was the first time the number had been spoken, the 4th number spoken is 0.
#Turn 5: Next, again consider the last number spoken, 0. Since it had been spoken before, the next number to speak is the 
#        difference between the turn number when it was last spoken (the previous turn, 4) and the turn number of the time it was 
#        most recently spoken before then (turn 1). Thus, the 5th number spoken is 4 - 1, 3.
#Turn 6: The last number spoken, 3 had also been spoken before, most recently on turns 5 and 2. So, the 6th number spoken is 5 - 2, 3.
#Turn 7: Since 3 was just spoken twice in a row, and the last two turns are 1 turn apart, the 7th number spoken is 1.
#Turn 8: Since 1 is new, the 8th number spoken is 0.
#Turn 9: 0 was last spoken on turns 8 and 4, so the 9th number spoken is the difference between them, 4.
#Turn 10: 4 is new, so the 10th number spoken is 0.