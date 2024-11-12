import pyautogui
import pyperclip
from openai import OpenAI
import time


api_key = "<your_api_key>"

client = OpenAI(
            api_key = api_key
        )

def is_last_message_from_sender(chat_log, sender_name="ayrav"):
    # Split the chat log into individual messages

    #[20:32, 11/11/2024] ayrav: thik ho jayega
    #[20:32, 11/11/2024] binayak: okk chal jaa


    messages = chat_log.strip().split("/2024] ")[-1]

    # [20:32, 11/11, ayrav: thik ho jayega]


    if sender_name in messages:
        return True 
    return False


time.sleep(2)

pyautogui.click(671, 755)
time.sleep(1)  # Wait for the system to respond

while True:

    time.sleep(1)

    # Step 2: Click and hold to start selecting at (522, 183)
    pyautogui.moveTo(520, 205)
    pyautogui.mouseDown()  # Press the left mouse button

    # Drag to position (711, 699) to select content
    pyautogui.moveTo(930, 700, duration=2)
    pyautogui.mouseUp()  # Release the mouse button
    time.sleep(2)

    # Step 3: Copy the selected content (Ctrl+C)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)  # Give time for the clipboard to update

    # Step 4: Deselect by clicking somewhere else
    pyautogui.click(900, 265)
    # Step 5: Get the copied content from the clipboard
    chat_log = pyperclip.paste()

    print(chat_log)

    print(is_last_message_from_sender(chat_log))

    if is_last_message_from_sender(chat_log):


        # integration of ai
        

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a person named Binayak who speaks hindi, odia as well as english. You are from India and you are a coder. You analyze chat history and roast people in a funny way. Output should be the next chat response (text message only)"},
                
                {"role": "system", "content": "Do not start like this [21:02, 12/6/2024] ayrav: "},
                {
                    "role": "user",
                    "content": chat_log
                }
            ]
        )

        response = completion.choices[0].message
        pyperclip.copy(response)
        

        # Optional Step: Click on position (605, 700) to paste (if needed)
        pyautogui.click(605, 700)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'v')

        # press the enter
        pyautogui.press("enter")
