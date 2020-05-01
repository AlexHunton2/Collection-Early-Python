import bs4, requests, webbrowser, sys
#Simple Program that opens the top video when searched on youtube. 
print("What Video do you want to see?")
response = input()

youtube = requests.get('https://www.youtube.com/results?search_query=' + ' '.join(response))
youtube.raise_for_status()

soup = bs4.BeautifulSoup(youtube.text)
selections = soup.select('.yt-lockup-title a')

for i in range(1):
    webbrowser.open("https://www.youtube.com/" + selections[i].get('href'))