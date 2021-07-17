##Nathan Hinton
##This program will take the data gathered by the program and will sample it for usage

from pickle import load
name = input('enter your name: ')
try:
    data = load(open('%s.sta'%name, 'rb'))
except FileNotFoundError:
    print('Profile file not found. Not loading data...')

keys = []
total_tries = 0
avg_speed = 0
times_watched = 0
for item in data:
    keys.append(item)
    dat = data[item]
    total_tries += dat[0]
    times_watched += dat[1]
    avg_speed += dat[-1]

words = len(keys)
avg_speed = avg_speed/len(keys)

print("""

Information:
Items in the dataset: %s
Total words: %s
Total tried: %s
Total times watched: %s
Average LPM: %s
"""%(len(keys), words, total_tries, times_watched, avg_speed))

print('analyzed! Printing suggestions:')
#Suggest increasing the speed
if times_watched <= words * 1.20:#if you have to watch again 20 percent of the time:
    print('Increase speed. You did not have to rewatch the words many times!')
elif total_tries <= words * 1.10:#if you were right 9 of 10 times
    print('Increase speed. You were often right (%95 to be exact)')
#suggest slowing down
if times_watched > words *1.40:#If you had to re watch about 30 percent of the time:
    print('Slow down. You had to rewatch the word many times.')
elif total_tries > words * 1.20:#If you often got the wrong word
    print('Slow down. You often entered the wrong word.')