###########################################################################
##                                                                       ##
## GnomeBingLockScreen                                                   ##
## Copyright (C) 2018 张泽平 (Randy Hoffman)                              ##
##                                                                       ##
## This program is free software: you can redistribute it and/or modify  ##
## it under the terms of the GNU General Public License as published by  ##
## the Free Software Foundation, either version 3 of the License, or     ##
## (at your option) any later version.                                   ##
##                                                                       ##
## This program is distributed in the hope that it will be useful,       ##
## but WITHOUT ANY WARRANTY; without even the implied warranty of        ##
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         ##
## GNU General Public License for more details.                          ##
##                                                                       ##
## You should have received a copy of the GNU General Public License     ##
## along with this program.  If not, see http://www.gnu.org/licenses/.   ##
##                                                                       ##
###########################################################################
##          Author: 张泽平 (Randy Hoffman)                                ##
## Website/Contact: https://github.com/zhangzp9970/                      ##
###########################################################################
#!/usr/bin/env python3
import json
import os
import urllib.request
import datetime
date=datetime.datetime.now().strftime('%Y-%m-%d')
day_s=datetime.datetime.now()-datetime.timedelta(days = 7)
day=day_s.strftime('%Y-%m-%d')
json_url="https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US"
bing_url="https://www.bing.com"
HOME=os.path.expandvars('$HOME')+"/"
json_file=HOME+".bing.json"
directory=HOME+"Pictures/Bing"
picture=directory+"/"+date+".jpg"
picture_del=directory+"/"+day+".jpg"
delete_old_picture = True
if not os.path.exists(directory):
	os.makedirs(directory)
if not os.path.exists(picture):
	#get the json file and hide the file
	urllib.request.urlretrieve(json_url,json_file)
	#open the file and import json string
	with open(json_file,"rb") as f:
		bing_json=json.load(f)
	url_append=bing_json['images'][0]['url']
	url=bing_url+url_append
	#get picture
	urllib.request.urlretrieve(url,picture)
	#change screen saver
	cmd="gsettings set org.gnome.desktop.screensaver picture-uri file:"+picture
	os.system(cmd)
	if os.path.exists(picture_del):
		if delete_old_picture == True:
			os.remove(picture_del)