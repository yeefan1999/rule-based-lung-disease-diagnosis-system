from tkinter import *
from tkinter import filedialog
import clips
import re


class Application:
    
    def __init__(self,window,env):
        self.window=window
        # the title of the application
        self.window.title('Common Lung Disease Diagnosis')
        self.env = env
        
        # to show the main title
        canvas = Canvas(window)
        canvas.pack()
        canvas_text = canvas.create_text(10,50, text='',font=(None,15),anchor='nw')

        welcome_string = "Common Lung Disease Diagnosis System"
        delta=100
        delay=0

        for i in range(len(welcome_string)+1):
            s = welcome_string[:i]
            # it will configure the text in canvas declared before
            update_text= lambda s=s: canvas.itemconfigure(canvas_text, text=s)
            # the canvas will update the text after the delay
            canvas.after(delay,update_text)
            # each word will slower 100 than the previous
            delay+=delta

        # the button will appear in the window after 4500ms
        self.window.after(4500,self.initial_button)
        

    # home page button
    def initial_button(self):
        self.initial = Button(text="Get started",width='20',height="5",command=self.infowindow,font=(None,12))
        self.initial.pack()
    
    def initial_page(self):
        for self.widget in self.window.winfo_children():
            self.widget.destroy()

        home_button = Button(self.window, text="Home",command=self.menu)
        home_button.pack(side=TOP,pady=10,padx=20,anchor='e')

        canvas = Canvas(self.window)
        canvas.pack()
        canvas_text = canvas.create_text(10,50, text='Common Lung Disease Diagnosis System',
                                         font=(None,15),anchor='nw')
    # the page for signing up information
    def infowindow(self):

        # function to check all the entries all peoperly filled
        def checkfunc(*args):
            self.gender = self.gender_var.get()
            self.name = self.name_var.get()
            self.age = self.age_var.get()

            if self.gender and self.name and self.age.isdigit():
                self.submit.config(state='normal')

            else:
                self.submit.config(state='disabled') 

        # to destroy all the widget in the previous window
        for self.widget in self.window.winfo_children():
            self.widget.destroy()

        # the title
        canvas = Canvas(self.window)
        canvas.pack()
        canvas_text = canvas.create_text(10,50, text='Common Lung Disease Diagnosis System',
                                         font=(None,15),anchor='nw')

        self.info_label = Label(text="Please sign up your information here")
        self.info_label.pack(side=TOP)

        self.name_var = StringVar(self.window)
        self.age_var = StringVar(self.window)
        self.gender_var = StringVar(self.window)

        # this will trace with the checkfunc function to check
        self.name_var.trace("w",checkfunc)
        self.age_var.trace("w",checkfunc)
        self.gender_var.trace("w",checkfunc)

        # name instruction label and field to get the name entry
        self.name_label = Label(text='Please enter your name')
        self.name_label.pack(padx=10,pady=10)
        self.name_entry = Entry(self.window,width=15, textvariable=self.name_var)
        self.name_entry.pack(padx=10,pady=10)

        # to enter the age
        self.age_label = Label(text='Please enter your age (Number only)')
        self.age_label.pack(padx=10,pady=10)
        self.age_entry = Entry(self.window,width=15, textvariable=self.age_var)
        self.age_entry.pack(padx=10,pady=10)

        # to choose the gender
        self.choice = ('M','F')
        self.gender_label = Label(text='Please choose your gender')
        self.gender_label.pack(padx=10,pady=10)
        self.option = OptionMenu(self.window,self.gender_var,*self.choice)
        self.option.pack()

        # submit and pass the value to the next 
        self.submit = Button(text='Submit',command=self.menu)
        self.submit.pack(pady=20)
        self.submit.config(state='disabled')
        
    # the function which shows the options for the user
    def menu(self):

        # the clips facts will be reset everytime the user return to menu page        
        self.env.reset()

        # destroy all the previous window widget
        for self.widget in self.window.winfo_children():
            self.widget.destroy()

        canvas = Canvas(self.window)
        canvas.pack()
        canvas_text = canvas.create_text(10,50, text='Common Lung Disease Diagnosis System',
                                         font=(None,15),anchor='nw')

        # assert the fact into clips
        fact = "(person (name "+self.name+") (age "+self.age+") (gender "+self.gender+"))"
        self.env.assert_string(fact)

        self.option_label = Label(text="Please choose to perform on any of the follow:",font=(None,15))
        self.option_label.pack()

        self.option1 = Button(text='Diagnosis based on symptom',height=5,width=40,font=(None,12),command=self.diagnose_symptom)
        self.option1.pack(side=LEFT,padx=10)

        self.option2 = Button(text='Diagnosis based on disease',height=5,width=40,font=(None,12),command=self.diagnose_disease)
        self.option2.pack(side=RIGHT,padx=10)

    # to choose the symptoms
    def diagnose_symptom(self):
        
        self.initial_page()
        
        first_symptom_label = Label(text='Please choose the symptoms you faced recently',font=(None,15)).place(x=170,y=200)
        
        symptom_one = Button(text='Shortness of breath\nFrequent coughing',height=10,width=25,font=(None,10),command=lambda: self.assert_symptom_one('one')).place(x=70,y=300)
        
        symptom_two = Button(text='Sharp / Stabbing Chest Pain \n Bluish skin \n Rapid breathing',command=lambda:self.assert_symptom_one('two'),height=10,width=25,font=(None,10)).place(x=300,y=300)
        
        symptom_three = Button(text='Common cold\nRunny nose\nLoss of appetitte\n Wheezing',command=lambda:self.assert_symptom_one('three'),height=10,width=25,font=(None,10)).place(x=530,y=300)
        
        symptom_four = Button(text='Chronic cough \nCyanosis (bluish skin)\nFatigue\nWheezing',command=lambda:self.assert_symptom_one('four'),height=10,width=25,font=(None,10)).place(x=70,y=500)
        
        symptom_five = Button(text='Chest Pain \n Shortness of breath \n Blood / Frequent coughing',command=lambda:self.assert_symptom_one('five'),height=10,width=25,font=(None,10)).place(x=300,y=500)
        
        none_above = Button(text='None of the above',height=10,width=25,font=(None,10),command=self.none_above).place(x=530,y=500)

   # to choose the disease
    def diagnose_disease(self):
        
        self.initial_page()
        
        first_symptom_label = Label(text='Please choose the disease you want to check on',font=(None,15)).place(x=170,y=200)
        
        symptom_one = Button(text='Asthma',height=10,width=25,font=(None,10),command=lambda: self.assert_disease('one')).place(x=70,y=300)
        
        symptom_two = Button(text='Pneumothorax',command=lambda:self.assert_disease('two'),height=10,width=25,font=(None,10)).place(x=300,y=300)
        
        symptom_three = Button(text='Bronchiolitis',command=lambda:self.assert_disease('three'),height=10,width=25,font=(None,10)).place(x=530,y=300)
        
        symptom_four = Button(text='Chronic Obsturctive\nPulmonary Disease\n(COPD)',command=lambda:self.assert_disease('four'),height=10,width=25,font=(None,10)).place(x=70,y=500)
        
        symptom_five = Button(text='Lung Cancer',command=lambda:self.assert_disease('five'),height=10,width=25,font=(None,10)).place(x=300,y=500)
        
        none_above = Button(text='None of the above',height=10,width=25,font=(None,10),command=self.none_above2).place(x=530,y=500)
    
    # function to assert the symptoms into clips
    def assert_symptom_one(self,symptom_option):

        # to ask the second question regarding the symptoms
        def ques_two(option):
            
            self.initial_page()

            # assert the facts regarding the option made
            option1 = "(ques1 "+option+")"
            option1 = self.env.assert_string(option1)
            
            ques2=""

            # to look for facts for the question 2 to be asked to the user
            for fact in self.env.facts():
                if str(fact).split()[0] == """(ques2""":
                    ques2 = str(fact).split()[1].split(')')[0]
                    fact.retract()
                
            second_ques = Label(text='Do you suffer from symptoms as '+re.sub('[-]',' ',ques2)+' ?',font=(None,15)).place(x=170,y=200)
            yes = Button(text='Yes',height=10,width=25,font=(None,15),command=lambda: self.result('yes')).place(x=70,y=300)
            no = Button(text='No',height=10,width=25,font=(None,15), command=lambda: self.result('no')).place(x=400,y=300)
            
        self.initial_page()
        
        symptom_fact1 = "(choose option-"+symptom_option+')'
        symptom_fact = self.env.assert_string(symptom_fact1)
        
        ques1=""
        
        self.env.activations()
        self.env.refresh()
        self.env.run(limit=None)

        # to look for facts to be asked to the user
        for fact in self.env.facts():
            if str(fact).split()[0] == """(ques1""":
                ques1 = str(fact).split()[1].split(')')[0]
                fact.retract()

        first_ques = Label(text='Do you suffer from symptoms as '+re.sub('[-]',' ',ques1)+' ?',font=(None,15)).place(x=170,y=200)
        yes = Button(text='Yes',height=10,width=25,font=(None,15),command=lambda: ques_two('yes')).place(x=70,y=300)
        no = Button(text='No',height=10,width=25,font=(None,15),command=lambda: ques_two('no')).place(x=400,y=300)

   # to get the disease based on the symptoms chosen
    def assert_disease(self,symptom_option):
                    
        self.initial_page()
        self.symptom_option = symptom_option
        symptom_fact1 = "(choose_disease option-"+symptom_option+')'
        symptom_fact = self.env.assert_string(symptom_fact1)
        
        ques1=""
        
        self.env.activations()
        self.env.refresh()
        self.env.run(limit=None)

        # to get the symptoms of the disease from clips
        self.symptom_staments=""
        for fact in self.env.facts():
            if len(str(fact).split('(disease_symptoms'))>1:
                self.symptom_staments = str(fact).split('(disease_symptoms ')[1]
        
        Label(text='Do you suffer from below symptoms?',font=(None,17)).place(x=80,y=180)
        i = 200
        
        if self.symptom_staments != "":
            length = len(self.symptom_staments.split(' '))

            self.symptom_staments = self.symptom_staments.split(' ')
            self.symptom_staments[-1] = self.symptom_staments[-1].split(')')[0]

            for a in range(length):
                if self.symptom_staments[a] != '' or self.symptom_staments[a] != ' ':
                    i+=30
                    self.symptom_staments[a] = re.sub("[-]"," ",self.symptom_staments[a])
                    Label(text=self.symptom_staments[a],font=(None,12)).place(x=160,y=i)

        yes = Button(text='Yes',height=8,width=25,font=(None,15),command=lambda: self.pre_result('yes')).place(x=70,y=i+50)
        no = Button(text='No',height=8,width=25,font=(None,15),command=self.none_above).place(x=400,y=i+50)

    # to assert the fact into clips to trigger the rules
    def pre_result(self,option):
        
        for fact in self.env.facts():
            pass
        fact.retract()
        for fact in self.env.facts():
            if str(fact).split()[0]=='(choose_disease':
                fact.retract()
            
        pre_result = "(disease_result option-"+self.symptom_option+')'
        pre_result = self.env.assert_string(pre_result)
        self.result(option)

    # the result page of the system
    def result(self,option):
        
        self.initial_page()
        
        option_last = "(ques2 "+option+")"
        option_last = self.env.assert_string(option_last)
        
        if(self.env.run()>=1):
            disease = ""
            
            for fact in self.env.facts():
                if len(str(fact).split('(disease'))>1:
                    disease = str(fact).split('(disease')[1]
            
            Label(text='Hi, '+self.name+'.',font=(None,15)).place(x=60,y=200)
            disease = disease.split(')')
            disease = disease[0].split()
            self.disease = re.sub('[-]',' ',disease[0])
            Label(text='Based on your symptoms, we suspect it is '+self.disease.capitalize()+'.',font=(None,15)).place(x=60,y=250)
            
            
            intro = ""
            for fact in self.env.facts():
                if str(fact).split()[0] == """(intro""":
                    
                    intro = str(fact).split('(intro ')[1].split(')')[0]
            i = 250

            # to replace the hyphen in the text with space
            if intro != "":
                length = len(intro.split('.'))
                
                intro = re.sub("[-]"," ",intro)
                intro = intro.split('.')

                
                for a in range(length):
                    if intro[a] != '' or intro[a] != ' ':
                        i+=50
                        Label(text=intro[a]+'.',font=(None,12)).place(x=60,y=i)

            info = Button(text='Click to know more',height=10,width=25,font=(None,10),command=self.know_more).place(x=300,y=i+50)

        else:
            Label(text='We cant diagnose based on the symptoms.\nThe symptoms provided from you are not sufficient.\nSorry.',font=(None,15)).place(x=170,y=200)

    # the information page of the disease
    def know_more(self):
        
        self.diagnosis_statement=""
        for fact in self.env.facts():
            if len(str(fact).split('(diagnosis'))>1:
                self.diagnosis_statement = str(fact).split('(diagnosis ')[1]
        
        self.treatment_statement=""
        for fact in self.env.facts():
            if len(str(fact).split('(treatment'))>1:
                self.treatment_statement = str(fact).split('(treatment ')[1]
                
        self.causes_statement=""
        for fact in self.env.facts():
            if len(str(fact).split('(causes'))>1:
                self.causes_statement = str(fact).split('(causes ')[1]
        self.initial_page()
                
        Label(text='Click on any of the options below to know more',font=(None,15)).place(x=180,y=250)
            
        Button(text='Diagnosis',height=10,width=25,font=(None,10),command=self.diagnosis_page).place(x=70,y=350)
        
        Button(text='Treatment',height=10,width=25,font=(None,10),command=self.treatment_page).place(x=300,y=350)
        
        Button(text='Causes/\nRisk factos',height=10,width=25,font=(None,10),command=self.causes_page).place(x=530,y=350)

    # page describes the diagnosis process of the disease
    def diagnosis_page(self):
        
        self.initial_page()
        
        Label(text='Diagnosis',font=(None,17)).place(x=80,y=200)
        Label(text='How is '+self.disease.capitalize()+' diagnosed?',font=(None,15)).place(x=80,y=230)
        i = 280
        if self.diagnosis_statement != "":
            length = len(self.diagnosis_statement.split('.'))

            self.diagnosis_statement = re.sub("[-]"," ",self.diagnosis_statement)
            self.diagnosis_statement = self.diagnosis_statement.split('.')
            self.diagnosis_statement[-1] = self.diagnosis_statement[-1].split(')')[0]
            
            
            for a in range(length):
                if self.diagnosis_statement[a] != '' or self.diagnosis_statement[a] != ' ':
                    i+=50
                    Label(text=self.diagnosis_statement[a]+'.',font=(None,12)).place(x=80,y=i)
            
        Button(text='Know more',height=8,width=25,font=(None,10),command=lambda:self.know_more()).place(x=300,y=i+50)

     # page describes the disease treatment
    def treatment_page(self):

        self.initial_page()

        Label(text='Treatment',font=(None,17)).place(x=80,y=200)
        Label(text='What to do with '+self.disease.capitalize()+' ?',font=(None,15)).place(x=80,y=230)
        i = 280
        if self.treatment_statement != "":
            length = len(self.treatment_statement.split(' '))

            self.treatment_statement = self.treatment_statement.split(' ')
            self.treatment_statement[-1] = self.treatment_statement[-1].split(')')[0]

            for a in range(length):
                if self.treatment_statement[a] != '' or self.treatment_statement[a] != ' ':
                    i+=25
                    self.treatment_statement[a] = re.sub("[-]"," ",self.treatment_statement[a])
                    Label(text=self.treatment_statement[a],font=(None,12)).place(x=160,y=i)

        Button(text='Know more',height=8,width=25,font=(None,10),command=lambda:self.know_more()).place(x=300,y=i+50)

    # page describes the risk factors of the disease
    def causes_page(self):
        
        self.initial_page()
        
        Label(text='Causes / Risk Factors',font=(None,17)).place(x=80,y=200)
        Label(text='What causes '+self.disease.capitalize()+' ?',font=(None,15)).place(x=80,y=230)
        i = 280
        if self.causes_statement != "":
            length = len(self.causes_statement.split(' '))
            
            self.causes_statement = self.causes_statement.split(' ')
            self.causes_statement[-1] = self.causes_statement[-1].split(')')[0]

            for a in range(length):
                if self.causes_statement[a] != '' or self.causes_statement[a] != ' ':
                    i+=25
                    self.causes_statement[a] = re.sub("[-]"," ",self.causes_statement[a])
                    Label(text=self.causes_statement[a],font=(None,12)).place(x=160,y=i)
            
        Button(text='Know more',height=8,width=25,font=(None,10),command=lambda:self.know_more()).place(x=300,y=i+50)
        
   # page which will be shown to the user when there are no symptoms matched
    def none_above(self):
        
        self.initial_page()
        
        self.none_result = Label(text='Sorry. As no symptoms matched, this system might not \ninclude the diagnosis for your lung disease. \nWe will try to improve our system.\nTry clickcking on Home for another testing.',font=(None,15)).place(x=150,y=200)

    # page which will be shown to the user when there are no diseases matched
    def none_above2(self):
        
        self.initial_page()
        
        self.none_result = Label(text='Sorry. As no diseases matched, this system might not \ninclude the diagnosis for your lung disease. \nWe will try to improve our system.\nTry clicking on Home for another testing.',font=(None,15)).place(x=150,y=200)

# the main function to call the class
def main():
    window = Tk()
    env = clips.Environment()
    env.load('es_rules.CLP')
    env.run(limit=None)
    app = Application(window,env)
    window.geometry('800x700')
    window.mainloop()
    
if __name__ == '__main__':
    
    main()
