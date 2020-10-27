fileName = 'LoadStatisticsFile'
build_number = 'Cloud service 20-07-2020'
shield_mode = 'Stream' # Crystal Stream Frame
load_statistics_file = 'File.csv'
remote_browser = 1  # 1 = yes, start remote gridlastic browser. 0 = no, start local browser
chrome_driver_path = '../drivers/chromedriver'
ff_driver_path = '../drivers/geckodriver'
headless_mode = 1
shield_status = 'ON'
# proxy_address = 'Shield-Load-80e1f451a8f2c519.elb.eu-central-1.amazonaws.com:3128' # AWS Load environment
# proxy_address = '136.244.111.246:3128'  # Sanity update environment
# proxy_address = 'ericom.shield-service.net'
# proxy_address = '130.61.135.124:3128'  # Oracle Cloud Frankfurt
# proxy_address = 'ec2-18-195-234-108.eu-central-1.compute.amazonaws.com:3127'  # Oracle Cloud Header Proxy to Frankfurt
# proxy_address = '129.213.173.66:3128'  # Oracle Cloud Ashburn
# proxy_address = '127.0.0.1:3111'  # SOCK test environment 20.05.661
# proxy_address = 'ec2-52-29-29-56.eu-central-1.compute.amazonaws.com:3111'  # AWS header proxy
# proxy_address = '141.226.185.143:3128' # Header Proxy without security connected to Med 1
# proxy_address='qa-proxy-med1.shield-service.net:3128' # Med1 direct proxy without header
# proxy_address='prod-proxy-israel.shield-service.net:3128' # Med1 production
# proxy_address='52.19.118.170:3128' # Squid for Beny
proxy_address='qa-proxy-eu-frankfurt-1.shield-service.net:3128' # QA cloud Frankfurt port
# proxy_address = '45.63.40.57:3128' # Orit SOAK TEST
# proxy_address = '126.0.3.51:3128' # Shield-Jer
# proxy_address = '1qa-med1-ericom.shield-service.net' # Service Cloud Med1 Proxy
# proxy_address = 'qa-farm-med1.shield-service.net' # Service Cloud Med1 Proxy-less
# proxy_address = 'qa-ericom.shield-service.net' # Service Cloud Geolocation resolve with Ericom tenant

tabs_count = 1
wait_time_between_new_tabs = 1  # seconds
# wait_time_before_browser_quit = 60  # seconds
load_run_time = 40  # minutes
ramp_up_time = 5 # seconds
max_concurrent_sessions = 60
max_session_time = 300

urls = ['https://www.ynet.co.il/']
# urls = ['http://www.easyjet.com',
#         'http://www.gmail.com',
#         'http://www.facebook.com',
#         'http://www.youtube.com',
#         'http://www.instagram.com',
#         'http://wordpress.com/',
#         'http://blogspot.com/',
#         'http://apple.com/',
#         'http://adobe.com/',
#         'http://tumblr.com/'
#         ]




