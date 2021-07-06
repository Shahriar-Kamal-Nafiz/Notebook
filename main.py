import datetime
mydate = datetime.datetime.now()

dd = mydate.strftime("%d")
mm = mydate.strftime("%B")
yy = mydate.strftime("%Y")
# print(dd,mm,yy)
day = mydate.strftime("%a")
hh = mydate.strftime("%I")
ap = mydate.strftime("%p")
mn = mydate.strftime("%M")

import os
if not os.path.exists("notebook.html"):
	with open("notebook.html","a") as init :
		init.write("""<!DOCTYPE html>
<html>
	<head>
		<meta http-equiv="content-type" content="text/html; charset=utf-8" />
		<meta name="" content="">
		<title></title>
		
	<!-- 	google font --> 
	<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Uchen&display=swap" rel="stylesheet">
		
		<style type="text/css" media="all">
			body{
				background: url(https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSBYvU1k3RWz20jy4zNhkSUDut2vOkysMC0jA&usqp=CAU);
			}
			.task{
				box-shadow: rgba(0, 0, 0, 0.25) 0px 14px 28px, rgba(0, 0, 0, 0.22) 0px 10px 10px;
				margin: 20px;
				background: rgb(173,255,241) ;
				width: 80%;
				padding: 25px;
				padding-left:15px ;
				margin-right: 20px;
				color: rgb(48,48,48) ;
				text-align: center;
				//animation: sc;
				transition: transform .5s;
				font-family: 'Uchen', serif;
				font-size: 18px;
				border-radius: 7px;
			}.task:hover{
				transform: scale(1.1);
				//text-shadow: 2px 2px #2fd5ff;
			}.date{
				float: right;
				text-align: right;
				font-family: monokai;
				font-size: 15px;
				display: block;
			}.time{
				float: left;
				text-align: left;
				font-family: monokai;
				font-size: 15px;
				display: block;
				
			}hr{
				font-weight: bolder;
				margin-top: 30px;
				color: #838383;
				width: 100%;
				height: 1px;
				border-bottom:none ;
			}
			timeline{
				padding-bottom:10px ;
			}
		</style>
	</head>
	<body>
""")

text = input("Write Something : ")
x = f"""
<div class="task">
			<div class="time">
				{day} , {hh}:{mn} {ap}
			</div>
			<div class="date">
				{dd},{mm},{yy}
			</div><hr />
			{text}
		</div>
"""
with open("notebook.html","a") as web:
	web.write(x)
print("Please view the notebook.html in the current directory .")