
calender_reminder = {
'10/01/2019': 'Doctor\'s Appointment',
'10/05/2019': 'Invitation at Samanta\'s Place',
'10/08/2019': 'Meeting with Professor',
'10/09/2019': 'Dinner at EVCU',
'10/12/2019': 'Cricket Tournament',
'10/18/2019': 'Last Date of Assignment Submission',
'10/26/2019': 'Picnic at Parvis Apu\'s Place',
'10/28/2019': 'Class Test 2',
'10/31/2019': 'Halloween Party'
}
print('Welcome to the Calender Reminder. We have the schedule of the month of October:')
for x in calender_reminder:
    print(x)
print('Which date would you like to see?')
x= input()

if x in calender_reminder:
    print('{} is reserved for {}.'.format(x, calender_reminder[x]))
else:
    print('Sorry, we don\'t have any event on {} .'.format(x))