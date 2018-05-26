from PIL import Image

imagen=Image.open('/Users/admin/Desktop/Clase3/weeb.jpeg')

imagen.thumbnail((100,100))

imagen_convertida=''

colores=['9','8','7','6','5','4','3','2','1','0',' ']

ancho,alto=imagen.size

for nro_pixel,pixel in enumerate(imagen.getdata()):
	r,g,b=pixel
	color=(r+g+b)/3
	factor=color/255
	posicion=int(factor*(len(colores)-1))
	imagen_convertida+=colores[posicion]
	if nro_pixel%ancho==0:
		imagen_convertida+='\n'

archivo=open('weeb.txt','w')
archivo.write(imagen_convertida)
archivo.close()
#print(imagen_convertida)