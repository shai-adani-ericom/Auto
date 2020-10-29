fileName = 'LoadStatisticsFileLocal'
build_number = 'Cloud service 11-08-2020'
shield_mode = 'Stream' # Crystal Stream Frame
load_statistics_file = 'File.csv'
remote_browser = 0  # 1 = yes, start remote gridlastic browser. 0 = no, start local browser
chrome_driver_path = '../drivers/chromedriver'
ff_driver_path = '../drivers/geckodriver'
headless_mode = 1
shield_status = 'ON'
proxy_address='108.61.198.223:3128' # 685 direct proxy without header
# proxy_address='prod-proxy-israel.shield-service.net:3128' # Med1 production

tabs_count = 1
wait_time_between_new_tabs = 10  # seconds
# wait_time_before_browser_quit = 60  # seconds
load_run_time = 60  # minutes
ramp_up_time = 5 # seconds
max_concurrent_sessions = 1
max_session_time = 5


urls = ['http://www.easyjet.com',
        'http://www.gmail.com',
        'http://www.facebook.com',
        'http://www.youtube.com',
        'http://www.instagram.com',
        'http://wordpress.com/',
        'http://blogspot.com/',
        'http://apple.com/',
        'http://adobe.com/',
        'http://tumblr.com/'
        ]




