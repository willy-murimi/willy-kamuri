print("please enter the dimensions of the room in sqft")

def calculate_area(length, width):
      area_sqft = length * width
      print(f"The total sqft is: {area_sqft}")



length = int(input("Enter the length of the object: "))
width = int(input("Enter the width of the object: "))
calculate_area(length, width)


#password encryption program
student_grade = {}

off = False
while not off:
    name = input("Enter student name: ")
    grade = input("Enter student grade: ")
    student_grade[name] = grade
    print("student added successfully")
    print(student_grade)
    add_another = input("would you like to add another students? Y or N").lower()
    if add_another == "Y":
        pass
    else:
        off = True


from bs4 import BeautifulSoup
def get_page(url):
    response = request.get(url)
    soup = BeautifulSoup(response.content, 'html parser')
    print(soup.a) #a for anchor tags .find .find all

get_page(input("what url would you like to scrap"))
