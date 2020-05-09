from gtts import gTTS
import os


#
# myText = "Ohayou Gozaimasu . Konnichiwa Konbanwa (こんばんは) - Oyasuminasai  Arigatou Gozaimas" \
#          " Yoroshiku Onegaishimasu .Watashi no Namae wa Sasuke Sama aka Harshit desu."

myText = "Ohayou Otakus, Watashi no Namae va Sasuke Sama aka Harshit desu. Join us in making Anime Succesful in India by joining our anime kurabu"
language = 'ja'
output = gTTS(text=myText, lang=language, slow=False)
output.save("output.mp3")
os.system("start output.mp3")

