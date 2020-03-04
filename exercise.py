#!/usr/bin/python
import sys 
import os
from random import randint #importing random number generator module to be later used in this script
grade = input("Please enter a degree of difficulty for today's ab workout (1-3): ") #asking for the difficulty of the workout and storing it in the grade variable
if type(grade) is int and grade>=1 and grade <=3: #checking if the input is either 1,2 or 3
	pass
else:
	print("Incorrect input for difficulty. Please enter integer value of 1, 2, or 3") #remind the user to enter a vaule of 1,2, or 3 as their answer if it is not 
	os.execv(__file__, sys.argv) #restarting the script if the value is not an integer in the correct range
number= 0 #declaring number varible which stores the number of exercises in the workout
diff=input("Please provide your level of fitness (1 for beginner, 2 for intermediate, and 3 for advanced): ") #asking for the fitness level and storing it in diff variable
if type(diff) is int and diff>=1 and diff <=3:
        pass
else:
        print("Incorrect input for level of fitness. Please enter a value of 1, 2, or 3 when prompted for the level of fitness") #remind the user to enter a vaule of 1,2, or 3 as their answer if it is not 
	os.execv(__file__, sys.argv) #remind the user to enter a vaule of 1,2, or 3 as their answer if it is not 

if grade==1: #defining the number of exercises based on the value of the grade variable
	number=3 
elif grade==2:
	number=6
else:
	number=9

repetitions=diff*10 #defining repetitions variable based upon the value of diff variable multiplied by 10
rounds=diff*2 #defining rounds variable based upon the value of diff variable mutliplied by 2
exercises = ("crunches","reverse crunches","double crunch","bicycle","side oblique crunch (each side)", "plank reach", "leg raises", "inverted frog legs", "side iso ab crunch (each side)", "v-up","oblique v-up (each side)","thread the needle","leg rotations", "Russian twists") #creating a list with exercises
        	

print ("Here is your personalized workout (in the exercise, repetions format) with a rest of 30 seconds between each round, for a total of " + str(rounds) + " rounds:")
exercise=[None]*number #initialize the exercise list 
for i in range (0, number):
	exercise[i]=exercises[randint(0,len(exercises)-1)] #get a random exercises from the exercises list
	for j in range (0,i): #check if the selected exercise already previously exists in the list to avoid any duplicates
		while exercise[i] == exercise[j]:
			exercise[i]=exercises[randint(0,len(exercises)-1)]
	print str(exercise[i]) + ", " + str(repetitions) #print the name of the exercises with the number of repetitions


