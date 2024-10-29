user_set_1 = {"Rahim","Karim", "Rahat"} #set of student name
user_set_2 = {"Fahim" ,"Sayem", "Rahat"} #set of student name

intersection_set = user_set_1.intersection(user_set_2) #set of student name available in both sets only
diff_set = user_set_1.symmetric_difference(user_set_2) #set of student name available in both sets without duplicates

print("Intersection: ",intersection_set) #showing results
print("Difference: ", diff_set) #showing results