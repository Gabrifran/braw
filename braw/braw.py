from PyQt6 import QtWidgets,QtCore,QtGui  
from os import path,walk
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
class Braw():
	#pegar infomaçoes do site
	def site(self,ids,ndame):
			self.dados=[]
			self.ids=[38053418,32477494,68706658,45302045,12424251]
			self.browser = webdriver.Chrome()
			try:
				self.le=open(path.dirname(path.abspath(__file__))+f'\\{ndame}.txt','w')
			except:
				self.le=open(path.dirname(path.abspath(__file__))+f'\\{ndame}.txt','a')
			self.browser.get(f'https://www.corehalla.com/stats/player/{self.ids[ids]}')
			self.ker=BeautifulSoup(self.browser.page_source,'html.parser')

			for iho in self.ker.find('h1',attrs={'class':"font-bold text-3xl lg:text-5xl flex items-center" }):
				if iho.string:
					self.dados.append(iho.string)
			self.dados.append(self.ids[ids])
			for ie in self.ker.find_all('p',attrs={'class':"font-bold"}):
				if 'Peak' not in ie.text:
					for ue in ((ie.text).replace('games','')).split(' '):
						try:
							self.dados.append(int(ue))
						except:
							pass
			for taxa in self.ker.find_all('div',attrs={'class':"flex justify-between font-bold text-md mt-2"}):
				if (taxa.text).replace('5W (50.00%)5L (50.00%)',''):
					for des in (taxa.text).split(')'):
						for dler in des.split('('):
							if dler:
								self.dados.append(((dler).replace('W',"")).replace('L',""))	
			for i in self.ker.find_all('div',attrs={'class':"font-semibold text-lg mt-2"}):
				for oi in i :
					self.dados.append(oi.string)
			del self.dados[20:]
			for dado in self.dados:
				self.le.write(str(dado)+'\n')	
			self.le.write('\n_________________')
			for u in self.ker.find_all('div',attrs={'class':'relative w-8 h-8 overflow-hidden rounded-sm'}):
				for h in u.find_all('img',alt=True):
					self.le.write('\n'+h['alt'])
			self.browser.close()
			self.le.close()

	#Gui		
	def braw(self,main):
			main.setGeometry(QtCore.QRect(0,0,1038,736))
			self.imf=[QtGui.QPixmap('{}/img/Fundo.jpg'.format(path.dirname(path.abspath(__file__))).replace('\\','/')),
			QtGui.QPixmap(f'{path.dirname(path.abspath(__file__))}/img/none.png')]
			self.fun=QtWidgets.QLabel(main)
			self.fun.setPixmap(self.imf[0])
			self.fun.setGeometry(QtCore.QRect(0,0,1038,736))
			main.setMaximumSize(1038,736)
			main.setMinimumSize(1038,736)
			self.per=QtWidgets.QLabel(main)
			self.per.setPixmap(QtGui.QPixmap('{}/img/ger.png'.format((path.dirname(path.abspath(__file__))).replace('\\','/'))))
			self.per.setScaledContents(True)
			self.per.setGeometry(QtCore.QRect(450,0,600,400))
			self.p1=QtWidgets.QLabel(main)
			self.p1.setPixmap(self.imf[1])
			self.p1.setGeometry(QtCore.QRect(525,357,150,180))
			self.p1.setScaledContents(True)
			self.p2=QtWidgets.QLabel(main)
			self.p2.setPixmap(self.imf[1])
			self.p2.setScaledContents(True)
			self.p2.setGeometry(QtCore.QRect(710,310,150,180))
			self.p3=QtWidgets.QLabel(main)
			self.p3.setGeometry(QtCore.QRect(890,357,150,180))
			self.p3.setPixmap(self.imf[1])
			self.p3.setScaledContents(True)
			self.p=QtWidgets.QPushButton(main)
			self.p.setGeometry(QtCore.QRect(5,10,370,63))
			self.p.setStyleSheet('border-image:url({}/img/pao.png)'.format(path.dirname(path.abspath(__file__))).replace('\\','/'))
			self.pa=QtWidgets.QPushButton(main)
			self.pa.setGeometry(QtCore.QRect(370,10,63,63))
			self.pa.clicked.connect(lambda:self.site(1,'Paoqueimado'))
			self.pa.setStyleSheet("border-image:url({}/img/loop.png);".format(path.dirname(path.abspath(__file__))).replace('\\','/'))
			self.p.clicked.connect(lambda:self.link("Paoqueimado"))
			self.pe=QtWidgets.QPushButton(main)
			self.pe.setGeometry(QtCore.QRect(5,176,370,63))
			self.pe.clicked.connect(lambda:self.link("Pedro"))
			self.pe.setStyleSheet("border-image:url({}/img/pedro.png);".format(path.dirname(path.abspath(__file__))).replace('\\','/'))
			self.pea=QtWidgets.QPushButton(main)
			self.pea.setGeometry(QtCore.QRect(370,176,63,63))
			self.pea.setStyleSheet("border-image:url({}/img/loop.png);".format(path.dirname(path.abspath(__file__))).replace('\\','/'))
			self.pea.clicked.connect(lambda:self.site(2,"Pedro"))
			self.y=QtWidgets.QPushButton(main)
			self.ya=QtWidgets.QPushButton(main)
			self.ya.setGeometry(QtCore.QRect(370,93,63,63))
			self.ya.setStyleSheet("border-image:url({}/img/loop.png);".format(path.dirname(path.abspath(__file__))).replace('\\','/'))
			self.ya.clicked.connect(lambda:self.site(0,'Pablo YamoshiYamato'))
			self.y.setStyleSheet('border-image:url({}/img/pablo.png);'.format(path.dirname(path.abspath(__file__))).replace('\\','/'))
			self.y.setGeometry(QtCore.QRect(5,93,370,63))
			self.y.clicked.connect(lambda:self.link("Pablo YamoshiYamato"))
			self.l=QtWidgets.QPushButton(main)
			self.la=QtWidgets.QPushButton(main)
			self.la.setGeometry(QtCore.QRect(370,272,63,63))
			self.la.setStyleSheet("border-image:url({}/img/loop.png);".format(path.dirname(path.abspath(__file__))).replace('\\','/'))
			self.la.clicked.connect(lambda:self.site(3,'Luffy'))
			self.l.setStyleSheet('border-image:url({}/img/luffy.png);'.format(path.dirname(path.abspath(__file__))).replace('\\','/'))
			self.l.setGeometry(QtCore.QRect(5,272,370,63))
			self.l.clicked.connect(lambda:self.link("Luffy"))
			self.font=QtGui.QFont('Arial black',24)
			self.font1=QtGui.QFont('Arial black',12)
			self.pl=QtWidgets.QLabel(main)
			self.pl.setFont(self.font)
			self.pl.setStyleSheet("color:#93c5d3;")
			self.pl.setGeometry(QtCore.QRect(500,0,500,125))
			self.pln1=QtWidgets.QLabel(main)
			self.pln1.setGeometry(QtCore.QRect(500,-150,500,500))
			self.pln1.setFont(self.font1)
			self.pln1.setText(f'Acoount Level:\nGame time:\nKOs:\nDano Causado:\nVitorias:')
			self.pln1.setStyleSheet('''QLabel{
						   					color:#93c5d3;
						   					text-align: justify;
						   					padding-top: 55px;	
						   }''')

			self.pln2=QtWidgets.QLabel(main)
			self.pln2.setGeometry(QtCore.QRect(750,-150,500,500))
			self.pln2.setFont(self.font1)
			self.pln2.setText(f'Games:\nSuicides:\nFalls:\nDano Tomado:\nDerrotas:\nXp Total:')
			self.pln2.setStyleSheet('''QLabel{
						   					color:#93c5d3;
						   					text-align: jsutify;
						   					padding-top: 75px;	
						   }''')
			self.mb=QtWidgets.QLabel(main)
			self.selp1=QtWidgets.QListWidget(main)
			self.selp1.addItem('none')
			self.selp1.setGeometry(QtCore.QRect(500,500,165,30))
			self.selp1.setFont(self.font1)
			for f,oe,o in walk(path.dirname(path.abspath(__file__))+'\\img or\\po'):
				for ors in o:
					self.selp1.addItem(ors.replace('.webp',''))
			self.selp1.setStyleSheet('''QListWidget::item{
											border:0 px solid;
							
							}''')
			self.selp2=QtWidgets.QListWidget(main)
			self.selp2.setGeometry(QtCore.QRect(700,450,165,30))
			self.selp2.setAutoScroll(False)
			self.selp2.addItem('none')
			for f,oe,o in walk(path.dirname(path.abspath(__file__))+'\\img or\\po'):
				for ors in o:
					self.selp2.addItem(ors.replace('.webp',''))
			self.selp2.setStyleSheet('''QListWidget::item{
											border:0 px solid;
							
							}''')			
			self.selp3=QtWidgets.QListWidget(main)
			self.selp3.setGeometry(QtCore.QRect(875,500,165,30))
			self.selp3.setAutoScroll(False)
			self.selp3.addItem('none')
			for f,oe,o in walk(path.dirname(path.abspath(__file__))+'\\img or\\po'):
				for ors in o:
					self.selp3.addItem((ors).replace('.webp',''))
			self.selp3.setStyleSheet('''QListWidget::item{
											border:0 px solid;
							
							}''')
			self.selp1.currentItemChanged.connect(lambda:self.pesonagem(self.p1,self.selp1))
			self.selp2.currentItemChanged.connect(lambda:self.pesonagem(self.p2,self.selp2))
			self.selp3.currentItemChanged.connect(lambda:self.pesonagem(self.p3,self.selp3))
			self.selp2.setFont(self.font1)
			self.selp3.setFont(self.font1)
			self.ker={}
			for fs,s,sd in walk(path.dirname(path.abspath(__file__))+'\\img or\\po'):
				for ge in sd:
						self.ker[ge.replace('.webp','')]=QtGui.QPixmap(path.dirname(path.abspath(__file__))+'\\img or\\po\\'+ge)
	def link(self,ndame):
		self.mb.setMovie(QtGui.QMovie())
		self.mb.setGeometry(QtCore.QRect(500,500,500,500))
		self.le=open(path.dirname(path.abspath(__file__))+f'\\{ndame}.txt','r')
		self.lea=(self.le.read()).split("\n")
		self.p1.setPixmap(QtGui.QPixmap(path.dirname(path.abspath(__file__))+f'/img or/po/{self.lea[-2]}.webp'))
		self.p2.setPixmap(QtGui.QPixmap(path.dirname(path.abspath(__file__))+f'/img or/po/{self.lea[-3]}.webp'))
		self.p3.setPixmap(QtGui.QPixmap(path.dirname(path.abspath(__file__))+f'/img or/po/{self.lea[-1]}.webp'))
		self.pln1.setText(f'Acoount Level:{self.lea[17]}\nGame time:{self.lea[19]}\nKOs:{self.lea[4]}\nDano Causado:{self.lea[7]}\nVitorias:{self.lea[13]} {self.lea[14]}')
		self.pln2.setText(f'Games:{self.lea[2]}\nSuicides:{self.lea[6]}\nFalls:{self.lea[5]}\nDano Tomado:{self.lea[8]}\nDerrotas:{self.lea[15]} {self.lea[16]}\nXp Total:{self.lea[18]}')
		self.pl.setText(f'<center>{ndame}<center>')
		self.le.close()
	def pesonagem(self,p,pi):
			try:
				p.setPixmap(self.ker[(pi.item(pi.currentRow())).text()])
			except:
				p.setPixmap(QtGui.QPixmap(f'{path.dirname(path.abspath(__file__))}/img/none.png'))
if __name__ == '__main__':
	import sys
	app=QtWidgets.QApplication(sys.argv)
	app2=QtWidgets.QMainWindow()
	app3=Braw()
	app3.braw(main=app2)
	app2.show()
	sys.exit(app.exec())
