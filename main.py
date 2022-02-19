from tkinter import *
import time

# get current time in seconds
t = time.time()
final = t + 60
count=0

word_list = ['you', 'look', 'so', 'beautiful', 'in', 'that', 'dress', 'i', 'love', 'your', 'face', 'like', 'that', 'baby', 'you', 'know',
             'you', 'should', 'always', 'call', 'me', 'when', 'ever', 'you', 'need', 'my', 'held', 'your', 'ass', 'smells', 'so', 'good', 'when', 'you',
             'fat', 'but', 'that', 'does', 'not', 'give', 'you', 'freelance', 'to', 'do', 'so', 'that', 'is', 'for', 'sure', 'not', 'healthy']
sentence = ' '.join(word_list)
def onKeyPress():
    global count
    test = text.get("1.0", 'end')
    text.configure(width=0, height=0)
    text1.delete("1.0", 'end')


    e = test.split(' ')
    for i in e:
        if i in word_list:
            count += 1
            word_list.remove(i)
    text1.insert('end', f'time up: your wpm is {count}wpm ')
    # if event.char == " ":
    #
    #

    # if time.time() >= final:





        # text.insert('end', 'You done %s\n' % (event.char,))

root = Tk()
root.geometry('300x400')

text1 = Text(root, width=30, height=6, background='white', foreground='black', font=('Comic Sans MS', 12))
text1.insert('end', f'{sentence}\n')
text1.pack()

text = Text(width=30, height=6, background='black', foreground='white', font=('Comic Sans MS', 12))

text.insert('1.0', ' ')
text.pack()

root.after(60000, onKeyPress)

# root.bind('<KeyPress>', onKeyPress)
root.mainloop()