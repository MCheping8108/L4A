import pymongo,os,json
from bson import ObjectId
from urllib import request

data_path = './data'

def main():
	for maindir, subdir, file_list in os.walk(data_path):
		for file_name in file_list:
			if file_name[file_name.rindex('.'):] == '.json':
				with open(data_path + '/' + file_name, encoding='utf-8') as file:
					str = json.loads(file.read())
					data = []
					data.extend(str['RECORDS'])

					# 删掉 ranking_list.json 中的ranking_id
					# if file_name == 'songs.json':
					# 	for dict in data:
					# 		dict.pop('ranking_id')
					# 	result = json.dumps({'RECORDS': data}, ensure_ascii=False)
					# 	write2file('songs.json', result)

					# 处理某个 xx.json 文件
					# if file_name == 'ranking_list.json':
					# 	for dict in data:
					# 		ranking_id = dict['_id']
					# 		songs_list = get_songs_id(ranking_id)
					# 		dict['songs_id'] = songs_list
					#
					# 	result = json.dumps({'RECORDS': data}, ensure_ascii=False)
					# 	write2file('ranking_list.json', result)

					if file_name == 'play_list.json':
						for dict in data:
							plist_id = dict['_id']
							song_ids = get_songs_id(plist_id)
							dict['songs_id'] = song_ids

						result = json.dumps({'RECORDS':data},ensure_ascii=False)
						write2file('play_list.json',result)

def get_ranking_list(ranking_id):
	ranking_list = []
	with open(data_path + '/' + 'ranking_list.json', encoding='utf-8') as file:
		str = json.loads(file.read())
		data = []
		data.extend(str['RECORDS'])
		for d in data:
			if d['ranking_id'] == ranking_id:
				d.pop('ranking_id')
				ranking_list.append(d)
	return ranking_list

def get_songs_id(plist_id):
	song_ids = []
	with open(data_path + '/' + 'plist_music.json', encoding='utf-8') as file:
		str = json.loads(file.read())
		data = []
		data.extend(str['RECORDS'])
		for d in data:
			if d['plist_id'] == plist_id:
				song_ids.append(d['music_id'])
	return song_ids

# 写入文件
def write2file(filename,content):
	with open(data_path + '/' + filename, 'w',encoding='utf-8') as file:
		file.write(content)

main()