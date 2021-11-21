from tkinter import*
window= Tk()
button= Button(window,text="Em chào thầy ạ, e là Bùi Gia Huy đây ạ.")
button.pack(padx=10, pady=10)  #hàm pack thêm chút khoảng ko vào xung quanh nút bấm
clickcount=0     
def onclick (event):
        global clickcount 
        clickcount+=1
        if clickcount==1:    
                button.configure(text="Nhanh thầy nhỉ chưa gì đã 2 năm rồi. ")
        elif clickcount==2:
                button.configure(text="Mới ngày nào thầy còn dạy code làm toét mắt ra :> ")
        elif clickcount==3:
                button.configure(text=" Nhân ngày 20-11 em kính chúc thầy và gia đình muốn mạnh khỏe\n và đạt nhiều thành công trong cuộc sống", background='red')        
        elif clickcount==4:
                button.configure(text="Thầy nhé") # cũng có màu đỏ, do set màu đỏ ở trên.
button.bind("<ButtonRelease-1 >",onclick)  
window.mainloop()  # vs code: view> Terminal == cmd


