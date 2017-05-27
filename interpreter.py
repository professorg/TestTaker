import io
import os


	
	

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



			

		
#READING FILES
allQuestions = []

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
	return Test(Questions)
			
#takes in test and file name, saves
def SaveToFile(thetest, filename):
	thisFile.open("tests/"+filename+".txt", "w")
	

#allQuestions += GetFromFile("custom.txt")
#allQuestions += GetFromFile("exqs.txt")

#GET INPUT
while True:
    response = raw_input("What would you like to do? ")
    if response.lower() in ("test", "show", "print"):
        # Print test
        pass
    elif response.lower() in ("create", "new"):
        # Create test
        test = createTest()
    elif response.lower() in ("exit", "quit"):
        break
    else:
        # Invalid input
        pass


#MAKE CUSTOM
def createTest():
    questions = []

    while raw_input("Would you like to add another question?").lower() in ("yes", "y"):
        Q = raw_input("Enter the question: ")
        A = []
        print "Enter four answers:"
        A.append(raw_input("0. "))
        A.append(raw_input("1. "))
        A.append(raw_input("2. "))
        A.append(raw_input("3. "))
        N = raw_input("Enter the number of the correct answer: ")
        question = Question(Q, A, C)
        questions.append(question)
    return Test(questions)

#ANSWER PRESET

def getFiles():
	files = []
	for file in os.listdir(os.path.dirname(os.path.realpath(__file__)) + "/tests"):
		if file.endswith(".txt"):
			files.append(str(file))
	return files
def pickTest():
	files = getFiles()
	for i in range(len(files)):
		print str(i) + ": " + files[i]
	selection = raw_input("Select a test to take: ")
	


def main():
	getFiles()
	
	
