'''
This program learns responses to questions from the user,
saves them into a .txt file, and repeats the answer when 
the question is asked again.
'''

# saves the user's name as variable 'userName'
userName = input("\n\nPlease enter your name: \n\n")
#takes variable 'userName' and makes the first letter of each name capital
userName = userName.title()
#puts each name in userName into a separate element of a list
userName = userName.split()
#derives 'firstName' from 'userName'
global firstName
firstName = userName[0]
global firstNameUpper
firstNameUpper = firstName.upper()

# prints personalized greeting from ancestor.py
print("\n\nMEMORY-BOT: Hello " + firstName + ", I'm Memory-Bot.  Ask me anything, and I'll answer as best I can.  If I don't know the answer to your question, you can provide it to me and I'll remember it for later.  What can I help you with today? \n")

# this is the start of the conversation loop
def conversation():
  
  # assigns user input to the variable 'question'
  question = input("\n" + firstNameUpper + ": ")
  
  # allows the user to end the conversation by including "end conversation" in input
  if "end conversation" in question:
    print("\nMEMORY-BOT: It was a pleasure to be of service, any questions and answers will remain saved.  Goodbye for now.\n\n")
    exit()
  
  else:
    # changes user input  to lowercase
    question = question.lower()
    
    # opens brain.txt with the variable brainRead
    with open("brain.txt", "r") as brainRead:
      
      # converts brain.txt into a list called questionsList, where each line is an item
      questionsList = brainRead.readlines()
      
      # gets the index for a given item in questionsList
      for questionIndex in questionsList:
        
        # checks if the user input exists within one of the items in questionsList
        if question in questionIndex:
          questionIndex = str(questionIndex)
          
          # finds the index for the answer to 'question' by finding the index for 'question' and adding 1
          
          answerIndex = questionsList.index(questionIndex) + 1
          print("\n" + "MEMORY-BOT" + ": " + questionsList[answerIndex])
          return
          
      # addresses unsaved questions		
      newAnswer = input("\n" + "MEMORY-BOT" + ": I'm sorry, I can't recall the answer to that question.  Please provide the answer and I'll make sure not to forget it, or let me know you'd like to skip the question. \n\n" + firstNameUpper + ": ")
      
      # if the input contains the word 'skip', move on without writing anything to brain.txt 
      if "skip" in newAnswer:
        print("\n" + "MEMORY-BOT" + ": Alright, we can skip that last question.\n")
        return

      # allows the user to end the conversation by including "end conversation" in input
      elif "end conversation" in newAnswer:
        print("\nMEMORY-BOT: It was a pleasure to be of service, goodbye for now.\n\n")
        exit()
        
      # if the user doesn't decide to skip the question, write the question and answer to brain.txt
      else:
        with open("brain.txt", "a") as brainWrite:
          #capitalizes the first word of the answer given by the user
          newAnswer= newAnswer.capitalize()
          # writes the question and answer to brain.txt
          brainWrite.write(question + "\n")
          brainWrite = open("brain.txt", "a")
          brainWrite.write(newAnswer + "\n")
          print("\n" + "MEMORY-BOT" + ": Your question and answer have been saved.  Anything else I can help you with?\n")
          return
          
while True: 
  conversation()
  
