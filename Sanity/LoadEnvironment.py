fileName = 'LoadStatisticsFile'
shield_mode = 'Stream'
build_number = '20.05.648'
load_statistics_file = 'File.csv'
remote_browser = 0  # 1 = yes, start remote gridlastic browser. 0 = no, start local browser
chrome_driver_path = '../drivers/chromedriver'
ff_driver_path = '../drivers/geckodriver'
headless_mode = 0
# proxy_address = 'Shield-Load-80e1f451a8f2c519.elb.eu-central-1.amazonaws.com:3128' # AWS Load environment                           
proxy_address = '136.244.111.246:3128'  # Sanity update environment                                                                   
# proxy_address = '126.0.3.51:3128' # Shield-Jer                                                                                      
tabs_count = 4
wait_time_between_new_tabs = 5  # seconds
wait_time_before_browser_quit = 20  # seconds
load_run_time = 1  # minutes
parallel_actions = 3
# ramp_up_time = 60 # seconds                                                                                                         
# ramp_up_sessions = 3                                                                                                                
# max_cucurrent_browsers = 2                                                                                                          
# max_cucurrent_sessions = 2                                                                                                          

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
