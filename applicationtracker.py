counter = 0
daily_quota = 0


daily_quota = int(input('what is ur daily quota for today? '))

file = open("day1.txt", "w")
while counter <= daily_quota:
    application = input('what is the company name? ')
    position = input('what is the position: ') 
    proceed = input('Proceed to the next position? ')
    file.write("\n")
    file.write("Company: " + str(application) + " |  Position: " + str(position) + "")
    if proceed == 'yes' or proceed == 'y':
        print("Company: " + str(application),  "Position: " + str(position))
        counter += 1
    else:
        break   
    print(counter)

file.close()
    
    


