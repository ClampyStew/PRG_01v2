
path = '[PATH]'

def read_snacks_file(filename):
    """Read snacks and their prices from the file and return two separate lists:
    one for names and one for prices."""
    snack_names = []
    snack_prices = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                if line.strip():  # check that line is not empty
                    name, price = line.strip().split(',')
                    snack_names.append(name)
                    snack_prices.append(float(price))
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    return snack_names, snack_prices


def get_valid_budget():
    """Prompt the user for a valid snack budget (greater than 0)."""
    while True:
        try:
            budget = float(input("Enter your snack budget: "))
            if budget <= 0:
                print("Your budget is too low! Try asking the office for a raise.")
            else:
                return budget
        except ValueError:
            print("Please enter a valid number.")


def classify_snack(price):
    """Classify the snack into a category based on its price."""
    if price < 2.0:
        return "Healthy snack"
    elif 2.0 <= price <= 5.0:
        return "Snack of the Gods"
    else:
        return "Luxury snack"


# Main program starts here
#Read the snacks from the file
snack_names, snack_prices = read_snacks_file(path+"snack_price.txt")

# If file is empty or no data, exit
if not snack_names or not snack_prices:
    print("No snack data found. Exiting program.")
    exit()

#Get the snacks budget
budget = get_valid_budget()

# Check if budget is below the cheapest item
if budget < min(snack_prices):
    print("Your budget is too low for any snacks. Try asking the office for a raise.")
    exit()

# Find affordable snacks
affordable_snacks = []
for name, price in zip(snack_names, snack_prices):
    if price <= budget:
        affordable_snacks.append((name, price))

# Print results
print("Here’s what you can buy:")
for name, price in affordable_snacks:
    category = classify_snack(price)
    print(f"- {name} (${price:.2f}) - {category}")

# Save to snack_list.txt
with open(path + "snack_list.txt", "w") as file:
    for name, price in affordable_snacks:
        file.write(f"{name},{price:.2f}\n")

print("Your snack list has been saved to 'snack_list.txt'.")
