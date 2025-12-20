print("Hello world")

#p1---------
 print('''hellooo
 this is the multi line 
 way to print all lines''')

# p2-------
for i in range(1,11):
    print(5*i)

# p3---------
import pyttsx3
engine = pyttsx3.init()
engine.say("Text-speech doesnt work in Codespace due to missing audio drivers, it works on local machine")
engine.runAndWait()
