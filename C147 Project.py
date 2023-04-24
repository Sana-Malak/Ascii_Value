from tkinter import *

root=Tk()
root.title("Ascii")

root.geometry("400x400")
root.configure(background= 'snow')

enter_word = Entry(root)
enter_word.place(relx=0.5,rely=0.4,anchor=CENTER)

label = Label(root, text = "Name in Ascii : ", bg="light yellow", fg="black")
label2 = Label(root, text = "Encrypted value : ", bg="light yellow", fg="black")

def asciiConverter(): 
    input_word = str(enter_word.get()) 
    
    for letter in input_word : 
        label["text"] += str(ord(letter)) + " " 
        ascii = int(ord(letter)) 
        encrypted = ascii - 1 
        label2["text"] += str(chr(encrypted))

btn=Button(root,text="Show name in Acsii",command=asciiConverter, bg='gold', fg = 'black')
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

label.place(relx=0.5,rely=0.6,anchor=CENTER)
label2.place(relx=0.5,rely=0.7,anchor=CENTER)
root.mainloop()



