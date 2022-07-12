print "hello world"
print "yes this is keerthi\n"     #After this output a new line comes
print "Am! the genius.."
print 'myself "keerthi" but it/is'   #with single quote you can display everything as it is no variable substitution
print 'what is this'

#Numbers and Math
print "this is what happens",  25 + 30, 25-30   #you can specify multiple statments with , 
#( first, then exponents, multiplication, division, addition and subtraction this is the order python follows
print "Roosters", 100 - 25 * 3 % 4      
#Always * takes precedence then % comes eg 75%4 [3 reminder and 18 is quotient] (100-3) = 97
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6 #1+4 % 2(gives 0) -1/4(gives 0) + 6  total is 7
print 3 + 2 > 5 - 7    #it returns keyword True (7 > -2) otherwise false.
print 10/3.0
print "Is it less or equal?", 5 <= -2   #output Is it less or equal false


#ASSIGNING VALUES TO VARIABLES AND PRINTING THOSE VARIABLES
cars = 7  #Assign vlaue 7 to variable cars
drivers = 10
space = 4.0  #assigning a floating number and result will be a floating number
total = cars * drivers
print "total value", total, "these all drivers value" #cama is must between these statements to separate it
#total value 70 these all drivers value

#Assigning variables string/text and displaying those values
my_name = "keerthi"
my_age = 35
my_hair = 'Black'
my_weight = 70.0
print my_weight
print "lets talk about my name %s" %my_name
print "my age  %d and hair color %s" %(my_age, my_hair)   #include parathessis to display values of multiple variables.
print "if i add my age %d and my weight %f and total value %d" %(my_age, my_weight, my_age + my_weight)   #you can add two variables and display its value

x = "There are %d types of people." % 10
print x
print "'%s'" %x   #the output is same as below command
print "I said: %r" % x  #it prints there are 10 types of people in single quotes and %r mainly used for debugging purpose.
#I said: 'There are 10 types of people.'

w = "this is india."
e = " Am appending"
k = w + e
print k  # Both strings are appended and stored in single string K
print "cancatenation of strings %s" %k  #same as above
#this is india. Am appending
print "%s\n" %k *10   #Printing same string 10 times with this command
print "this is %s." % 'keerthi'  #appedning keerthi to the string. this is keerthi

print "I am 6'2\" tall"  #you need to put backslash before double quotes because the string is in double quotes 
print 'I am 6\'2" tall.'  #same as above the string is in single quote so backslash before single quote

#we 3 double quotes you can print any number of lines
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
this is really crazy
"""
print "\\n"    #\ using black slash we can disable \n \t \a etc similarly single and double quotes within a string output.

#print "How old are you?",
#age = raw_input()           #this allows you to enter input values as a string. 
#print "How tall are you?",
#height = raw_input()
#print "How much do you weigh?",
#weight = raw_input()

#Another way to enter the above commands
age = int(raw_input("How old are you? "))
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %d old, %r tall and %r heavy." % (age, height, weight)   #either specify %s or %r to display string



 
