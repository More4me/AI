'''
Created on 11/5/2016

@author: Menna Mamdouh
'''
from __future__ import print_function
#from tkinter.tix import COLUMN
from copy import deepcopy
#Deadline 15/5/2016
COLUMN=9
ROWS=9
arr=[[2,3,5,0,0,0,0,0,4],
     [0,0,0,6,9,0,2,0,5],
     [6,8,9,0,4,5,1,3,7],
     [0,1,0,0,0,4,7,9,0],
     [0,0,0,8,1,2,3,0,0],
     [0,6,8,7,0,0,0,0,2],
     [0,2,1,5,0,0,0,4,9],
     [9,0,6,4,2,1,0,0,0],
     [4,0,0,9,0,0,0,2,1]]
listss=[1,2,3,4,5,6,7,8,9]
class Game:
    
    
    def state(self,arr): 
        for i in range(COLUMN):
            for j in range(ROWS):
                if arr[i][j]==0:
                    print('|',' ',end="")
                else:
                    print('|',arr[i][j],end="")
            print('|\n____________________________',end="\n")
    
    def checkValue(self,arr,listss,row,col):
        board=self.verticaleliminate(arr,listss,row)
        board=self.horizontaleliminate(arr,board,col)
        board=self.tableeliminate(arr,board,row,col)
        return board
        
    def verticaleliminate(self,arr,listssss,row):
        board=deepcopy(listss)
        for j in range(COLUMN):
            if arr[row][j]>0:
               # print(i,"+",board)
                if board.__contains__(arr[row][j]):
                #    print(board.index(arr[j][col]))
                    board.pop(board.index(arr[row][j]))
        return board
    #Need to check the 9 element#
    def horizontaleliminate(self,arr,listss,col):
        board=deepcopy(listss)
        for j in range(ROWS):
            if arr[j][col]>0:
               # print(i,"+",board)
                if board.__contains__(arr[j][col]):
                #    print(board.index(arr[j][col]))
                    board.pop(board.index(arr[j][col]))
        return board
    
    def tableeliminate(self,arr,listss,row,col):
        board=deepcopy(listss)
        begi=int(row/3)
        begi=begi*3
        begj=int(col/3)
        begj=begj*3
        endi=begi+3
        endj=begj+3
        while begi < endi:
            j=begj
            while j < endj:
                if  board.__contains__(arr[begi][j]):
                    board.pop(board.index(arr[begi][j]))
                j=j+1
            begi=begi+1
                
        return board
    def finished(self,listss):
        for i in range(ROWS):
            for j in range(COLUMN):
                #print (listss[i][j])
                if listss[i][j]==0 :
                    return [i,j]
        return [-1,-1]
    
    def ValidAssignment(self,var,board,value):
        avlist=self.checkValue(board,listss,var[0],var[1])
        if value in avlist:
            return True
        return False
    
    def CSP(self,b):
        if self.finished(b)==[-1,-1]:
            return b
        var=self.finished(b)
        result=deepcopy(b)
        for value in self.checkValue(arr,listss,var[0], var[1]):
            print ("index of :",var,"Domain is:",self.checkValue(arr,listss, var[0], var[1]))
            result[var[0]][var[1]]=value 
            self.state(result)
            input("Enter test")
            print ("=============================================")
            if  (self.finished(b)==[-1,-1]):
                return
            elif(self.ValidAssignment(var,b,value)):
                result=self.CSP(result)
        if(self.finished(b)!=[-1,-1]):
            result[var[0]][var[1]]=0
        return result
            
        '''
        z=0
        k=self.checkValue(list,i,j)
        while (z<len(k)):
            value=k[z]
            board=deepcopy(b)
            board[i][j]=value
            state(board)
            if j<ROWS:
                j=j+1
            elif i<COLUMN:
                j=0
                i=i+1
            else:
                return
            z=z+1
            CSP(i,j,value)
            return
        '''      
                      
if __name__ == '__main__':
    print(arr)
    x= Game()
    print(arr[0][ROWS-1])
    x.state(arr)
   # b=x.verticaleliminate(listss,0)
    #print(b)
   # b=x.horizontaleliminate(b, 0)
    #print(b)
    #b=x.tableeliminate(b,0,0)
    #print(b)
    x.CSP(arr)