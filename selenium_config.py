from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--start-maximized')

# Define a custom user agent
user_agent = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
)

# Upload extension
extension_path = "extension_1_4_0_0.crx"
chrome_options.add_extension(extension_path)

# Set the custom user agent as an argument for Chrome
chrome_options.add_argument(f'user-agent={user_agent}')
