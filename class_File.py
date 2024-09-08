class manyFun:
    def Subfields():
        subDomain_list=['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Neutral Language Processing']
        print("Sub-fields in AI are:")
        for item in subDomain_list:
            print(item)
    def OddEven():
        num=int(input("Enter Number"))
        if(num%2==1):
            print(num,"is Odd Number")
        else:
            print(num,"is Even Number")
    def Elegible():
        gender=input("Enter gender")
        age=int(input("Enter age"))
        if(gender=="male"):
            if(age>=21):
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        elif(gender=="female"):
            if(age>=18):
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        else:
            print("valid input")
    def percentage():
        marks=list(map(int,input("Enter your marks").split(" ")))
        Total=0
        j=1
        for i in marks:
            print(f"Subject{j}={i}")
            Total+=i
            j=j+1
        print(f"Total:{Total}")
        print(f"Percentage:{Total/5}")
    def triangle():
        height=int(input("Enter height"))
        base=int(input("Enter base"))
        side1=int(input("Enter side one"))
        side2=int(input("Enter side two"))
        side3=int(input("Enter side three"))
        area=(height*base)/2
        perimeter=side1+side2+side3
        print("Area of Triangle:",area)
        print("Perimeter of Triangle:",perimeter)

