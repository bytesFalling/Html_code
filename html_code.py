
#This program output HTML code of the page

#importing module
from urllib.request import urlopen
def main():
    user_url = "https://www.bytesfalling.com"
    html_page = urlopen( user_url )
    html_text = html_page.read().decode ( "utf-8")
    print ( html_text )

main()
