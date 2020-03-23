class Examinee:
		#Private variables
    __Name= None
    __Address= None
    __Ph_Number= None
    __Course= None

    def set_Name(self, Value):
        try:
            if(type(Value)==int):
                self.__Name=Value
            else:
                print('enter string value')
                
        except Exception as error:
            print(error)
    def get_Name(self):
        return self.__Name

    def set_Address(self, Value):
        self.__Address=Value

    def get_Address(self):
        return self.__Address

    def set_Ph_Number(self, Value):
        self.__Ph_Number=Value

    def get_Ph_Number(self):
        return self.__Ph_Number

    def set_Course(self, Value):
        self.__Course=Value

    def get_Course(self):
        return self.__Course

    def Display(self):

        return f'Examinee name is {self.__Name}\n Examinee address is {self.__Address}\n Examinee Ph_Number is {self.__Ph_Number}\nCourse is{self.__Course} '

    def __Private_Method(self):
        print('This is Private Method')
    def get_Method(self):
        return self.__Private_Method()


class Teacher(Examinee):
    __salary= None

    def set_Salary(self, Value):
        self.__salary=Value

    def get_Salary(self):
        return self.__salary


#Create Object of class
Student1=Examinee()
Student1.set_Name(input('Enter your name\n'))
Student1.set_Address(input('Enter your address\n'))
Student1.set_Ph_Number(input('enter your Number\n'))
Student1.set_Course(input('ENter your course\n'))

obj=Examinee()


print(Student1.Display())

