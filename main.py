import subprocess
import os

os.system('cls')

print('Enter your choice...')
print('Avaliable choices:')
print(' 1 - Say good morning!')
print(' 2 - Say good afternoon!')
print(' 3 - Say goodbye!')
print(' 4 - Exit the program')
x = input()
if x == '1':
    print('Good morning!')
    os.system('pause>nul')
    os.system('main.py')
elif x == '2':
    print('Good afternoon!')
    os.system('pause>nul')
    os.system('main.py')
elif x == '3':
    print('Goodbye!')
    os.system('pause>nul')
    os.system('main.py')
elif x == '4':
    os.system('cls')
    exit()
else:
    subprocess.run("error.bat")