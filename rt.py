import datetime

print()

# Print when to retired
print()
today=datetime.datetime.now()
retired=datetime.datetime(1982+60,2,17)
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
