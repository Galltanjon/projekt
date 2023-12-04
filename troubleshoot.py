from fuzzywuzzy import fuzz, process

#Free text will be changed to entering numbers corresponding to single ingredient, rendering this code obsolete.
#Will instead add other type o troubleshooting for other stuff

def get_best_match(user_input, choices):
    # Get a list of tuples with choices and their similarity scores
    matches = process.extract(user_input, choices)

    # Filter matches with a similarity score above a certain threshold (adjust as needed)
    filtered_matches = [match for match in matches if match[1] >= 80]

    # If there are filtered matches, return the best match, otherwise return None
    if filtered_matches:
        best_match = max(filtered_matches, key=lambda x: x[1])
        return best_match[0]
    else:
        return None

# Example usage
predefined_list = ["chicken", "beef", "pork", "fish", "vegetables"]

user_input = input("Enter a food item: ")

best_match = get_best_match(user_input, predefined_list)

if best_match:
    print(f"Suggested match: {best_match}")
else:
    print("No match found. Please enter a valid food item.")
