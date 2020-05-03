import sys
import pyperclip
import webbrowser
def main(link):
    #Link goes to abhiram to get text
    #Text goes to Sid to get three links

    sample_links = [link,link,link]
    webbrowser.open_new_tab(sample_links[0])
    webbrowser.open_new_tab(sample_links[1])
    webbrowser.open_new_tab(sample_links[2])

main(sys.argv[1])

