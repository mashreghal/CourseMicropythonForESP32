import os
#swich to the directory where the file is located
os.chdir("C:\\Users\\User\\Desktop\\CourseMicropythonForESP32")
print(os.getcwd()) # Gibt das aktuelle Verzeichnis zurueck
my_data = open("meine_daten.dat", "wt") # open file for writing text
my_data.write("Hello World")
my_data.close()
my_data = open("meine_daten.dat", "rt") # open file for reading text
my_values = my_data.read()
print(my_values)
my_data.close()


         

