import turtle
turtle.penup()
def MyWindoW(MyWindoWx, MyWindoWy, My="【游戏终端】"):
    turtle.Screen().cv._rootwindow.resizable(False, False)
    turtle.setup(int(MyWindoWx)*100, int(MyWindoWy)*100)
    turtle.title(str(My))
    
WindoW = [[] for MyWindoW in range(16)]
turtle.bgcolor("#161718")
def WrWindoW(MyWindoW, MyColor, WhereMy=0, My=100000, Color=("#161718")):
    global WindoW
    if WhereMy > 15:
        raise ValueError("Pyprinter <WhereMy> Cant Get this Component")
    try: WindoW[WhereMy][My] = [str(MyWindoW), MyColor, Color]
    except: WindoW[WhereMy].append([str(MyWindoW), MyColor, Color])

turtle.tracer(False)
turtle.hideturtle()
def MyWindoW_Writing(Beginning, WhereMy=0, WhichMy=0, Going=True):
    MyKind = ["华文彩云", "黑体"]
    if WhichMy > 1: 
        raise ValueError("Pyprinter <WhichMy> Cant Get this Component")
        
    if isinstance(Beginning, list) == False:
        raise ValueError("Pyprinter <Beginning> Must Be <List>") 
    if len(Beginning) != 2:
        raise ValueError("Pyprinter <Beginning> length Must Be <2>")
    if Going: MyWindoW_Update()

    if Beginning[0] < 0: 
        Beginning[0] = float(str(Beginning[0])[0:4])
    else: Beginning[0] = float(str(Beginning[0])[0:3])
    if Beginning[1] < 0: 
        Beginning[1] = float(str(Beginning[1])[0:4])
    else: Beginning[1] = float(str(Beginning[1])[0:3])

    if WhereMy > 15:
        raise ValueError("Pyprinter <WhereMy> Cant Get this Component")
    
    for My in range(len(WindoW[WhereMy])):
        turtle.pencolor(WindoW[WhereMy][My][1])
        Goprinting = 0
        for Writing in WindoW[WhereMy][My][0]:
            if Writing == "W":
                turtle.pencolor(WindoW[WhereMy][My][2])
            else:
                turtle.goto(-(Beginning[0]*100)+Goprinting, (Beginning[1]*100)-(My*21))
                turtle.write(Writing, font=(MyKind[WhichMy], 15, "bold"))
                turtle.pencolor(WindoW[WhereMy][My][1])
            
                if Writing not in "(<0123456789>)": Goprinting += 22
                elif Writing in "(<0123456789>)": Goprinting += 22/2

def MyWindoW_Update():
    turtle.clear()
    turtle.update()

MyWindoWEnd = turtle.mainloop
MyWindoWKey = {"GOING": ["Up", "Down", "Left", "Right"], "WINDOW": ["Return", "space"], 
               "NUMBER": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]}

def MyWindoW_EventKey(Mykey, Key, My=None):
    if Mykey not in ["GOING", "WINDOW", "NUMBER"]:
        raise ValueError("Pyprinter <Mykey> Cant Get <" + str(Mykey) + "> In <GOING WINDOW NUMBER>")

    if isinstance(Key, int) == False: raise ValueError("Pyprinter <Key> Must Be <int>")
    if Key >= len(MyWindoWKey[Mykey]): raise ValueError("Pyprinter <Key> not Have this <Key Number>")

    turtle.onkey(My, MyWindoWKey[Mykey][Key])
    turtle.listen()

def MyWindoW_InputIng(WindoW="你好  请问你要编辑哪些内容", MyWindoW="测试窗口"):
    if isinstance(WindoW, str) == False: raise ValueError("Pyprinter <WindoW> Must Be <str>")
    if isinstance(MyWindoW, str) == False: raise ValueError("Pyprinter <MyWindoW> Must Be <str>")
    return turtle.textinput(MyWindoW, WindoW)

def MyWindoW_EventDomy(Where, WhereKeyb, WhereKeyd, MyKey):
    if isinstance(Where, list) == False or isinstance(WhereKeyb, list) == False or isinstance(WhereKeyd, list) == False: 
        raise ValueError("Pyprinter <Where WhereKeyb WhereKeyd> Must Be <list>")      
    if len(Where) != 2 or len(WhereKeyb) != 2 or len(WhereKeyd) != 2: 
        raise ValueError("Pyprinter <Where WhereKeyb WhereKeyd> length Must Be <2>")

    if Where[0] < 0: Where[0] = float(str(Where[0])[0:4])
    else: Where[0] = float(str(Where[0])[0:3])
        
    if Where[1] < 0: Where[1] = float(str(Where[1])[0:4])
    else: Where[1] = float(str(Where[1])[0:3])
    
    def InputIng(WindoWx, WindoWy):
        if WindoWx > -(Where[0]*100)+(WhereKeyb[0]*11) and WindoWx < -(Where[0]*100)+(WhereKeyd[0]*11):
            if WindoWy < (Where[1]*100)-(WhereKeyb[1]*21)+21 and WindoWy > (Where[1]*100)-(WhereKeyd[1]*21)+21:
                MyKey()
    turtle.onscreenclick(InputIng, btn=1, add=True)