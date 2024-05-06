#create a list of dictionary of questions
questions= [
  {
   
   "quest":  "1.Who is the author of the Mahabharata?",
   "options": "A. Vyasa\nB. Valmiki\nC. Rama\nD. Krishna",
   "answer": 'A'
   },
{
   "quest":  "2.Who was the blind king of Hastinapur?",
   "options": "A. Pandu\nB. Dhritharashtra\nC. Bheeshma\nD. Karna",
   "answer": 'B'
},
{
   "quest":  "3.Who was the mother of the Pandavas?",
   "options": "A. Draupadi\nB. Kunti\nC. Gandhari\nD. Satyavati",
   "answer": 'B'
},
{
   "quest": "4.Who is the father of Karna?",
   "options": "A. Duryodhana\nB. Pandu\nC. Kunti\nD. King Surya",
   "answer": 'D'
},
{
   "quest":  "5.What is the name of Arjuna's charioteer in the Bhagavad Gita?",
   "options": "A. Krishna\nB. Dronacharya\nC. Bheema\nD. Yudhishthira",
   "answer": 'A'
},
{
    "quest": "6.Which river did Arjuna refuse to drink from, during the Agyaatvaas?",
   "options": "A. Yamuna\nB. Ganga\nC. Saraswati\nD. Shatadru",
   "answer": 'B'
},
{
    "quest":  "7.Who was the last commander of the Kaurava army in the Kurukshetra war?",
   "options": "A. Duryodhana\nB. Bheeshma\nC. Dronacharya\nD. Karna",
   "answer": 'A'
},
{
   "quest":  "8.Who was the teacher of the Pandavas and the Kauravas?",
   "options": "A. Vyasa\nB. Bheeshma\nC. Dronacharya\nD. Krishna",
   "answer": 'C'
 },
{
   "quest":  "9.Who killed Duryodhana in the Kurukshetra war?",
   "options": "A. Bheema\nB. Arjuna\nC. Nakula\nD. Sahadeva",
   "answer": 'A'
   },
{
   "quest":  "10.Whom did Yudhishthira ask Yaksha to revive first, during the Agyaatvaas?",
    "options": "A. Arjuna\nB. Bheema\nC. Draupadi\nD. Nakula",
    "answer": 'C'
}
]

def run_quiz(questions):
    score =0
    print("Upp for a little quizzzz ;]")
    for question in questions:
        print("{}\n{}".format(question['quest'],question['options']))
        answer = input("Enter your answer (A,B,C or D): ")
        if answer==question['answer']:
            score+=1
            print("Correct ,hooray!!\n")
        else:
            print("Oops you missed :( \nThe Correct answer was ",question['answer'],"\n")
    if score>=6:    
       print("Your score is {}/{}.\nYou are a pro in Mahabharatham .".format(score,len(questions))) 
    elif score<6:
        print("Your score is {}/{}.\nBetter luck next time buddy:)".format(score,len(questions)))
        

run_quiz(questions)