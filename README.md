# Project 4:  Brevet time calculator with Ajax



README:

Author: John Drake
github repo: https://github.com/johnmdrake1/proj4-brevets
github profile: https://github.com/johnmdrake1/

Description: An ACP time calculator for brevets and their controles, written as a reimplementation of the calculator at 
https://rusa.org/octime_acp.html. This reimplementation is accomplished through a client-server relationship,
and is utilized through a webpage which has several inputs and outputs connected to it.

Functionality, and other information for users of the calculator:
Once the server has been started(as described below), connecting to it will display an HTML web page with several spaces for 
input and output of information. 

At the top of the page, a dropdown list labeled 'Distance' allows the user to select the total distance of their brevet
that they wish to calculate controles for. Brevet distances can be 200, 300, 400, 600, and 1000 according to official rules.
The final controle in a brevet can be slightly greater than the total distance of the brevet(e.g. controle at 605km on a 600km brevet)
and the calculator accounts for this possibility and adjusts values accordingly to maintain accordance to brevet rules relevant 
to the situation. The 'Distance' box must be accurate, as certain controle distances depend on brevet distance to determine 
their open and close times accurately. 

Also at the top of the page are date and time boxes. The value entered here must be the starting date and time of the brevet, 
so the calculator can return both the date and time of controle openings and closings. NOTE: In practice the calculator uses
a 24 hour time format for its functionality, but choice of browser may affect how the date and time input boxes are
displayed. Adjust accordingly should this be the case. 

Once this information has been inputted and is in place, the user can start entering brevet controle distances. These may be 
entered either in the 'Miles' or 'Km' columns for each controle entered. The calculator will perform and display the necessary
conversions regardless of what measurement is used. Optionally, a location for each inputted brevet may be specified, but this
will not affect calculator performance. 

Once a controle distance has been inputted, pressing the enter key will populate the 'Open' and 'Close' time fields for 
the row that controle was entered in. Note that this should display in 24-hour format. As each controle is computed individually,
it is not necessary to input all of the controles for a given brevet to see the information about that controle(this is not
the case in the official ACP calculator, however).

The rules state a specific maximum close time for each brevet length. Due to this, all values that exceed the chosen brevet length
will correspond to this same specific value, (e.g. controles 200, 205, and 210 for a 200km brevet). 

Refreshing the page should reset the calculator if information about a different brevet is desired. Restarting the server is not
necessary for this functionality.

Instructions for Developers and starting the server:

Information about relevant source files and their communication:
Technologies such as AJAX and flask are used to handle the client-server relationship for inputting and outputting data.
Information inputted in the fields contained in calc.html is sent to flask_brevets.py so it can be used. In flask_brevets.py,
the functions from acp_times.py are called using these inputs and their outputs are passed back to the html for their display
to the user. 

There are two such functions in acp_times.py, and they are solely responsible for the calculations themselves(of controle open
and close times based on a brevet distance and controle distance). 

open_time and close_time use the same 3 arguments:
1. The distance to the controle(value inputted in text entry field)
2. The total brevet distance(value from dropdown menu)
3. The starting date and time(value entered in the appropriate date/time fields)

The opening and closing times are computed using a table driven approach, indexing data structures that define values relevant 
to certain ranges of user inputs. Little is changed between open_time and closing_time, as the differences mainly consist
of different table values.


-Commands:
Note: credentials.ini must be placed in the brevets directory.
1. 'cd' to local directory with calculator files
2. 'make install' (installs all necessary modules and technologies for source code to function, and creates virtual environment)
3. 'make start' will start the server(in the virtual environment).
4. The calculator can now be accessed at 'http://localhost:8000/' from within a client such as a web browser.
5. Server will continue to run until command 'make stop' is entered. This will stop the server.

Testing: 
Once cd into project directory:
'make test' will run a python nosetest suite contained within brevets/test_acp_times.py
The command prompt should output the following:
----------------------------------------------
Ran 5 tests in x.xxx seconds

OK
----------------------------------------------
If anything about failure appears, one of the assertions in the test failed to match the expected value.

Test details:
test_acp_times.py defines 5 functions that utilize nose testing. Each of these functions will test several possible 
cases and many combinations of input/output values. Each function serves a unique purpose, described in code comments in the test
suite file.
Outputted times may not always be rounded to the proper minute(i.e. the minute the official ACP calculator settles on) but 
the date and hour should be exactly the same. When there are errors in minute output they should only be +-1. A function 'nearly(x,y)' 
takes an output and its expected value and compares the dates and hours for equivalency, while making sure the minute falls within
the expected error range. All test cases simply call the 'nearly' function.



