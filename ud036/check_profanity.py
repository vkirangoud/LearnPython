import urllib

def read_text():
    quotes = open("C:\sdrive\prac\movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output = connection.read()
    connection.close()

    connection = urllib.urlopen("http://isithackday.com/arrpi.php?text="+text_to_check)
    pirateSpeech = connection.read()
    connection.close()

    #print(output)
    
    if "true" in output:
        print("Profanity Alert!! - Why do you love")
    elif "false" in output:
        print("This document has no curse words! - wdyl")
    else:
        print("Could not scan the document properly.")

    print(pirateSpeech)
    
    if "true" in pirateSpeech:
        print("Profanity Alert!! - Pirate Speech")
    elif "false" in pirateSpeech:
        print("No curse words - Pirate Speech")
    else:
        print("Not scanned the doc")

        

        

read_text()
