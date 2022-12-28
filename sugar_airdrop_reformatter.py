import json

# Load the JSON data from the file
with open("airdrop_list.json", "r") as f:
    data = json.load(f)

# Loop through each key-value pair in the data
for key, value in data.items():
    # Delete the "mints" field and its contents
    del value["mints"]
    # Get the value of the "amount" field
    amount = value["amount"]
    # Set the value for the current key to be the value of the "amount" field
    data[key] = amount

# Write the reformatted data back to the file
with open("airdrop_list.json", "w") as f:
    json.dump(data, f)
