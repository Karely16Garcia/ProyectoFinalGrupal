
de  tkinter  Importar  Botón , Etiqueta , Tk , diálogo de archivo , ttk , Marco , FotoImage
importar  pygame
importar al  azar
importar  mutágeno

de  mutágeno . mp3  importar  MP3

pygame . mezclador . pre_init ( frecuencia = 44100 )
pygame . mezclador . init ()
pygame . mezclador . init ( frecuencia = 44100 )
cancion_actual  = ''
direcion  =  ''



def  abrir_archivo ():
	 direcion global , pos , n , cancion_actual
	pos  =  0
	n  =  0
	direcion  =  filedialog . askopenfilenames ( dir_inicial  = '/' ,
											title = 'Escoger la cancion (es)' ,
										filetype = (( 'archivos mp3' , '* .mp3 *' ), ( 'Todos los archivos' , '*. *' )))
	n  =  len ( dirección )
	cancion_actual  =  direcion [ pos ]

	nombre_cancion  =  cancion_actual . dividir ( '/' )
	nombre_cancion  =  nombre_cancion [ - 1 ]

lista  = []
para  i  en el  rango ( 50 , 200 , 10 ):
	lista . añadir ( i )

def  iniciar_reproduccion ():
	 cancion_actual global , direcion , pos , n , actualizar
	barra1 [ 'valor' ] =  aleatorio . elección ( lista )
	barra2 [ 'valor' ] =  aleatorio . elección ( lista )
	barra3 [ 'valor' ] =  aleatorio . elección ( lista )
	barra4 [ 'valor' ] =  aleatorio . elección ( lista )
	barra5 [ 'valor' ] =  aleatorio . elección ( lista )
	barra6 [ 'valor' ] =  aleatorio . elección ( lista )
	barra7 [ 'valor' ] =  aleatorio . elección ( lista )
	barra8 [ 'valor' ] =  aleatorio . elección ( lista )
	barra9 [ 'valor' ] =  aleatorio . elección ( lista )
	barra10 [ 'valor' ] =  aleatorio . elección ( lista )
	barra11 [ 'valor' ] =  aleatorio . elección ( lista )
	barra12 [ 'valor' ] =  aleatorio . elección ( lista )
	barra13 [ 'valor' ] =  aleatorio . elección ( lista )
	barra14 [ 'valor' ] =  aleatorio . elección ( lista )
	barra15 [ 'valor' ] =  aleatorio . elección ( lista )
	barra16 [ 'valor' ] =  aleatorio . elección ( lista )
	barra17 [ 'valor' ] =  aleatorio . elección ( lista )
	barra18 [ 'valor' ] =  aleatorio . elección ( lista )
	barra19 [ 'valor' ] =  aleatorio . elección ( lista )
	barra20 [ 'valor' ] =  aleatorio . elección ( lista )
	barra21 [ 'valor' ] =  aleatorio . elección ( lista )
	barra22 [ 'valor' ] =  aleatorio . elección ( lista )
	barra23 [ 'valor' ] =  aleatorio . elección ( lista )
	barra24 [ 'valor' ] =  aleatorio . elección ( lista )
	barra25 [ 'valor' ] =  aleatorio . elección ( lista )
	barra26 [ 'valor' ] =  aleatorio . elección ( lista )
	barra27 [ 'valor' ] =  aleatorio . elección ( lista )
	barra28 [ 'valor' ] =  aleatorio . elección ( lista )
	barra29 [ 'valor' ] =  aleatorio . elección ( lista )
	barra30 [ 'valor' ] =  aleatorio . elección ( lista )
	
	

	cancion_actual  =  direcion [ pos ]
	nombre_cancion  =  cancion_actual . dividir ( '/' )
	nombre_cancion  =  nombre_cancion [ - 1 ]
	nombre [ 'texto' ] =  nombre_cancion

	tiempo  =  pygame . mezclador . la música . get_pos ()
	x  =  int ( int ( tiempo ) * 0.001 )
	tiempo [ 'valor' ] =  x   #posicion de la cancion

	y  =  float ( int ( volumen . get ()) * 0.1 )
	pygame . mezclador . la música . set_volume ( y )
	nivel [ 'texto' ] =  int ( y * 100 )

	audio  =  mutágeno . Archivo ( cancion_actual )	
	log  =  audio . info . largo
	minutos , segundos  =  divmod ( log , 60 )

	minutos , segundos  =  int ( minutos ), int ( segundos )
	tt  =  minutos * 60  +  segundos
	tiempo [ 'máximo' ] =  tt   # tiempo total de la cancion
	texto [ 'texto' ] =  str ( minutos ) +  ":"  +  str ( segundos )

	actualizar  =  ventana . después ( 100 , iniciar_reproduccion )

	si  x  ==  tt :
		ventana . after_cancel ( actualizar )
		texto [ 'texto' ] =  "00:00"
		detener_efecto ()

		si  pos  ! =  n :
			pos  =  pos  +  1
			ventana . después ( 100 , iniciar_reproduccion )
			pygame . mezclador . la música . jugar ()
		si  pos  ==  n :
			pos  =  0

def  iniciar ():
	 cancion_actual global

	pygame . mezclador . la música . cargar ( cancion_actual )
	pygame . mezclador . la música . jugar ()
	iniciar_reproduccion ()

def  retroceder ():
	 pos global , n

	si  pos  > 0 :
		pos  =  pos - 1
	otra cosa :
		pos  =  0
	cantidad [ 'texto' ] =  str ( pos ) + '/' + str ( n )

def  adelantar ():
	 pos global , n

	si  pos  ==  n - 1 :
		pos  =  0
	otra cosa :
		pos  =  pos  +  1
	cantidad [ 'texto' ] =  str ( pos ) + '/' + str ( n )


def  detener_efecto ():
	barra1 [ 'valor' ] =  50
	barra2 [ 'valor' ] =  60
	barra3 [ 'valor' ] =  70
	barra4 [ 'valor' ] =  80
	barra5 [ 'valor' ] =  90
	barra6 [ 'valor' ] =  100
	barra7 [ 'valor' ] =  90
	barra8 [ 'valor' ] =  80
	barra9 [ 'valor' ] =  70
	barra10 [ 'valor' ] =  60
	barra11 [ 'valor' ] =  60
	barra12 [ 'valor' ] =  70
	barra13 [ 'valor' ] =  80
	barra14 [ 'valor' ] =  90
	barra15 [ 'valor' ] =  100
	barra16 [ 'valor' ] =  90
	barra17 [ 'valor' ] =  80
	barra18 [ 'valor' ] =  70
	barra19 [ 'valor' ] =  60
	barra20 [ 'valor' ] =  50
	barra21 [ 'valor' ] =  60
	barra22 [ 'valor' ] =  60
	barra23 [ 'valor' ] =  70
	barra24 [ 'valor' ] =  80
	barra25 [ 'valor' ] =  90
	barra26 [ 'valor' ] =  100
	barra27 [ 'valor' ] =  90
	barra28 [ 'valor' ] =  80
	barra29 [ 'valor' ] =  70
	barra30 [ 'valor' ] =  60
	
	
	

def  detener ():
	 actualización global
	pygame . mezclador . la música . detener ()
	ventana . after_cancel ( actualizar )
	detener_efecto ()

   
def  pausa ():
	 actualización global
	pygame . mezclador . la música . pausa ()
	ventana . after_cancel ( actualizar )
	detener_efecto ()


def  continuar ():
	pygame . mezclador . la música . deshacer la pausa ()
	ventana . después ( 100 , iniciar_reproduccion )


ventana  = Tk ()
ventana . título ( 'Reproductor de Música' )
# ventana.iconbitmap ('icono.ico')
ventana . config ( bg = 'negro' )
ventana . redimensionable ( 12 , 34 )

estilo  =  ttk . Estilo ()
estilo . theme_use ( 'almeja' )
estilo . configure ( "Vertical.TProgressbar" , foreground = 'green2' , background = 'green2' , troughcolor = 'black' ,
	bordercolor = 'negro' , color claro = 'verde2' , color oscuro = 'verde2' )

frame1  =  Frame ( ventana , bg = 'black' , width = 600 , height = 350 )
marco1 . cuadrícula ( columna = 0 , fila = 0 , pegajosa = 'nsew' )
frame2  =  Frame ( ventana , bg = 'black' , width = 600 , height = 50 )
marco 2 . cuadrícula ( columna = 0 , fila = 1 , pegajosa = 'nsew' )

barra1  =  ttk . Barra de progreso ( frame1 , orient =  'vertical' , length = 300 ,   maximum = 300 , style = "Vertical.TProgressbar" ) #, takefocus = True mode = 'determinado',
barra1 . cuadrícula ( columna = 0 , fila = 0 , padx  =  1 )
barra2  =  ttk . Barra de progreso ( frame1 , orient =  'vertical' , length = 300 ,   maximum = 300 , style = "Vertical.TProgressbar" )
barra2 . cuadrícula ( columna = 1 , fila = 0 , padx  =  1 )
barra3  =  ttk . Barra de progreso ( frame1 , orient =  'vertical' , length = 300 ,   maximum = 300 , style = "Vertical.TProgressbar" )
barra3 . cuadrícula ( columna = 2 , fila = 0 , padx  =  1 )
barra4  =  ttk . Barra de progreso ( frame1 , orient =  'vertical' , length = 300 ,   maximum = 300 , style = "Vertical.TProgressbar" )
barra4 . cuadrícula ( columna = 3 , fila = 0 , padx  =  1 )
barra5  =  ttk . Barra de progreso ( frame1 , orient =  'vertical' , length = 300 ,   maximum = 300 , style = "Vertical.TProgressbar" )
barra5 . cuadrícula ( columna = 4 , fila = 0 , padx  =  1 )
barra6  =  ttk . Barra de progreso ( frame1 , orient =  'vertical' , length = 300 ,   maximum = 300 , style = "Vertical.TProgressbar" )
barra6 . cuadrícula ( columna = 5 , fila = 0 , padx  =  1 )
barra7  =  ttk . Barra de progreso ( frame1 , orient =  'vertical' , length = 300 ,   maximum = 300 , style = "Vertical.TProgressbar" ) #, takefocus = True
barra7 . cuadrícula ( columna = 6 , fila = 0 , padx  =  1 )
barra8  =  ttk . Barra de progreso ( frame1 , orient =  'vertical' , length = 300 ,   maximum = 300 , style = "Vertical.TProgressbar" )
barra8 . cuadrícula ( columna = 7 , fila = 0 , padx  =  1 )
barra9  =  ttk . Barra de progreso ( frame1 , orient =  'vertical' , length = 300 ,   maximum = 300 , style = "Vertical.TProgressbar" )
barra9 . cuadrícula ( columna = 8 , fila = 0 , padx  =  1 )
barra10  =  ttk . Barra de progreso ( frame1 , orient =  'vertical' , length = 300 ,   maximum = 300 , style = "Vertical.TProgressbar" )
barra10 . cuadrícula ( columna = 9 , fila = 0 , padx  =  1 )
barra11  =  ttk . Barra de progreso ( frame1 , orient =  'vertical' , length = 300 ,   maximum = 300 , style = "Vertical.TProgressbar" )
barra11 . cuadrícula ( columna = 10 , fila = 0 , padx  =  1 )
barra12  =  ttk . Barra de progreso ( frame1 , orient =  'vertical' , length = 300 ,   maximum = 300 , style = "Vertical.TProgressbar" )
barra12 . cuadrícula ( columna = 11 , fila = 0 , padx  =  1 )
barra13  =  ttk . Barra de progreso ( frame1 , orient =  'vertical' , length = 300 ,   maximum = 300 , style = "Vertical.TProgressbar" )
barra13 . cuadrícula ( columna = 12 , fila = 0 , padx  =  1 )
barra14  =  ttk . Barra de progreso ( frame1 , orient =  'vertical' , length = 300 ,   maximum = 300 , style = "Vertical.TProgressbar" )
barra14 . cuadrícula ( columna = 13 , fila = 0 , padx  =  1 )
barra15  =  ttk . Barra de progreso ( frame1 , orient =  'vertical' , length = 300 ,   maximum = 300 , style = "Vertical.TProgressbar" )
barra15 . cuadrícula ( columna = 14 , fila = 0 , padx  =  1 )
barra16  =  ttk . Barra de progreso ( frame1 , orient =  'vertical' , length = 300 ,   maximum = 300 , style = "Vertical.TProgressbar" )
barra16 . cuadrícula ( columna = 15 , fila = 0 , padx  =  1 )
barra17  =  ttk . Barra de progreso ( frame1 , orient =  'vertical' , length = 300 ,   maximum = 300 , style = "Vertical.TProgressbar" )
barra17 . cuadrícula ( columna = 16 , fila = 0 , padx  =  1 )
barra18  =  ttk . Barra de progreso ( frame1 , orient =  'vertical' , length = 300 ,   maximum = 300 , style = "Vertical.TProgressbar" )
barra18 . cuadrícula ( columna = 17 , fila = 0 , padx  =  1 )
barra19  =  ttk . Barra de progreso ( frame1 , orient =  'vertical' , length = 300 ,   maximum = 300 , style = "Vertical.TProgressbar" )
barra19 . cuadrícula ( columna = 18 , fila = 0 , padx  =  1 )
barra20  =  ttk . Barra de progreso ( frame1 , orient =  'vertical' , length = 300 ,   maximum = 300 , style = "Vertical.TProgressbar" )
barra20 . cuadrícula ( columna = 19 , fila = 0 , padx  =  1 )
barra21  =  ttk . Barra de progreso ( frame1 , orient =  'vertical' , length = 300 ,   maximum = 300 , style = "Vertical.TProgressbar" )
barra21 . cuadrícula ( columna = 20 , fila = 0 , padx  =  1 )
barra22  =  ttk . Barra de progreso ( frame1 , orient =  'vertical' , length = 300 ,   maximum = 300 , style = "Vertical.TProgressbar" )
barra22 . cuadrícula ( columna = 21 , fila = 0 , padx  =  1 )
barra23  =  ttk . Barra de progreso ( frame1 , orient =  'vertical' , length = 300 ,   maximum = 300 , style = "Vertical.TProgressbar" )
barra23 . cuadrícula ( columna = 22 , fila = 0 , padx  =  1 )
barra24  =  ttk . Barra de progreso ( frame1 , orient =  'vertical' , length = 300 ,   maximum = 300 , style = "Vertical.TProgressbar" )
barra24 . cuadrícula ( columna = 23 , fila = 0 , padx  =  1 )
barra25  =  ttk . Barra de progreso ( frame1 , orient =  'vertical' , length = 300 ,   maximum = 300 , style = "Vertical.TProgressbar" )
barra25 . cuadrícula ( columna = 24 , fila = 0 , padx  =  1 )
barra26  =  ttk . Barra de progreso ( frame1 , orient =  'vertical' , length = 300 ,   maximum = 300 , style = "Vertical.TProgressbar" )
barra26 . cuadrícula ( columna = 25 , fila = 0 , padx  =  1 )
barra27  =  ttk . Barra de progreso ( frame1 , orient =  'vertical' , length = 300 ,   maximum = 300 , style = "Vertical.TProgressbar" )
barra27 . cuadrícula ( columna = 26 , fila = 0 , padx  =  1 )
barra28  =  ttk . Barra de progreso ( frame1 , orient =  'vertical' , length = 300 ,   maximum = 300 , style = "Vertical.TProgressbar" )
barra28 . cuadrícula ( columna = 27 , fila = 0 , padx  =  1 )
barra29  =  ttk . Barra de progreso ( frame1 , orient =  'vertical' , length = 300 ,   maximum = 300 , style = "Vertical.TProgressbar" )
barra29 . cuadrícula ( columna = 28 , fila = 0 , padx  =  1 )
barra30  =  ttk . Barra de progreso ( frame1 , orient =  'vertical' , length = 300 ,   maximum = 300 , style = "Vertical.TProgressbar" )
barra30 . cuadrícula ( columna = 29 , fila = 0 , padx  =  1 )

estilo1  =  ttk . Estilo ()
estilo1 . theme_use ( 'almeja' )
estilo1 . configure ( "Horizontal.TProgressbar" , foreground = 'red' , background = 'black' , troughcolor = 'DarkOrchid1' ,
																bordercolor = '# 970BD9' , color claro = '# 970BD9' , color oscuro = 'negro' )

tiempo  =  ttk . Barra de progreso ( frame2 , orient =  'horizontal' , length  =  390 , mode = 'determinte' , style = "Horizontal.TProgressbar" )
tiempo . cuadrícula ( fila = 0 , columnpan = 8 , padx = 5 )
texto  =  Etiqueta ( marco2 , bg = 'negro' , fg = 'verde2' , ancho = 5 )
texto . cuadrícula ( fila = 0 , columna = 8 )

nombre  =  Etiqueta ( frame2 , bg = 'black' , fg = 'red' , width = 55 )
nombre . cuadrícula ( columna = 0 , fila = 1 , espacio de columnas = 8 , padx = 5 )
cantidad  =  Etiqueta ( frame2 , bg = 'black' , fg = 'green2' )
cantidad . cuadrícula ( columna = 8 , fila = 1 )

# imagen1 = PhotoImage (archivo = 'carpeta.png')
# imagen2 = PhotoImage (file = 'play.png')
# imagen3 = PhotoImage (archivo = 'pausa.png')
# imagen4 = PhotoImage (archivo = 'repetir.png')
# imagen5 = PhotoImage (file = 'stop.png')
# imagen6 = PhotoImage (file = 'anterior.png')
# imagen7 = PhotoImage (archivo = 'adelante.png')

boton1  =  Botón ( marco2 , ancho = 13 , alto = 3 , fuente = "Helvetica 9 negrita" , texto = "Abrir archivos" , comando =  abrir_archivo )
boton1 . cuadrícula ( columna = 0 , fila = 2 , pady = 10 )
boton2  =  Botón ( frame2 , bg = 'yellow' ,   width = 6 , height = 3 , font = "Helvetica 9 bold" , text = "Play" , command = iniciar )
boton2 . cuadrícula ( columna = 1 , fila = 2 , pady = 10 )
boton3  =  Botón ( frame2 , bg = 'red' , width = 6 , height = 3 , font = "Helvetica 9 bold" , text = "Stop" , command = stop )
boton3 . cuadrícula ( columna = 2 , fila = 2 , pady = 10 )
boton4  =  Botón ( frame2 , bg = 'blue' , width = 6 , height = 3 , font = "Helvetica 9 bold" , text = "Pausa" , command = pausa )
boton4 . cuadrícula ( columna = 3 , fila = 2 , pady = 10 )
boton5  =  Botón ( frame2 ,   bg = 'green2' , width = 7 , height = 3 , font = "Helvetica 9 bold" , text = "Continuar" , command = continuar )
boton5 . cuadrícula ( columna = 4 , fila = 2 , pady = 10 )
atras  =  Botón ( marco2 ,   bg = 'naranja' , ancho = 6 , alto = 3 , fuente = "Helvetica 9 negrita" , texto = "Anterior" , comando =  retroceder )
atras . cuadrícula ( columna = 5 , fila = 2 , pady = 10 )
adelante  =  Botón ( frame2 ,   bg = 'green' , width = 6 , height = 3 , font = "Helvetica 9 bold" , text = "Next" , command = adelantar )
adelante . cuadrícula ( columna = 6 , fila = 2 , pady = 10 )

volumen  =  ttk . Escala ( frame2 , to  =  10 , from_  = 0 , orient = 'horizontal' , length = 90 , style =  'Horizontal.TScale' )
volumen . cuadrícula ( columna = 7 , fila = 2 )

estilo  =  ttk . Estilo ()
estilo . configure ( "Horizontal.TScale" , bordercolor = 'green2' , troughcolor = 'black' , background =  'green2' ,
	primer plano = 'verde2' , color claro = 'verde2' , color oscuro = 'negro' )  

nivel  =  Etiqueta ( marco2 , bg = 'negro' , fg = 'verde2' , ancho = 3 )
nivel . cuadrícula ( columna = 8 , fila = 2 )

ventana . mainloop ()







































