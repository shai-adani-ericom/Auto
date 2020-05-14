#Environmet Details for Sanity
#Shai Adani
#20/2/2020


chrome_driver_path = '../drivers/chromedriver'
firefox_driver_path = '../drivers/geckodriver'
edge_driver_path = '../drivers/msedgedriver'
chrome_download_folder = '/Users/shaiadani/Downloads/'

shield_ip = '78.141.216.60'
shield_machine_user = 'root'
shield_machine_pass = '+m4MJP]4,+Z]V6s'

proxy_address = shield_ip+':3128'
admin_address = 'https://'+shield_ip+':30181'
consul_farm_address = 'https://'+shield_ip+':30880'
consul_management_address = 'https://'+shield_ip+':31526'
rancher_address = 'https://'+shield_ip+':8443'
proxy_state = 1  # 1 with proxy 0 without proxy
admin_user_name = 'admin'
admin_password = 'ericomshield'
rancher_user_name = 'admin'
rancher_password = 'ericomshield'

headless_mode = 0 # 1 true 0 false
build_number = '20.05.644'
branch = 'dev' # dev staging

jenkins_url = 'https://jenkins.shield-service.net/job/ENV/job/create-test-env/'
jenkins_user = 'user'
jenkins_password = 'e12345'
email = 'shai.adani@ericom.com'

activation_portal_url = 'http://shieldactivation.ericom.com/login'
activation_portal_user = 'ericom'
activation_portal_password = 'ericom2017'

restore_file_path = '/Users/shaiadani/PycharmProjects/Ericom/Automation/Sanity/backup.json'