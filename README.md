# JavPie
A Java-like compiler created in Python and Java as the target language.

# Things to Install/Set Up Before Running JavPie
1. Use the latest version of python from this website https://www.python.org/downloads/
2. Install Visual Studio Code from this website https://code.visualstudio.com/Download
    a. To allow git with VSCode go to settings, type 'git enabled' and make sure that options is checked
3. to Clone a repository go to 'Source Control Option' and Select 'Clone Repository' then paste the repository link on the prompt VSCode provides



# How to Install Code Coverage in VSCode:
1. pip install coverage
2. python -m coverage run Coverage_file_name.py in src folder
3. python -m coverage report --show-missing - #shows uncovered lines
4. python -m coverage html #creates a concise html version of report
5. python -m pytest #for testing Coverage_file_name.py



# How to run the test files

Due to issues on making test files work via computer or outside terminal, tests would need to excecute by coding enviroments compila and run integrations.

Coding Environment used to run code, run tests, and get coverage: Visual Studio Code

1. In Tests folder, open any test file and within the coding environment compile/run the code. Do not use outside terminal,
    otherwise there will be a 'Module Not Found' Error.
 
    Ex. VSCode: Top right of current window the triangle or using 'Ctrl+Alt+N' for test_Lexer.py file

# Citation
Source Code:
https://github.com/davidcallanan/py-myopl-code