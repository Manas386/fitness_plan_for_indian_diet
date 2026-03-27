import model

def main():
    print("🏋️ Fitness & Diet Recommendation System\n")

    age = int(input("Enter your age: "))
    height = float(input("Enter your height (cm): "))
    weight = float(input("Enter your weight (kg): "))
    goal = input("Enter your goal (loss/gain/maintain): ").lower()

    bmi = model.calculate_bmi(height, weight)
    category = model.bmi_category(bmi)
    calories = model.calculate_calories(weight, height, age, goal)
    diet = model.diet_recommendation(goal)

    print("\n📊 Results:")
    print(f"BMI: {bmi:.2f}")
    print(f"Category: {category}")
    print(f"Recommended Calories: {calories} kcal/day")
    print(f"Diet Suggestion: {diet}")

if __name__ == "__main__":
    main()
