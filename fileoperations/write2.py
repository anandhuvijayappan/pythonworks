f=open("P:\\Luminar\\pythonworks\\dataset\\test2.txt","w")

languages = [
    "English", "Spanish", "Mandarin", "Hindi", "Arabic", "French", "Russian", 
    "Portuguese", "Bengali", "German", "Japanese", "Korean", "Italian", 
    "Turkish", "Vietnamese", "Dutch", "Swahili", "Tamil", "Urdu", "Persian",]

for l in languages:

    f.write(l+"\n")

f.close()