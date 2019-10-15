from flask_mysqldb import MySQL
import calendar
import datetime
import time
from flask import Flask, session, redirect, url_for, escape, request, render_template,jsonify
from hashlib import md5
import MySQLdb
from flask_mysqldb import MySQL
from flask import Response
import json

app = Flask(__name__)

MySQL_HOST = 'localhost'
MySQL_USER = 'root'
MySQL_PASSWORD = 'sachin@123'
MYSQL_DB = 'MG_JOURNEY'

@app.route("/")
def index():
	
	return("WELCOME TO MEIGO..!")


@app.route("/registeruser",methods=['POST'])
def registeruser():
    if request.method == 'GET':
        return("not allowed")
    data=(request)
    print(data)
    print(data.json)
    print(data.json.get('email'))
    # for key,value in data.json.items():
    #     print(value)
    registeremail=data.json.get('email')
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%y-%m-%d %H:%M:%S')
    print(st)
    db = MySQLdb.connect(MySQL_HOST,MySQL_USER,MySQL_PASSWORD,MYSQL_DB)
    cur = db.cursor()
    cur.execute("SELECT UserEmail  from MG_User_Creation WHERE UserEmail=%s ",[registeremail])
    x=cur.fetchone()
    # print(x)
    if x==None:
        cur.execute("INSERT INTO MG_User_Creation (UserEmail,usertimestamp) values(%s,%s)",(registeremail,st))
        db.commit()
        return(jsonify({ 'userMobileNo':registeremail,'message': 'Registered successfully'}))
    else:
        return(jsonify({'userMobileNo':registeremail, 'message': 'user already exists'}))
    
@app.route("/createjourney",methods=['POST'])
def createjourney():
    if request.method == 'GET':
        return(" Method not allowed")
    data=(request)
    cv=data.json
    username=cv["userid"]
    duedate=cv["Journey_Duedate"]
    journeypurpose=cv["journeypurpose"]
    journeytype=cv["jourtype"]
    journeymode=cv["jourmode"]
    ts = time.time()
    timestamp=round(time.time())
    # print(timestamp)
    j_id=str("J1_")+str(timestamp)
    st = datetime.datetime.fromtimestamp(ts).strftime('%y-%m-%d %H:%M:%S')
    # print(x)
    # print(st)
    db = MySQLdb.connect(MySQL_HOST,MySQL_USER,MySQL_PASSWORD,MYSQL_DB)
    cur = db.cursor()
    cur.execute("SELECT UserEmail from MG_JRNY_Creation WHERE UserEmail=%s ",[username])
    x=cur.fetchone()
    if x==None:
        cur.execute("INSERT INTO MG_JRNY_Creation (journeyID,UserEmail,Journey_Duedate,journeypurpose,journeytimestamp,journeytype,journeymode) values(%s,%s,%s,%s,%s,%s,%s)",(j_id,username,duedate,journeypurpose,st,journeytype,journeymode))
        db.commit()
        return(jsonify({ 'journeyID':j_id,'message': 'journey is created successfully'})) 
    else:
        cur.execute("SELECT journeyID from MG_JRNY_Creation WHERE UserEmail=%s ",[username])
        y=cur.fetchone()
        print(y)
        return(jsonify({ 'userid':username,'message': 'userID already exist'}))
    

@app.route("/deletejourney",methods=['POST'])
def deletejourney():
    if request.method == 'GET':
        return(" Method not allowed")
    
    data=(request)
    cv=data.json
    # print(cv["userid"])
    useremail=cv["userid"]
    journeyid=cv["journeyID"]
    db = MySQLdb.connect(MySQL_HOST,MySQL_USER,MySQL_PASSWORD,MYSQL_DB)
    cur = db.cursor()
    cur.execute("SELECT journeyID from MG_JRNY_Creation WHERE journeyID=%s or UserEmail=%s ",[journeyid,useremail])
    m=cur.fetchall()
    print(m)
    if m:
        cur.execute("SELECT journeyID from MG_JRNY_Creation WHERE journeyID=%s ",[journeyid])
        x=cur.fetchall()
        print(x)
        if x:
            cur.execute("SELECT UserEmail from MG_JRNY_Creation WHERE UserEmail=%s ",[useremail])
            y=cur.fetchall()
            print(y)
            if y:
                cur.execute("DELETE FROM MG_JRNY_Creation where journeyID =%s and UserEmail=%s",(journeyid,useremail))
                db.commit()
                return(jsonify({'journeyID':journeyid, 'message': 'journey is deleted successfully'}))
            else:
                return(jsonify({'userID':useremail,'message': 'Invalid userID'}))
        
        return(jsonify({'journeyID':journeyid,'message': 'Invalid journeyID'}))
        

    return(jsonify({'message': 'record not found'}))


    
    # cur.execute("SELECT journeyID from MG_JRNY_Creation WHERE journeyID=%s ",[journeyid])
    # x=cur.fetchall()
    # print(x)
    # if x:
    #     cur.execute("SELECT UserEmail from MG_JRNY_Creation WHERE UserEmail=%s ",[useremail])
    #     y=cur.fetchall()
    #     print(y)
    #     if y:
    #         cur.execute("DELETE FROM MG_JRNY_Creation where journeyID =%s and UserEmail=%s",(journeyid,useremail))
    #         db.commit()
    #         return(jsonify({'journeyID':journeyid, 'message': 'journey is deleted successfully'}))
    #     else:
    #         return(jsonify({'userID':useremail,'message': 'Invalid userID'}))

    # return(jsonify({'journeyID':journeyid,'message': 'Invalid journeyID'}))

@app.route("/updatejourneytags",methods=['POST'])
def updatejourneytags():
    if request.method == 'GET':
        return(" Method not allowed")
    
    data=(request)
    cv=data.json
    print(cv["journeyid"])
    journeyid=cv["journeyid"]
    usermail=cv["userid"]
    journeytype=cv["journeytype"]
    journeymode=cv["journeymode"]
   
    db = MySQLdb.connect(MySQL_HOST,MySQL_USER,MySQL_PASSWORD,MYSQL_DB)
    cur = db.cursor()
    cur.execute("SELECT journeyID from MG_JRNY_Creation WHERE journeyID=%s",[journeyid])
    x=cur.fetchall()
    print(x)
    if x:
        cur.execute("SELECT UserEmail from MG_JRNY_Creation WHERE UserEmail=%s ",[usermail])
        y=cur.fetchall()
        print(y)
        if y:
            cur.execute("UPDATE MG_JRNY_Creation SET journeymode=%s,journeytype=%s WHERE UserEmail=%s and journeyID=%s ",[journeymode,journeytype,usermail,journeyid])
            db.commit()
            return(jsonify({'journeyID':journeyid, 'message': 'journey is updated sucessfully'}))
        else:
            return(jsonify({'userID':usermail,'message': 'Invalid userID'}))
    return(jsonify({'journeyID':journeyid,'message': 'Invalid journeyID'}))

@app.route("/getjourneys",methods=['GET'])
def getjourneys():
    if request.method == 'POST':
        return("not allowed")
    user_type = request.args.get('type',)
    if user_type =="all":
        db = MySQLdb.connect(MySQL_HOST,MySQL_USER,MySQL_PASSWORD,MYSQL_DB)
        cur = db.cursor()
        cur.execute("SELECT journeyID,journeytype from  MG_JRNY_Creation ")
        x=cur.fetchall()
    else :
        db = MySQLdb.connect(MySQL_HOST,MySQL_USER,MySQL_PASSWORD,MYSQL_DB)
        cur = db.cursor()
        cur.execute("SELECT journeyID,journeytype from  MG_JRNY_Creation  where journeytype=%s  ",(user_type,))
        x=cur.fetchall()
    print(x)
    # for key,value in x:
    #     print(key,value)
    return(jsonify(x))

@app.route("/getjourneypurpose/",methods=['GET'])
def getjourneypurpose():
    if request.method == 'POST':
        return("not allowed")
    db = MySQLdb.connect(MySQL_HOST,MySQL_USER,MySQL_PASSWORD,MYSQL_DB)
    cur = db.cursor()
    cur.execute("SELECT journeypurpose from  MG_JRNY_Creation")
    x=cur.fetchall() 
    purpose = []
    result={

    }
    for y in x:
        purpose.append(str(y[0]))
    print(purpose)
    result["purpose"]=purpose
    return(jsonify(result))


@app.route("/insertemotion",methods=['POST'])
def insertemotion():
    if request.method == 'GET':
        return("not allowed")
    data=(request)
    # print(data.json)
    useremotion=[]
    for m,n in data.json.items():
        # print(n)
        useremotion.append(n)
    print(useremotion[0])
    print(useremotion[1])
    db = MySQLdb.connect(MySQL_HOST,MySQL_USER,MySQL_PASSWORD,MYSQL_DB)
    cur = db.cursor()
    cur.execute("SELECT journeyID from  MG_JRNY_Creation  where UserEmail=%s ",(useremotion[1],))
    x=cur.fetchone()
    print(x)
    ts = time.time()
    journey_st = datetime.datetime.fromtimestamp(ts).strftime('%y-%m-%d %H:%M:%S')
    print(journey_st)
    emotion_st = datetime.datetime.fromtimestamp(ts).strftime('%y-%m-%d %H:%M:%S')
    print(emotion_st)
    cur.execute("INSERT INTO MG_JRNY_Operations (journeyID,Emotion_tag,emotiontag_timestamp,journeytimestamp) values(%s,%s,%s,%s)",(x,useremotion[0],emotion_st,journey_st))
    db.commit()
    return(jsonify({'message': 'emotion inserted sucessfully'}))

@app.route("/getemotiontags/",methods=['GET'])
def getemotiontags():
    if request.method == 'POST':
        return("not allowed")
    user_id = request.args.get('type')
    db = MySQLdb.connect(MySQL_HOST,MySQL_USER,MySQL_PASSWORD,MYSQL_DB)
    cur = db.cursor()
    cur.execute("SELECT journeyID,UserEmail from  MG_JRNY_Creation  where UserEmail=%s ",(user_id,))
    x=cur.fetchone()
    print(x[0])
    print(x[1])
    if x:
        cur.execute("SELECT Emotion_tag from  MG_JRNY_Operations  where journeyID=%s ",(x[0],))
        y=cur.fetchall()
        print(y)
        return(jsonify({'userid':x[1],'journeyID': x[0],'emotionTAGS':y}))
   
    
    

@app.route("/comparejourneys",methods=['POST'])
def comparejourneys():
    if request.method == 'GET':
        return("not allowed")
    data=(request)
    cv=data.json
    print(cv["userid"])
    usermail=cv["userid"]
    journeyid=cv["journeyID"]
    journeypurpose=cv["journeypurpose"]
    emotiontag=cv["emotion_tag"]
    db = MySQLdb.connect(MySQL_HOST,MySQL_USER,MySQL_PASSWORD,MYSQL_DB)
    cur = db.cursor()
    cur.execute("SELECT UserEmail from  MG_JRNY_Creation  where  UserEmail=%s ",(usermail,))
    x=cur.fetchone()
    print(x)
    if x:
        cur.execute("SELECT journeyID from  MG_JRNY_Creation  where  journeyID=%s and UserEmail=%s  ",(journeyid,usermail,))
        y=cur.fetchall()
        print(y)
        if y:
            cur.execute("SELECT journeypurpose from  MG_JRNY_Creation  where  journeypurpose=%s and UserEmail=%s ",(journeypurpose, usermail,))
            z=cur.fetchall()
            print(z)
            if z:
                cur.execute("SELECT Emotion_tag from  MG_JRNY_Operations  where Emotion_tag=%s ",(emotiontag,))
                s=cur.fetchall()
                print(s)
                if s:
                    cur.execute("SELECT journeyID from  MG_JRNY_Operations  where Emotion_tag=%s ",(emotiontag,))
                    a=cur.fetchall()
                    print(a)
                    return(jsonify({'userid':usermail,'journeyID':journeyid ,'similarjourneys': a}))
                return(jsonify({'emotion tag':emotiontag, 'message': 'emotion tag  invalid'}))


            return(jsonify({'journeypurpose':journeypurpose,'message':'INVALID journeypurpose'}))

        return(jsonify({'journeyID':journeyid ,'message':'INVALID journeyid'}))

    
    return(jsonify({'userID':usermail,'message':'INVALID userid'}))

@app.route("/suggestjourneytags",methods=['POST'])
def suggestjourneytags():
    if request.method == 'GET':
        return("not allowed")
    data=(request)
    cv = data.json
    guestmail=cv["emailguest"]
    journeyid=cv["journeyID"]
    usermail=cv["userID"]
    helprequest=cv["helprequests"]
    guestvalue=cv["guestvalue"]
    db = MySQLdb.connect(MySQL_HOST,MySQL_USER,MySQL_PASSWORD,MYSQL_DB)
    cur = db.cursor()
    cur.execute("SELECT UserEmail from  MG_JRNY_CREATION  where UserEmail=%s ",(usermail,))
    x=cur.fetchall()
    print(x)
    if x:
        cur.execute("SELECT journeyID from  MG_JRNY_CREATION  where journeyID=%s and UserEmail=%s   ",(journeyid,usermail,))
        y=cur.fetchall()
        print(y)
        if y:
            cur.execute("SELECT Emotion_tag from  MG_JRNY_Operations  where journeyID=%s  ",(journeyid,))
            z=cur.fetchall()
            tag=helprequest
            print(tag)
            ts = time.time()
            journey_st = datetime.datetime.fromtimestamp(ts).strftime('%y-%m-%d %H:%M:%S')
            print(journey_st)
            for t in z:
                # print(t[0].upper()==tag.upper())
                if tag.upper()==t[0].upper():
                    cur.execute("INSERT INTO MG_JRNY_Requests (journeyID,Guest_Email,Emotion_tag,Emotion_tag_value,journeytimestamp) values(%s,%s,%s,%s,%s)",(journeyid,guestmail,helprequest,guestvalue,journey_st))
                    db.commit()
                    return(jsonify({'userid':usermail,'message': 'successfully updated'}))
            return(jsonify({'helprequest':helprequest,'message': 'help request not found'}))

            

        return(jsonify({'journeyid':journeyid,'message': 'invalid journeyid'}))

    
    return(jsonify({'userid':usermail,'message': 'invalid userid'}))


@app.route("/initiatejourneysupport",methods=['POST'])
def initiatejourneysupport():
    if request.method == 'GET':
        return("not allowed")
    data=(request)
    cv = data.json
    # print(cv["userid"])
    usermail=cv["userid"]
    journeyid=cv["journeyID"]
    helprequests=cv["helprequests"]
    db = MySQLdb.connect(MySQL_HOST,MySQL_USER,MySQL_PASSWORD,MYSQL_DB)
    cur = db.cursor()
    cur.execute("SELECT UserEmail from  MG_JRNY_CREATION  where  UserEmail=%s ",(usermail,))
    x=cur.fetchone()
    print(x)
    if x:
        cur.execute("SELECT journeyID from  MG_JRNY_CREATION  where  journeyID=%s and UserEmail=%s  ",(journeyid,usermail,))
        y=cur.fetchone()
        print(y)
        if y:
            cur.execute("SELECT Emotion_tag from  MG_JRNY_operations  where  journeyID=%s ",(journeyid,))
            z=cur.fetchall()
            print(z)
            tag1=helprequests
            print(tag1)
            for p in z:
                # print(p[0]==tag1)
                if tag1.upper()==p[0].upper():
                    cur.execute("SELECT Emotion_tag_value from MG_JRNY_Requests where Emotion_tag=%s and journeyID=%s  ",(helprequests,journeyid,))
                    m=cur.fetchall()
                    print(m)
                    return(jsonify({'userid':usermail,'journeyID':journeyid,'helprequests:': m}))
            return(jsonify({'helprequest':helprequests,'message': 'emotion not found'}))

        return(jsonify({'journeyID':journeyid,'message': 'invalid journeyid'}))
        

    return(jsonify({'userID':usermail,'message': 'invalid userid'}))

    
@app.route("/dailytask",methods=['POST'])
def dailytask():
    if request.method == 'GET':
        return("not allowed")
    data=(request)
    print(data)
    task=[]
    for key,value in data.json.items():
        #  print(value)
         task.append(value)
    print(task)
    db = MySQLdb.connect(MySQL_HOST,MySQL_USER,MySQL_PASSWORD,MYSQL_DB)
    cur = db.cursor()
    cur.execute("SELECT journeyID from  MG_JRNY_CREATION  where  UserEmail=%s ",(task[5],))
    x=cur.fetchone()
    print(x)
    if x:
        cur.execute("INSERT INTO MG_JRNY_Details (journeyID,journeyDATE,Emotion_tag,userupload,Activity,Others) values(%s,%s,%s,%s,%s,%s)",(x,task[0],task[1],task[4],task[2],task[3]))
        db.commit()
    else:
        return(jsonify({'message': ' inserted unsuccessfully'})) 

    return(jsonify({'message': 'inserted successfully'})) 

@app.route("/getjourneydetails",methods=['POST'])
def getjourneydetails():
    if request.method == 'GET':
        return("not allowed")
    data=(request)
    cv= data.json
    # print(cv["userid"])
    usermail=cv["userid"]
    journeyid=cv["journeyID"]
    db = MySQLdb.connect(MySQL_HOST,MySQL_USER,MySQL_PASSWORD,MYSQL_DB)
    cur = db.cursor()
    cur.execute("SELECT UserEmail from  MG_JRNY_Creation  where  UserEmail=%s ",(usermail,))
    x=cur.fetchall()
    # print(x)
    if x:
        cur.execute("SELECT journeyID from  MG_JRNY_Creation  where  journeyID=%s and UserEmail=%s ",(journeyid,usermail,))
        y=cur.fetchall()
        # print(y)
        if y:
            cur.execute("SELECT journeyDATE,Emotion_tag,userupload, Activity,Others  from  MG_JRNY_Details  where   journeyID=%s ",(journeyid,))
            z=cur.fetchall()
            print(z)
            return(jsonify({'journeyID':journeyid,'dailytasks': z}))

        return(jsonify({'journeyid':journeyid, 'message': "invalid journeyid" }))   

    return(jsonify({'userid':usermail, 'message': "invalid userid" }))

@app.route("/updatejourney",methods=['POST'])
def updatejourney():
    if request.method == 'GET':
        return("not allowed")
    data=(request)
    cv= data.json
    print(cv["userid"])
    usermail=cv["userid"]
    journeyid=cv["journeyID"]
    journeydate=cv["journeyDate"]
    emotiontag=cv["emotionTag"]
    db = MySQLdb.connect(MySQL_HOST,MySQL_USER,MySQL_PASSWORD,MYSQL_DB)
    cur = db.cursor()
    cur.execute("SELECT UserEmail from  MG_JRNY_Creation  where  UserEmail=%s ",(usermail,))
    x=cur.fetchall()
    # print(x)
    if x:
        cur.execute("SELECT journeyID from  MG_JRNY_Creation  where  journeyID=%s and UserEmail=%s  ",(journeyid,usermail,))
        y=cur.fetchall()
        # print(y)
        if y:
            cur.execute("SELECT Emotion_tag  from  MG_JRNY_Details  where   journeyID=%s ",(journeyid,))
            z=cur.fetchall()
            print(z)
            print(emotiontag)
            for p in z:
                # print(p[0]==emotiontag)
                if emotiontag.upper()==p[0].upper():
                    cur.execute("UPDATE MG_JRNY_Details SET journeyDATE=%s WHERE journeyID=%s  and  Emotion_tag=%s",[journeydate,journeyid,emotiontag,])
                    db.commit()
                    cur.execute("SELECT journeyDATE,Emotion_tag,userupload, Activity,Others  from  MG_JRNY_Details  where   journeyID=%s ",(journeyid,))
                    m=cur.fetchall()
                    # print(m)
                    return(jsonify({'journeyID':journeyid,'dailytasks': m}))

            return(jsonify({'emotiontag':emotiontag, 'message': "invalid emotiontag" }))
            

        return(jsonify({'journeyid':journeyid, 'message': "invalid journeyid" }))   

    return(jsonify({'userid':usermail, 'message': "invalid userid" }))
    




    




    

if __name__ == '__main__':
    app.run(debug=True,port=5000,host="0.0.0.0")
