# Function to calculate ticket price based on distance and class
def calculate_ticket_price(distance, travel_class):
    base_price_per_km = 0.1  # Base price per kilometer
    class_multiplier = 1  # Default multiplier for economy class

    # Adjust multiplier for different travel classes
    if travel_class == "business":
        class_multiplier = 1.5
    elif travel_class == "first":
        class_multiplier = 2

    # Calculate total price
    total_price = base_price_per_km * distance * class_multiplier
    return round(total_price, 2)  # Round to 2 decimal places

# Example usage
distance = 500  # Distance in kilometers
travel_class = "economy"  # Travel class: "economy", "business", or "first"
total_price = calculate_ticket_price(distance, travel_class)
print("Total ticket price: $" + str(total_price))
