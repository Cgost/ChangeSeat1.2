from tkinter import *
import random


class ChangeSeat():

    def __init__(self):
        window = Tk()
        window.title("敬班專用1.2")
        self.canvas = Canvas(window, bg='white', width = 1200, height = 600)
        self.canvas.pack()

        bt = Button(window, text = "Shuffle", command = self.Display)
        bt.pack()

        self.namelist = ["石O華","石O允","江O純","林O辰","林O皓","林O華","邱O媛","洪O宏","俸O文","徐O恒",
                         "高O鈞","高O閎","張O琳","莊O翔","許O耀","許O諺","許O筑","陳O霖","陳O凱","陳O諭",
                         "陳O婕","陳O佳","曾O淇","黃O驛","黃O紘","詹O強","廖O翔","趙O毅","蔡O琦","蔡O欣",
                         "鄭O陽","葉O妤","王O皓","吳O成","林O祺","章O理","官O鎮","顏O翔","陳O瑜"]

        window.mainloop()

    def Display(self):
        self.canvas.delete("text")
        #01 75
        for i in range(0, 6):
            self.show(75, 75*i + 50, i)
            
        #02 250
        for i in range(0, 7):
            self.show(250, 75*i + 50, i+6)

        #03 425
        for i in range(0, 7):
            self.show(425, 75*i + 50, i+13)

        #04 600
        for i in range(0, 7):
            self.show(600, 75*i + 50, i+20)

        #05 775
        for i in range(0, 7):
            self.show(775, 75*i + 50, i+27)

        #06 950
        for i in range(0, 6):
            self.show(950, 75*i + 50, i+33)
        
        random.shuffle(self.namelist)

    def show(self, width, hight, num):
        self.canvas.create_text(width,
        	                    hight,
        	                    text = self.namelist[num],
        	                    font=("Purisa", 36),
        	                    fill = '#FF1200#FF1200',
        	                    tags = "text")

ChangeSeat()
