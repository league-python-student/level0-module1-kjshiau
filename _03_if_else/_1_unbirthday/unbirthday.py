from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':

    window = Tk()
    window.withdraw()
    birthdayquestion=simpledialog.askstring(title="Unbirthday or Birthday?", prompt="Is your birthday today? I just want to know cause I'm bored and that was the first question that popped in my head. Don't judge me >:( !!!!!")

    if birthdayquestion == "yes":

        simpledialog.askstring(title="Birthday!!!!", prompt="Happy birthday, I guess. To be honest I don't really know you that well.")

    elif birthdayquestion == "no":

        simpledialog.askstring(title="Unbirthday!!!", prompt="Happy unbirthday!!!! What?! You don't know what an unbirthday is? Bit it's in Alice in Wonderland! WHAT??!! You haven't heard of Alice and Wonderland!!!!! I only mildly liked you before, \n but now I REALLY HATE YOU >:( !!!!!!!")

    else:
        simpledialog.askstring(title="????", prompt="Look. I am just a computer code. So I am only written to react to yes and no responses. So go back and type either yes or no. Come on! I don't got all day! Oh wait, I do.")