def calculate_bmi(height, weight):
    """
    Calculate BMI using formula: weight (kg) / height (m)^2
    """
    return weight / ((height / 100) ** 2)


def bmi_category(bmi):
    """
    Classify BMI into categories
    """
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def calculate_calories(weight, height, age, goal):
    """
    Estimate daily calorie needs using BMR formula
    """
    # Mifflin-St Jeor Equation (approx for males)
    bmr = 10 * weight + 6.25 * height - 5 * age + 5

    if goal == "loss":
        return int(bmr - 500)   # calorie deficit
    elif goal == "gain":
        return int(bmr + 500)   # calorie surplus
    else:
        return int(bmr)         # maintenance


def diet_recommendation(goal):
    """
    Provide Indian diet suggestions based on goal
    """
    if goal == "loss":
        return (
            "Oats, dal, roti, green vegetables, fruits, "
            "low oil sabzi, buttermilk"
        )
    elif goal == "gain":
        return (
            "Paneer, rice, dal, roti, banana shake, "
            "peanut butter, milk, eggs"
        )
    else:
        return (
            "Balanced diet: roti, dal, vegetables, fruits, "
            "milk, and moderate protein"
        )
