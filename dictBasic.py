#Dictionary basics
student={
      "name" :"Annie",
      "city" :"Bhubneswar",
      "Age":17,
      "Roll no.":1,
      "name":"Mani",
}

print(type(student))
print(student["name"])
print(student)
print(student["city"])
student["city"]="tokyo"
print(student)
student["fAV SUBJECT"]="Chemistry"
print(student)
student.pop("Roll no.")
print(student)
print(student.keys)