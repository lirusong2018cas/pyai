# -*- coding: utf-8 -*-
import os
from baidu_aip import *
from werkzeug.utils import secure_filename
from flask import Flask, flash, request, redirect, url_for,render_template

UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['GET', 'POST'])
def upload():
	if request.method == 'POST':
		# check if the post request has the file part
		if 'fileselect[]' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['fileselect[]']
		# if user does not select file, browser also
		# submit an empty part without filename
		if file.filename == '':
			flash('没有选择到文件')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			msg_all = aip_client(str(os.path.join(app.config['UPLOAD_FOLDER'], filename)))
		#else:
			#return render_template('tz.html',res_tz_a="What do you want to do？")
			if int(msg_all[0]) == 0:
				msg_all[0] = "成功"
				if msg_all[7] =='none':
					msg_all[7] = "面无表情"
				elif msg_all[7] == 'smile':
					msg_all[7] = '微微一笑很倾城'
				else:
					msg_all[7] = '看起来挺开心'
				if msg_all[4] == 'sun':
					msg_all[4] = '墨镜'
				elif msg_all[4] == 'common':
					msg_all[4] = '普通眼镜'
				else:
					msg_all[4] = '无'
				if msg_all[2] =='yellow':
					msg_all[2] = '黄色'
				elif msg_all[2] == 'black':
					msg_all[2] ='黑色'
				elif msg_all[2] == 'white':
					msg_all[2] = '白色'
				else:
					msg_all[2] = '阿拉伯'

				if msg_all[5] == 'oval':
					msg_all[5] = "椭圆"
				elif msg_all[5] == 'square':
					msg_all[5] = "正方形"
				elif msg_all[5] == 'triangle':
					msg_all[5] = "三角形"
				elif msg_all[5] == 'heart':
					msg_all[5] = "心形"
				else:
					msg_all[5] = '圆形'
				

				if msg_all[6] =='male':
					msg_all[6] = "男"
				else:
					msg_all[6] = "女"
				return render_template('res.html', result = msg_all[0],filename = filename,result_xb = msg_all[6],result_nl=msg_all[1],result_lx=msg_all[5],result_yz=msg_all[3],result_fs = msg_all[2],result_yj=msg_all[4],result_bq = msg_all[7])
			else:
				return render_template('tz.html',res_tz_a="识别失败，请尽量保证图片清晰，使用正脸！")
	return render_template('tz.html',res_tz_a="What do you want to do？")

def allowed_file(filename):
	return '.' in filename and \
			filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')


if __name__ == '__main__':
	app.run(host='0.0.0.0',port=80)
