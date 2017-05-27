import io

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

testQuestion = Question("Which number is best?", ["1: 1", "2: 7", "3: 5", "4: 9"], 2)
testTest = Test([testQuestion])

testTest.run()

			
		
		
#READING FILES
thisFile = open("exqs.txt", "r")
linenum = 0
while True:
	thisLine = thisFile.readline()
	linenum += 1
	if thisLine == "":
		break
	else:
		if linenum == 1:
			
	

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

