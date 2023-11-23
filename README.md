# Japanese Listening Comprehension App

## Overview

This application is designed to improve your Japanese listening comprehension skills. It generates audio prompts with different formats, including:

- Dollar and cent amounts
- Month and day expressions
- Yen amounts
- Phone numbers
- Time duration from one date to another

## How to Use

### Option 1: Run EXE

Run [japanese_listening_comprehension_app.exe](dist/japanese_listening_comprehension_app.exe)

### Option 2: Manual Installation

1. **Installation:** Ensure you have Python and the required libraries installed. Install the dependencies using:

    ```bash
    pip install -r requirements.txt
    ```

2. **Run the Application:**

    ```bash
    python japanese_listening_comprehension_app.py
    ```

3. **User Interface:**

    - The main window includes a text area, buttons, and a label displaying the question count.

    - Press "Show Answer" to reveal the correct answer after listening to the audio prompt.

    - Click "Play" to listen to the audio prompt.

    - Use "Next" to move to the next question. The button changes to "Restart" at the end.

4. **Listening and Writing:**

    - Before pressing "Show Answer," prepare your writing material to note down what you hear.

    - Compare your written answer with the revealed answer after pressing "Show Answer."

5. **Supported Formats:**

    - Dollar and cent amounts (e.g., "25 dollars 78 cents").
    - Month and day expressions (e.g., "March 15").
    - Yen amounts (e.g., "540 yen").
    - Phone numbers (e.g., "3 の 7 の 9").
    - Time duration from one date to another (e.g., "from 10:30 AM to 12:15 PM").

## Note

- The application saves temporary audio files in the "temp_audio" folder. These files are deleted when you restart the application.

- Ensure your system's audio is enabled and the volume is adjusted for optimal listening experience.
