import json



class AI_Project_Functions:
    def get_crm_data():
        crm_data = {}
        try:
            with open('crm.json', 'r') as file:
                crm_data = json.load(file)
        except FileNotFoundError:
            print("Error: The file 'crm_data.json' was not found.")
            
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON from the file.")
            
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
        return crm_data
    
    def get_all_users(crm_data):
        """
        This function returns the names of all users in the given CRM data.
        :param crm_data: Dictionary containing CRM user data
        :return: List of user names
        """
        return list(crm_data.keys())
    
    def get_user_info(crm_data, name):
        name = str(name)
        """
        This function returns the past purchases and interests of a given user.
        :param crm_data: Dictionary containing CRM user data
        :param name: Name of the user
        :return: Dictionary with past purchases and interests or None if user not found
        """
        return crm_data.get(name, None)
    
    def add_entry_to_crm(name, part_purchase_list, interests_list, file_path='crm_data.json'):
        try:
            # Open the file to read its existing contents
            with open(file_path, 'r') as file:
                data = json.load(file)

            # Add the new entry to the data
            data[name] = {
                "past_purchases": list(part_purchase_list),
                "interests": list(interests_list)
            }

            # Open the file to write the updated data
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)

            print(f"Successfully added {name}'s information to the file.")

        except FileNotFoundError:
            print("Error: The file was not found.")
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON from the file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    
    def update_interests(name, new_interests, file_path='crm_data.json'):
        try:
            # Try to open and read the JSON file
            with open(file_path, 'r') as file:
                data = json.load(file)

            # Check if the user exists
            if name not in data:
                raise ValueError(f"Error: {name} not found in the file.")

            # Ensure "interests" key exists for the user
            if "interests" not in data[name]:
                data[name]["interests"] = []

            # Handle different data types for new_interests
            if isinstance(new_interests, str):
                # Append only if it's not already in the list
                if new_interests not in data[name]["interests"]:
                    data[name]["interests"].append(new_interests)
            elif isinstance(new_interests, list):
                # Replace the entire list
                data[name]["interests"] = new_interests
            else:
                raise TypeError("Error: new_interests must be a string or a list.")

            # Write back the updated JSON data
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)

            print(f"Successfully updated {name}'s interests.")

        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON. The file might be corrupted or empty.")
        except ValueError as ve:
            print(ve)
        except TypeError as te:
            print(te)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    def queryToSentiment(name, query):
        crm_data = AI_Project_Functions.get_crm_data()
        user_Data = AI_Project_Functions.get_user_info(name=str(name), crm_data=crm_data)
        interests = user_Data["interests"]
        past_purchases = user_Data["past_purchases"]
        state_of_mind = 5  
        emotion = "happy"  
        
    
        suggestions = "Do purchase that. Be happy. etc etc .... " 
        
        # Returning data based on analysis
        data_to_return = {
            "state_of_mind": state_of_mind,
            "emotion": emotion,
            "suggestions": suggestions,
        }
        
        return data_to_return

crm_data = AI_Project_Functions.get_crm_data()
# print(AI_Project_Functions.get_all_users(crm_data=crm_data))
# print(AI_Project_Functions.get_user_info(crm_data, "Pratheek Rao K B"))
print(AI_Project_Functions.queryToSentiment("Pratheek Rao K B", "hai i am happy today"))
# AI_Project_Functions.add_entry_to_crm("Pratheek Rao K B", ["Laptop", "Mobile Phone"], ["Watching Movies", "Playing Cricket"], "crm.json")
# AI_Project_Functions.update_interests("Pratheek Rao K B", ["Playing Cricket", "Playing Football"], "crm.json")