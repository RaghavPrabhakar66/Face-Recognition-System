import cv2
import os 
import face_recognition
import numpy as np
from datetime import datetime
import pickle
from facenet_pytorch import MTCNN
import pyrebase

import time
##

#firebase=pyrebase.initialize_app(config)
#db = firebase.database()

##
detector=MTCNN(select_largest=False,device='cuda',post_process=False,margin=20, keep_all=True,min_face_size=80)
##
stride=4
resize=1
skip=1
##
images = []
classNames = []

try:
    with open('face_names.pkl','rb') as f: classNames = pickle.load(f)
    with open('encodings.pkl','rb') as f: encodeListKnown = pickle.load(f)
except:
    print("Encoding Read failed")

try:
    with open('model.pkl','rb') as f: model = pickle.load(f)
except:
    print("Model Read failed")

def markfaces2(name):
    # print("YOOOOOO")
    hostel="M"
    now = datetime.now()
    dtString = now.strftime('%H-%M-%S')
    dtDate=str(datetime.now().date())
    inTime=dtString+"-"+dtDate

    data={"rollNumber":name,"time":dtString,"date":dtDate,"hostel":hostel,"isOut":True}
    db.child("users").push(data)

def markfaces(name):
    try:
        with open('markfaces.csv','r+') as f:
            myDataList = f.readlines()
            nameList = []
            time=[]
            for line in myDataList:
                entry = line.split(',')
                # print(entry)
                # nameList.insert(entry[0],index=1)
                nameList.append(entry[0])
                # time.append(entry[-1])
                # time.append(datetime.strptime(entry[1].split('\n')[0], '%Y-%m-%d %H:%M:%S'))
            # print(datetime.time()-time[nameList.index(name)])
            # time1=datetime.strptime(line1.split(',')[-1].split('\n')[0], '%Y-%m-%d %H:%M:%S')
            # time2=datetime.strptime(line2.split(',')[-1].split('\n')[0], '%Y-%m-%d %H:%M:%S')
            now=datetime.now().replace(microsecond=0)   
            # before=time[nameList.index[name]]
            # print(nameList.index(name))
            # if name not in nameList or (time[nameList.index[name]]-now > 2):
                # now = datetime.now()
            # print("here")
            dtstring = datetime.now().replace(microsecond=0)
            # print(dtstring)
            # dtstring = now.strftime('%H-%M-%S')
            f.writelines(f'\n{name},{dtstring}')
    except:
        print("no file with markfaces")
        # write code to create a file

def main():
    print("Starting.....")

    # cap = cv2.VideoCapture("Samples/celeb.mp4")
    cap = cv2.VideoCapture(0)
    print(cap)
    # cap = cv2.VideoCapture("rtsp://172.16.69.251:8080/h264_ulaw.sdp")
    # cap=cv2.VideoCapture('http://172.16.36.6:4747/video')
    framerate = cap.get(cv2.CAP_PROP_FPS)//1
    print(framerate)
    print(int(framerate*skip))
    framecount = 0
    # fc=0
    totalframes=0
    start=time.time()
    while True:
        # print("in while")
        s1=time.time()
        ret, img = cap.read()
        # img = cv2.imread("1.jpg")
        # img = cv2.imread("t1.jpeg")
        totalframes+=1
        framecount += 1
        # fc+=1
        

        # print(framecount)
        # if framecount != stride:
        #     continue
        # framecount=0
        # print(framecount)
        img2 = img 
        # Check if this is the frame closest to 10 seconds
        # if framecount == (framerate * 1) :
    
        # Close after video ends or when frame is not detected
        
        if not ret:
            break
        elif framecount == int(framerate*skip):
            framecount = 0
            r=1/resize       # helper for resizing
            red_img = cv2.resize(img, (0,0),None,r,r)
            red_img = cv2.cvtColor(red_img,cv2.COLOR_BGR2RGB)
            cor_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            

            # face_location = face_recognition.face_locations(red_img,number_of_times_to_upsample=2,model="cnn")
            # y2 x2 x1 y1
            # faces, confid = detector.detect(red_img)
            faces,confidences = detector.detect(cor_img)
            face_location=[]
            if faces is None:
                continue
            for face,confidence in zip(faces,confidences):

                if not confidence>0.96:
                    continue
                x1=face[0]
                y1=face[1]
                x2=face[2]
                y2=face[3]
                # r1=resize   #resize helper
                # y1,x2,y2,x1 = y1*r1,x2*r1,y2*r1,x1*r1
                x1=max(0,int(face[0]))
                y1=max(0,int(face[1]))
                x2=max(0,int(face[2]))
                y2=max(0,int(face[3])) 

                face_location.append(tuple([y1,x2,y2,x1]))
            
            print(face_location)
            # print("h1")
            encode_of_curr_frame = face_recognition.face_encodings(cor_img,face_location,num_jitters=2)
            # print("h2")
            # print(encode_of_curr_frame)

            count=0

            for encode_face, face_loc in zip(encode_of_curr_frame,face_location):
                matches = face_recognition.compare_faces(encodeListKnown,encode_face,tolerance=0.40)
                face_dis = face_recognition.face_distance(encodeListKnown,encode_face)
                # print(matches)
                # print(face_dis)
                matchIndex = np.argmin(face_dis)
                # print(matchIndex)
                
                pred=model.predict(encode_face.reshape(1,-1))
                print("PRED :",pred)
                matches1=model.predict_log_proba(encode_face.reshape(1,-1))
                print("Matches: ",matches1[0])
                print(matches1.shape) # matches is cd array
                # break;
                matchIndex=np.argmax(matches1)
                print("Match Index: ",matchIndex)
                print(matches1[0][matchIndex])
                y1,x2,y2,x1 = face_loc
                # r1=resize   #resize helper
                # y1,x2,y2,x1 = y1*r1,x2*r1,y2*r1,x1*r1
                
                
                # y1,x2,y2,x1 = y1*2,x2*2,y2*2,x1*2 
                cv2.rectangle(img2, (x1,y1),(x2,y2),(0,255,0),2)
                # cv2.rectangle(img2, (x1,y2+35),(x2,y2),(0,255,0), cv2.FILLED)
                
                
                if matches1[0][matchIndex] > -0.7:
                    # name = classNames[matchIndex]
                    name=pred[0]
                    cv2.putText(img2 ,name, (x1+6,y2+30), cv2.FONT_HERSHEY_SIMPLEX,1.02,(0,0,0),2,cv2.LINE_AA)
                    cv2.putText(img2 ,name, (x1+6,y2+30), cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2,cv2.LINE_AA)
                    # markfaces2(name.split('_')[0])
                    markfaces(name.split('_')[0])
                else:
                    cv2.putText(img2 ,"Unknown", (x1+6,y2+30), cv2.FONT_HERSHEY_SIMPLEX,1.02,(0,0,0),2,cv2.LINE_AA)
                    cv2.putText(img2 ,"Unknown", (x1+6,y2+30), cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2,cv2.LINE_AA)
                    count = count+1
                    now = datetime.now()
                    dtstring = now.strftime('%H-%M-%S')
                    ne_img = img2[y1:y2, x1:x2]
                    path = ".//UnknownFaces//"
                    path = path+dtstring+"_"+str(count)+".jpg"
                    # print(path)
                    # cv2.imshow("img",ne_img)
                    cv2.imwrite(path,ne_img)

            e1=time.time()
            fps=stride//(e1-s1)
            # print("FPS :",fps)

            # FPS
            # cv2.putText(img2,"FPS :{}".format(fps),(0,30),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

            cv2.imshow("RECOG",img2)
        
        r=1/(resize)        #resize helper
        img2=cv2.resize(img,(0,0),None,r,r)   
        cv2.imshow("LIVE",img2)
        
        key = cv2.waitKey(10)
        if key == 27:
            break
    end=time.time()
    avg=totalframes/(end-start)
    print("AVG :",avg)
    cap.release()
    cv2.destroyAllWindows()
    return;


if __name__ == "__main__":
    main()
    exit(1)
