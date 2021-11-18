class Demo:
    def DemoMethod(self):
     print("This is from Demo class")

class User:
    def UserMethod(self):
       print("This is from User class")

class Info(Demo,User):
    def InfoMethod(self):
        print("This is from Info class")        


i=Info()
i.DemoMethod()
i.UserMethod()
i.InfoMethod()