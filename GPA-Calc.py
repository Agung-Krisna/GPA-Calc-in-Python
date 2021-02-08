#GPA CALCULATOR, Agung Krisna, 2021.
"""
Normal way to do it:

def GPA(value):
    if value >= 85 and value <= 100:
        print ("A+")
    elif value >= 80 and value <= 85:
        print ('B')
    ...
    very inefficient. especially without switch-case.
"""
#Note:
#Ternary operator would be good, but I'm afraid of the code being not too human-friendly.

#better way of doing it
def true_GPA(value):
    #One more question Professor, Why does the steps become irregular at 75 to 65?
    #I originally wanted to make a better and more streamlined program, but that made me forfeit my quest :(

    grades = [85, 80, 75, 65, 60, 55, 50, 45] #list made our lives easier, so why don't we use it now?
    letter = ["A", "B+", "B", "C+", "C", "D", "E"] #this too
    #some irregular case
    if value >= 85 and value <= 100: 
        print ("A+")
    elif value == 80:
        print("A")
    elif value >= 45 and value < 55:
        print("D")
    else:
        #also equiped with exception handling, 
        #I also want to store it immediately to a database, 
        #but that would've been too excessive our first program
        try:
            for i in range(0, 9, 1):
                if value < grades[i] and value >= grades[i + 1]:
                    #why this? during the testing I found some index error, 
                    #to ensure I got the right result right, I decided to do this. 
                    if i == 0:
                        print('A')
                    else:
                        print(letter[i])
                    break
        except IndexError:
            print ('E')

#some of the things to test program, if you're interested in corner casing (like I do)

#i = 100
#while (i > 0):
value = float(input("Masukkan angka disini\n"))
#print(i)
print("Hasil Kalkulasi")
true_GPA(value)
#true_GPA(i)
#i -= 1

#if you're curious, all of this only took 23 lines of code (LoC), but due to the comments I made, it got into 57 lines of code
