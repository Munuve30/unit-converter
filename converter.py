name = input('Enter your name: ')
welcome_note= ('Welcome ' + name)
print(welcome_note)

#Kshs -usd
#m -km
#kgs - g
#Hrs - sec
# watts - kw

operation = input ( ('Choose one of the 5 operations to perform. \n 1. Kshs to USD \n 2. Meters to Kms \n 3. Kgs to Grammes \n 4. Hrs to Seconds \n 5. Kilowatts to watts \n Enter your choice: '))
print(operation)

if operation == '1':
    amount = float(input('Enter amount in Kshs: '))
 
    usd = amount/111
    print(str(amount) + ' Kshs is equal to '+ str(usd) + ' USD')
elif operation == '2':
    meters= float(input ('Enter length in meters: '))
 
    Kilometers= meters/1000
    print(str(meters) + 'Meters is equal to '+ str(Kilometers) + 'Kilometers')
elif operation== '3':
    grams = float(input('Enter weight in grams:'))
   
    Kilograms= grams/1000
    print(str(grams) + ' Gramms is equal to '+ str(Kilograms) + 'Kilograms')
elif operation== '4':
    hrs = float(input('Enter time in hours: '))
    sec = hrs*3600
    print (str(hrs) + ' hrs is equal to '+ str(sec) +' seconds')
elif operation == '5':
    watts = float(input('Enter power in watts: '))
    kw = watts/1000
    print(str(watts) + 'watts = ' + str(kw) + ' kilowatts')
else:
    print('Your selection is invalid. Run the program again and choose a valid option')
