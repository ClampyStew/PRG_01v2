
path = '[PATH]'

def calculate_ingredient_score(ingredients):
    score = 0
    for item in ingredients:
        item_lower = item.strip().lower()
        if item_lower == "sugar":
            score += 5
        elif item_lower == "butter":
            score += 4
        elif item_lower == "chocolate chips":
            score += 3
        elif item_lower == "flour":
            score -= 2
        else:
            score += 1
    return score

def main_cookielist(filename):
    with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(', ')
                if len(parts) < 2:
                    continue
                cookie_name = parts[0]
                ingredients = parts[1:]
                score = calculate_ingredient_score(ingredients)
                print(f"Cookie: {cookie_name}")
                print(f"Score: {score}")
                if score < 5:
                    print("This cookie is a disaster!")
                elif 5 <= score <= 15:
                    print("This cookie is mediocre, but we’re not judging.")
                else:
                    print("This cookie deserves a gold medal.")



while True:
        user_input = input("Would you like to score some cookies? (Type 'Stop' to quit, 'Yes' to start): ")
        if user_input.strip().lower() == "stop":
            print("Goodbye!")
            break
        else:
            main_cookielist(path+'ingredients.txt')