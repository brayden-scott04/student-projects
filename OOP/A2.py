from abc import ABC, abstractmethod
from datetime import date

def round_nearest_10cents(amt):
    return round(amt * 10) / 10

class Session(ABC): 
    __session_id = 1

    def __init__(self, patient, duration, base_rate):
        self.session_id = Session.__session_id
        Session.__session_id += 1
     
        self.__patient = patient
        self.__duration = duration
        self.__base_rate = base_rate
    
    @abstractmethod
    def calculate_cost(self):
        pass

    def _get_patient(self):
        return self.__patient
    
    def _get_duration(self):
        return self.__duration
    
    def _get_base_rate(self):
        return self.__base_rate
    

class GeneralTherapy(Session):
    def __init__(self,patient,duration,base_rate,focus_area):
        super().__init__(patient, duration, base_rate)
        self.__focus_area = focus_area
    
    def calculate_cost(self):
        cost = self._get_base_rate() * (self._get_duration()/ 30)
        if self._get_patient().getAge() >= 60:
            cost *= 0.8
        return round_nearest_10cents(cost)
    

class SportsInjury(Session):
    def __init__(self, patient, duration, base_rate, sport_type, injury_severity, pro_athlete = False):
        super().__init__(patient, duration, base_rate)
        self.__sport_type = sport_type
        self.__injury_severity = injury_severity
        self.__pro_athlete = pro_athlete

    def calculate_cost(self):
        cost = self._get_base_rate() * (self._get_duration() / 30)
        if self.__pro_athlete: 
            cost *= 0.2
        if self._get_patient().getAge() >= 60:
            cost *= 0.8
        return round_nearest_10cents(cost)
    

class PostSurgeryRehab(Session):
    def __init__(self,patient, duration, base_rate, surgery_type):
        super().__init__(patient, duration, base_rate)
        self.__surgery_type = surgery_type

    def calculate_cost(self):
        cost = self._get_base_rate() * (self._get_duration() / 30)
        cost *= 1.15
        if self._get_patient().getAge() >= 60:
            cost *= 0.8
        return round_nearest_10cents(cost)
    

class PaediatricTherapy(Session):
    def __init__(self, patient, duration, base_rate, guardian_name):
        super().__init__(patient, duration, base_rate)
        self.__guardian_name = guardian_name

    def calculate_cost(self):
        cost = self._get_base_rate() * (self._get_duration() / 30) 
        cost *= 0.9
        return round_nearest_10cents(cost)
    

class Patient:

    __next_id = 1
    def __init__(self, name, birthdate):
        self.__patient_id = Patient.__next_id
        Patient.__next_id += 1
        self.__name = name
        self.__birthdate = birthdate

    def getAge(self):
        today = date.today()
        years = today.year - self.__birthdate.year
        if (today.month, today.day) < (self.__birthdate.month, self.__birthdate.day):
            years -= 1
        return years
    
    @property
    def patient_id(self):
        return self.__patient_id

    def __str__(self):
        return f"Patient(id:{self.__patient_id}, name:{self.__name}, age:{self.getAge()})"
    
        
class ClinicBookingSystem:
    def __init__(self):
        self.__patients = {}
        self.__sessions = {}

    def add_patient(self, name, birthdate):
        new_patient = Patient(name, birthdate)
        pid = new_patient.patient_id #pid stands for patient id
        self.__patients[pid] = new_patient
        self.__sessions[pid] = []
        return pid

    def get_patient(self, patient_id):
        return self.__patients.get(patient_id, False)
    
    def get_sessions(self, patient_id=None):
        if patient_id is None or patient_id not in self.__patients:
            return False
        return self.__sessions.get(patient_id, [])

    def book_session(self, session_type, patient_id, duration, base_rate, **booking_args):
        patient = self.get_patient(patient_id)
        if not patient:
            return False
     
        if not (isinstance(duration, int) and duration > 0 and duration % 30 == 0): # dur can't be 0 or not multiple of 30
            return False
        
        session = None

        if session_type == "General":
            if "focus_area" not in booking_args:
                return False
            session = GeneralTherapy(patient, duration, base_rate, booking_args['focus_area'])

        elif session_type == "Sports":
            required_info = ["sport_type", "injury_severity", "pro_athlete"]
            if not all(key in booking_args for key in required_info): #check if in book args
                return False
            session = SportsInjury(patient,duration, base_rate, 
                                   booking_args["sport_type"], 
                                   booking_args["injury_severity"], 
                                   booking_args["pro_athlete"])
        
        elif session_type == "PostSurgery":
            if "surgery_type" not in booking_args:
                return False
            session = PostSurgeryRehab(patient,duration, base_rate, 
                                       booking_args["surgery_type"])
        
        elif session_type == "Paediatric":
            if patient.getAge() > 18:
                return False
            if "guardian_name" not in booking_args:
                return False
            session = PaediatricTherapy(patient, duration, base_rate, 
                                        booking_args["guardian_name"])
        
        else:
            return False
        
        self.__sessions[patient_id].append(session)
        return True