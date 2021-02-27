# web-scraping

To auto-login into Moodle, run moodleLogin.py
    Then enter your username and password
    Password will not be visible as you type for security reasons
    Moodle will then be opened and the captcha will be solved
    You will be logged into your Moodle account within seconds

To get CodeForces problems given the contest number, run fetch_round.py
    Then enter the contest number
    A new folder will be created with the name as the contest number entered
    This folder will contain folders with the problem labels as the name
    Each of those folders will contain the screenshot of the problem, input and output files.
    Please wait for a few seconds for the files to appear as the browser will be run headlessly.

To get CodeForces problems based on difficulty, run fetch_difficulty.py
    Then enter the minimum and maximum difficulty of the problems you are looking for.
    Then enter the number of problems(<=100) you require
    A new folder with the name (minDifficulty-maxDifficulty) will be created which will contain the required problems similar to fetch_round.py
    Please wait for a few seconds for the files to appear as the browser will be run headlessly.

Happy Coding!