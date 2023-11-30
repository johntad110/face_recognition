def absent_students(full_name_list):
    with open('attendace.csv', 'r') as f:
        a_line = f.readlines()
        print(a_line)
    for a_name in a_line:
        if a_name not in full_name_list:
            with open('absent.csv', 'r+') as ab:
                ab.writelines(f'\n{a_name}')
        else:
            print(a_name)


full_name = ['dibo', 'Fitsum (1)', 'hena', 'mercy', 'Miki', 'New_Name', 'Sami', 'Tesfa', 'Zerihun']
absent_students(full_name)
