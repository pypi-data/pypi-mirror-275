import openai
import subprocess

def run_program(file_path, interpreter,secret):
    def genAIErrorMessage(error_message,secret):
        openai.api_key = secret

        chat_complete = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=[{"role":"user","content":str(error_message)}])

        print(chat_complete.choices[0].message.content)
    try:
        result = subprocess.run(
            [interpreter, file_path],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            genAIErrorMessage(result.stderr,secret)
        else:
            print("Program output:")
            print(result.stdout)
    
    except Exception as e:
        print(f"An exception occurred: {e}")