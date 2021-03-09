import re

str = """\
add cout
```cpp
std::cout << "hello world";
```"""

# words = re.split('[```]', str)
words = str.split('```')
print(words)
key = words[0].split()[1]
value = words[1]
print(key, "\n", value)

msg = 'add commands'
if msg in ['commands', 'help', '-h']:
        print("found")

if msg.startswith(("rem", "add", "blame")):
        print("starts")
# msg = message.content[message.content.rfind('>') + 1:]
        # print(msg)
