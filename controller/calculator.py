class DemoController:

    def addition(self,num1,num2):
        if type(num1) == int and type(num2) == int:
            if num1<0 or num2<0:
                return "Only +ve numbers are required"
            else:
                result = num1 + num2
                return result
        else:
            raise Exception("Invalid Params")


    def authentication(self,username,password):
        if username and password:
            if len(username)>=4 and len(password)>=4:
                if username == "Yogesh" and password=="Yogesh123":
                    return "Login Successful..!"
            else:
                raise Exception("Invalid Length Username/Password")
        else:
            raise Exception("Invalid Username and Password")
