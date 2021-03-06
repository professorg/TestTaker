import io
import random
import os
import time

class Test(object):
	def __init__(self, questions, name):
		self.questions = questions
		self.name = name[6:]
		self.score = 0
	def run(self):
		for question in self.questions:
			question.run()
			self.score += question.correct
		os.system('cls')
		print "Congrats! The test is over!"
		print "Your score: " + str(self.score) + "/" + str(len(self.questions))
		print ""
		print "Press enter to continue"
		file = open("highscores.txt", "a")
		file.write(self.name +": "+ str(self.score)+"\n") #the thing
		file.close()
		pause = raw_input("")
class Question(object):
	def __init__(self, prompt, answers, correct_answer):
		self.prompt = prompt
		self.answers = answers
		self.correct_answer = correct_answer
		self.correct = 0
	def run(self):
		os.system('cls')
		print self.prompt
		randomized = random.sample(self.answers, len(self.answers))
		randomized_correct = randomized.index(self.answers[self.correct_answer])
		for i in range(1, len(self.answers) + 1):
			print str(i) + ": " + randomized[i - 1]
		print ""
		answer = raw_input("Your Answer:  ")
		if int(answer) - 1 == randomized_correct:
			self.correct = 1

		os.system('cls')

#Takes in file path of text doc, returns test
def GetFromFile(filename):
	Questions = []
	thisFile = open(filename, "r")
	linenum = 0
	Q = ""
	A = []
	C = 0
	working = True
	while working:
		thisLine = thisFile.readline()
		linenum += 1
		if thisLine == "":
			working = False
		else:
			if linenum == 1:
				Q = thisLine
			if linenum in [2, 3, 4, 5]:
				A.append(thisLine)
			if linenum == 6:
				C = int(thisLine)
				linenum = 0
				Questions.append(Question(Q, A, C))
				Q = ""
				A = []
				C = 0
	thisFile.close()
	return Test(Questions, filename)
			
#takes in test and file name, saves
def SaveToFile(thetest, filename):
	thisFile = open("tests/"+filename+".txt", "w")
	total = ""
	for i in thetest.questions:
		total += i.prompt+"\n"
		for x in i.answers:
			total += x+"\n"
		total += i.correct_answer+"\n"
	thisFile.write(total)
	thisFile.close()
	

#MAKE CUSTOM
def createTest():
    questions = []

    while raw_input("Would you like to add another question?").lower() in ("yes", "y"):
		os.system('cls')
		Q = raw_input("Enter the question: ")
		A = []
		print "Enter four answers:"
		A.append(raw_input("0. "))
		A.append(raw_input("1. "))
		A.append(raw_input("2. "))
		A.append(raw_input("3. "))
		N = raw_input("Enter the number of the correct answer: ")
		question = Question(Q, A, N)
		questions.append(question)
    return Test(questions)


def getFiles():
	files = []
	for file in os.listdir(os.path.dirname(os.path.realpath(__file__)) + "/tests"):
		if file.endswith(".txt"):
			files.append(str(file))
	return files
def pickTest():
	os.system('cls')
	files = getFiles()
	for i in range(len(files)):
		print str(i) + ": " + files[i]
	selection = raw_input("Select a test to take: ")
	GetFromFile("tests/" + files[int(selection)]).run()

#GET INPUT
while True:
	os.system('cls')
	print "What would you like to do?"
	print "test, show, print - show test"
	print "create, new - create new test"
	print "exit, quit - exit this prompt"
	response = raw_input("> ")
	if response.lower() in ("test", "show", "print"):

		pickTest()
	elif response.lower() in ("create", "new"):
		# Create test
		test = createTest()
		SaveToFile(test, raw_input("Enter the file name: "))
	elif response.lower() in ("exit", "quit"):
		break
	else:
		print "invalid input"
		time.sleep(1)
