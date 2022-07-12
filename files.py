#open a file and print contents in that file

txt = open("keerthi.txt")    #open a file with file_name Keerthi.txt and txt is a file object
print "contents of the file"
contents_of_file = txt.read()
print "display contents in file :\n", contents_of_file
txt = open("keerthi.txt")   #you need to read evertime if you want to display contents of file.
print "can it display again:\n", txt.read()             #using variable.read() to dispaly contents it is same as above

print "Enter file name again"
file_name = raw_input (">")
txt_again = open(file_name)
print txt_again.read()

#open a file in write mode, clear its contents then write few lines in that file
target = open("dad.txt", 'w')
target.truncate()   #clearing contents of the file

print "write new contents in the file \"dad.txt\" \n"
line1 = raw_input("line1 :")
line2 = raw_input("line2 :")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
print "closing the file :\n"
target.close()
#open the file again
txt = open("dad.txt")
print "display contents of file"
print txt.read()
txt.close()

#Copy contents from keerthi.txt to brocade.txt one file to another file
from sys import argv
from os.path import exists

in_file = open("keerthi.txt")
contents = in_file.read()
#print the number of bytes for input file.
print "Total number of byes: %d" % len(contents)
print "check the output file exist : %s" %exists("brocade.txt")

#open a new file brocade.txt in write mode
out_file = open("brocade.txt", 'w')
out_file.truncate()

#copy contents of keerthi.txt to brocade.txt
out_file.write(contents)
out_file.close()   #closing both files
in_file.close()
#open new file and print its contents
new_file = open("brocade.txt")
print "New file brocade.txt contentents :\n", new_file.read()

