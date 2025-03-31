from tkinter import messagebox
from tkinter import *
from cvzone.HandTrackingModule import HandDetector
from math import sqrt,hypot
from os import listdir
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from gtts import gTTS
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import cvzone, numpy as np, time, csv, random, pygame.mixer, datetime, cv2 as cv,playsound

pathCSV=""
timern="TIME"
name_to_greet=""

def askname():
    global name_to_greet
    root=Tk()
    root.title("What's Your Name ?")
    root.geometry("300x100")
    root.resizable(False,False)
    root.config(bg="lightblue")
    def ok():
        global name_to_greet
        if entrybtn.get() != "" :
            name_to_greet=entrybtn.get()
        else:
            messagebox.showwarning("Name?", "Kindly Enter Your Name, Before You Proceed.")
            askname()
        root.destroy()
    def ok2(event):
        global name_to_greet
        if entrybtn.get() != "" :
            name_to_greet=entrybtn.get()
        else:
            messagebox.showwarning("Name?", "Kindly Enter Your Name, Before You Proceed.")
            askname()
        root.destroy()
    entrybtn=Entry(root,font=("Comic Sans MS",15),borderwidth=10,relief=RIDGE,bg="red",fg="yellow")
    okbtn=Button(root,text="Ok",font=("Comic Sans MS", 15),command=ok,width=20,borderwidth=7,relief=RIDGE,bg="yellow",fg="red",activebackground="yellow",activeforeground="red")

    entrybtn.pack(padx=2,pady=2)
    okbtn.pack(padx=2,pady=2)

    root.bind("<Return>",ok2)
    root.mainloop()
def greetIt():
    global name_to_greet
    a=str(datetime.datetime.now())[11:13]
    if int(a) >= 4 and int(a) < 12:
        morning_message=gTTS(f"Welcome to Witness Vision Wonders, {name_to_greet}",lang='en',slow=False)
        morning_message.save(f"__resources/Resources/NameGreetings/{name_to_greet}.mp3")
        pygame.mixer.init()
        pygame.mixer.music.load(f"__resources/Resources/NameGreetings/{name_to_greet}.mp3")
        pygame.mixer.music.play()
    elif int(a) >= 12 and int(a) < 18:
        afternoon_message=gTTS(f"Welcome to Witness Vision Wonders, {name_to_greet}",lang='en',slow=False)
        afternoon_message.save(f"__resources/Resources/NameGreetings/{name_to_greet}.mp3")
        pygame.mixer.init()
        pygame.mixer.music.load(f"__resources/Resources/NameGreetings/{name_to_greet}.mp3")
        pygame.mixer.music.play()
    else:
        pygame.mixer.init()
        evening_message=gTTS(f"Welcome to Witness Vision Wonders, {name_to_greet}",lang='en',slow=False)
        evening_message.save(f"__resources/Resources/NameGreetings/{name_to_greet}.mp3")
        pygame.mixer.music.load(f"__resources/Resources/NameGreetings/{name_to_greet}.mp3")
        pygame.mixer.music.play()
def QuizGui():
    try:
        global pathCSV

        def geo():
            global pathCSV
            pathCSV="__resources/Resources/QuizR/GeographyQuiz.csv"
            root.destroy()
        def math():
            global pathCSV
            pathCSV="__resources/Resources/QuizR/MathQuiz.csv"
            root.destroy()
        def his():
            global pathCSV
            pathCSV="__resources/Resources/QuizR/HistoryQuiz.csv"
            root.destroy()
        def gk():
            global pathCSV
            pathCSV="__resources\\Resources\\QuizR\\GkQuiz.csv"
            root.destroy()
        root=Tk()
        root.title("Quiz Selection")
        root.config(bg="lightgreen")

        geobtn=Button(root,text="Geography Quiz",relief=RIDGE,borderwidth=9,font=("comic sans ms",25),bg="pink",activebackground="lightgreen",fg="red",activeforeground="red",command=geo,width=20)
        gkbtn=Button(root,text="GK Quiz",relief=RIDGE,borderwidth=9,font=("comic sans ms",25),bg="pink",activebackground="lightgreen",fg="red",activeforeground="red",command=gk,width=20)
        hisbtn=Button(root,text="History Quiz",relief=RIDGE,borderwidth=9,font=("comic sans ms",25),bg="pink",activebackground="lightgreen",fg="red",activeforeground="red",command=his,width=20)
        mathbtn=Button(root,text="Math Quiz",relief=RIDGE,borderwidth=9,font=("comic sans ms",25),bg="pink",activebackground="lightgreen",fg="red",activeforeground="red",command=math,width=20)

        gkbtn.pack()
        geobtn.pack()
        hisbtn.pack()
        mathbtn.pack()

        root.mainloop()
        return pathCSV
    except: 
        pass
def digi():
    global timern
    timern=str(datetime.datetime.now().strftime("%H:%M:%S"))
    timeee['text']=timern
    timeee.after(1000,digi)
def PingPong():
    cap = cv.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)

    # Importing all images
    imgBackground = cv.imread("__resources/Resources/PingPongR/Background.png")
    imgGameOver = cv.imread("__resources/Resources/PingPongR/gameOver.png")
    imgBall = cv.imread("__resources/Resources/PingPongR/Ball.png", cv.IMREAD_UNCHANGED)
    imgBat1 = cv.imread("__resources/Resources/PingPongR/bat1.png", cv.IMREAD_UNCHANGED)
    imgBat2 = cv.imread("__resources/Resources/PingPongR/bat2.png", cv.IMREAD_UNCHANGED)

    # Hand Detector
    detector = HandDetector(detectionCon=0.8, maxHands=3)

    # Variables
    ballPos = [100, 100]
    speedX = 25
    speedY = 25
    gameOver = False
    score = [0, 0]

    while True:
        _, img = cap.read()
        img = cv.flip(img, 1)
        imgRaw = img.copy()
        l=score[0]+score[1]
        
        hands, img = detector.findHands(img, flipType=False)

        img = cv.addWeighted(img, 0.2, imgBackground, 0.8, 0)

        if hands:
            for hand in hands:
                x, y, w, h = hand['bbox']
                h1, w1, _ = imgBat1.shape
                y1 = y - h1 // 2
                y1 = np.clip(y1, 20, 415)

                if hand['type'] == "Left":
                    img = cvzone.overlayPNG(img, imgBat1, (59, y1))
                    if 59 < ballPos[0] < 59 + w1 and y1 < ballPos[1] < y1 + h1:
                        speedX = -speedX
                        ballPos[0] += 30
                        score[0] += 1

                if hand['type'] == "Right":
                    img = cvzone.overlayPNG(img, imgBat2, (1195, y1))
                    if 1195 - 50 < ballPos[0] < 1195 and y1 < ballPos[1] < y1 + h1:
                        speedX = -speedX
                        ballPos[0] -= 30
                        score[1] += 1

        if ballPos[0] < 40 or ballPos[0] > 1200:
            gameOver = True

        if gameOver:
            img = imgGameOver
            cv.putText(img, str(score[1] + score[0]).zfill(2), (585, 360), cv.FONT_HERSHEY_COMPLEX,
                        2.5, (200, 0, 200), 5)

        else:
        
            # Move the Ball
            if ballPos[1] >= 500 or ballPos[1] <= 10:
                speedY = -speedY

            ballPos[0] += speedX
            ballPos[1] += speedY

            # Draw the ball
            img = cvzone.overlayPNG(img, imgBall, ballPos)

            cv.putText(img, str(score[0]), (300, 650), cv.FONT_HERSHEY_COMPLEX, 3, (255, 255, 255), 5)
            cv.putText(img, str(score[1]), (900, 650), cv.FONT_HERSHEY_COMPLEX, 3, (255, 255, 255), 5)

        img[580:700, 20:233] = cv.resize(imgRaw, (213, 120))

        cv.imshow("Image", img)
        key = cv.waitKey(1)
        if key == ord('r'):
            ballPos = [100, 100]
            speedX = 15
            speedY = 15
            gameOver = False
            score = [0, 0]
            imgGameOver = cv.imread("__resources/Resources/PingPongR/gameOver.png")
        if cv.waitKey(20) == ord('q'):
            cv.destroyAllWindows()
            break
def RPS():
    cap = cv.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    detector = HandDetector(detectionCon=0.8)

    timer = 0
    stateResult = False
    startGame = False
    scores = [0, 0]

    x = [300, 245, 200, 170, 145, 130, 112, 103, 93, 87, 80, 75, 70, 67, 62, 59, 57]
    y = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
    coff = np.polyfit(x, y, 2)  # y = Ax^2 + Bx + C

    distanceCM=0

    while True:
        imgBG = cv.imread("__resources/Resources/RPSR/BG.png")
        success, img = cap.read()

        imgScaled = cv.resize(img, (0, 0), None, 0.875, 0.875)
        imgScaled = imgScaled[:, 80:480]

        # Find Hands
        hands, img = detector.findHands(imgScaled)  # with draw

        if startGame:

            if stateResult is False:
                timer = time.time() - initialTime
                cv.putText(imgBG, str(int(timer)), (605, 435), cv.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 4)

                if timer > 1:
                    stateResult = True
                    timer = 0

                    if hands:
                        playerMove = None
                        hand = hands[0]
                        fingers = detector.fingersUp(hand)
                        if fingers == [0, 0, 0, 0, 0]:
                            playerMove = 1
                        if fingers == [1, 1, 1, 1, 1]:
                            playerMove = 2
                        if fingers == [0, 1, 1, 0, 0]:
                            playerMove = 3

                        randomNumber = random.randint(1, 3)
                        imgAI = cv.imread(f'__resources/Resources/RPSR/{randomNumber}.png', cv.IMREAD_UNCHANGED)
                        imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))

                        # Player Wins
                        if (playerMove == 1 and randomNumber == 3) or \
                                (playerMove == 2 and randomNumber == 1) or \
                                (playerMove == 3 and randomNumber == 2):
                            scores[1] += 1

                        # AI Wins
                        if (playerMove == 3 and randomNumber == 1) or \
                                (playerMove == 1 and randomNumber == 2) or \
                                (playerMove == 2 and randomNumber == 3):
                            scores[0] += 1

        imgBG[234:654, 795:1195] = imgScaled

        if stateResult:
            imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))

        cv.putText(imgBG, str(scores[0]), (410, 215), cv.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
        cv.putText(imgBG, str(scores[1]), (1112, 215), cv.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)

        cv.imshow("H-RPS-CV", imgBG)
        if hands:
            lmList = hands[0]['lmList']
            x, y, w, h = hands[0]['bbox']
            x1, y1, z1 = lmList[5]
            x2, y2, z2 = lmList[17]

            distance = int(sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2))
            A, B, C = coff
            distanceCM = A * distance ** 2 + B * distance + C
            
            key = cv.waitKey(1)
            if int(distanceCM) < 60 :
                startGame = True
                initialTime = time.time()
                stateResult = False
                continue
        key3 = cv.waitKey(20)
        if key3 == ord('q'):
            cv.destroyAllWindows()
            break   
'''
def VGC():
    pygame.mixer.init()
    pygame.mixer.music.load("__resources/Resources/VGCR/VGC-SoundSample.mp3")
    pygame.mixer.music.play()
        
    devices=AudioUtilities.GetSpeakers()
    interface=devices.Activate(IAudioEndpointVolume._iid_,CLSCTX_ALL,None)
    volume=cast(interface,POINTER(IAudioEndpointVolume))
    cap=cv.VideoCapture(0)
    detector=HandDetector(detectionCon=0.8,maxHands=1)
    # While Loop Starts
    while True:
        success,img=cap.read()
        hands,img=detector.findHands(img)
        # detector.findFps(img,position=(20,50))
        if hands:
            lmList=hands[0]['lmList']
            if len(lmList) != 0:
                x1,y1=lmList[4][1],lmList[4][2]
                x2,y2=lmList[8][1],lmList[8][2]
                cx,cy=(x1+x2)//2,(y1+y2)//2
                length,img,info=detector.findDistance(lmList[8],lmList[12])
                
                volRange=volume.GetVolumeRange()
                minVol=volRange[0]
                maxVol=volRange[1]

                length=round(hypot(x2-x1,y2-y1),2)
                
                per=np.interp(length,[30,225],[minVol,maxVol])
                volBarPer=np.interp(length,[30,225],[410,160])

                volume.SetMasterVolumeLevel(float(per),None)

                cv.rectangle(img,(20,160),(80,410),(0,255,0),4)
                cv.rectangle(img,(20,int(volBarPer)),(80,410),(0,255,0),cv.FILLED)
                
                cv.line(img,(lmList[8][0],lmList[8][1]),(lmList[4][0],lmList[4][1]),(255,255,0),5)
                if length<50:
                    cv.circle(img,(lmList[8][0],lmList[8][1]),10,(0,255,0),cv.FILLED)
                    cv.circle(img,(lmList[4][0],lmList[4][1]),10,(0,255,0),cv.FILLED)
                if length>225:
                    cv.circle(img,(lmList[8][0],lmList[8][1]),10,(255,0,0),cv.FILLED)
                    cv.circle(img,(lmList[4][0],lmList[4][1]),10,(255,0,0),cv.FILLED)
            
        cv.imshow("Advanced Deep Computer Vision Volume Gesture Control",img)
        if cv.waitKey(20) & 0xFF == ord('q'):
            pygame.mixer.music.pause()
            cv.destroyAllWindows()
            break
'''
def VP():
    eraser=50
    brush=13
    xp,yp=0,0
    folderPath="__resources/Resources/VirtualPainterR"
    overlaylist=[]
    for file in listdir(folderPath):
        overlaylist.append(cv.imread(f"{folderPath}/{file}"))
    imgCanvas=np.zeros((480,640,3),np.uint8)
    header=overlaylist[3]
    detector=HandDetector(detectionCon=0.85)
    cap=cv.VideoCapture(0)
    color=(255,0,255)
    # While Loop Starts
    while True:
        success,img=cap.read()
        img=cv.flip(img,1)
        h,w,c=header.shape
        img[0:h,0:w]=header
        hands,img=detector.findHands(img)
        if hands:
            lmList=hands[0]["lmList"]
        
            if len(lmList) != 0:
                x1,y1 = lmList[8][0],lmList[8][1]
                x2,y2 = lmList[12][0],lmList[12][1]
                fingers=detector.fingersUp(hands[0])
                
                if fingers[1] and fingers[2]:
                    xp,yp=0,0
                    cv.rectangle(img,(x1,y1-25),(x2,y2+25),color,cv.FILLED)
                    if y1<125:
                        if 125 < x1 < 225:
                            header=overlaylist[3]
                            color=(255,0,255)
                        elif 225 < x1 < 375:
                            header=overlaylist[0]
                            color=(255,255,0)
                        elif 400 < x1 < 475:
                            header=overlaylist[2]
                            color=(0,255,0)
                        elif 525 < x1 < 600:
                            header=overlaylist[1]
                            color=(0,0,0)
                        
                if fingers[1] and fingers[2] == False:
                    cv.circle(img,(x1,y1),13,color,cv.FILLED)     
                    if xp == 0 and yp == 0: 
                        xp,yp=x1,y1
                    
                    if color==(0,0,0):
                        cv.line(img,(xp,yp),(x1,y1),color,eraser)
                        cv.line(imgCanvas,(xp,yp),(x1,y1),color,eraser)
                    else:
                        cv.line(img,(xp,yp),(x1,y1),color,brush)
                        cv.line(imgCanvas,(xp,yp),(x1,y1),color,brush)
                    xp,yp=x1,y1
                    
        imgGray=cv.cvtColor(imgCanvas,cv.COLOR_BGR2GRAY)
        _, imgInv=cv.threshold(imgGray,50,255,cv.THRESH_BINARY_INV)
        imgInv=cv.cvtColor(imgInv,cv.COLOR_GRAY2BGR)
        img=cv.bitwise_and(img,imgInv)
        img=cv.bitwise_or(img,imgCanvas)    

        # h,w,c=header.shape
        # img[0:h,0:w]=header
        img=cv.addWeighted(img,1,imgCanvas,1,0)
        
        cv.imshow("Advanced Deep Computer Vision AI Virtual Painter",img)
        cv.imshow("Canvas",imgCanvas)
        if cv.waitKey(20) & 0xFF == ord('q'):
            break
    cv.destroyAllWindows()
def Quiz():
  try:
    pathCSV=QuizGui()

    cap=cv.VideoCapture(0)
    cap.set(3,1280)
    cap.set(4,720)
    detector=HandDetector(detectionCon=0.8,maxHands=1)

    class mcq():
        def __init__(self,data):
            self.question=data[0]
            self.choice1=data[1]
            self.choice2=data[2]
            self.choice3=data[3]
            self.choice4=data[4]
            self.answer=int(data[5])

            self.userAns=None
            
        def update(self,cursor,bboxs):
            for x,bbox in enumerate(bboxs):
                x1,y1,x2,y2=bbox
                if x1<cursor[0]<x2 and y1<cursor[1]<y2:
                    self.userAns=x+1
                    for mcq in mcqlist:
                        if mcq.answer==mcq.userAns:
                            cv.rectangle(img,(x1,y1),(x2,y2),(0,255,0),cv.FILLED)

    with open(pathCSV,newline="\n") as f:
        reader = csv.reader(f)
        dataAll =list(reader)[1:]

    mcqlist=[]
    for q in dataAll:
        mcqlist.append(mcq(q))

    qNo=0
    qTotal=len(dataAll)

    while True:
        success,img=cap.read()
        hands, img=detector.findHands(img)
        if qNo<qTotal:
            mcq=mcqlist[qNo]

            img, bbox=cvzone.putTextRect(img,mcq.question,[100,100],2,2,offset=50,border=5)
            img, bbox1=cvzone.putTextRect(img,mcq.choice1,[100,255],2,2,offset=50,border=5)
            img, bbox2=cvzone.putTextRect(img,mcq.choice2,[600,255],2,2,offset=50,border=5)
            img, bbox3=cvzone.putTextRect(img,mcq.choice3,[100,375],2,2,offset=50,border=5)
            img, bbox4=cvzone.putTextRect(img,mcq.choice4,[600,375],2,2,offset=50,border=5)
        
            if hands:
                lmList=hands[0]['lmList']
                cursor=lmList[8]
                length,info,x=detector.findDistance(cursor,lmList[12])    
                if length<50:
                    mcq.update(cursor,[bbox1,bbox2,bbox3,bbox4])
                    if mcq.userAns is not None:
                        time.sleep(0.5)
                        qNo+=1
        else:
            score=0
            for mcq in mcqlist:
                if mcq.answer==mcq.userAns:
                    score+=1
            score=round((score/qTotal)*100,2)
            img,_=cvzone.putTextRect(img,f'Quiz Completed!',[250,300],2,2,offset=16)
            img,_=cvzone.putTextRect(img,f'Your score is {score}%',[200,350],2,2,offset=16)

        barValue=150+(950//qTotal)*qNo
        cv.rectangle(img,(150,600-100),(barValue,650-100),(0,255,0),cv.FILLED)
        cv.rectangle(img,(150,600-100),(1100,650-100),(0,255,0),5)
        img,_=cvzone.putTextRect(img,f'{round((qNo/qTotal)*100)}%',[1130,635-100],2,2,offset=16)
        
        # img=cv.flip(img,1)
        cv.imshow("Air Quiz",img)

        if cv.waitKey(20)==ord('q'):
            cv.destroyAllWindows()  
            break
  except:
      pass
def PressGame():
    cap = cv.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)

    detector = HandDetector(detectionCon=0.8, maxHands=1)
    
    x = [300, 245, 200, 170, 145, 130, 112, 103, 93, 87, 80, 75, 70, 67, 62, 59, 57]
    y = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
    coff = np.polyfit(x, y, 2)  # y = Ax^2 + Bx + C

    cx, cy = 250, 250
    color = (255, 0, 255)
    counter = 0
    score = 0
    timeStart = time.time()
    totalTime = 20

    while True:
        success, img = cap.read()
        img = cv.flip(img, 1)

        if time.time()-timeStart < totalTime:

            hands,img = detector.findHands(img, draw=False)

            if hands:
                lmList = hands[0]['lmList']
                x, y, w, h = hands[0]['bbox']
                x1, y1, z1 = lmList[5]
                x2, y2, z2 = lmList[17]

                distance = int(sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2))
                A, B, C = coff
                distanceCM = A * distance ** 2 + B * distance + C

                if 30 < distanceCM < 40:
                    if x < cx < x + w and y < cy < y + h:
                        counter = 1
                cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 3)
                cvzone.putTextRect(img, f'{int(distanceCM)} cm', (x + 5, y - 10))

            if counter:
                playsound.playsound("__resources/Resources/pop.mp3")
                counter += 1
                color = (0, 255, 0)
                if counter == 3:
                    cx = random.randint(100, 1100)
                    cy = random.randint(100, 600)
                    color = (255, 0, 255)
                    score +=1
                    counter = 0

            # Draw Button
            cv.circle(img, (cx, cy), 30, color, cv.FILLED)
            cv.circle(img, (cx, cy), 10, (255, 255, 255), cv.FILLED)
            cv.circle(img, (cx, cy), 20, (255, 255, 255), 2)
            cv.circle(img, (cx, cy), 30, (50, 50, 50), 2)

            # Game HUD
            cvzone.putTextRect(img, f'Time: {int(totalTime-(time.time()-timeStart))}',
                            (1000, 75), scale=3, offset=20)
            cvzone.putTextRect(img, f'Score: {str(score).zfill(2)}', (60, 75), scale=3, offset=20)
        else:
            cvzone.putTextRect(img, 'Game Over', (400, 400), scale=5, offset=30, thickness=7)
            cvzone.putTextRect(img, f'Your Score: {score}', (450, 500), scale=3, offset=20)
            cvzone.putTextRect(img, 'Press R to restart', (460, 575), scale=2, offset=10)


        cv.imshow("Image", img)
        key = cv.waitKey(1)

        if key == ord('r'):
            timeStart = time.time()
            score = 0
        if key == ord('q'):
            cv.destroyAllWindows()
            break
def fingerCounter():
    # OpenCV Function
    
    # Creating A Function Which Counts The Number Of Fingers Via A Deep Computer Vision Model and Displaying An Image Corresponding To The Fingers
    cap=cv.VideoCapture(0)
    detector=HandDetector(maxHands=1)
    folderPath="__resources/Resources/fingerImages"
    mylist=listdir(folderPath)
    overlaylist=[]
    for file in mylist:
        image=cv.imread(f"{folderPath}/{file}")
        overlaylist.append(image)
    text=None
    # While Loop Starts
    while True:
        success,img=cap.read()
        image=overlaylist[0]
        img=cv.flip(img,1)
        lmlist,img=detector.findHands(img)
        cv.rectangle(img,(5,250),(205,450),(0,255,0),cv.FILLED)
        
        if len(lmlist) != 0:
            fingers=detector.fingersUp(lmlist[0])
            totalFingers=fingers.count(1)
            if totalFingers == 0:
                image=overlaylist[5]
                text=0
            if totalFingers == 1:
                image=overlaylist[0]
                text=1
            if totalFingers == 2:
                image=overlaylist[1]
                text=2
            if totalFingers == 3:
                image=overlaylist[2]
                text=3
            if totalFingers == 4:
                image=overlaylist[3]
                text=4
            if totalFingers == 5:
                image=overlaylist[4]
                text=5
            cv.putText(img,str(text),(40,400),cv.FONT_HERSHEY_COMPLEX,5,(0,0,255),15)
            img[0:200,0:200]=image
            
        cv.imshow("Deep Computer Vision Finger Counter",img)
        if cv.waitKey(20) & 0xFF == ord('q'):
            break
    cv.destroyAllWindows()
askname()
greetIt()

mainroot=Tk()
mainroot.title("WvW-Witness Vision Wonders")    
mainroot.config(bg="lightblue")
mainroot.geometry("1200x600")

Label(mainroot,text=" WvW-Witness Vision Wonders",font=("comic sans ms",32,"bold"),fg="blue",bg="lightblue").grid(row=0,column=0)
timeee=Label(mainroot,text=f"{timern}",font=("comic sans ms",40,"bold"),fg="blue",bg="lightblue")

pingpongbtn=Button(mainroot,text="Ping-Pong",relief=RIDGE,borderwidth=9,font=("comic sans ms",25),bg="pink",activebackground="lightgreen",fg="red",activeforeground="red",command=PingPong,width=20)
RPSbtn=Button(mainroot,text="RPS",relief=RIDGE,borderwidth=9,font=("comic sans ms",25),bg="pink",activebackground="lightgreen",fg="red",activeforeground="red",command=RPS,width=20)
VPbtn=Button(mainroot,text="Virtual Painter",relief=RIDGE,borderwidth=9,font=("comic sans ms",25),bg="pink",activebackground="lightgreen",fg="red",activeforeground="red",command=VP,width=20)
FCbtn=Button(mainroot,text="Finger Counter",relief=RIDGE,borderwidth=9,font=("comic sans ms",25),bg="pink",activebackground="lightgreen",fg="red",activeforeground="red",command=fingerCounter,width=20)
PressGamebtn=Button(mainroot,text="Press Game",relief=RIDGE,borderwidth=9,font=("comic sans ms",25),bg="pink",activebackground="lightgreen",fg="red",activeforeground="red",command=PressGame,width=20)
Quizbtn=Button(mainroot,text="QUIZ",relief=RIDGE,borderwidth=9,font=("comic sans ms",25),bg="pink",activebackground="lightgreen",fg="red",activeforeground="red",command=Quiz,width=20)

timeee.grid(row=0,column=1)

VPbtn.grid(row=2,column=1)
pingpongbtn.grid(row=3,column=0)
RPSbtn.grid(row=3,column=1)
PressGamebtn.grid(row=2,column=0)
Quizbtn.grid(row=4,column=0)
FCbtn.grid(row=4,column=1)

mainroot.after(1000,digi)
mainroot.mainloop()