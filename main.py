import model

def main():
    print("🏋️ Fitness & Diet Recommendation System")
    print("----------------------------------------")

    try:
        age = int(input("Enter your age: "))
        height = float(input("Enter your height (cm): "))
        weight = float(input("Enter your weight (kg): "))
        goal = input("Enter your goal (loss/gain/maintain): ").lower()

        if goal not in ["loss", "gain", "maintain"]:
            print("❌ Invalid goal. Please enter loss/gain/maintain.")
            return

    except ValueError:
        print("❌ Invalid input. Please enter correct numeric values.")
        return

    # Calculate values
    bmi = model.calculate_bmi(height, weight)
    category = model.bmi_category(bmi)
    calories = model.calculate_calories(weight, height, age, goal)
    diet = model.diet_recommendation(goal)

    # Extra feature (for higher marks)
    protein = round(weight * 1.6)

    # Output
    print("\n📊 Your Results")
    print("----------------------------------------")
    print(f"BMI: {bmi:.2f} ({category})")
    print(f"Recommended Calories: {calories} kcal/day")
    print(f"Recommended Protein Intake: {protein} g/day")
    print(f"Diet Suggestion: {diet}")
    print("----------------------------------------")

if __name__ == "__main__":
    main()
