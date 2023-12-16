# PingFederateSpray
PingFederateSpray is a robust and efficient tool designed for security professionals and penetration testers. It leverages the power of Selenium to perform automated username enumeration and password spraying attacks against PingFederate authentication systems. This tool aims to assist in identifying weak credentials and potential vulnerabilities within enterprise environments that rely on PingFederate for identity management and access control.
This repo includes 2 scripts. 
* PingFederateEnum.py - User Enumeration.
* PingFederateSpray.py - Spray Passwords.

# Key Features
* Automated User Enumeration: Efficiently determines valid usernames by interacting with the PingFederate authentication page.
* Password Spraying Capabilities: Executes password spraying attacks, testing a list of common passwords against identified valid users, aiding in uncovering weak credentials.
* Headless Browser Support: Runs in headless mode for seamless operation in background and automated environments.
* Incognito Mode Option: Ensures cleaner sessions with less traceability, enhancing the tool's discreetness during testing.
* Customizable Workflow: Supports various command-line arguments for a personalized and flexible usage experience.
  
# Usage Scenarios
PingFederateSpray is particularly useful in penetration testing and security auditing scenarios where organizations utilize PingFederate. It helps in:
* Educational Purposes
* Assessing the strength of user credentials in the target system.
* Identifying potential security gaps related to user authentication.
* Complementing broader security assessments with focused testing on authentication mechanisms.

# Usage
PingFederateEnum.py [-h] --url URL --users USERS --output OUTPUT --incognito --headless

options:
*  -h, --help       show this help message and exit
*  --url URL        URL
*  --users USERS    Path to the input user file
*  --output OUTPUT  Path to the output valid user file
*  --incognito      Enable incognito mode for the browser
*  --headless       Enable headless mode for the browser

PingFederateSpray.py [-h] --url URL --output OUTPUT --password PASSWORD --users USERS [--incognito] [--headless]

options:
*  -h, --help           show this help message and exit
*  --url URL            URL
*  --output OUTPUT      Path to the output file for valid sprayed users
*  --password PASSWORD  Password to use for spraying
*  --users USERS        Path to the input user file
*  --incognito          Enable incognito mode for the browser
*  --headless           Enable headless mode for the browser

# PoC 
* PingFederateEnum.py success enumeration will look like : 
![image](https://github.com/MorielHarush/PingFederateSpray/assets/93482738/cb592823-3329-44ad-8e77-15ec24de04b0)

* PingFederateSpray.py bad spray try will look like:
![image](https://github.com/MorielHarush/PingFederateSpray/assets/93482738/72c93896-dfcb-466f-8992-a5594bbd1984)


# Clean CMD Ouput
PingFederateEnum.py will create a txt file with the valid usernames. 
But anyway if the selenium chrome driver "DevTools" print line is annoying , you can use FireFox driver it wont print that horrible line.
