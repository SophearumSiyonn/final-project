import tkinter as tk
from tkinter import messagebox
import random
from liquor_data import liquor_details

# Define the main GUI application class
class LiquorRecommendationApp:
    def __init__(self, master):
        # Initialize the main window
        self.master = master
        master.title("🍹 Liquor Recommendation System 🍸")

        # Display a welcome label
        self.label = tk.Label(master, text="✨ Welcome to the Liquor Recommendation System ✨")
        self.label.pack()

        # Ask for age input
        self.age_label = tk.Label(master, text="Are you legal?? (Enter your age) 🥂")
        self.age_label.pack()

        # Age entry field
        self.age_entry = tk.Entry(master)
        self.age_entry.pack()

        # Button to check age
        self.age_button = tk.Button(master, text="Check Age", command=self.check_age)
        self.age_button.pack()

    # Function to check age
    def check_age(self):
        age = int(self.age_entry.get())
        if age >= 18:
            # If age is valid, proceed to preferences
            self.ask_preferences()
        else:
            # If age is invalid, show message
            messagebox.showinfo("Sorry", "You must be 18 or older to use this service. 🚫")

    # Function to ask for liquor preferences
    def ask_preferences(self):
        # Remove age-related widgets
        self.age_label.destroy()
        self.age_entry.destroy()
        self.age_button.destroy()

        # Label for preference selection
        self.preference_label = tk.Label(self.master, text="Pick one of the following: Whiskey, Vodka, Rum, Tequila, Gin, Brandy, Liqueur): ")
        self.preference_label.pack()

        # Entry field for preferences
        self.preference_entry = tk.Entry(self.master)
        self.preference_entry.pack()

        # Button to get recommendation
        self.preference_button = tk.Button(self.master, text="Recommend Liquor", command=self.get_recommendation)
        self.preference_button.pack()

    # Function to get liquor recommendation
    def get_recommendation(self):
        preferences = self.preference_entry.get().split(",")
        recommended_category, recommended_brand = recommend_liquor(preferences)

        if recommended_category and recommended_brand:
            # If recommendation is found, display it
            messagebox.showinfo("Recommendation", f"We recommend trying {recommended_brand} {recommended_category}. 🎉")
            details = liquor_details[recommended_category][recommended_brand]
            messagebox.showinfo("Details", f"Origin: {details['origin']}\nAlcohol Percentage: {details['alcohol_percentage']}\nDescription: {details['description']} 📝")
        else:
            # If no recommendation is found, show message
            messagebox.showinfo("Sorry", "Sorry, we couldn't find a liquor recommendation based on your preferences. 😔")

# Function to recommend liquor based on preferences
def recommend_liquor(preferences):
    available_categories = [category for category in liquor_details if category in preferences]
    if available_categories:
        selected_category = random.choice(available_categories)
        selected_brand = random.choice(list(liquor_details[selected_category].keys()))
        return selected_category, selected_brand
    else:
        return None, None

# Main function to start the application
def main():
    root = tk.Tk()
    app = LiquorRecommendationApp(root)
    root.mainloop()

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
