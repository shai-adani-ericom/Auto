#Environmet Details for QA Service Sanity
#Shai Adani
#28/10/2020

env_setup_wiki = 'https://ericom.atlassian.net/wiki/spaces/SW/pages/31424513/Cloud+Environment+Setup'

chrome_driver_path = '../drivers/chromedriver'
firefox_driver_path = '../drivers/geckodriver'
edge_driver_path = '../drivers/msedgedriver'
chrome_download_folder = '/Users/shaiadani/Downloads/'
# Management
admin_url = 'https://qa-cloudadmin.shield-service.net'
admin_user = 'admin'
admin_password = 'ericomshield'
tenant_url = 'https://qa-tenantadmin.shield-service.net'
tenant_user = 'admin@SanityTest'
tenant_password = 'ericomshield'
elk_url = 'https://qa-elastic.shield-service.net'
rancher_url = 'https://mr.shield-service.net/'
rancher_user = 'qa'
rancher_password = 'Ericom123$'

# Ashburn-US east OCI
ashburn_proxy = 'qa-proxy-us-ashburn-1.shield-service.net:3128'
ashburn_proxyless = 'https://qa-farm-us-ashburn-1.shield-service.net'
# Israel Med1
med1_proxy = 'qa-proxy-med1.shield-service.net:3128'
med1_proxyless = 'https://qa-farm-med1.shield-service.net'
# Frankfurt  OCI
frankfurt_proxy = 'qa-proxy-eu-frankfurt-1.shield-service.net:3128'
frankfurt_proxyless = 'https://qa-farm-eu-frankfurt-1.shield-service.net'
# Milano  AWS
milano_proxy = 'qa-proxy-aws-eu-south-1.shield-service.net:3128'
milano_proxyless = 'https://qa-farm-aws-eu-south-1.shield-service.net/'
#geo location
geo_proxy = 'qa-ericom.shield-service.net:3128'
geo_proxyless = 'https://qa-proxyless.shield-service.net'


# QA pops list
qa_pops_proxy = [
            ashburn_proxy,
            med1_proxy,
            frankfurt_proxy,
            milano_proxy,
            geo_proxy
           ]

qa_pops_proxyless = [
            ashburn_proxyless,
            med1_proxyless,
            frankfurt_proxyless,
            milano_proxyless,
            geo_proxyless
           ]
#SAML details
saml_user = 'qa@adfs2019.local'
saml_password = 'Ericom123$'

#Check location link = https://qa-proxyless.shield-service.net/?url=https://tools.keycdn.com/geo
# Sanity link = https://ericom.atlassian.net/projects/SHIELD?selectedItem=com.atlassian.plugins.atlassian-connect-plugin%3Acom.kanoah.test-manager__main-project-page#!/testCase/SHIELD-T418

proxy_state = 1  # 1 with proxy 0 without proxy
headless_mode = 0 # 1 true 0 false
wait_time = 60

