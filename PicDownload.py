import os
import requests

# Define the path where the images will be saved
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "Random")
# Create the directory if it doesn't exist
os.makedirs(desktop_path, exist_ok=True)

# Loop to download multiple images
for i in range(0, 70):
    # Define the URL for downloading a random image
    url = "https://picsum.photos/200/200/?random"
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Generate a unique file name for the image
        file_name = 'not_5euro_{}.jpg'.format(i)
        # Construct the full file path
        file_path = os.path.join(desktop_path, file_name)

        # Write the image content to a file
        with open(file_path, 'wb') as f:
            print("Saving: " + file_name)
            f.write(response.content)
