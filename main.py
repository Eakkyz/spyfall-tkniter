import tkinter as tk
from tkinter import messagebox
from functools import partial
import random
import threading
import time

app = tk.Tk()
app.title("Spyfall")
app.geometry("500x500")


player_list = [];
player_role = [];
random_place = ''
place_list = ['คาเฟ่','โรงเเรม','ร้านอาหาร','โรงหนัง','โรงเรียน','ธนาคาร']
l1_role = ['คนอบขนม','คนชงชา','ลูกค้า','คนทำความสะอาด','Spy'] 
l2_role = ['เจ้าหน้าที่รักษาความปลอดภัย','พนักงานต้อนรับ','เจ้าของโรงเเรม','เเขก','Spy']
l3_role = ['เชฟ','เด็กเสิร์ฟ','อินฟลูเอนเซอร์ร์','เจ้าของร้าน','Spy']
l4_role = ['คนขายตั๋ว','ผู้รับชม','ผู้กับกับ','ดาราผู้เเสดง','Spy']
l5_role = ['นักเรียน','ครู','ผู้อำนวยการโรงเรียน','ภาโรง','Spy']
l6_role = ['เจ้าหน้าที่รักษาความปลอดภัย','ผู้ตรวจสอบบัญชี','นักการเงิน','โจร','Spy']

frame = tk.Frame(app)
frame.pack(side=tk.TOP, expand=False, fill="both")
player_entry = tk.Entry(frame)

def startGame():
    
    #top
    title = tk.Label(frame, text="Spyfall")
    title.pack()
    
    #todo Add player
    player_label = tk.Label(frame, text = "Player : ")
    player_label.pack()
    player_entry.pack()
    
    #todo Start Button
    start_button = tk.Button(frame, text="Start", command=GameMenu)
    start_button.pack()
    
    #todo Exit Button
    exit_button = tk.Button(frame, text="Exit")
    exit_button.pack()

def GameMenu():
    #set player
    playerCount = player_entry.get()
    #เคลียหน้านี้เพื่อเริ่มเกม
    for item in frame.winfo_children():
        item.destroy()
    #เพิ่มผู้เล่น 1, 2, 3, 4
    for player in range(0, int(playerCount)):
        player_list.append("Player "+str(player+1))
    #สุ่มสถานที่
    global random_place
    random_place = random.choice(place_list)

    #Add role
    role = []
    index = place_list.index(random_place)
    if(index == 0):
        role = l1_role
    elif(index == 1):
        role = l2_role
    elif(index == 2):
        role = l3_role
    elif(index == 3):
        role = l4_role
    elif(index == 4):
        role = l5_role
    elif(index == 5):
        role = l6_role
    for player in player_list:
        random_role = random.choice(role)
        if(random_role == "Spy"):
            role.remove('Spy')
        player_role.append(random_role)

    #show player
    for player in player_list:
        tk.Button(frame, text=player, command=partial(showDetails, player_list.index(player))).pack()
    #show all place
    for place in place_list:
        tk.Label(frame, text=place).pack()

    def endgame():
        app.destroy()

    #show end button
    end_button = tk.Button(frame, text="End Game",command=endgame)
    end_button.pack()
    #กรณีที่ player เป็นสปาย
def showDetails(player):
    if(player_role[player] == "Spy"):
        random_p = random.choice(place_list)
        while(random_p == random_place):
            random_p = random.choice(place_list)
        messagebox.showinfo("Player Information", "Place : "+random_p+"\nJob : "+player_role[player])
    else:
        messagebox.showinfo("Player Information", "Place : "+random_place+"\nJob : "+player_role[player])

startGame()

app.mainloop()