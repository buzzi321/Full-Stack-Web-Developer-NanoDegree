import urllib
def read_text():
    quotes = open("C:\Sekhar_DTV\Learning\Full Stack Web Developer NanoDegree\movie_quotes.txt")
    contents_of_file = quotes.read()
    #print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    #print(output)
    connection.close()
    if "true" in output:
        print("Profanity Alert!")
    elif "false" in output:
        print ("No curse words!")
    else:
        print "system error!"



read_text()