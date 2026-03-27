def calculate_bmi(height, weight):
    return weight / ((height / 100) ** 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def calculate_calories(weight, height, age, goal):
    # Simple BMR (Mifflin-St Jeor approx)
    bmr = 10 * weight + 6.25 * height - 5 * age + 5

    if goal == "loss":
        return int(bmr - 500)
    elif goal == "gain":
        return int(bmr + 500)
    else:
        return int(bmr)

def diet_recommendation(goal):
    if goal == "loss":
        return "Low calorie, high protein diet"
    elif goal == "gain":
        return "High protein, high calorie diet"
    else:
        return "Balanced diet with moderate calories"
