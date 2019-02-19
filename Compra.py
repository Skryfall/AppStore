from tkinter import *
from tkinter import messagebox
import random

#Se definen las globales de almacenamiento de datos y globales de comprobación
#Se define la global idioma, si es 0 el idioma es español y si es 1 el idioma es en inglés
idioma = 0
#Se define la global descargas, si es 0 es en Costa Rica y si es 1 es en un país extranjero
descargas = 0
#Se define la global iniciado, si es 0 el usuario no ha iniciado sesión y si es 1 el usuario ya inició sesión
iniciado = 0
#Se define la global app que sirve de contador
app = 0
#Se define la global usuario que sirve de contador
usuario = 0
#Almacena los nombres de los compradores de la tienda
nombrecompradores = []
#Almacena las ids de los compradores de la tienda
idscompradores = []
#Almacena texto para introducirlo a una label
txt = ''
#Almacena si una app está activa o inactiva
estados = []
#Almacena las ids de los vendedores de las apps
idvendedores = []
#Almacena las ids de las aplicaciones
idproductos = []
#Almacena los nombres de las apps
nombreapps = []
#Almacena las categorías de las app
catapps = []
#Almacena las descripciones en español de las apps
descespapps = []
#Almacena las descripciones en inglés de las apps
descingapps = []
#Almacena los precios de las apps
preciosapps = []
#Almacena las ganancias totales generadas por las apps
totalprecios = []
#Almacena las descargas mundiales de cada app
descarmunapps = []
#Almacena las descargas en Costa Rica de cada app
descarcrapps = []
#Almacena los nombres de las screenshots 1 de cada app
screens1apps = []
#Almacena los nombres de las screenshots 2 de cada app
screens2apps = []

#Función para obtener los datos del archivo apps.txt
#E: Los datos de un archivo
#S: Los datos de las apps que se almacenarán en globales, almacenar los datos para comprobar si una app está activa o inactiva, almacenar las ids de cada app, almacenar las ids de los vendedores asociados a cada app, almacenar los nombres de las apps, almacenar las categorías de las apps, almacenar las descripciones en español e inglés de las apps, almacenar los precios de las apps, almacenar las ganancias totales, almacenar las descargas mundiales y en Costa Rica y almacenar los nombres de las screenshots 1 y 2
#R: El archivo a entrar tiene que ser apps.txt en modo lectura y el orden de los datos en el archivo deben estar de forma correcta
def leerapps(arch):
    global estados
    global idproductos
    global idvendedores
    global nombreapps
    global catapps
    global descespapps
    global descingapps
    global preciosapps
    global totalprecios
    global descarmunapps
    global descarcrapps
    global screens1apps
    global screens2apps
    a = arch.readline()
    if a == '':
        arch.close()
    else:
        a = a.split(",")
        estados = estados + [a[0]]
        idvendedores = idvendedores + [a[1]]
        idproductos = idproductos + [a[2]]
        nombreapps = nombreapps + [a[3]]
        catapps = catapps + [a[4]]
        descespapps = descespapps + [a[5]]
        descingapps = descingapps + [a[6]]
        preciosapps = preciosapps + [a[7]]
        totalprecios = totalprecios + [a[8]]
        descarmunapps = descarmunapps + [a[9]]
        descarcrapps = descarcrapps + [a[10]]
        screens1apps = screens1apps + [a[11]]
        b = a[12]
        c = len(b)
        screens2apps = screens2apps + [b[:c - 1]]
        return leerapps(arch)

arch = open("apps.txt", "r")
leerapps(arch)

#Función para colocar 3 apps al azar en la página frontal de la tienda
#E: La cantidad de elementos de la lista de las ids de las apps y tres números al azar
#S: La cantidad de elementos de la lista de las ids de las apps y tres números al azar
#R: Los números no deben ser iguales
def obtenerapps(ran, ran1, ran2, ran3):
    if ran1 == ran2:
        ran2 = random.randint(0, ran)
        return obtenerapps(ran, ran1, ran2, ran3)
    elif ran1 == ran3:
        ran3 = random.randint(0, ran)
        return obtenerapps(ran, ran1, ran2, ran3)
    elif ran2 == ran3:
        ran3 = random.randint(0, ran)
        return obtenerapps(ran, ran1, ran2, ran3)
    else:
        return obtenerapps_aux(ran, ran1, ran2, ran3)

#E: La cantidad de elementos de la lista de las ids de las apps y tres números al azar
#S: Tres números al azar
#R: Los tres números no deben tener una app inactiva asociada
def obtenerapps_aux(ran, ran1, ran2, ran3):
    global estados
    if estados[ran1] == "I":
        ran1 = random.randint(0, ran)
        return obtenerapps(ran, ran1, ran2, ran3)
    elif estados[ran2] == "I":
        ran2 = random.randint(0, ran)
        return obtenerapps(ran, ran1, ran2, ran3)
    elif estados[ran3] == "I":
        ran3 = random.randint(0, ran)
        return obtenerapps(ran, ran1, ran2, ran3)
    else:
        return obtenerapps_aux2(ran1, ran2, ran3)

#Este es un código de interfaz gráfica de la ventana principal de la tienda, el cual obtiene los 3 números al azar de las funciones anteriores
#Primero se obtiene la screenshot asociada a la app del primer número (cada número está relacionado a una id de una app) y se coloca en una label
#Se colocan 3 labels: el de del nombre de la app, el de la id de la app y el del precio de la app
#Finalmente, se hace lo mismo con el segundo número y el tercer número
def obtenerapps_aux2(ran1, ran2, ran3):
    global nombreapps
    global idproductos
    global screens1apps
    global preciosapps
    img1 = PhotoImage(file = screens1apps[ran1])
    labelimg1 = Label(compra, image = img1)
    labelimg1.place(x = 50, y = 250)
    labelimg1.image = img1
    nom1 = Label(compra, text = nombreapps[ran1], font = ("IMPACT", "14"), bg = "#3A0C60", fg = "#C6BAD1")
    nom1.place(x = 60, y = 200)
    id1 = Label(compra, text = idproductos[ran1], font = ("IMPACT", "16"), bg = "#3A0C60", fg = "#C6BAD1")
    id1.place(x = 150, y = 500)
    precio1 = Label(compra, text = preciosapps[ran1] + "$", font = ("IMPACT", "16"), bg = "#3A0C60", fg = "#C6BAD1")
    precio1.place(x = 150, y = 550)
    img2 = PhotoImage(file = screens1apps[ran2])
    labelimg2 = Label(compra, image = img2)
    labelimg2.place(x = 370, y = 250)
    labelimg2.image = img2
    nom2 = Label(compra, text = nombreapps[ran2], font = ("IMPACT", "14"), bg = "#3A0C60", fg = "#C6BAD1")
    nom2.place(x = 380, y = 200)
    id2 = Label(compra, text = idproductos[ran2], font = ("IMPACT", "16"), bg = "#3A0C60", fg = "#C6BAD1")
    id2.place(x = 470, y = 500)
    precio2 = Label(compra, text = preciosapps[ran2] + "$", font = ("IMPACT", "16"), bg = "#3A0C60", fg = "#C6BAD1")
    precio2.place(x = 470, y = 550)
    img3 = PhotoImage(file = screens1apps[ran3])
    labelimg3 = Label(compra, image = img3)
    labelimg3.place(x = 700, y = 250)
    labelimg3.image = img3
    nom3 = Label(compra, text = nombreapps[ran3], font = ("IMPACT", "14"), bg = "#3A0C60", fg = "#C6BAD1")
    nom3.place(x = 710, y = 200)
    id3 = Label(compra, text = idproductos[ran3], font = ("IMPACT", "16"), bg = "#3A0C60", fg = "#C6BAD1")
    id3.place(x = 800, y = 500)
    precio3 = Label(compra, text = preciosapps[ran3] + "$", font = ("IMPACT", "16"), bg = "#3A0C60", fg = "#C6BAD1")
    precio3.place(x = 800, y = 550)

#Este es un código de interfaz gráfica del menú principal de la tienda
#Se asignan las características de la ventana del menú principal, se coloca un canvas y dos Entrys (el de búsqueda y el de compra)
#Se obtiene el largo de la lista de la ids de productos, se obtienen los 3 números al azar entre el rango de la cantidad de ids y se ejecuta la función de obtenerapps
#Se colocan 3 labels, las cuales son de las Ids de las apps
compra = Tk()
compra.title("KsCz Astore")
compra.withdraw()
compra.minsize(1000, 700)
compra.maxsize(1000, 700)
canvascomp = Canvas(compra, width = 1000, height = 700, bg = "#3A0C60")
canvascomp.place(x = 0, y = 0)
insidapp = Entry(compra)
insidapp.place(x = 750, y = 660)
ran = len(idproductos) - 1
ran1 = random.randint(0, ran)
ran2 = random.randint(0, ran)
ran3 = random.randint(0, ran)
obtenerapps(ran, ran1, ran2, ran3)
idapp1 = Label(compra, text = "ID:", font = ("IMPACT", "16"), bg = "#3A0C60", fg = "#C6BAD1")
idapp1.place(x = 80, y = 500)
idapp2 = Label(compra, text = "ID:", font = ("IMPACT", "16"), bg = "#3A0C60", fg = "#C6BAD1")
idapp2.place(x = 400, y = 500)
idapp3 = Label(compra, text = "ID:", font = ("IMPACT", "16"), bg = "#3A0C60", fg = "#C6BAD1")
idapp3.place(x = 730, y = 500)
buscador = Entry(compra)
buscador.place(x = 350, y = 50)

#Este es un código de interfaz gráfica del inicio de sesión de la tienda
#Se asignan las características de la ventana de inicio de sesión, se coloca un canvas y 4 Entrys (el de nombre y correo de iniciar sesión y los mismos dos de registrarse)
iniciar = Toplevel(width = 600, height = 300)
iniciar.maxsize(600, 300)
iniciar.minsize(600, 300)
canvasinicio = Canvas(iniciar, width = 600, height = 300, bg = "#3A0C60")
canvasinicio.place(x = 0, y = 0)
canvasinicio.create_line(280, 10, 280, 290, fill = "#C6BAD1")
insnoms = Entry(iniciar)
insnoms.place(x = 12, y = 100) 
inscorreos = Entry(iniciar)
inscorreos.place(x = 12, y = 150)
insnomr = Entry(iniciar)
insnomr.place(x = 300, y = 100)
inscorreor = Entry(iniciar)
inscorreor.place(x = 300, y = 150)
iniciar.withdraw()

#Este es un código de interfaz gráfica de la tabla de compradores de la tienda
#Se asignan las características de la ventana de la tabla de compradores y se coloca un canvas
tabla = Toplevel(width = 600, height = 500)
tabla.maxsize(600, 500)
tabla.minsize(600, 500)
canvastabla = Canvas(tabla, width = 600, height = 500, bg = "#3A0C60")
canvastabla.place(x = 0, y = 0)
tabla.withdraw()

#Este es un código de interfaz gráfica del F.A.Q. del programa
#Se asignan las características de la ventana del F.A.Q. y se coloca un canvas
pregun = Toplevel(width = 500, height = 240)
pregun.maxsize(500, 240)
pregun.minsize(500, 240)
canvaspregun = Canvas(pregun, width = 500, height = 240, bg = "#3A0C60")
canvaspregun.place(x = 0, y = 0)
pregun.withdraw()

#Este es un código de interfaz gráfica de la pantalla de compra del programa
#Se asignan las características de la ventana de la pantalla de compra y se coloca un canvas
#Se colocan 3 labels
pcompra = Toplevel(width = 720, height = 400)
pcompra.maxsize(720, 400)
pcompra.minsize(720, 400)
pcanvas = Canvas(pcompra, width = 720, height = 400, bg = "#3A0C60")
pcanvas.place(x = 0, y = 0)
nombre = Label(pcompra, font = ("LMSansDemiCond10", "16"),  bg = "#3A0C60", fg = "#C6BAD1")
prec = Label(pcompra, font = ("LMSansDemiCond10", "16"),  bg = "#3A0C60", fg = "#C6BAD1")
desc = Label(pcompra, font = ("LMSansDemiCond10", "12"),  bg = "#3A0C60", fg = "#C6BAD1")
pcompra.withdraw()

#Se asigna la global de la ventana de búsqueda
busqueda = Toplevel

#E: Un número al azar del 10 al 99 y el respaldo de la ids de los compradores
#S: Un número al azar del 10 al 99
#R: El número a retornar no puede repetirse a la de los compradores
def randomizar(num, idsr):
    global idscompradores
    if idsr == []:
        return num
    elif num == int(idsr[0]):
        return randomizar(random.randint(10,99), idscompradores)
    else:
        return randomizar(num, idsr[1:])

#E: Los datos del archivo compradores.txt
#S: Los datos de los nombres de los compradores y las ids de los compradores
#R: Debe ser el archivo de compradores.txt
def comprobar_compradores(arch):
    global nombrecompradores
    global idscompradores
    a = arch.readline()
    if a == '':
        arch.close()
        iniciar.deiconify()
    else:
        a = a.split(",")
        nombrecompradores = nombrecompradores + [a[0]]
        idscompradores = idscompradores + [a[1]]
        return comprobar_compradores(arch)

#Función para leer los datos del archivo compradores.txt y colocarlos en la tabla
#E: Los datos del archivo compradores.txt y un contador
#S: Una label en la ventana de la tabla de compradores, con los datos de los compradores registrados
#R: Debe ser el archivo de compradores.txt
def leercompradores(arch, txt):
    a = arch.readline()
    if a == '':
        arch.close()
        tcomp = Label(tabla, text = txt, font = ("LMSansDemiCond10", "12"),  bg = "#3A0C60", fg = "#C6BAD1")
        tcomp.place(x = 30 , y = 110)
        tabla.deiconify()
    else:
        a = a.split(",")
        txt = txt + a[1] + '   ' + a[0] + '   ' + a[2] + '   ' + a[3] + '\n'
        return leercompradores(arch, txt)

#E: Un botón
#S: Cambiar la global descargas a 1, para indicar que se ingresó a la tienda desde un país extranjero hispanohablante y ejecuta la función de Costa Rica
def paislat():
    global descargas
    descargas = 1
    paiscr()

#Este es un código de interfaz gráfica en general de la tienda
#Lo que hace esta función es que si el país que elije el usuario es de habla española se colocan todos los labels en español en todas las ventanas del programa
#También se colocan los botones en idioma español en sus ventanas correspondientes
def paiscr():
    pais.destroy()
    compra.deiconify()
    nombre = Label(compra, text = "BIENVENIDO USUARIO \n A KSCZ STORE", font = ("IMPACT", "16"), bg = "#3A0C60", fg = "#C6BAD1")
    nombre.place(x = 10, y = 10)
    requiere = Label(compra, text = "Requiere iniciar sesión o crear una cuenta para comprar, \n puede hacerlo ya (presionando el botón de abajo) \n o más adelante", font = ("Times New Roman", "12"), bg = "#3A0C60", fg = "#C6BAD1")
    requiere.place(x = 600, y = 10)
    inicio = Button(compra, text = "Registrarse ó \n Iniciar Sesión", font = ("LMSansDemiCond10", "12"), bg = "#9E84B3", fg = "#C6BAD1", command = iniciarsesionven)
    inicio.place(x = 720, y = 80)
    usuarios = Button(compra, text = "Lista de Usuarios \n Registrados", font = ("LMSansDemiCond10", "12"), bg = "#9E84B3", fg = "#C6BAD1", command = iniciartabla)
    usuarios.place(x = 25, y = 80)
    faq = Button(compra, text = "F.A.Q.", font = ("IMPACT", "12"), bg = "#9E84B3", fg = "#C6BAD1", command = pregun.deiconify)
    faq.place(x = 20, y = 650)
    inserteidapp = Label(compra, text = "Inserte la ID de la App a comprar:", font = ("LMSansDemiCond10", "12"), bg = "#3A0C60", fg = "#C6BAD1")
    inserteidapp.place(x = 730, y = 620)
    revisar = Button(compra, text = "Revisar", font = ("IMPACT", "12"), bg = "#9E84B3", fg = "#C6BAD1", command = revisarapps)
    revisar.place(x = 890, y = 653)
    cerrarcom = Button(compra, text = "Cerrar", font = ("IMPACT", "12"), bg = "#9E84B3", fg = "#C6BAD1", command = compra.destroy)
    cerrarcom.place(x = 70, y = 650)
    precio1 = Label(compra, text = "Precio:", font = ("IMPACT", "16"), bg = "#3A0C60", fg = "#C6BAD1")
    precio1.place(x = 50, y = 550)
    precio2 = Label(compra, text = "Precio:", font = ("IMPACT", "16"), bg = "#3A0C60", fg = "#C6BAD1")
    precio2.place(x = 370, y = 550)
    precio3 = Label(compra, text = "Precio:", font = ("IMPACT", "16"), bg = "#3A0C60", fg = "#C6BAD1")
    precio3.place(x = 700, y = 550)
    cat = Label(compra, text = "Números de Categorías en el F.A.Q.", font = ("Times New Roman", "14"), bg = "#3A0C60", fg = "#C6BAD1")
    cat.place(x = 20, y = 600)
    buscas = Label(compra, text = "¿Buscas algo?", font = ("IMPACT", "14"), bg = "#3A0C60", fg = "#C6BAD1")
    buscas.place(x = 350, y = 10)
    buscar = Button(compra, text = "Buscar", font = ("IMPACT", "12"), bg = "#9E84B3", fg = "#C6BAD1", command = buscadorapps)
    buscar.place(x = 385, y = 80)
    recomen = Label(compra, text = "Algunas Recomendaciones:", font = ("Times New Roman", "14"), bg = "#3A0C60", fg = "#C6BAD1")
    recomen.place(x = 350, y = 150)
        
    iniciar.title("Iniciar Sesión/Registrarse")
    ini = Label(iniciar, text = "Iniciar Sesión", font = ("LMSansDemiCond10", "12"),  bg = "#3A0C60", fg = "#C6BAD1")
    ini.place(x = 80, y = 30)
    reg = Label(iniciar, text = "Registrarse", font = ("LMSansDemiCond10", "12"),  bg = "#3A0C60", fg = "#C6BAD1")
    reg.place(x = 380, y = 30)
    noms = Label(iniciar, text = "Nombre y Primer Apellido:", font = ("LMSansDemiCond10", "12"),  bg = "#3A0C60", fg = "#C6BAD1")
    noms.place(x = 10, y = 75)
    correos = Label(iniciar, text = "Correo:", font = ("LMSansDemiCond10", "12"),  bg = "#3A0C60", fg = "#C6BAD1")
    correos.place(x = 10, y = 125)
    nomr = Label(iniciar, text = "Nombre y Primer Apellido:", font = ("LMSansDemiCond10", "12"),  bg = "#3A0C60", fg = "#C6BAD1")
    nomr.place(x = 298, y = 75)
    correor = Label(iniciar, text = "Correo:", font = ("LMSansDemiCond10", "12"),  bg = "#3A0C60", fg = "#C6BAD1")
    correor.place(x = 298, y = 125)
    cancelar = Button(iniciar, text = "Cancelar", font = ("IMPACT", "12"), bg = "#9E84B3", fg = "#C6BAD1", command = iniciarwithdraw)
    cancelar.place(x = 520, y = 250)
    inse = Button(iniciar, text = "Iniciar Sesión", font = ("LMSansDemiCond10", "12"), bg = "#9E84B3", fg = "#C6BAD1", command = iniciarsesion)
    inse.place(x = 80, y = 210)
    rese = Button(iniciar, text = "Registrarse", font = ("LMSansDemiCond10", "12"), bg = "#9E84B3", fg = "#C6BAD1", command = registrarse)
    rese.place(x = 380, y = 210)

    tabla.title("Tabla de Compradores")
    tablac = Label(tabla, text = "Tabla de Compradores", font = ("LMSansDemiCond10", "14"),  bg = "#3A0C60", fg = "#C6BAD1")
    tablac.place(x = 200, y = 20)
    estruc = Label(tabla, text = "Estructura:", font = ("LMSansDemiCond10", "8"),  bg = "#3A0C60", fg = "#C6BAD1")
    estruc.place(x = 30, y = 20)
    idc = Label(tabla, text = "ID Comprador", font = ("LMSansDemiCond10", "10"),  bg = "#3A0C60", fg = "#C6BAD1")
    idc.place(x = 30, y = 50)
    nomc = Label(tabla, text = "Nombre del Comprador", font = ("LMSansDemiCond10", "10"),  bg = "#3A0C60", fg = "#C6BAD1")
    nomc.place(x = 120, y = 50)
    corrc = Label(tabla, text = "Correo del Comprador", font = ("LMSansDemiCond10", "10"),  bg = "#3A0C60", fg = "#C6BAD1")
    corrc.place(x = 270, y = 50)
    apcom = Label(tabla, text = "Apps Compradas", font = ("LMSansDemiCond10", "10"),  bg = "#3A0C60", fg = "#C6BAD1")
    apcom.place(x = 415, y = 50)
    esp = Label(tabla, text = "----------------------------------------------------------------------------------------------------------------------------------------------", font = ("LMSansDemiCond10", "10"),  bg = "#3A0C60", fg = "#C6BAD1")
    esp.place(x = 10, y = 80)
    cerrar = Button(tabla, text = "Cerrar", font = ("LMSansDemiCond10", "12"), bg = "#9E84B3", fg = "#C6BAD1", command = tabla.withdraw)
    cerrar.place(x = 520, y = 450)

    txt = "¿Cómo comprar? \n Para comprar en esta appstore es bastante sencillo, simplemente debes escribir \n la ID de la app que quieres en la barra de la esquina inferior derecha de la ventana \n principal y presionar el botón, al hacerlo se te enviará a la pantalla de compra. \n Cerca de los nombres de todas las apps de esta tienda se encuentra la ID \n perteneciente a la app que quieras comprar. \n \n Debes estar registrado para poder comprar. \n Gracias. :) \n \n Categorías: \n 1 - Plataformas     2 - Acción     3 - Disparos \n 4 - Puzzles     5 - Terror     6 - Otro"
    como = Label(pregun, text = txt, font = ("LMSansDemiCond10", "10"), justify = LEFT,  bg = "#3A0C60", fg = "#C6BAD1")
    como.place(x = 10, y = 10)
    cerrarfaq = Button(pregun, text = "Cerrar", font = ("LMSansDemiCond10", "12"), bg = "#9E84B3", fg = "#C6BAD1", command = pregun.withdraw)
    cerrarfaq.place(x = 430, y = 200)

    preci = Label(pcompra, text = "Precio ($):", font = ("LMSansDemiCond10", "16"),  bg = "#3A0C60", fg = "#C6BAD1")
    preci.place(x = 10, y = 50)
    cerrarc = Button(pcompra, text = "Cerrar", font = ("LMSansDemiCond10", "12"), bg = "#9E84B3", fg = "#C6BAD1", command = pcompra.withdraw)
    cerrarc.place(x = 650, y = 350)
    desc = Label(pcompra, text = "Descripción:", font = ("LMSansDemiCond10", "16"), bg = "#3A0C60", fg = "#C6BAD1")
    desc.place(x = 10, y = 250)
    comprar = Button(pcompra, text = "Comprar", font = ("LMSansDemiCond10", "12"), bg = "#9E84B3", fg = "#C6BAD1", command = iniciarcompra)
    comprar.place(x = 10, y = 120)

#Este es un código de interfaz gráfica en general de la tienda
#Lo que hace esta función es que si el país que elije el usuario es de habla inglesa se colocan todos los labels en inglés en todas las ventanas del programa
#También se colocan los botones en idioma inglés en sus ventanas correspondientes
def paising():
    global descargas
    global idioma
    idioma = 1
    descargas = 1
    pais.destroy()
    compra.deiconify()
    nombre = Label(compra, text = "WELCOME USER \n A KSCZ STORE", font = ("IMPACT", "16"), bg = "#3A0C60", fg = "#C6BAD1")
    nombre.place(x = 30, y = 10)
    requiere = Label(compra, text = "It is required to log in in order to buy in this Astore, \n you can do it now (pressing the button below) \n or later", font = ("Times New Roman", "12"), bg = "#3A0C60", fg = "#C6BAD1")
    requiere.place(x = 600, y = 10)
    inicio = Button(compra, text = "Register or \n Log In", font = ("LMSansDemiCond10", "12"), bg = "#9E84B3", fg = "#C6BAD1", command = iniciarsesionven)
    inicio.place(x = 720, y = 80)
    usuarios = Button(compra, text = "List of Registered \n Users", font = ("LMSansDemiCond10", "12"), bg = "#9E84B3", fg = "#C6BAD1", command = iniciartabla)
    usuarios.place(x = 25, y = 80)
    faq = Button(compra, text = "F.A.Q.", font = ("IMPACT", "12"), bg = "#9E84B3", fg = "#C6BAD1", command = pregun.deiconify)
    faq.place(x = 20, y = 650)
    inserteidapp = Label(compra, text = "Insert the ID of the app you want to buy:", font = ("LMSansDemiCond10", "12"), bg = "#3A0C60", fg = "#C6BAD1")
    inserteidapp.place(x = 710, y = 620)
    revisar = Button(compra, text = "Check", font = ("IMPACT", "12"), bg = "#9E84B3", fg = "#C6BAD1", command = revisarapps)
    revisar.place(x = 890, y = 653)
    cerrarcom = Button(compra, text = "Close", font = ("IMPACT", "12"), bg = "#9E84B3", fg = "#C6BAD1", command = compra.destroy)
    cerrarcom.place(x = 70, y = 650)
    precio1 = Label(compra, text = "Price:", font = ("IMPACT", "16"), bg = "#3A0C60", fg = "#C6BAD1")
    precio1.place(x = 50, y = 550)
    precio2 = Label(compra, text = "Price:", font = ("IMPACT", "16"), bg = "#3A0C60", fg = "#C6BAD1")
    precio2.place(x = 370, y = 550)
    precio3 = Label(compra, text = "Price:", font = ("IMPACT", "16"), bg = "#3A0C60", fg = "#C6BAD1")
    precio3.place(x = 700, y = 550)
    cat = Label(compra, text = "Categories Numbers in the F.A.Q.", font = ("Times New Roman", "14"), bg = "#3A0C60", fg = "#C6BAD1")
    cat.place(x = 20, y = 600)
    buscas = Label(compra, text = "¿Looking for something?", font = ("IMPACT", "14"), bg = "#3A0C60", fg = "#C6BAD1")
    buscas.place(x = 320, y = 10)
    buscar = Button(compra, text = "Search", font = ("IMPACT", "12"), bg = "#9E84B3", fg = "#C6BAD1", command = buscadorapps)
    buscar.place(x = 385, y = 80)
    recomen = Label(compra, text = "Some Recomendations:", font = ("Times New Roman", "14"), bg = "#3A0C60", fg = "#C6BAD1")
    recomen.place(x = 350, y = 150)
        
    iniciar.title("Log In/Register")
    ini = Label(iniciar, text = "Log In", font = ("LMSansDemiCond10", "12"),  bg = "#3A0C60", fg = "#C6BAD1")
    ini.place(x = 80, y = 30)
    reg = Label(iniciar, text = "Register", font = ("LMSansDemiCond10", "12"),  bg = "#3A0C60", fg = "#C6BAD1")
    reg.place(x = 380, y = 30)
    noms = Label(iniciar, text = "Name and Last Name:", font = ("LMSansDemiCond10", "12"),  bg = "#3A0C60", fg = "#C6BAD1")
    noms.place(x = 10, y = 75)
    correos = Label(iniciar, text = "Email:", font = ("LMSansDemiCond10", "12"),  bg = "#3A0C60", fg = "#C6BAD1")
    correos.place(x = 10, y = 125)
    nomr = Label(iniciar, text = "Name and Last Name:", font = ("LMSansDemiCond10", "12"),  bg = "#3A0C60", fg = "#C6BAD1")
    nomr.place(x = 298, y = 75)
    correor = Label(iniciar, text = "Email:", font = ("LMSansDemiCond10", "12"),  bg = "#3A0C60", fg = "#C6BAD1")
    correor.place(x = 298, y = 125)
    cancelar = Button(iniciar, text = "Cancel", font = ("IMPACT", "12"), bg = "#9E84B3", fg = "#C6BAD1", command = iniciarwithdraw)
    cancelar.place(x = 520, y = 250)
    inse = Button(iniciar, text = "Log In", font = ("LMSansDemiCond10", "12"), bg = "#9E84B3", fg = "#C6BAD1", command = iniciarsesion)
    inse.place(x = 80, y = 210)
    rese = Button(iniciar, text = "Register", font = ("LMSansDemiCond10", "12"), bg = "#9E84B3", fg = "#C6BAD1", command = registrarse)
    rese.place(x = 380, y = 210)

    tabla.title("Buyers Table")
    tablac = Label(tabla, text = "Buyers Table", font = ("LMSansDemiCond10", "14"),  bg = "#3A0C60", fg = "#C6BAD1")
    tablac.place(x = 200, y = 20)
    estruc = Label(tabla, text = "Structure:", font = ("LMSansDemiCond10", "8"),  bg = "#3A0C60", fg = "#C6BAD1")
    estruc.place(x = 30, y = 20)
    idc = Label(tabla, text = "Buyer's ID", font = ("LMSansDemiCond10", "10"),  bg = "#3A0C60", fg = "#C6BAD1")
    idc.place(x = 30, y = 50)
    nomc = Label(tabla, text = "Buyer's Name", font = ("LMSansDemiCond10", "10"),  bg = "#3A0C60", fg = "#C6BAD1")
    nomc.place(x = 120, y = 50)
    corrc = Label(tabla, text = "Buyer's Email", font = ("LMSansDemiCond10", "10"),  bg = "#3A0C60", fg = "#C6BAD1")
    corrc.place(x = 270, y = 50)
    apcom = Label(tabla, text = "Bought Apps", font = ("LMSansDemiCond10", "10"),  bg = "#3A0C60", fg = "#C6BAD1")
    apcom.place(x = 415, y = 50)
    esp = Label(tabla, text = "----------------------------------------------------------------------------------------------------------------------------------------------", font = ("LMSansDemiCond10", "10"),  bg = "#3A0C60", fg = "#C6BAD1")
    esp.place(x = 10, y = 80)
    cerrar = Button(tabla, text = "Close", font = ("LMSansDemiCond10", "12"), bg = "#9E84B3", fg = "#C6BAD1", command = tabla.withdraw)
    cerrar.place(x = 520, y = 450)

    txt = "¿How to buy? \n Buying in this appstore is really simple, you only have to write \n the ID of the app you want in the entry that is located on the right lower side \n of the main window and press the button, you will be sent to the buying window. \n You can find the apps' IDs near their names. \n \n You must be registered in order to buy. \n Thank You. :) \n \n Categories: \n 1 - Platforming     2 - Action     3 - Shooter \n 4 - Puzzles     5 - Terror     6 - Other"
    como = Label(pregun, text = txt, font = ("LMSansDemiCond10", "10"), justify = LEFT,  bg = "#3A0C60", fg = "#C6BAD1")
    como.place(x = 10, y = 10)
    cerrarfaq = Button(pregun, text = "Close", font = ("LMSansDemiCond10", "12"), bg = "#9E84B3", fg = "#C6BAD1", command = pregun.withdraw)
    cerrarfaq.place(x = 430, y = 200)

    preci = Label(pcompra, text = "Price ($):", font = ("LMSansDemiCond10", "16"),  bg = "#3A0C60", fg = "#C6BAD1")
    preci.place(x = 10, y = 50)
    cerrarc = Button(pcompra, text = "Close", font = ("LMSansDemiCond10", "12"), bg = "#9E84B3", fg = "#C6BAD1", command = pcompra.withdraw)
    cerrarc.place(x = 650, y = 350)
    desc = Label(pcompra, text = "Description:", font = ("LMSansDemiCond10", "16"), bg = "#3A0C60", fg = "#C6BAD1")
    desc.place(x = 10, y = 250)
    comprar = Button(pcompra, text = "Buy", font = ("LMSansDemiCond10", "12"), bg = "#9E84B3", fg = "#C6BAD1", command = iniciarcompra)
    comprar.place(x = 10, y = 120)

#Función para revisar la existencia de una app de la lista
#E: Un botón
#S: La cadena de la Entry de ingresar la ID de la App para la ventana de compra
def revisarapps():
    global app
    app = 0
    idapp = insidapp.get()
    insidapp.delete(0, END)
    revisarapps_aux(idapp)

#E: ID de la app introducida
#S: Conseguir la posición de la app a mostrar en la ventana de compra
#R: La app tiene que existir
def revisarapps_aux(idapp):
    global idproductos
    global app
    if len(idproductos) == app:
        return messagebox.showinfo("Error", "La app no existe/The app doesn´t exists")
    elif idapp == idproductos[app]:
        return revisarapps_aux2()
    else:
        app += 1
        return revisarapps_aux(idapp)

#Esta función revisa si la global app, donde tengo almacenada la posición de la app a mostrar está activa o inactiva
def revisarapps_aux2():
    global estados
    global app
    if estados[app] == "I":
        return messagebox.showinfo("Error", "La app no está disponible/The app isn´t available")
    else:
        return revisarapps_aux3()

#Este es un código de interfaz gráfica de la ventana de compra
#Lo que hace esta función es colocar en labels en todos los datos de importancia de la App para poder comprarla, screenshots, precio y nombre
#Si la global idioma es 0, coloca en una label la descripción en español, sino en inglés
def revisarapps_aux3():
    global app
    global nombreapps
    global descespapps
    global descingapps
    global preciosapps
    global screens1apps
    global screens2apps
    global idioma
    pcompra.update()
    nombre.config(text = nombreapps[app])
    nombre.place(x = 10, y = 10)
    img1 = PhotoImage(file = screens1apps[app])
    screen1 = Label(pcompra, image = img1)
    screen1.place(x = 250, y = 10)
    screen1.image = img1
    img2 = PhotoImage(file = screens2apps[app])
    screen2 = Label(pcompra, image = img2)
    screen2.place(x = 480, y = 10)
    screen2.image = img2
    prec.config(text = preciosapps[app])
    prec.place(x = 10, y = 80)
    if idioma == 0:
        desc.config(text = descespapps[app])
        desc.place(x = 10, y = 280)
        pcompra.deiconify()
    else:
        desc.config(text = descingapps[app])
        desc.place(x = 10, y = 280)
        pcompra.deiconify()

#Esta función es para iniciar la tabla de los compradores registrados en la tienda
def iniciartabla():
    global txt
    txt = ''
    arch = open("compradores.txt", "r")
    leercompradores(arch, '')

#Función para cerrar la ventana de inicio de sesión y abrir la ventana del menú principal
def iniciarwithdraw():
    iniciar.withdraw()
    compra.deiconify()

#Función para almacenar los datos del archivo compradores.txt
def iniciarsesionven():
    global nombrecompradores
    global idscompradores
    compra.withdraw()
    nombrecompradores = []
    idscompradores = []
    arch = open("compradores.txt", "r")
    comprobar_compradores(arch)

#Función para registrarse a la tienda
#E: Un botón
#S: El nombre introducido por el usuario de la Entry, el correo introducido en la Entry, un número al azar entre 10 y 99 y un contador
#R: El usuario no puede haber iniciado sesión anteriormente y las Entrys deben tener algo escrito
def registrarse():
    global idscompradores
    global iniciado
    nomr = insnomr.get()
    correor = inscorreor.get()
    if iniciado == 1:
        messagebox.showinfo("Error", "La sesión ya fue iniciada/You are already logged in")
        insnomr.delete(0, END)
        inscorreor.delete(0, END)
        iniciarwithdraw()
    elif nomr == '' or correor == '':
        messagebox.showinfo("Error", "Intentalo de nuevo/Try Again")
        insnomr.delete(0, END)
        inscorreor.delete(0, END)
    else:
        idscompradoresr = idscompradores
        num = randomizar(random.randint(10,99), idscompradoresr)
        return registrarse_aux(nomr, correor, num, 0)

#E: El nombre, el correo, un número al azar entre 10 y 99 y un contador
#S: El nombre, el correo y el número
#R: El nombre no puede estar en uso
def registrarse_aux(nomr, correor, num, c):
    global nombrecompradores
    if len(nombrecompradores) == c:
        return registrarse_aux2(nomr, correor, num)
    elif nombrecompradores[c] == nomr:
        messagebox.showinfo("Error", "El nombre ya está en uso/This name already exists")
        insnomr.delete(0, END)
        inscorreor.delete(0, END)
    else:
        return registrarse_aux(nomr, correor, num, c + 1)

#E: El nombre, el correo y el número
#S: Escibir los datos en el archivo de compradores.txt sin sobrescribir los anteriores
def registrarse_aux2(nomr, correor, num):
    arch = open("compradores.txt", "a")
    arch.write(nomr)
    arch.write(',')
    arch.write(repr(num))
    arch.write(',')
    arch.write(correor)
    arch.write(',')
    arch.write(repr(0))
    arch.write('\n')
    arch.close()
    messagebox.showinfo("Listo/Ready", "Registrado, ahora inicia sesión/Registered, now log in")
    insnomr.delete(0, END)
    inscorreor.delete(0, END)

#Función para inciar sesión
#E: Un boton
#S: El nombre introducido en la Entry
#R: El usuario no puede haber iniciado sesión y los espacios en las Entry deben estar llenos
def iniciarsesion():
    global usuario
    global iniciado
    noms = insnoms.get()
    correos = inscorreos.get()
    if iniciado == 1:
        messagebox.showinfo("Error", "La sesión ya fue iniciada/You are already logged in")
        insnoms.delete(0, END)
        inscorreos.delete(0, END)
        iniciarwithdraw()
    elif noms == '' or correos == '':
        messagebox.showinfo("Error", "Intentalo de nuevo/Try Again")
        insnoms.delete(0, END)
        inscorreos.delete(0, END)
    else:
        usuario = 0
        return iniciarsesion_aux(noms)

#E: El nombre de usuario
#S: Mensaje de sesión iniciada
#R: El usuario debe existir
def iniciarsesion_aux(noms):
    global iniciado
    global nombrecompradores
    global usuario
    if len(nombrecompradores) == usuario:
        messagebox.showinfo("Error", "El usuario no existe/The user doesn´t exist")
        insnoms.delete(0, END)
        inscorreos.delete(0, END)
    elif nombrecompradores[usuario] == noms:
        iniciado = 1
        messagebox.showinfo("Listo/Ready", "Sesión Iniciada/Logged In")
        insnoms.delete(0, END)
        inscorreos.delete(0, END)
        iniciarwithdraw()
    else:
        usuario += 1
        return iniciarsesion_aux(noms)

#Función para comprar una app
#E: Un botón
#S: Los datos del archivo compradores.txt
#R: El usuario tuvo que haber iniciado sesión
def iniciarcompra():
    global iniciado
    if iniciado == 0:
        messagebox.showinfo("Error", "No has iniciado sesión/You´re not logged in")
        pcompra.withdraw()
    else:
        arch = open("compradores.txt", "r")
        a = arch.readlines()
        arch.close()
        return iniciarcompra_aux(a)

#E: Los datos del archivo compradores.txt
#S: Los datos del archivo guardados en listas
def iniciarcompra_aux(a):
    global usuario
    an = a[:usuario]
    dn = a[usuario + 1:]
    a = a[usuario]
    arch = open("compradores.txt", "w")
    return iniciarcompra_aux2(arch, an, dn, a)

#E: Los datos del archivo guardados en listas
#S: Los datos del comprador a modificar y escribir todos los datos antes del dato a modificar
def iniciarcompra_aux2(arch, an, dn, a):
    if an == []:
        return iniciarcompra_aux3(arch, dn, a)
    else:
        arch.write(an[0])
        return iniciarcompra_aux2(arch, an[1:], dn, a)

#E: Los datos del comprador a modificar
#S: Los datos que están después del archivo a modificar
def iniciarcompra_aux3(arch, dn, a):
    a = a.split(",")
    arch.write(a[0])
    arch.write(",")
    arch.write(a[1])
    arch.write(",")
    arch.write(a[2])
    arch.write(",")
    b = int(a[3])
    b += 1
    arch.write(repr(b))
    arch.write("\n")
    return iniciarcompra_aux4(arch, dn)

#E: Los datos después del archivo a modificar
#S: Los datos del archivo apps.txt
def iniciarcompra_aux4(arch, dn):
    if dn == []:
        arch.close()
        arch = open("apps.txt", "r")
        a = arch.readlines()
        arch.close()
        return iniciarcompra_aux5(a)
    else:
        arch.write(dn[0])
        return iniciarcompra_aux4(arch, dn[1:])

#E: Los datos del archivo apps.txt
#S: Los datos del archivo en listas
def iniciarcompra_aux5(a):
    global app
    an = a[:app]
    dn = a[app + 1:]
    arch = open("apps.txt", "w")
    return iniciarcompra_aux6(arch, an, dn)

#E: Los datos del archivo en listas
#S: Los datos de la app a modificar y escribir todos los datos antes del dato a modificar
def iniciarcompra_aux6(arch, an, dn):
    if an == []:
        return iniciarcompra_aux7(arch, dn)
    else:
        arch.write(an[0])
        return iniciarcompra_aux6(arch, an[1:], dn)

#E: Los datos de la app a modificar
#S: Los datos posteriores a la app a modificar
def iniciarcompra_aux7(arch, dn):
    global estados
    global idproductos
    global idvendedores
    global nombreapps
    global catapps
    global descespapps
    global descingapps
    global preciosapps
    global totalprecios
    global descarmunapps
    global descarcrapps
    global screens1apps
    global screens2apps
    global app
    global descargas
    arch.write(estados[app])
    arch.write(",")
    arch.write(idvendedores[app])
    arch.write(",")
    arch.write(idproductos[app])
    arch.write(",")
    arch.write(nombreapps[app])
    arch.write(",")
    arch.write(catapps[app])
    arch.write(",")
    arch.write(descespapps[app])
    arch.write(",")
    arch.write(descingapps[app])
    arch.write(",")
    arch.write(preciosapps[app])
    arch.write(",")
    a = float(totalprecios[app])
    a = a + float(preciosapps[app])
    arch.write(repr(a))
    arch.write(",")
    if descargas == 0:
        arch.write(descarmunapps[app])
        arch.write(",")
        a = int(descarcrapps[app])
        a += 1
        arch.write(repr(a))
        arch.write(",")
        arch.write(screens1apps[app])
        arch.write(",")
        arch.write(screens2apps[app])
        arch.write("\n")
        return iniciarcompra_aux8(arch, dn)
    else:
        a = int(descarmunapps[app])
        a += 1
        arch.write(repr(a))
        arch.write(",")
        arch.write(descarcrapps[app])
        arch.write(",")
        arch.write(screens1apps[app])
        arch.write(",")
        arch.write(screens2apps[app])
        arch.write("\n")
        return iniciarcompra_aux8(arch, dn)

#E: Los posteriores a la app a modificar y escribir en el archivo
#S: Un mensaje indicando que se realizó la compra
def iniciarcompra_aux8(arch, dn):
    if dn == []:
        arch.close()
        arch = open("apps.txt", "r")
        leerapps(arch)
        return messagebox.showinfo("Listo/Ready", "Comprada/Bought")
    else:
        arch.write(dn[0])
        return iniciarcompra_aux8(arch, dn[1:])

#Función para buscar apps
#E: Un botón
#S: La cadena introducida a la Entry de búsqueda y un contador
#R: Debe haber algo escrito
def buscadorapps():
    global buscador
    global txt
    buscado = buscador.get()
    buscado = buscado.lower()
    txt = ''
    if buscado == '':
        return messagebox.showinfo("Error", "No hay coincidencias/There are no coincidences")
    else:
        buscador.delete(0, END)
        return buscadorapps_aux(buscado, 0)

#E: La cadena de la Entry y un contador
#S: La cadena y un contador
#R: Lo escrito debe tener alguna coincidencia
def buscadorapps_aux(buscado, c):
    global catapps
    if len(catapps) == c:
        messagebox.showinfo("Error", "No hay coincidencias/There are no coincidences")
    else:
        return buscadorapps_aux_aux(buscado, c)

#E: La cadena y un contador
#S: La cadena y la posición con la app encontrada
def buscadorapps_aux_aux(buscado, c):
    global catapps
    global nombreapps
    global descespapps
    global descingapps
    a = len(buscado)
    n = nombreapps[c]
    n = n[:a]
    n = n.lower()
    de = descespapps[c]
    de = de[:a]
    de = de.lower()
    di = descingapps[c]
    di = di[:a]
    di = di.lower()
    if catapps[c] == buscado or buscado == n or buscado == de or buscado == di:
        return buscadorapps_aux2(buscado, c)
    else:
        return buscadorapps_aux(buscado, c + 1)

#E: La cadena y la posición con la app encontrada
#S: Si la app está inactiva buscar otra y sino envía a la cadena y la posición
def buscadorapps_aux2(buscado, c):
    global estados
    if estados[c] == "I":
        return buscadorapps_aux(buscado, c + 1)
    else:
        return buscadorapps_aux3(buscado, c)

#E: La cadena y la posición
#S: Almacenar en una global txt los datos de la app y si está en español o en inglés almacenar la descripción correspondiente y envía la cadena y el contador más uno
def buscadorapps_aux3(buscado, c):
    global txt
    global idproductos
    global nombreapps
    global descespapps
    global descingapps
    global preciosapps
    global screens2apps
    global idioma
    txt = txt + "ID:" + " " + idproductos[c]+ "     " + nombreapps[c] + "     " + preciosapps[c] + "$" + "     "
    if idioma == 0:
        txt = txt + descespapps[c] + "\n" + "\n"
        return buscadorapps_aux4(buscado, c + 1)
    else:
        txt = txt + descingapps[c] + "\n" + "\n"
        return buscadorapps_aux4(buscado, c + 1)

#E: La cadena y un contador
#S: Si el largo de la lista de categorías es igual al contador, envía el comando de iniciar la siguiente auxiliar, sino va a buscar otra coincidencia
def buscadorapps_aux4(buscado, c):
    global catapps
    global nombreapps
    global descespapps
    global descingapps
    if len(catapps) == c:
        return buscadorapps_aux6()
    else:
        return buscadorapps_aux4_aux(buscado, c)

#E: La cadena y el contador
#S: Si encuentra una coincidencia manda la función de comprobación, sino continua buscando coincidencias
def buscadorapps_aux4_aux(buscado, c):
    a = len(buscado)
    n = nombreapps[c]
    n = n[:a]
    n = n.lower()
    de = descespapps[c]
    de = de[:a]
    de = de.lower()
    di = descingapps[c]
    di = di[:a]
    di = di.lower()
    if catapps[c] == buscado or buscado == n or buscado == de or buscado == di:
        return buscadorapps_aux5(buscado, c)
    else:
        return buscadorapps_aux4(buscado, c + 1)

#E: La cadena y un contador
#S: Si la app está inactiva sigue buscando coincidencias, sino va a guardar la información
def buscadorapps_aux5(buscado, c):
    global estados
    if estados[c] == "I":
        return buscadorapps_aux4(buscado, c + 1)
    else:
        return buscadorapps_aux3(buscado, c)

#Este es un código de interfaz gráfica en la ventana de búsqueda
#Lo que hace esta función es colocar labels con los datos obtenidos de la búsqueda
#También se coloca el botón de cerrar la ventana
def buscadorapps_aux6():
    global txt
    global idioma
    busqueda = Toplevel(width = 870, height = 450)
    busqueda.maxsize(870, 450)
    busqueda.minsize(870, 450)
    bcanvas = Canvas(busqueda, width = 870, height = 450, bg = "#3A0C60")
    bcanvas.place(x = 0, y = 0)
    resultados = Label(busqueda, text = txt, font = ("LMSansDemiCond10", "14"), bg = "#3A0C60", fg = "#C6BAD1")
    resultados.place(x = 10, y = 50)
    if idioma == 0:
        resu = Label(busqueda, text = "Resultados de la búsqueda:", font = ("IMPACT", "16"), bg = "#3A0C60", fg = "#C6BAD1")
        resu.place(x = 10, y = 10)
        cerrarr = Button(busqueda, text = "Cerrar", font = ("IMPACT", "12"), bg = "#9E84B3", fg = "#C6BAD1", command = busqueda.destroy)
        cerrarr.place(x = 10, y = 410)
    else:
        resu = Label(busqueda, text = "Results from the search:", font = ("IMPACT", "16"), bg = "#3A0C60", fg = "#C6BAD1")
        resu.place(x = 10, y = 10)
        cerrarr = Button(busqueda, text = "Close", font = ("IMPACT", "12"), bg = "#9E84B3", fg = "#C6BAD1", command = busqueda.destroy)
        cerrarr.place(x = 10, y = 410)

#Este es un código de interfaz gráfica en la ventana de elección de país y le coloca un canvas
#Lo que hace esta función es colocar 3 labels y 3 botones, uno de cada país
#También se colocan 3 imagenes en 3 Labels
pais = Toplevel(width = 500, height = 500)
pais.title("País/Country")
pais.maxsize(500, 500)
canvaspais = Canvas(pais, width = 500, height = 500, bg = "#3A0C60")
canvaspais.place(x = 0, y = 0)
elije = Label(pais, text = "Elija un País/Choose a country", font = ("Times New Roman", "16"), bg = "#3A0C60", fg = "#C6BAD1")
elije.place(x = 120, y = 10)
crb = Button(pais, text = "COSTA RICA", font = ("Times New Roman", "14"), bg = "#3A0C60", command = paiscr, fg = "#C6BAD1")
crb.place(x = 250, y = 100)
espb = Button(pais, text = "LATINO AMÉRICA/ \n ESPAÑA", font = ("Times New Roman", "14"), bg = "#3A0C60", fg = "#C6BAD1", command = paislat)
espb.place(x = 225, y = 200)
ingb = Button(pais, text = "UNITED \n STATES", font = ("Times New Roman", "14"), bg = "#3A0C60", fg = "#C6BAD1", command = paising)
ingb.place(x = 270, y = 320)
imgcr = PhotoImage(file = "costarica.gif")
canvaspais.create_image(140, 97, anchor = NW, image = imgcr)
imglat = PhotoImage(file = "latam.gif")
canvaspais.create_image(100, 206, anchor = NW, image = imglat)
imging = PhotoImage(file = "ingles.gif")
canvaspais.create_image(150, 323, anchor = NW, image = imging)

compra.mainloop()
