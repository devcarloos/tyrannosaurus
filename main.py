import signal
import time
import pyautogui
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

paused = False

def signal_handler(sig, frame):
    global paused
    paused = not paused

signal.signal(signal.SIGTSTP, signal_handler)

def send_words(words):
    global paused
    time.sleep(2)
    for word in words:
        if paused:
            input('Script paused. Press Enter to resume...')
            paused = False

        logging.info(f'Sending word: {word}')
        logging.info('Typing word...')
        pyautogui.typewrite(word, interval=0.1)
        logging.info('Pressing Enter...')
        pyautogui.press('enter')
        time.sleep(0.5)
        logging.info('Clicking left button...')
        pyautogui.click(button='left')

def main():
    default_words = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    user_input = input('Would you like to use a custom file for words? (y/n): ')

    if user_input.lower() == 'y':
        custom_file = input('Enter the path of the file with words: ')
        with open(custom_file, 'r') as file:
            words = file.read().split()
    else:
        words = default_words

    input('Press Enter to start sending words...')
    send_words(words)

if __name__ == '__main__':
    main()
