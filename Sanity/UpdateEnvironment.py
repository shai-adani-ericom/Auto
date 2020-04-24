#Environmet Details for Sanity
#Shai Adani
#20/2/2020


chrome_driver_path = '../drivers/chromedriver'
firefox_driver_path = '../drivers/geckodriver'
edge_driver_path = '../drivers/msedgedriver'
chrome_download_folder = '/Users/shaiadani/Downloads/'

shield_ip = '108.61.117.185' # 45.77.136.39
shield_machine_user = 'root'
shield_machine_pass = ',5dF8UH9t.pYZ,(_'

proxy_address = shield_ip+':3128'
admin_address = 'https://'+shield_ip+':30181'
consul_farm_address = 'https://'+shield_ip+':30880'
consul_management_address = 'https://'+shield_ip+':31526'
rancher_address = 'https://'+shield_ip+':8443'
proxy_state = 1  # 1 with proxy 0 without proxy
admin_user_name = 'admin'
admin_password = 'ericomshield1'
rancher_user_name = 'admin'
rancher_password = 'ericomshield'

headless_mode = 0 # 1 true 0 false
build_number = '20.04.640'
branch = 'dev' # dev staging

restore_file_path = '/Users/shaiadani/PycharmProjects/Ericom/Automation/Sanity/backup.json'

#Tests List
# Deployment - upgrade
# Admin UI - URL Policies - Start

