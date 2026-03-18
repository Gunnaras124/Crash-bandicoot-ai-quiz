import openai
from tkinter import ttk, Label, Button
from ttkthemes import ThemedTk
window = ThemedTk(theme="equilux")
window.geometry("600x300")
client=openai.OpenAI(api_key = "ENTER YOUR OWN KEY")
lbl=Label(window,text="Password Generator")
lbl.place(x=100,y=10)
questionlvl=0
score=0
def check(balalaika):
    global score, questionlvl
    if balalaika==answer:
        score+=1
        questionlvl+=1
    else:
        questionlvl+=1
    if questionlvl>=5:
        yes.destroy()
        no.destroy()
        if score==0:
            lbl.configure(text="You should get spinned")
        if score==1:
            lbl.configure(text="WOAH this is bad")
        if score==2:
                lbl.configure(text="Not well not well not well")
        if score==3:
            lbl.configure(text="You are filled with DETERMINATION")
        if score==4:
            lbl.configure(text="You won a wumpa fruit!!!!")
        if score==5:
            lbl.configure(text="PLATINUM")
    else:
        generate_questions()
def generate_questions():
    global answer
    response=client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"system","content":"Generate a simple yes/no question in English about crash bandicoot suitable for experienced gamers with a clear correct answer without introduction. Return the format: 'Question: <question> | Answer: <yes/no>'."},
            {"role":"user","content":"Generate a simple yes/no question."}
        ]
    )
    print(response)
    result=response.choices[0].message.content.strip()
    print(result)
    question_part,answer_part=result.split(" | ")
    print(question_part)
    print(answer_part)
    question=question_part.replace("Question: ","").strip()
    answer=answer_part.replace("Answer: ","").strip().lower()
    print(question)
    print(answer)
    lbl.configure(text=question)



yes=Button(window,text="Yes",command=lambda:check("yes"))
yes.place(x=285,y=50)
no=Button(window,text="No",command=lambda:check("no"))
no.place(x=286,y=100)
generate_questions()




window.mainloop()