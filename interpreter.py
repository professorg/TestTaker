import io
import random

class Test(object):
	def __init__(self, questions):
		self.questions = questions
		self.score = 0
	def run(self):
		for question in self.questions:
			question.run()
			self.score += question.correct
		print "Congrats! The test is over!"
		print "Your score: " + str(self.score) + "/" + str(len(self.questions))
		
class Question(object):
	def __init__(self, prompt, answers, correct_answer):
		self.prompt = prompt
		self.answers = answers
		random.shuffle(self.answers)
		self.correct_answer = correct_answer
		self.correct = 0
	def run(self):
		print self.prompt
		for i in self.answers:
			print i
		print ""
		input = raw_input("Your Answer:  ")
		if str(input) == self.correct_answer:
			self.correct = 1

testQuestion = Question("Which number is best?", ["1: 1", "2: 7", "3: 5", "4: 9"], 2)
testTest = Test([testQuestion])

testTest.run()

			
		
		
#READING FILES
allQuestions = []

def GetFromFile(filename):
	Questions = []
	thisFile = open(filename, "r")
	linenum = 0
	Q = ""
	A = []
	C = 0
	while True:
		thisLine = thisFile.readline()
		linenum += 1
		if thisLine == "":
			break
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
	return Questions
			

allQuestions += GetFromFile("custom.txt")
allQuestions += GetFromFile("exqs.txt")

#GET INPUT
response = ""
while True:
    if response.lower() in ("test", "show", "print"):
        # Print test
        pass
    elif response.lower() in ("create", "new"):
        # Create test
        pass
    else:
        # Invalid input
        pass


#MAKE CUSTOM
def createProblem():
    pass


#ANSWER PRESET

