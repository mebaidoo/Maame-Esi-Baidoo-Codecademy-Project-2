# Create calculate_insurance_cost() function below: 
def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
  output_message = "The estimated insurance cost for " + name + " is " + str(estimated_cost) + " dollars."
  print (output_message)
  return output_message
  return estimated_cost

# Estimate Maria's insurance cost
maria_insurance_cost = calculate_insurance_cost("Maria", 28, 0, 26.2, 3, 0)

# Estimate Omar's insurance cost 
omar_insurance_cost = calculate_insurance_cost("Omar", 35, 1, 22.2, 0, 1)

#Estimating Maame Esi's insurance cost
maame_esi_insurance_cost = calculate_insurance_cost("Maame Esi", 23, 0, 18.5, 0, 0)

# Creating a function to calculate the difference between insurance costs of any two individuals
def calculate_difference(name1, insurance_cost1, name2, insurance_cost2):
  print("The difference in insurance cost between " + name1 + " and " + name2 + " is " + str(insurance_cost1 - insurance_cost2) + " dollars.")

# Calculating the difference in insurance cost between Maria and Omar
maria_and_omar_difference = calculate_difference("Omar", 28336.0, "Maria", 5469.0)
