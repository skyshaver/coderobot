com_list = ["add", "rem", "update", "blame", "help", "commands"]

commands = """
* **rem** and **add** only work for **helpful** role
**add -** <add> followed by <key> followed by a \`\`\` delimited block of code:
add cout 
\`\`\`cpp
std::cout << "hello world";
\`\`\`
**blame -** print name and time of last update to snippet
**list -** lists all available keys for snippets
**rem -** <rem> followed by <key> to be removed from snippets database:
rem cout
"""

