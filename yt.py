#Imports
import urllib.request
import re
import webbrowser

#Watch Function
def watch(name : str):
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + name)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    link = "https://www.youtube.com/watch?v=" + video_ids[0]
    return link

#Inputs
name = input("Search: ")
want_to_open = input("Would you like to open the link? (no/yes): ")

if want_to_open == "no":
    print("Here is the video link: ", link)

elif want_to_open == "yes":
    webbrowser.open_new_tab(watch(name = name))

else:
    print("please type 'yes' or 'no'")