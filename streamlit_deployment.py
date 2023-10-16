import streamlit as st
import os

# Set the title and description of your Streamlit app
st.title("Car Racing Game")


# Function to allow users to download the game files
def download_game():
    # Path to the folder containing your game files
    game_folder = "C:\\Users\\ASUS\\Desktop\\Car_Racing_Game"
    
    # List all files in the game folder
    files = os.listdir(game_folder)

    # Create a ZIP file containing all game files
    with st.zipfile.ZipFile("car_racing_game.zip", "w") as zipf:
        for file in files:
            file_path = os.path.join(game_folder, file)
            zipf.write(file_path, os.path.basename(file_path))

# Create a button to trigger the download
if st.button("Download Game"):
    download_game()
    st.success("Game files are ready for download! Click the link below.")
    
    # Provide a download link for the ZIP file
    st.markdown("[Download Car Racing Game](car_racing_game.zip)")

