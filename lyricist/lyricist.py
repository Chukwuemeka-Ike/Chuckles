from lyricsgenius import Genius
import matplotlib.pyplot as plt
import numpy as np

# Need a token for the Genius API. You'll need a Genius account to get one.
token = ""
genius = Genius(token)
album = genius.search_album(
    "METRO BOOMIN PRESENTS SPIDER-MAN: ACROSS THE SPIDER-VERSE (SOUNDTRACK " +\
        "FROM AND INSPIRED BY THE MOTION PICTURE / DELUXE EDITION)",
        "Metro Boomin"
)

# Print the full title as a sanity check, then save all the lyrics to a text file.
print(album.full_title)
album.save_lyrics("lyrics", extension="txt")

# The strings to search for.
text_metro = "Metro"
text_21 = "21"

# Load the lyrics.
f = open("lyrics.txt", "r")
lyrics = f.read()
f.close()

# Make all the lyrics lowercase.
lyrics = lyrics.lower()

# Count occurrences of both substrings in the lyrics.
num_metro = lyrics.count(text_metro.lower())
num_21 = lyrics.count(text_21.lower())

# Plot our findings.
fig = plt.figure(figsize = (10, 5))
plt.bar([text_metro, text_21], [num_metro, num_21], color ='blue',
        width = 0.4)
plt.yticks(np.arange(0, num_21+1, 2))
plt.grid(True)
plt.xlabel("Ad-Lib")
plt.ylabel("No. of occurrences in the album")
plt.title("Occurrences of 'Metro' and '21' in ATSV Album")
plt.show()