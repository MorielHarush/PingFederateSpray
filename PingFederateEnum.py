from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import argparse


def check_user(username, url, output_file, incognito, headless):
    options = Options()
    if incognito:
        options.add_argument("--incognito")
    if headless:
        options.add_argument("--headless")

    with webdriver.Chrome(options=options) as driver:
        driver.get(url)
        username_input = driver.find_element_by_name('subject')
        username_input.send_keys(username)

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

        driver.implicitly_wait(100)
        time.sleep(3)

        try:
            driver.find_element_by_name('subject')
            print(f'[-] The User: {username} not found')
            time.sleep(3)
            return
        except Exception as e:
            print('Keep Working...')

        try:
            driver.find_element_by_name('pf.pass')
            print(f'[+] The User: {username} found! ')
            f = open(output_file, "a")
            f.write(username + "\n")
            f.close()
        except Exception as e:
            print(f'[-] The User: {username} not found')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True, help="URL to check the users")
    parser.add_argument("--users", required=True, help="Path to the input user file")
    parser.add_argument("--output", required=True, help="Path to the output valid user file")
    parser.add_argument("--incognito", required=True, action='store_true', help="Enable incognito mode for the browser")
    parser.add_argument("--headless", required=True, action='store_true', help="Enable headless mode for the browser")
    args = parser.parse_args()

    with open(args.users, 'r') as file:
        for line in file:
            check_user(line.strip(), args.url, args.output, args.incognito, args.headless)
