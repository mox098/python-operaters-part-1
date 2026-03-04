# 1) Ask the user to enter marks for 4 subjects: math, english, science, and hindi.
english=int(input("enter marks for english"))
maths=int(input("enter marks for maths"))
science=int(input("enter marks for science"))
geography=int(input("enter marks for geography"))
# Store each mark in its own variable.

# 2) Add all 4 subject marks and store the total in `sum`.
sum=english+maths+science+geography
# 3) Print the total marks stored in `sum`.
print("the sum is ",sum)
# 4) Calculate the percentage:

# - Divide `sum` by 400 (total maximum marks for 4 subjects, assuming each is out of 1
abc=(sum/400)*100
# - Multiply the result by 100

# Store the final value in `perc`.

# 5) Print the percentage stored in `perc`.
print("the percentage is",abc)