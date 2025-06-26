from models.status_enum import Status


class Agent:
    def __init__(self,code_name,real_name,location,status : Status,missions_completed,id=None):
        self.__id = id
        self.__code_name = code_name
        self.__real_name = real_name
        self.__location = location
        self.__status = status
        self.__missions_completed = missions_completed
    #id
    @property
    def id(self):
        return self.__id

    #code_name
    @property
    def code_name(self):
        return self.__code_name

    @code_name.setter
    def code_name(self,new_code_name):
        self.__code_name = new_code_name

    #real_name
    @property
    def real_name(self):
        return self.__real_name

    @real_name.setter
    def real_name(self, new_real_name):
        self.__real_name = new_real_name

    #location
    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, new_location):
        self.__location = new_location

    #status
    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, new_status : Status ):
        self.__status = new_status

    #missions_completed
    @property
    def missions_completed(self):
        return self.__missions_completed

    @missions_completed.setter
    def missions_completed(self, new_missions_completed):
        self.__missions_completed = new_missions_completed



    def __str__(self):
        return f"claas name: {self.__class__.__name__}.\ncode name: {self.__code_name}.\nreal name: {self.__real_name}.\nstatus: {self.__status.value}.\nlocation: {self.__location}.\nmissions_Completed: {self.__missions_completed}."



# a = Agent("a", "Moshe", "usa", Status.ACTIVE, 5)
#
# print(a)