

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


question = raw_input("Test Question:  ")