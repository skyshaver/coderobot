com_list = ["add", "rem", "update", "blame","list", "help","-h", "commands"]

commands = """
**$ -** use as a prefix to post a code snippet by its key
_$cout_
```cpp
std::cout << "hello world";
```
* **rem** and **add** only work for **helpful** role *
** Use `@CodeRobot` before these commands: **
**add -** adds a snippet, <add> followed by <key> followed by a \`\`\` delimited block of code:
`@CodeRobot` _add cout 
\`\`\`cpp
std::cout << "hello world";
\`\`\`_
**blame -** print name and time of last update to snippet:
`@CodeRobot` _blame_
**list -** lists all available keys for snippets:
`@CodeRobot` _list_
**rem -** removes a snippet, <rem> followed by <key> to be removed from snippets database:
`@CodeRobot` _rem cout_
"""

