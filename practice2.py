#define a function message(text="Keep learning!") and call it with and without Arguments.
def message(text="Keep learning!"):
    print(text)

message()
message("Python is fun!")
#creat a function login(Username , password="1234") that prints the credentials.
def login(Username , password="1234"):
    print("Username:",Username)
    print("password:",password)

login("Annie")
login("Annie",591531)
#Local VS Global
def show():
    score=50
    print(score)
show()
#global variable
score=159
def show():
    print(score)
show()
#Global keywords wala question
score=59
def change_score():
    global score
    score=99
change_score()
print(score)
#write a program with a local variable score inside a function and a global one outside.
score=99
def game():
    score=50
    print("Local score:",score)
game()
print("Global:",score)
