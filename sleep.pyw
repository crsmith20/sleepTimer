import subprocess
import tkinter as tk
class SleepApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.label = tk.Label(self, text="", width=10)
        self.label.pack()
        self.remaining = 0
        self.countdown(4500)
        

    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining
        if self.remaining <= 0:
            self.label.configure(text="Good Night!")
            p = subprocess.Popen([r"C:\Users\User\Desktop\sleep.cmd"])
            p.communicate()
            return
        else:
            if self.remaining >= 3600:
                hour = self.remaining // 3600
                minute = self.remaining % 3600 // 60
                seconds = self.remaining % 3600 % 60
                self.label.configure(text="%dh %dm %ds" %(hour, minute, seconds))
            elif self.remaining >= 60:
                minute = self.remaining // 60
                seconds = self.remaining % 60
                self.label.configure(text="%dm %ds" %(minute, seconds))
            else:
                self.label.configure(text="%ds" %self.remaining)
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)

if __name__ == "__main__":
    app = SleepApp()
    app.mainloop()
