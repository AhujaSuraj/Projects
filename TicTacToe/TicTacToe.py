import tkinter as tk
import tkinter.messagebox as tmb
root = tk.Tk()
root.resizable(False,False)



class tictac(tk.Frame):
    #this is to check whose turn is currntly goiung
    clickedButton=True
    
    #this to check who will play first in the new round
    playerturn=True
    
             
    #this is to check how many turn.click have been done in asingle round
    roundturn=0
    def __init__(self, master=None):
        tk.Frame.__init__(self,master)
        self.grid()
        
        #Generall Game Buttons
        newgame=tk.Button(text= 'New Game')
        nextround=tk.Button(text= 'Next Round',state='disabled')
        exitgame=tk.Button(text= 'Exit Game') #not using it
        startgame=tk.Button(text= 'Start Game')
        
        #players identification objects
        player1_label=tk.Label(text='Player 1 Name (X)')
        player1=tk.Entry()
        player2_label=tk.Label(text='Player 2 Name (O)')
        player2=tk.Entry()
        
        #player scoreing
        
        #player 1 scoreing
        player1_name_label=tk.Label(text='Player 1 Score')
        player1_score=tk.Entry()
        player1_score.insert(0,'0')
        player1_score.config(state='readonly')
        #player 2 scoreing
        player2_name_label=tk.Label(text='Player 2 Score')
        player2_score=tk.Entry()
        player2_score.insert(0,'0')
        player2_score.config(state='readonly')
        
        #Game Board Buttons
        gameboard=tk.Label(text='Game Board')
        b1 = tk.Button(text=' ',font=('Times 20'),bg = 'black', fg = 'white', height = 4, width = 8,state="disabled")
        b2 = tk.Button(text=' ',font=('Times 20'),bg = 'black', fg = 'white', height = 4, width = 8,state="disabled")
        b3 = tk.Button(text=' ',font=('Times 20'),bg = 'black', fg = 'white', height = 4, width = 8,state="disabled")
        b4 = tk.Button(text=' ',font=('Times 20'),bg = 'black', fg = 'white', height = 4, width = 8,state="disabled")
        b5 = tk.Button(text=' ',font=('Times 20'),bg = 'black', fg = 'white', height = 4, width = 8,state="disabled")
        b6 = tk.Button(text=' ',font=('Times 20'),bg = 'black', fg = 'white', height = 4, width = 8,state="disabled")
        b7 = tk.Button(text=' ',font=('Times 20'),bg = 'black', fg = 'white', height = 4, width = 8,state="disabled")
        b8 = tk.Button(text=' ',font=('Times 20'),bg = 'black', fg = 'white', height = 4, width = 8,state="disabled")
        b9 = tk.Button(text=' ',font=('Times 20'),bg = 'black', fg = 'white', height = 4, width = 8,state="disabled")
       
        #setting objects of the game in list.
        screenobjects = [newgame,nextround,exitgame,
                         player1_label,player1,player2_label,player2,
                         startgame,
                         player1_name_label,player1_score,player2_name_label,player2_score,
                         gameboard,b1,b2,b3,b4,b5,b6,b7,b8,b9]
        
        self.createWidget(screenobjects)
    
    def createWidget(self,objects):
        #New Game button
        objects[0].grid(row=0,column=0)
        objects[0]['command'] = lambda:self.NewGame(objects)
       
        #Next Round Button
        objects[1].grid(row=6,column=1)
        objects[1]['command'] = lambda:self.NextRound(objects)
        
        #Exit Game Button 
        objects[2].grid(row=0,column=1)
        objects[2]['command'] = lambda:self.ExitGame(objects)
        
        #player 1:
        objects[3].grid(row=1,column=0) #labels
        objects[4].grid(row=1,column=1) #input
        
        #player 2:
        objects[5].grid(row=2,column=0) #labels
        objects[6].grid(row=2,column=1) #input
        
        #Start Game Button
        objects[7].grid(row=3,column=1)
        objects[7]['command'] = lambda:self.StartGame(objects)
        
        #Game Scoring
        
        #player 1 Score
        objects[8].grid(row=4,column=0)  #label value of playe 1 name text box
        objects[9].grid(row=4,column=1)  #player 1score
        
        #player 2 Score
        objects[10].grid(row=5,column=0)  #label value of playe 2 name text box
        objects[11].grid(row=5,column=1)  #player 2score
        
        
        #Game Grid 
        objects[12].grid(row=6,column=0) #gameboard labe;
        
        gamebobjects=objects[13:] ##getting only game board boxes
        scoringobject=[objects[4],objects[9],objects[6],objects[11],objects[1]]
        
        #Game Board Box 1
        objects[13].grid(row=10,column=0) 
        objects[13]['command'] = lambda:self.ButtonClick(gamebobjects,objects[13],scoringobject)
        
        #Game Board Box 2
        objects[14].grid(row=10,column=1) 
        objects[14]['command'] = lambda:self.ButtonClick(gamebobjects,objects[14],scoringobject)
        
        #Game Board Box 3
        objects[15].grid(row=10,column=2) 
        objects[15]['command'] = lambda:self.ButtonClick(gamebobjects,objects[15],scoringobject)
        
        #Game Board Box 4
        objects[16].grid(row=11,column=0) 
        objects[16]['command'] = lambda:self.ButtonClick(gamebobjects,objects[16],scoringobject)
        
        #Game Board Box 5
        objects[17].grid(row=11,column=1) 
        objects[17]['command'] = lambda:self.ButtonClick(gamebobjects,objects[17],scoringobject)
        
        #Game Board Box 6
        objects[18].grid(row=11,column=2) 
        objects[18]['command'] = lambda:self.ButtonClick(gamebobjects,objects[18],scoringobject)
        
        #Game Board Box 7
        objects[19].grid(row=12,column=0) 
        objects[19]['command'] = lambda:self.ButtonClick(gamebobjects,objects[19],scoringobject)
        
        #Game Board Box 8
        objects[20].grid(row=12,column=1) 
        objects[20]['command'] = lambda:self.ButtonClick(gamebobjects,objects[20],scoringobject)
        
        #Game Board Box 9
        objects[21].grid(row=12,column=2)
        objects[21]['command'] = lambda:self.ButtonClick(gamebobjects,objects[21],scoringobject)
    
    def NewGame(self,arg): 
        global roundturn
        self.roundturn=0
        #clearing Grids
        grid=arg[13:]#grid columns and rows......
        for i in range(len(grid)):
            grid[i]['text']=' '
            grid[i]['state']='disabled'
        
        #clearing player names
        arg[4]['state']='normal'
        arg[4].delete(0,'end')
        arg[6]['state']='normal'
        arg[6].delete(0,'end')
        
        #clearing scoring objiects
        arg[8]['text']='Player 1 Score'
        arg[10]['text']='Player 2 Score'
        arg[9]['state']='normal'
        arg[9].delete(0)
        arg[9].insert(0,'0')
        arg[9]['state']='readonly'
        arg[11]['state']='normal'
        arg[11].delete(0)
        arg[11].insert(0,'0')
        arg[11]['state']='readonly'
        
        #disable nextround button
        arg[1]['state']='disabled'
                
    def StartGame(self,arg):
        #going to check if player names are given
        player1=str(arg[4].get())
        player2=str(arg[6].get())
        if player1 and player2:
            #setting scoring labels with player names
            arg[8]['text']=player1+''''s'''+' Score'
            arg[10]['text']=player2+''''s'''+' Score'
            arg[4]['state']='readonly'
            arg[6]['state']='readonly'
            grid=arg[13:]#grid columns and rows......
            for i in range(len(grid)):
                grid[i]['state']='normal'
            tmb.showinfo(title='Start Game',message='Game On')
        else:
            tmb.showerror(title='Error',message='Players Name Not Given')
    
    def NextRound(self,arg):
        global roundturn
        self.roundturn=0
        grid=arg[13:]#grid columns and rows......
        for i in range(len(grid)):
            grid[i]['text']=' '
        #who will start.. its one by one
        global playerturn
        global clickedButton
        if self.playerturn:
            self.clickedButton=False
            self.playerturn=False
            tmb.showinfo('Who will start in this Round',str(arg[6].get())+' (O) Will start')
        else:
            self.clickedButton=True
            self.playerturn=True
            tmb.showinfo('Who will start in this Round',str(arg[4].get())+' (X) Will Start')
            
        #disabling next roun
        arg[1]['state']='disabled'
    def ExitGame(self,arg):
        root.destroy()    
    
    def ButtonClick(self,arg,arg1,arg3):
         
         winnincheck=-1
         global clickedButton
         global roundturn
         self.roundturn=self.roundturn+1
         if arg1['text'] == ' ' and self.clickedButton == True:
               #arg == 'X'
               arg1['text'] = 'X'
               self.clickedButton = False       
         elif arg1['text'] == ' ' and self.clickedButton == False:
              #arg == 'O'
              arg1['text'] = 'O'
              self.clickedButton = True
         #checking player 1 (X) won the game or not   
         if (arg[0]['text'] == 'X' and arg[1]['text'] == 'X'   and arg[2]['text'] == 'X' 
           or  arg[3]['text'] == 'X' and arg[4]['text'] == 'X' and arg[5]['text'] == 'X'
           or  arg[6]['text'] == 'X' and arg[7]['text'] == 'X' and arg[8]['text'] == 'X'
           or  arg[0]['text'] == 'X' and arg[3]['text'] == 'X' and arg[6]['text'] == 'X'
           or  arg[1]['text'] == 'X' and arg[4]['text'] == 'X' and arg[7]['text'] == 'X'
           or  arg[2]['text'] == 'X' and arg[5]['text'] == 'X' and arg[8]['text'] == 'X'
           or  arg[0]['text'] == 'X' and arg[4]['text'] == 'X' and arg[8]['text'] == 'X'
           or  arg[2]['text'] == 'X' and arg[4]['text'] == 'X' and arg[6]['text'] == 'X'):   
             #updating player 1 score
             currscore=int(arg3[1].get())
             currscore=currscore+1
             arg3[1]['state']='normal'
             arg3[1].delete(0)
             arg3[1].insert(0,str(currscore))
             arg3[1]['state']='readonly'
             #winning message
             playername=str(arg3[0].get())
             tmb.showinfo('Winning Message', playername+' (X) Won The Game Round')
             #enabling next round button
             arg3[4]['state']='normal'
             winnincheck=1
         #checking player 2 (O) won the game or not     
         elif (arg[0]['text'] == 'O' and arg[1]['text'] == 'O'   and arg[2]['text'] == 'O' 
           or  arg[3]['text'] == 'O' and arg[4]['text'] == 'O' and arg[5]['text'] == 'O'
           or  arg[6]['text'] == 'O' and arg[7]['text'] == 'O' and arg[8]['text'] == 'O'
           or  arg[0]['text'] == 'O' and arg[3]['text'] == 'O' and arg[6]['text'] == 'O'
           or  arg[1]['text'] == 'O' and arg[4]['text'] == 'O' and arg[7]['text'] == 'O'
           or  arg[2]['text'] == 'O' and arg[5]['text'] == 'O' and arg[8]['text'] == 'O'
           or  arg[0]['text'] == 'O' and arg[4]['text'] == 'O' and arg[8]['text'] == 'O'
           or  arg[2]['text'] == 'O' and arg[4]['text'] == 'O' and arg[6]['text'] == 'O'):   
             #updating player 1 score
             currscore=int(arg3[3].get())
             currscore=currscore+1
             arg3[3]['state']='normal'
             arg3[3].delete(0)
             arg3[3].insert(0,str(currscore))
             arg3[3]['state']='readonly'
             #winning message
             playername=str(arg3[2].get())
             tmb.showinfo('Winning Message',playername+' (O) Won The Game Round')   
             #enabling next round button
             arg3[4]['state']='normal'
             winnincheck=2
         if(self.roundturn==9 and winnincheck==-1):
             tmb.showinfo('Draw Message','its a draw')
             arg3[4]['state']='normal'
              

app = tictac()
app.master.title('Tic Tac Toe')
root.mainloop()