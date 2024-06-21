class car:
    def company(self):
        while True:
            print("Toyota, Mercedes")
            self.n = input("enter the car company: ")
            if self.n == "Toyota":
              print("welcome to toyoto")
              self.models()
              break
            elif self.n=="Mercedes":
              print("welcome to meet")
              self.models()
              break
            else:
              print("enter valid company") 
    def models(self):
         if self.n == "Toyota":
            while True:
               print("select from fortuner and LC")
               self.choice = input("enter the car model: ")
               if self.choice == "fortuner":
                  self.price(self.choice)
                  break
               elif self.choice=="LC":
                  self.price(self.choice) 
                  break
               else:
                  print("enter valid")
         elif self.n=="Mercedes":
            while True:
               print("select from amg and gw")
               self.choice = input("enter the car model")
               if self.choice == "amg":
                  self.price(self.choice) 
                  break
               elif self.choice=="gw":
                  self.price(self.choice) 
                  break
               else:
                  print("enter valid")
    def price(self,choice):
        self.cgst = 5555
        self.sgst = 5555
        self.insurance = 5555
        if choice=="Fortuner":
            self.p = 4500000
        elif choice=="LC":
            self.p = 1000000
        elif choice=="amg":
            self.p = 24432874
        elif choice=="gw":
            self.p = 843726837 
        tot_p = self.p + self.sgst + self.cgst + self.insurance 
        print(tot_p)

c = car()
c.company()