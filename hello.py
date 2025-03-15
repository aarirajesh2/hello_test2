import datetime

def greet_user(name, location, date):
    """Greets the user with their name, location, and the current date."""
    print(f"Hello, {name}!")
    print(f"Today is {date.strftime('%A, %B %d, %Y')}")
    print(f"You are currently in {location}.")

# Get the user's name (you can hardcode this for a simple example)
user_name = input("Rajesh? ")

# Set the location and date
location = "Bengaluru, Karnataka"
current_date = datetime.date(2025, 3, 15)

# Call the greeting function
greet_user(user_name, location, current_dat)
