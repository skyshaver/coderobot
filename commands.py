com_list = ["add", "rem", "update", "blame","list", "help","-h", "commands"]

commands = """
**$ -** use as a prefix to post a code snippet by its key
_$cout_
```cpp
std::cout << "hello world";
```
* **add update** and **rem** only work for **helpful** role *
** Use `@CodeRobot` before these commands: **
**add -** adds a snippet, _add_ followed by <key> followed by a \`\`\` delimited block of code:
`@CodeRobot` _add cout 
\`\`\`cpp
std::cout << "hello world";
\`\`\`_
**update -** use the same syntax as _add_ to update a snippet
**blame -** print name and time of last update to snippet:
`@CodeRobot` _blame cout_
**list -** lists all available keys for snippets:
`@CodeRobot` _list_
**rem -** removes a snippet, _rem_ followed by <key> to be removed from snippets database:
`@CodeRobot` _rem cout_
"""

question = """
1. Understand the code to the best of your ability
2. Clearly describe the problem
3. Provide code that illustrates the problem
4. Make sure the code you're sharing can reproduce the problem
5. Format your code consistently
6. Check yourself for typos
7. Explain what you did to troubleshoot the problem
"""