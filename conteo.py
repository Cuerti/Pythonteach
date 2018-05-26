from PIL import Image,ImageDraw

imagen=Image.open('/Users/admin/Desktop/Clase3/weeb.jpeg')
#{x:'a' for x in range(3)} -->{0:'a',1:'a',2:'a'}
red=[0 for _ in range(256)]#{}
green=[0 for _ in range(256)]#{}
blue=[0 for _ in range(256)]#{}
for r,g,b in imagen.getdata():
	red[r]+=1
	green[g]+=1
	blue[b]+=1
	#if r not in red:
	#	red[r]=1
	#red[r]+=1
	#if g not in green:
	#	green[g]=1
	#green[g]+=1
	#if b not in blue:
	#	blue[b]=1
	#blue[b]+=1
def generar_histo(conteos, nombre_archivo):
	lienzo=Image.new('RGB',(256,256))
	lapi=ImageDraw.Draw(lienzo)

	maximo_conteo=max(conteos)
	for color,conteo in enumerate(conteos):
		factor=color/maximo_conteo
		lapi.line([(color,256),(color,256-factor*256)])

	lienzo.save(nombre_archivo)

generar_histo(red,'histored.jpg')
generar_histo(green,'histogreen.jpg')
generar_histo(blue,'histoblue.jpg')


#print(red)
#print(green)
#print(blue)