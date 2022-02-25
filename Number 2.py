start = input("How old were you on the start date?")
end = input("How old are you today?")
# Converting string to integer for the formula
start = int(start)
end = int(end)
# Years of service variable to know how many years the employee worked for the company
yearsOfService = (end - start)
# Print of congratulatory message
print("Happy birthday and congratulations on turning " + str(end) +
      ".\nThank you for " + str(yearsOfService) + " years of awesome service!")