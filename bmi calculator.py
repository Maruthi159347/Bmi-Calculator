def calculate_bmi(weight, height_meters):
    return weight / (height_meters ** 2)

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("=" * 40)
    print("        BMI CALCULATOR")
    print("=" * 40)

    while True:
        try:
            weight = float(input("Enter your weight (in kg): "))
            height_feet = float(input("Enter your height (in feet, e.g., 5.3): "))

            if weight <= 0 or height_feet <= 0:
                print("⚠ Please enter positive values only.\n")
                continue

            # Convert feet to meters
            height_meters = height_feet * 0.3048

            bmi = calculate_bmi(weight, height_meters)
            category = categorize_bmi(bmi)

            print("\n--- RESULT ---")
            print(f"Your BMI: {bmi:.2f}")
            print(f"Category: {category}")
            print("-" * 20)

        except ValueError:
            print("⚠ Invalid input! Please enter numeric values.\n")
            continue

        again = input("Do you want to calculate again? (yes/no): ").lower()
        if again != "yes":
            print("\nThank you for using the BMI Calculator!")
            break

if __name__ == "__main__":
    main()
