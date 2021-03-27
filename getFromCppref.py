from bs4 import BeautifulSoup
import requests;

# from a path
# path = "https://en.cppreference.com/w/cpp/string/basic_string/find"
path = "https://en.cppreference.com/w/cpp/numeric/random"
r = requests.get(path)
soup = BeautifulSoup(r.content, 'html.parser')

# from file
# with open("cpprer-str-find.html") as fin:
#     soup = BeautifulSoup(fin, 'html.parser')

test = soup.find_all(attrs={"class" : "cpp source-cpp"})
for a in test:
    print(a.get_text())