from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':

    window = Tk()
    window.withdraw()
    secretcode=simpledialog.askstring(title="Code For Accessing Top Secret Files", prompt="I am PROTECTOR 13678. I am a computer program written to block secret files from society. Enter the corect code, and the secrets will be yours. (enter a code in the box down bellow)")

    if secretcode == "IJUSTPRANKEDYOU":

        simpledialog.askstring(title="YOU ARE CORRECT!!!!!", prompt="You are correct. The secrets are yours. And the secerets are... IN THE CODE!!! You just got PRANKED >:)!!!!!!")

    else:

        simpledialog.askstring(title="INTRUDER!!!!!!!", prompt="INTRUDER!!!!!!!! INTRUDER!!!!!!!! SOUND THE ALARMS!!!!!!")