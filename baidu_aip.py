# -*- coding: utf-8 -*-
import base64
from aip import AipFace

def aip_client(image_path):
	""" 你的 APPID AK SK """
	APP_ID = '10848231'
	API_KEY = 'NqlZYpBvgebz6rCRB0n4nGGQ'
	SECRET_KEY = 'm5ic5LO52gDUMQ2p2S9uGUOvlljgzRyl'

	client = AipFace(APP_ID, API_KEY, SECRET_KEY)

	imageType = "BASE64"

	options = {}
	options["face_field"] = "age,beauty,face_shape,gender,glasses,race,expression" #需要检测的参数
	options["max_face_num"] = 1 #默认检测图中最大的那张脸盘
	options["face_type"] = "LIVE"

	""" 带参数调用人脸检测 """
	with open(image_path, "rb") as f: #二进制读入
		img = base64.b64encode(f.read()) #b64编码
		image = str(img,'utf-8')

	res_all = client.detect(image, imageType, options)
	msg_list = []   
	error_code = res_all['error_code']  #错误代码
	msg_list.append(str(error_code))
	if int(error_code) == 0:
		error_msg = res_all['error_msg']	#错误信息
		res_all_temp = res_all['result']['face_list'][0]
		age = res_all_temp['age'] #检测年龄
		msg_list.append(str(age))
		race = res_all_temp['race']['type'] #检测肤色
		msg_list.append(race)
		beauty = res_all_temp['beauty'] #检测颜值
		msg_list.append(str(beauty))
		glasses = res_all_temp['glasses']['type'] #是否佩戴眼镜
		msg_list.append(glasses)
		face_shape = res_all_temp['face_shape']['type'] #检测脸型
		msg_list.append(face_shape)
		gender = res_all_temp['gender']['type'] #检测性别
		msg_list.append(gender)
		expression = res_all_temp['expression']['type'] #检测表情
		msg_list.append(expression)
		return msg_list
	return "1"
