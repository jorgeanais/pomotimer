import numpy as np
import time
from datetime import datetime, timedelta
import click
import os

"""
This script is intended to be used as a Pomodoro alarm to divide a work session into blocks.
Between blocks, there are breaks to relax or talk among the participants.
At the end of each section it will produces a sound alarm.

Feel free to remodify this code at your own will.
"""

welcome_string = '''
  _____       _             _        _______        _           _       
 / ____|     | |           | |      |__   __|      | |         (_)      
| (___   __ _| | __ _    __| | ___     | |_ __ __ _| |__   __ _ _  ___  	
 \___ \ / _` | |/ _` |  / _` |/ _ \    | | '__/ _` | '_ \ / _` | |/ _ \ 
 ____) | (_| | | (_| | | (_| |  __/    | | | | (_| | |_) | (_| | | (_) |
|_____/ \__,_|_|\__,_|  \__,_|\___|    |_|_|  \__,_|_.__/ \__,_| |\___/ 
                                                              _/ |      
                                                             |__/ 
                                       Alumnos Magister en Astronomía UA
'''

# Session settings
block_duration = 30  # minutes
break_duration = 10  # minutes
blocks_number = 3

# Sound settings (requires sox; sudo apt install sox)
nice_sound = 'play -nq -t alsa synth pl G2 pl B2 pl D3 pl G3 pl D4 pl G4 delay 0 .05 .1 .15 .2 .25 remix - fade 0 4 .1 norm -1'
# annoying_sound = 'play -nq -t alsa synth 3 sin 0+19000 sin 1000+20000 remix 1,2 channels 2'
# sine_sound = 'play -nq -t alsa synth 3 sine 500'

# Time calculations
blocks = np.arange(blocks_number)
block_time = int(block_duration * 60)
break_time = int(break_duration * 60)
total_time_in_seconds = int(blocks_number * (block_time + break_time))

# Start
click.clear()
click.echo(welcome_string)
print('Block last: ', block_duration, ' min')
print('Break last: ', break_duration, ' min')
print()
click.pause()

click.clear()
click.echo(welcome_string)
start_time = datetime.now()
end_time = start_time + timedelta(seconds=total_time_in_seconds)
print('Block last: ', block_duration, ' min')
print('Break last: ', break_duration, ' min')
print()
print('Start time:', start_time.strftime('%H:%M'))
print('End time:', end_time.strftime('%H:%M'))
print()

for blk in range(blocks_number):

    # Working block
    print('Block ', blk + 1)
    with click.progressbar(range(block_time)) as bar:
        for _ in bar:
            time.sleep(1)

    # Break
    print('Break')
    os.system(nice_sound)

    with click.progressbar(range(break_time)) as bar:
        for _ in bar:
            time.sleep(1)

    os.system(nice_sound)

