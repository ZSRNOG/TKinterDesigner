#coding=utf-8

#import libs 
import TabPage2_cmd
import Fun
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
ElementBGArray={}  
ElementBGArray_Resize={} 
ElementBGArray_IM={} 

#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  TabPage2:
    def __init__(self,root,isTKroot = True):
        className = self.__class__.__name__
        Fun.G_UIElementArray[className]={}
        Fun.G_ElementBindingDataArray[className]={}
        global ElementBGArray
        global ElementBGArray_Resize
        global ElementBGArray_IM
        Fun.AddElement(className,'UIClass',self)
        self.root = root
        if isTKroot == True:
            root.title("Form1")
            root.geometry("565x295")
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 565,height = 295)
        Form_1.configure(bg = "#efefef")
        Fun.AddElement(className,'root',root)
        Fun.AddElement(className,'Form_1',Form_1)
        #Create the elements of root 
        Canvas_2= tkinter.Canvas(root)
        Canvas_2.place(x = 10,y = 12,width = 548,height = 272)
        Canvas_2.configure(bg = "#ff0080")
        Fun.AddElement(className,'Canvas_2',Canvas_2)
        #Inital all element's Data 
        Fun.InitElementData(className)
        #Add Some Logic Code Here: (Keep This Line of comments)

#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = TabPage2(root)
    root.mainloop()
