
# # p1------
# print('''this is for the 
#       use of multi line printing without 
#       use of repat print in multi lines''')

# p2------
# for i in range(1,11):
#    print(5*i)

# p3------
# import pyttsx3
# engine = pyttsx3.init()
# engine.say("hello i will speak this text")
# engine.runAndWait()

# p4------
import os
directory_path = '/'  #specify the directory you want in the list 
content = os.listdir(directory_path) #list all the directories you want in the specified path
for item in content:  #print each file and the directory name
    print(item)
