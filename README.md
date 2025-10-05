# devops_practice
Python programms assignments


Q1. In DevOps, security is a crucial aspect, and ensuring strong passwords is essential. Create a Python script to check the strength of the password. 
●       Implement a Python function called check_password_strength that takes a password string as input.
●       The function should check the password against the following criteria:
○       Minimum length: The password should be at least 8 characters long.
○       Contains both uppercase and lowercase letters.
○       Contains at least one digit (0-9).
○       Contains at least one special character (e.g., !, @, #, $, %).
●       The function should return a boolean value indicating whether the password meets the criteria.
●       Write a script that takes user input for a password and calls the check_password_strength function to validate it.
●       Provide appropriate feedback to the user based on the strength of the password.  



Q2. As a DevOps engineer, it is crucial to monitor the health and performance of servers. Write a Python program to monitor the health of the CPU. Few pointers to be noted:
●       The program should continuously monitor the CPU usage of the local machine.
●       If the CPU usage exceeds a predefined threshold (e.g., 80%), an alert message should be displayed.
●       The program should run indefinitely until interrupted.
●       The program should include appropriate error handling to handle exceptions that may arise during the monitoring process.
Hint:
●       The psutil library in Python can be used to retrieve system information, including CPU usage. You can install it using pip install psutil.
●       Use the psutil.cpu_percent() method to get the current CPU usage as a percentage.


Q3. In DevOps, automating configuration management tasks is essential for maintaining consistency and managing infrastructure efficiently.
●       The program should read a configuration file (you can provide them with a sample configuration file).
●       It should extract specific key-value pairs from the configuration file.
●       The program should store the extracted information in a data structure (e.g., dictionary or list).
●       It should handle errors gracefully in case the configuration file is not found or cannot be read.
●       Finally save the output file data as JSON data in the database.
●       Create a GET request to fetch this information.
