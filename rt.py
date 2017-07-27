import datetime
import os
import send2trash

print('*'*40)

os.chdir('/home/peter/Pictures')
print('Skip to %s ...' %os.getcwd())

if not os.listdir()==[]:
    for i in os.listdir():
        send2trash.send2trash(i)
        print('%s deleted' %i)
else:
    print('The folder is empty.')
        
print('*'*40)

# Print when to retired
print()
today=datetime.datetime.now()
retired=datetime.datetime(1981+60,1,24)
rest=(retired-today).days
years=1982+60-datetime.datetime.now().year
print('You will retire after ', rest, 'days, less than ', years, 'years.')
print('*'*40)
print('''
Time is very slow for those who wait;
very fast for those who are scared;
very long for those who lament;
very short for those who celebrate;
but for those who love, time is eternal.''')
print('- William Shakespeare'.rjust(40))
print('*'*40)
