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

        self.namelist = ["石乃華","石博允","江永純","林羿辰","林暐皓","林槐華","邱詩媛","洪銘宏","俸經文","徐培恒",
                         "高若鈞","高璿閎","張緯琳","莊竣翔","許家耀","許峰諺","許雅筑","陳奕霖","陳彥凱","陳柏諭",
                         "陳郁婕","陳靜佳","曾郁淇","黃茹驛","黃際紘","詹智強","廖紹翔","趙紘毅","蔡孟琦","蔡詠欣",
                         "鄭智陽","葉純妤","王  皓","吳祐成","林元祺","章得理","官宇鎮","顏于翔","陳玟瑜"]

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
