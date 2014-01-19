import json

# SOCIAL NETWORK APIS
apis_file = open('./conf/apis.json','r')
apis = json.loads(apis_file.read())
apis_file.close()

# SITE CONFIGURATION
site_conf = open('./conf/site-conf.json','r')
confs = json.loads(site_conf.read())
site_conf.close()

# Uncomment the following line for Production
# conf = confs['Production']

# Uncomment the following line for Development
conf = confs['Development']

for sn in apis:
    apis[sn]['auth_url'] = apis[sn]['auth_url'].replace('%%REDIRECT_URI%%',conf['redirect'])
    apis[sn]['token_url'] = apis[sn]['token_url'].replace('%%REDIRECT_URI%%',conf['redirect'])
    apis[sn]['redirect_uri'] = conf['redirect']
