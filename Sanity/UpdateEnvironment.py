#Environmet Details for Sanity
#Shai Adani
#20/2/2020
env='UPDATE'

chrome_driver_path = '../drivers/chromedriver'
firefox_driver_path = '../drivers/geckodriver'
edge_driver_path = '../drivers/msedgedriver'
chrome_download_folder = '/Users/shaiadani/Downloads/'

shield_ip = '136.244.111.246' # Shai Env
# shield_ip = '136.244.111.230' # Tzippy  136.244.111.230
shield_machine_user = 'root'
shield_machine_pass = '5zE.qsF,rKQ?fbu1' # Shai Env
# shield_machine_pass = 'K2-kw{hmAT6dUPY.' # Tzippy Env
proxy_address = shield_ip+':3128'
admin_address = 'https://'+shield_ip+':30181'
consul_farm_address = 'https://'+shield_ip+':30880'
consul_management_address = 'https://'+shield_ip+':31526'
rancher_address = 'https://'+shield_ip+':8443'
proxy_state = 1  # 1 with proxy 0 without proxy
admin_user_name = 'admin'
admin_password = 'ericomshield  '
rancher_user_name = 'admin'
rancher_password = 'ericomshield'

headless_mode = 0 # 1 true 0 false
build_number = '20.05.656'
branch = 'dev' # dev staging

restore_file_path = '/Users/shaiadani/PycharmProjects/Ericom/Automation/Sanity/backup.json'

#Tests List
# Deployment - upgrade
# Admin UI - URL Policies - Start

#usfull command post installation
# ##########
# sudo helm list --all-namespaces
# sudo kubectl get pods --all-namespaces
# kubectl describe pods mng-admin-7f49bb79b4-5hmtc --namespace management