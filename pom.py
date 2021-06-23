import time
import sys
from playsound import playsound



def user_input():
    focus_duration = int(input('Please Enter duration (mins) of focus: '))
    break_duration = int(input('Please Enter break duration(mins) of interval: '))
    total_duration = int(input('Please enter number of sessions: '))
    return focus_duration, break_duration, total_duration


def countdown(focus_duration):
    for j in range(focus_duration-1,-1,-1):
        for i in range(59,-1,-1):
            if i <= 9:
                sys.stdout.write \
                (f'\rDuration: {j} Minutes {i} seconds to go')
            else:
                sys.stdout.write \
                (f'\rDuration: {j} Minutes {i} seconds to go')
                
            time.sleep(1)

if __name__ == "__main__":
    session_count = 0
    focus_duration, total_duration, break_duration = user_input()
    while session_count < total_duration:
        playsound(r'Sicko mode.mp3')
        countdown(focus_duration)
        playsound(r'Giorno theme.mp3')
        print('\nBreak time!')
        countdown(break_duration)
        session_count += 1
        print('\nsession number: ',session_count)
    print('\nEnd of Session!')