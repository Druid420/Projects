import re

def getSongNames():
    # Load the HTML file
    with open(r'C:\Users\risha\Desktop\projects\Projects\AppleMusictoSpotify\_Yhex by Rishabh Patel - Apple Music.html', 'r', encoding='cp437') as file:
        html_content = file.read()

    # Use regular expression to find unique song names
    song_names_set = set(re.findall(r'"name":"([^"]+)"', html_content))

    # Convert the set back to a list
    song_names = list(song_names_set)
    return(song_names)