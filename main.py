import pyinputplus as pyip
import sys
import entropy

def start():
    start_up = pyip.inputYesNo(prompt=('[?] Begin random number gen? [Y/N]: '))
    if start_up == 'yes':
        entropy.generator()
    if start_up == 'no':
        sys.exit()

entropy.temp_gen()

if __name__ == "__main__":
    start()