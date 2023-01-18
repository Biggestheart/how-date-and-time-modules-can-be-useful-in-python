"""
Simple database made with dictionary and list
To make it work you have to copy to IDLE due to 
restrictions on Sololearn

"""


base = {}  # empty dictionary for start

while True:
    print()
    print('Base')  
    print('Chose option:')
    print('New input "n"')
    print('Delete "d"')
    print('Overview "p"')
    print('Exit "z"')
    print()

    inputopt = input('Please input option: ')
    if inputopt == 'n':
        name = input('Enter name: ')
        birth = input('Enter date of birth (dd/mm/yyyy): ')
        salary = input('Enter salary: ')
        date = input('Date of begining: ') 
        base.update({name : [birth, salary, date]})  # after we gather all required inputs from user  
        print(base)                                  # Key - first input (name), Value - list with 3 elements         
        # print result so we can overview all steps (if there is multiply inputs)
        
    if inputopt == 'd':
        delete = input('Enter name: ')
        del base[delete]  # delete key in dictionary together with its value 
        print(base) # print result so we can overview this step

    if inputopt == 'p':
        i = 1
        for k, v in base.items():  #printing overwiev with ascending number and content of database (dictionary)
            print(i, '.', k, ',', v[0], ',', v[1], ',', v[2])  
            i = i + 1
 
    if inputopt == 'z':
        break   #exit