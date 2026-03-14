import datetime

class Trainee:
    def __init__(self,trainee_id,name,birthdate,email):
        self.__trainee_id = trainee_id
        self.__trainee_name = name
        self.__birthdate = birthdate
        self.__email = email
        self.__age = None
    
    def get_age(self):
        today = datetime.date.today()
        age = today.year - self.__birthdate.year
        if (today.month, today.day) <(self.__birthdate.month, self.__birthdate.day):
            age -= 1
        self.__age = age
        return self.__age
    

    def __str__(self):
        age_disp = self.get_age()
        date_str = f'{self.__birthdate.year}-{self.__birthdate.month}-{self.__birthdate.day}'
        return f"Trainee(id:{self.__trainee_id}, name:{self.__trainee_name}, birthdate:{date_str}, email=:{self.__email}, age:{age_disp})"


class Trainer:
    def __init__(self,trainer_id,name):
        self.__trainer_id = trainer_id
        self.__trainer_name = name
    
    def __str__(self):
        return f"Trainer(id:{self.__trainer_id}, name:{self.__trainer_name})"



class ExerciseSession:
    def __init__(self, session_id, trainer_id, trainee_id, duration, intensity, date):
        self.__session_id = session_id
        self.__trainer_id = trainer_id
        self.__trainee_id = trainee_id
        self.__duration = duration
        self.__intensity = intensity
        self.__date = date

    
    def __str__(self):
        date_str = f'{self.__date.year}-{self.__date.month}-{self.__date.day}'
        return f"ExerciseSession(id:{self.__session_id}, trainer_id:{self.__trainer_id}, trainee_id:{self.__trainee_id}, duration:{self.__duration} min, intensity:{self.__intensity}, date:{date_str})"
    


class PersonalTrainingManagementSystem:
    def __init__(self, trainers = None, trainees = None, sessions = None):
        self.__trainers = trainers if trainers is not None else []
        self.__trainees = trainees if trainees is not None else []
        self.__sessions = sessions if sessions is not None else []

    
    def add_trainer(self,ID,name):
        if self.get_trainer(ID) is False: #this helps to avoid duplicates, false meaning it doesn't exist yet
            trainer = Trainer(ID, name)
            self.__trainers.append(trainer)
            return True
        return False 

    def add_trainee(self,ID, name, birthdate, email):
        if self.get_trainee(ID) is False: #again avoids duplicates
            trainee = Trainee(ID, name, birthdate, email)
            self.__trainees.append(trainee)
            return True
        return False
    
    def create_session(self,ID,trainer_id, trainee_id, duration,intensity,date):
        if self.get_session(ID) is False: #avoids duplicate sessions
            session = ExerciseSession(ID, trainer_id, trainee_id, duration, intensity, date)
            self.__sessions.append(session)
            return True
        return False
    
    def get_trainer(self,trainer_id):
        for trainer in self.__trainers:
            if trainer._Trainer__trainer_id == trainer_id:
                return trainer
        return False
    
    def get_trainee(self, trainee_id):
        for trainee in self.__trainees:
            if trainee._Trainee__trainee_id == trainee_id:
                return trainee
        return False
    
    def get_session(self, session_id):
        for session in self.__sessions:
            if session._ExerciseSession__session_id == session_id:
                return session
        return False
    
    def get_trainee_total_duration(self,trainee_id):
        total_dur = 0 #total duration set to 0 first

        for session in self.__sessions:
            if session._ExerciseSession__trainee_id == trainee_id:
                total_dur += session._ExerciseSession__duration

        return total_dur
    
    
    def get_trainee_ave_intensity(self,trainee_id):
        count = 0 #to count number of sessions
        total_intensity = 0 #add total intensity to later divide by count 

        for session in self.__sessions:
            if session._ExerciseSession__trainee_id == trainee_id:
                count += 1
                total_intensity += session._ExerciseSession__intensity
        
        return round((total_intensity/count),2) if count > 0 else 0
    
    
    def get_trainer_total_duration(self, trainer_id): 
        tot_duration = 0

        for session in self.__sessions:
            if session._ExerciseSession__trainer_id == trainer_id:
                tot_duration += session._ExerciseSession__duration
        
        return tot_duration
    
    def get_trainer_total_duration_with_trainee(self, trainer_id, trainee_id):
        total_duration = 0

        for session in self.__sessions:
            if session._ExerciseSession__trainer_id == trainer_id and session._ExerciseSession__trainee_id == trainee_id:
                total_duration += session._ExerciseSession__duration

        return total_duration
    
    def remove_session(self, session_id):
        for i, session in enumerate(self.__sessions): #assignin index to each as it goes down list
            if session._ExerciseSession__session_id == session_id: 
                del self.__sessions[i]
                return True
            
        return False #means that session wasn't found..