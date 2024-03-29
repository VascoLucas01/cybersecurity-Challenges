#!/usr/bin/python3

# Script : Cookie_Capture_Capades.py
# Purpose:
# Why    :

import requests

def print_cookies(cookies):

    for cookie in cookies:
        print('cookie domain = ' + cookie.domain)
        print('cookie name = ' + cookie.name)
        print('cookie value = ' + cookie.value)
        print('******************************************')

def bringforthcookiemonster(): # Because why not!
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.

        ''')


def main():

    bringforthcookiemonster()

    url = 'https://google.com'
    
    response = requests.get(url)

    cookies = response.cookies

    print_cookies(cookies)

    response = requests.get(url, cookies=cookies)

    print_cookies(cookies)

if __name__ == "__main__":
    main()
