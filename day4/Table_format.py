Students = {4: {"name":"Aashish Sah","cgpa":7.49,"dept":"CSE","gen":"Male"},
            5: {"name":"Dikshya Singh","cgpa":7.9,"dept":"CSE","gen":"Female"},
            6: {"name":"Priya","cgpa":9.5,"dept":"CE","gen":"Female"},
            7: {"name":"Aabhash","cgpa":8.49,"dept":"IT","gen":"Male"},
            8: {"name":"uzi","cgpa":6.49,"dept":"IOT","gen":"Male"},
            9: {"name":"Avi","cgpa":9.2,"dept":"CSD","gen":"Male"}
            }
print("-"*55)
print("| {:<5} | {:<15} | {:<7} | {:<7} | {:<7}|".format("ID","NAME","CGPA","DEPT","GENDER"))
print("-"*55)

for id, info in Students.items():
    print("| {:<5} | {:<15} | {:<7} | {:<7} | {:<7}|".format((id),info["name"],info["cgpa"],info["dept"],info["gen"]))
    print("-"*55)

    