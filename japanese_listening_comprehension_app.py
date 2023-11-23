import random
from datetime import datetime, timedelta
import calendar
from googletrans import Translator
from gtts import gTTS
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel
from PyQt5.QtCore import QUrl
import os

class LearnJapaneseApp(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize variables
        self.words = self.generate_words()
        self.count = 0
        self.init_ui()
        self.unique_filename = ""
        self.played = False

        # Initialize media player
        self.media_player = QMediaPlayer()

        # Create a temporary folder by deleting the existing one (if it exists) and creating a new one
        self.temp_folder = "temp_audio"
        if os.path.exists(self.temp_folder):
            # Delete existing folder and its contents
            self.deleteTempFiles()
        else:
            # If the folder doesn't exist, create a new one
            os.makedirs(self.temp_folder)

    def init_ui(self):
        # Set up the layout
        layout = QVBoxLayout()

        # Text area
        self.text_area = QTextEdit(self)
        self.text_area.setPlaceholderText("Answer will be displayed here.")
        self.text_area.setReadOnly(True)
        self.text_area.hide()

        # QLabel to show count and total questions
        self.label_count = QLabel(self)
        self.update_label_count()

        # Buttons
        self.show_text_button = QPushButton('Show Answer', self)
        self.show_text_button.clicked.connect(self.show_text)

        self.replay_button = QPushButton('Play', self)
        self.replay_button.clicked.connect(self.replay)

        self.next_button = QPushButton('Next', self)
        self.next_button.clicked.connect(self.next_text)

        # Add widgets to the layout
        layout.addWidget(self.label_count)
        layout.addWidget(self.text_area)
        layout.addWidget(self.show_text_button)
        layout.addWidget(self.replay_button)
        layout.addWidget(self.next_button)

        # Set the layout for the main window
        self.setLayout(layout)

        # Set up the main window
        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle('Japanese Listening Comprehension App')

        self.show()

    def generate_words(self):
        return [self.generate_word(random.randint(1, 5)) for _ in range(10)]

    def generate_word(self, format_numbers):
        # Dollar and Cent formats
        if format_numbers == 1:
            temp = random.randint(1, 7)
            dollars_range = (10 ** (temp - 1), 10 ** temp - 1)
            dollars = random.randint(*dollars_range)
            cents = random.randint(0, 99)
            return f"{dollars} dollar {cents} cent"
        # Month Day format
        elif format_numbers == 2:
            month = calendar.month_name[random.randint(1, 12)]
            return f"{month} {random.randint(1, 31)}"
        # Yen formats
        elif format_numbers == 3:
            temp = random.randint(1, 7)
            yen_range = (10 ** (temp - 1), 10 ** temp - 1)
            return f"{random.randint(*yen_range)} yen"
        # Phone number formats
        elif format_numbers == 4:
            num1 = " ".join(str(random.randint(1, 9)) for _ in range(3))
            num2 = " ".join(str(random.randint(1, 9)) for _ in range(3))
            num3 = " ".join(str(random.randint(1, 9)) for _ in range(3))
            return f"{num1} の {num2} の {num3}"
        # from ~
        else:
            start_time = datetime(2023, 1, 1, 10, 0) + timedelta(minutes=random.randint(0, 120))
            end_time = start_time + timedelta(minutes=random.randint(1, 120))
            return f"from {start_time.strftime('%I:%M %p')} to {end_time.strftime('%I:%M %p')}"
        
    def show_text(self):
        self.text_area.show()
        self.text_area.setPlainText(f'{self.words[self.count]}')

    def translate_and_play(self, word):
        translator = Translator()
        translated_text = translator.translate(word, dest='ja').text

        # Generate a unique file name in the temp folder
        if(self.played==False):
            self.unique_filename = os.path.join(self.temp_folder, f"temp_{datetime.now().strftime('%Y%m%d%H%M%S')}.mp3")
            # Save translated text to the temporary file
            tts = gTTS(translated_text, lang='ja', slow=True)
            tts.save(self.unique_filename)

        # Play audio using QMediaPlayer
        audio_url = QUrl.fromLocalFile(self.unique_filename)
        media_content = QMediaContent(audio_url)
        self.media_player.setMedia(media_content)
        self.media_player.play()
        self.played = True


    def replay(self):
        self.translate_and_play(self.words[self.count])

    def update_label_count(self):
        self.label_count.setText(f"{self.count + 1}/{len(self.words)}")

    def next_text(self):
        self.played = False
        if self.count < len(self.words) - 1:
            self.count += 1
            self.text_area.hide()
            self.update_label_count()
            if self.count == 9:
                self.next_button.setText('Restart')
        else:
            self.regenerate_words()

    def regenerate_words(self):
        self.next_button.setText('Next')

        self.deleteTempFiles()
        
        self.words = self.generate_words()
        self.count = 0
        self.text_area.hide()
        self.update_label_count()

    def deleteTempFiles(self):
        # Delete all audio temp files in the temporary folder
        for filename in os.listdir(self.temp_folder):
            file_path = os.path.join(self.temp_folder, filename)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = LearnJapaneseApp()
    sys.exit(app.exec_())
