import os

from time import sleep
   
    while True:
 

        # assigning a random VPN server code

        choiceCode = random.choice(codeList)
 

        # changing IP after a particular time period

        sleep(random.randrange(120, 300))
 

        # connecting to a different VPN server

        print("!!! Changing the IP Address........")

   except:
           pass
     try:
      for i in listfiles:
        
        so = i.split("\\")
        if len(so)==2:
              newname=f"{drive}:\\"
        if len(so)==3:
              newname=f"{drive}:\\{so[1]}"
        if len(so)==4:
              newname=f"{drive}:\\{so[1]}\\{so[2]}"
        if len(so)==5:
              newname=f"{drive}:\\{so[1]}\\{so[2]}\\{so[3]}"
        if len(so)==6:
              newname=f"{drive}:\\{so[1]}\\{so[2]}\\{so[3]}\\{so[4]}"
        if len(so)==7:
              newname=f"{drive}:\\{so[1]}\\{so[2]}\\{so[3]}\\{so[4]}\\{so[5]}"
        if len(so)==8:
              newname=f"{drive}:\\{so[1]}\\{so[2]}\\{so[3]}\\{so[4]}\\{so[5]}\\{so[6]}"
       
        try:
        
         copy(f"{oneaddress}",f"{newname}")
        except:
           pass 
     except:
           pass
 
 
 
 try:
  lo.remove(f"{Drive}:\\$SYSRESET")
 except:
       pass
 for i in lo:
    try:
        st = i.split() 
        tim=str(len(st))
        newname = i
        if tim == "2":
              newname=st[0]+st[1]
        if tim == "3":
              newname=st[0]+st[1]+st[2]
        if tim == "4":
              newname=st[0]+st[1]+st[2]+st[3]
        if tim == "5":
              newname=st[0]+st[1]+st[2]+st[3]+st[4]
        rename(f"{Drive}:\\{i}",f"{Drive}:\\{newname}")
        
        try:
         po =listdir(f"{Drive}:\\{newname}")
         for p in po :
          stt = p.split() 
          timm=str(len(stt))
          newnamee = p
          if timm == "2":
              newnamee=stt[0]+stt[1]
          if timm == "3":
            newnamee=stt[0]+stt[1]+stt[2]
          if timm == "4":
              newnamee=stt[0]+stt[1]+stt[2]+stt[3]
          if timm == "5":
              newnamee=stt[0]+stt[1]+stt[2]+stt[3]+stt[4]
          rename(f"{Drive}:\\{newname}\\{p}",f"{Drive}:\\{newname}\\{newnamee}")
          
        except:
           pass
import random
 
# list of VPN server codes

codeList = ["TR", "US-C", "US", "US-W", "CA", "CA-W",

            "FR", "DE", "NL", "NO", "RO", "CH", "GB", "HK"]
 

try:
 

    # connect to VPN

    os.system("windscribe connect")

    while True:
 

        # assigning a random VPN server code

        choiceCode = random.choice(codeList)
 

        # changing IP after a particular time period

        sleep(random.randrange(120, 300))
 

        # connecting to a different VPN server

        print("!!! Changing the IP Address........")

        os.system("windscribe connect " + choiceCode)
 

except:
 

    # disconnect VPN

    os.system("windscribe disconnect")

    print("sorry, some error has occurred
          
        try:
  lo.remove(f"{Drive}:\\$SYSRESET")
 except:
       pass
 for i in lo:
    try:
        st = i.split() 
        tim=str(len(st))
        newname = i
        if tim == "2":
              newname=st[0]+st[1]
        if tim == "3":
              newname=st[0]+st[1]+st[2]
        if tim == "4":
              newname=st[0]+st[1]+st[2]+st[3]
        if tim == "5":
              newname=st[0]+st[1]+st[2]+st[3]+st[4]
        rename(f"{Drive}:\\{i}",f"{Drive}:\\{newname}")
        
        try:
         po =listdir(f"{Drive}:\\{newname}")
         for p in po :
          stt = p.split() 
          timm=str(len(stt))
          newnamee = p
          if timm == "2":
              newnamee=stt[0]+stt[1]
          if timm == "3":
            newnamee=stt[0]+stt[1]+stt[2]
          if timm == "4":
              newnamee=stt[0]+stt[1]+stt[2]+stt[3]
          if timm == "5":
              newnamee=stt[0]+stt[1]+stt[2]+stt[3]+stt[4]
          rename(f"{Drive}:\\{newname}\\{p}",f"{Drive}:\\{newname}\\{newnamee}")
          
        except:
           pass   