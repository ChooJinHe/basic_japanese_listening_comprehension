import random
from datetime import datetime, timedelta
import calendar
from googletrans import Translator
from gtts import gTTS
import os

def generate_word(format_numbers):
    # Dollar and Cent formats
    if format_numbers == 1:
        temp = random.randint(1, 7)
        dollars_range = (10 ** (temp - 1), 10 ** temp - 1)
        dollars = random.randint(*dollars_range)
        cents = random.randint(0, 99)
        word = f"{dollars} dollar {cents} cent"
    # Month Day format 
    elif format_numbers == 2:
        month = calendar.month_name[random.randint(1, 12)]
        word = f"{month} {random.randint(1, 31)}"
    # Yen formats
    elif format_numbers == 3:
        temp = random.randint(1, 7)
        yen_range = (10 ** (temp - 1), 10 ** temp - 1)
        word = f"{random.randint(*yen_range)} yen"
    # Phone number formats
    elif format_numbers == 4:
        num1 = " ".join(str(random.randint(1, 9)) for _ in range(3))
        num2 = " ".join(str(random.randint(1, 9)) for _ in range(3))
        num3 = " ".join(str(random.randint(1, 9)) for _ in range(3))
        word = f"{num1} の {num2} の {num3}"
    # from ~
    else:
        start_time = datetime(2023, 1, 1, 10, 0) + timedelta(minutes=random.randint(0, 120))
        end_time = start_time + timedelta(minutes=random.randint(1, 120))
        word = f"from {start_time.strftime('%I:%M %p')} to {end_time.strftime('%I:%M %p')}"


    return word

import keyboard

def translate_and_play(word):
    translator = Translator()
    translated_text = translator.translate(word, dest='ja').text

    # Save translated text to a temporary file
    tts = gTTS(translated_text, lang='ja')
    tts.save("temp.mp3")
    os.system("start temp.mp3") 
    # Play the temporary file in a loop until a right mouse click
    while True:
        if keyboard.is_pressed('r'):  # Detects a left mouse click
            os.system("start temp.mp3")
        elif keyboard.is_pressed('space'):  
            break
    

# Generate 10 sets of format numbers
format_numbers_list = [random.randint(1, 5) for _ in range(10)]

# Generate and translate 10 words
count = 1
for format_numbers in format_numbers_list:
    generated_word = generate_word(format_numbers)
    print(f'{count}) {generated_word}')
    translate_and_play(generated_word)
    count += 1
