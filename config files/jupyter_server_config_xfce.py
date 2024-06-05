import os
import os.path

uid=os.getuid()

WEBSOCKET=8900+1000+uid
print(WEBSOCKET)

#xfec_path = os.path.abspath("xfec_desk3.sh")
config_path = '/home/amyserver/.jupyter/config_novnc.sh'
vapor_config_path = '/home/amyserver/.jupyter/config_vapor.sh'

path = 'novnc/?resize=remote&reconnect=1&autoconnect=1&port=' + str(WEBSOCKET)


c.ServerProxy.servers = {
           'novnc': {
                    'command': [config_path],
                    'timeout': 30,
		    'port': WEBSOCKET,
                    'absolute_url': False,
                    'launcher_entry': {
                        'title': 'Xfce Desktop',
			'path_info': path,
		},
		    'new_browser_tab': True,
          }
    }

