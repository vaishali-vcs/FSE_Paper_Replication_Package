
tasks = """- Contact administrators:
  - Implement a contact form functionality
  - Provide a direct messaging channel for users to reach administrators
- Add recycling center information:
  - Design a form for administrators to input recycling center details
  - Implement a database storage system for the recycling center information
- View user error logs:
  - Create a user error log interface for administrators to monitor errors
  - Implement a search function to easily locate specific user error logs
- Onboard recycling centers on the platform:
  - Develop an onboarding process for recycling centers to join the platform
  - Design a verification system to ensure the accuracy of added recycling centers
- Update recycling center information:
  - Allow administrators to edit existing recycling center details
  - Implement a notification system to inform users of updated information"""
import re

# Splitting the string based on the main categories
main_categories = re.split(r'\n-\s', tasks.strip())
main_categories = [cat for cat in main_categories if cat]

# Further splitting each category into its title and sub-items
structured_data = {}
for category in main_categories:
    parts = category.split(':\n  - ')
    if len(parts) == 2:
        title = parts[0].strip()
        sub_items = parts[1].split('\n  - ')
        structured_data[title] = sub_items

# Displaying the structured data
for title, sub_items in structured_data.items():
    print(f"{title}:")
    for item in sub_items:
        print(f"  - {item}")

i = 1
