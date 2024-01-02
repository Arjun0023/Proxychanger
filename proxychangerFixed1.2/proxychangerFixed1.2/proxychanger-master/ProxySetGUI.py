import tkinter
import os
import time
import pyperclip
import ProxySolution2 as PS

class setProxy(object):
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Change Your Proxy Scripts!")
        self.lable = tkinter.Label(self.root, text="The proxy file name is : ")
        self.button_enable = tkinter.Button(self.root, command = self.enableProxy, text = "I WANT GOOGLE!")
        self.button_disable = tkinter.Button(self.root, command = self.disableProxy, text = "I am cool now.")
        self.filename_input = tkinter.Entry(self.root,width = 30)
        self.original_proxy = "HTTP:AMD YES"

    def gui_arrange(self):
        self.lable.pack()
        self.filename_input.pack()
        self.button_disable.pack()
        self.button_enable.pack()

    def enableProxy(self):       
        file = self.filename_input.get()
        rfile = open(file, mode = 'r')
        pr = rfile.readlines()
        for line in pr:
            line = line[:-1]
        proxy = pr[0] 
        rfile.close()
        print(proxy)
        #os.system("echo '%s' | pbcopy" % proxy)
        
        # Real Magic Happens Here
    #-------------------------------------------------------
        os.system('start ms-settings:network-proxy')
        time.sleep(1)
        PS.press(PS.VK_TAB)   
        time.sleep(0.5)
        PS.press(PS.VK_TAB)
        time.sleep(0.5)
        PS.keyBinding(PS.VK_CONTROL,PS.VK_A)
        #PS.keyBinding(PS.VK_CONTROL,PS.VK_C)
        #time.sleep(0.15)
        #self.original_proxy = pyperclip.paste()
        pyperclip.copy(proxy)
        PS.keyBinding(PS.VK_CONTROL,PS.VK_V)
        PS.press(PS.VK_TAB)
        time.sleep(0.5)
        PS.press(PS.VK_RETURN)
        time.sleep(1)
        PS.keyBinding(PS.VK_MENU,PS.VK_F4)
        #tkinter.messagebox.showinfo('Done', 'Enjoy the goodness of Goolge!')


    
    def disableProxy(self):
        os.system('start ms-settings:network-proxy')
        time.sleep(1)
        PS.press(PS.VK_TAB)   
        time.sleep(0.5)
        PS.press(PS.VK_TAB)
        time.sleep(0.5)
        PS.keyBinding(PS.VK_CONTROL,PS.VK_A)
        pyperclip.copy(self.original_proxy)
        PS.keyBinding(PS.VK_CONTROL,PS.VK_V)
        PS.press(PS.VK_TAB)
        time.sleep(0.5)
        PS.press(PS.VK_RETURN)
        time.sleep(1)
        PS.keyBinding(PS.VK_MENU,PS.VK_F4)
        #tkinter.messagebox.showinfo('Done', 'You are back in default')

if __name__ == "__main__":
    sP = setProxy()
    sP.gui_arrange()
    tkinter.mainloop()
    pass