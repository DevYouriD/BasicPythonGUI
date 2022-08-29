from tkinter import *

window = Tk()
#window.iconbitmap('Resources/[FILENAME].ico')
window.title('Password Generator GUI')
window.config(height=500, width=500, background='black')

#headerImage = PhotoImage(file='Resources/[FILENAME].png')
#Label(window, image=headerImage, bg='black').place(relx=0.5, rely=0.16, anchor=CENTER)

#MAIN FUNCTIONALITY


#CLOSE
def close_window():
    window.destroy()
    exit()

Button(window, text='EXIT', width=6, command=close_window, font='none 10 bold').place(relx=0.08, rely=0.95, anchor=CENTER)

window.mainloop()