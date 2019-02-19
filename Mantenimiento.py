from tkinter import *
from tkinter import messagebox
import random

#Se define la ventana principal del programa, la cual sería la del menú y se le coloca un canvas
manten = Tk()
manten.withdraw()
manten.minsize(300, 300)
manten.maxsize(300, 300)
canvasing = Canvas(manten, width = 300, height = 300, bg = "#F8E0EC")
canvasing.place(x = 0, y = 0)

#Se definen todas las sub-ventanas que se utilizan en el programa, para poder ser modificadas
ve = Toplevel
app = Toplevel
fve = Toplevel
cons = Toplevel
adapp = Toplevel
aapp = Toplevel
ada = Toplevel

#Se definen las globales de almacenamiento de datos, cada una almacena una lista de datos específicos
#Almacena texto para introducirlo a una label
txt = ''
#Almacena unos y ceros, con tal de comprobar si el vendedor tiene una app asociada
apps10 = []
#Almacena las ids de los vendedores
ids = []
#Almacena si una app está activa o inactiva
activ = []
#Almacena las ids de los vendedores que están asociados a aplicaciones
idsvap = []
#Almacena las ids de las aplicaciones
idsapp = []
#Almacena los nombres de las screenshots 1 de cada app
screens1 = []
#Almacena los nombres de las screenshots 2 de cada app
screens2 = []
#Almacena las ganancias totales de cada app
tprecio = []
#Almacena las descargas mundiales de cada app
descarmun = []
#Almacena las descargas en Costa Rica de cada app
descarcr = []

#E: Los datos de un archivo
#S: Los datos que se mostrarán en la tabla de vendedores, almacenar las ids de los vendedores en la global ids y almacenar datos de comprobación en caso de que el vendedor tenga una app asociada
#R: El archivo a entrar tiene que ser vendedor.txt en modo lectura y el orden de los datos en el archivo deben estar de forma correcta
def leervendedores(arch):
    global ids
    global apps10
    global txt
    a = arch.readline()
    if a == '':
        arch.close()
    else:
        a = a.split(",")
        txt = txt + a[0] + '   ' + a[1] + '   ' + a[2] + '   ' + a[3] + '   ' + a[4] + '\n'
        ids = ids + [a[0]]
        b = a[5]
        b = b[0]
        apps10 = apps10 + [b]
        return leervendedores(arch)

#Este es un código de interfaz gráfica de la tabla de vendedores, donde primero se reinician las globales apps10, ids y txt y se ejecuta leervendedores para obtener datos del archivo vendedor.txt
#Se asignan las características de la ventana ve, se coloca un canvas y se colocan labels para cada dato de la tabla
#Se colocan 3 botones: el de salir de la ventana, el de agregar un vendedor y el de eliminar un vendedor
#Finalmente, se coloca una label con los datos de la global txt, la cual tendrá los datos del archivo vendedor.txt
def vendedoresesp():
    global ve
    global ids
    global apps10
    global txt
    apps10 = []
    ids = []
    txt = ''
    arch = open("vendedor.txt", "r")
    leervendedores(arch)
    ve = Toplevel(width = 650, height = 550)
    ve.title("Lista de Vendedores")
    ve.maxsize(650, 550)
    canvasven = Canvas(ve, width = 650, height = 550, bg = "#F8E0EC")
    canvasven.place(x = 0, y = 0)
    tbv = Label(ve, text = "Tabla de Vendedores", font = ("Times New Roman", "18"), bg = "#F8E0EC")
    tbv.place(x = 210, y = 10)
    idl1 = Label(ve, text = "ID", font = ("Times New Roman", "16"), bg = "#F8E0EC")
    idl1.place(x = 100, y = 70)
    nombl1 = Label(ve, text = "Nombre", font = ("Times New Roman", "16"), bg = "#F8E0EC")
    nombl1.place(x = 150, y = 70)
    corrl1 = Label(ve, text = "Correo", font = ("Times New Roman", "16"), bg = "#F8E0EC")
    corrl1.place(x = 250, y = 70)
    sitwbl1 = Label(ve, text = "Sitio Web", font = ("Times New Roman", "16"), bg = "#F8E0EC")
    sitwbl1.place(x = 350, y = 70)
    ray = Label(ve, text = "----------------------------------------------------------------------------------------", font = ("Times New Roman", "16"), bg = "#F8E0EC")
    ray.place(x = 10, y = 100)
    eliminar = Button(ve, text = "SALIR", font = ("Times New Roman", "12"), bg = "#F8E0EC", command = ve.destroy)
    eliminar.place(x = 570, y = 490)
    agregar = Button(ve, text = "AGREGAR \n VENDEDOR", font = ("Times New Roman", "12"), bg = "green", command = agregarvendesp)
    agregar.place(x = 320, y = 485)
    eliminar = Button(ve, text = "ELIMINAR \n VENDEDOR", font = ("Times New Roman", "12"), bg = "red", command = fuerav)
    eliminar.place(x = 450, y = 485)
    estruc = Label(ve, text = "Estructura:", font = ("Times New Roman", "12"), bg = "#F8E0EC")
    estruc.place(x = 10, y = 70)
    ldvv = Label(ve, text = txt, font = ("Times New Roman", "12"), bg = "#F8E0EC")
    ldvv.place(x = 30 , y = 130)

#E: Un botón
#S: Cerrar la ventana de eliminar un vendedor y ejecutar la ventana de la tabla de vendedores
#R: Tiene que ser el botón de cancelar de la ventana fve
def cancelarv():
    fve.destroy()
    vendedoresesp()

#Este es un código de interfaz gráfica de la ventana de eliminar vendedores, donde primero se le asigna que se usará la global Entry insid
#Se asignan las características de la ventana fve, se coloca un canvas y se coloca un label para indicar la acción a hacer
#Se colocan 3 botones: el de cancelar y cerrar la ventana y el de eliminar un vendedor
def fuerav():
    global insid
    global fve
    ve.destroy()
    fve = Toplevel(width = 350, height = 300)
    fve.maxsize(350, 300)
    fve.title("Borrar Vendedor")
    canvdve = Canvas(fve, width = 350, height = 300, bg = "#F8E0EC")
    canvdve.place(x = 0, y = 0)
    insid = Entry(fve)
    insid.place(x = 100, y = 100)
    labid = Label(fve, text = "Inserte el ID del vendedor a borrar:", font = ("Times New Roman", "14"), bg = "#F8E0EC") 
    labid.place(x = 40, y = 50)
    butid = Button(fve, text = "ELIMINAR", font = ("Times New Roman", "14"), bg = "red", command = fuerac)
    butid.place(x = 112, y = 200)
    canc = Button(fve, text = "Cancelar", font = ("Times New Roman", "12"), bg = "#F8E0EC", command = cancelarv)
    canc.place(x = 270, y = 250)

#Función de eliminar un vendedor
#E: Un botón
#S: Función aux de eliminar un vendedor con un contandor
#R: Tiene que ser el botón Eliminar de la ventana fve
def fuerac():
    fuera_aux(0)

#E: Un contador
#S: La posición del vendedor a eliminar en la global ids
#R: El vendedor tiene que existir
def fuera_aux(c):
    global insid
    global ids
    if len(ids) == c:
        return messagebox.showinfo("Error", "No hay un vendedor con esa id")
    elif insid.get() == ids[c]:
        return fuera_aux2(c)
    else:
        return fuera_aux(c + 1)

#E: Un contador
#S: Datos del archivo vendedor.txt y la extracción del vendedor a eliminar
#R: El vendedor no debe tener una app asociada
def fuera_aux2(c):
    global apps10
    if apps10[c] == "1":
        return messagebox.showinfo("Error", "El vendedor tiene una app asociada")
    else:
        arch = open("vendedor.txt", "r")
        a = arch.readlines()
        arch.close()
        a.pop(c)
        return fuera_aux3(a, '')

#E: Datos del archivo con el vendedor eliminado y una cadena contadora
#S: Sobrescribir los datos del archivo vendedor.txt, cerrarlo, cerrar la ventana fve y abrir la tabla de vendedores nuevamente
#R: El archivo debe se vendedor.txt
def fuera_aux3(lista, a1):
    if lista == []:
        arch = open("vendedor.txt", "w")
        arch.write(a1)
        arch.close()
        fve.destroy()
        vendedoresesp()
    else:
        a1 = a1 + lista[0]
        return fuera_aux3(lista[1:], a1)

#Función de randomizar un número
#E: Un número al azar entre el 10 y el 99 y el respaldo de la lista ids
#S: Un número al azar entre el 10 al 99
#R: El programa no debe repetir números existentes en la lista de ids de vendedores
def randomizar1(num, idsr):
    global ids
    if idsr == []:
        return num
    elif num == int(idsr[0]):
        return randomizar1(random.randint(10,99), ids)
    else:
        return randomizar1(num, idsr[1:])

#Este es un código de interfaz gráfica de la ventana de agregar vendedores, donde primero se asigna que se usarán las globales Entry insid, Entry inscorreo, Entry insistioweb y Entry insapell
#Se asignan las características de la ventana ada, se coloca un canvas y se colocan labels para indicar los datos a introducir en los Entrys
#Se colocan 2 botones: el de cancelar y cerrar la ventana y el de agregar el vendedor
def agregarvendesp():
    global insname
    global inscorreo
    global inssitioweb
    global insapell
    global ada
    ve.destroy()
    ada = Toplevel(width = 350, height = 300)
    ada.title("Añadir Vendedor")
    ada.maxsize(350, 400)
    canvasada = Canvas(ada, width = 400, height = 400, bg = "#F8E0EC")
    canvasada.place(x = 0, y = 0)
    agrinfo = Label(ada, text = "Por favor, escriba los datos que se le solicitan", font = ("Times New Roman", "12"), bg = "#F8E0EC")
    agrinfo.place(x = 10, y = 10)
    names = Label(ada, text = 'Nombre:', font = ("Times New Roman", "12"), bg = "#F8E0EC")
    names.place(x = 10, y = 50)
    insname = Entry(ada)
    insname.place(x = 12, y = 75)
    apell = Label(ada, text = 'Apellido:', font = ("Times New Roman", "12"), bg = "#F8E0EC")
    apell.place(x = 10, y = 100)
    insapell = Entry(ada)
    insapell.place(x = 12, y = 125)
    correolb = Label(ada, text = 'Correo Electrónico:', font = ("Times New Roman", "12"), bg = "#F8E0EC")
    correolb.place(x = 10, y = 150)
    inscorreo = Entry(ada)
    inscorreo.place(x = 12, y = 175)
    sitioweblb = Label(ada, text = 'Sitio Web:', font = ("Times New Roman", "12"), bg = "#F8E0EC")
    sitioweblb.place(x = 10, y = 200)
    inssitioweb = Entry(ada)
    inssitioweb.place(x = 12, y = 225)
    anadirvend = Button(ada, text = "AGREGAR", font = ("Times New Roman", "12"), bg = "green", command = agregado)
    anadirvend.place(x = 250, y = 200)
    cancelvend = Button(ada, text = "CANCELAR", font = ("Times New Roman", "12"), bg = "red", command = adadestroy)
    cancelvend.place(x = 245, y = 250)

#E: Un botón
#S: Cerrar la ventana de agregar un vendedor y ejecutar la ventana de la tabla de vendedores
#R: Tiene que ser el botón de cancelar de la ventana ada
def adadestroy():
    ada.destroy()
    vendedoresesp()

#Función de agregar un vendedor
#E: Un botón
#S: Los datos del vendedor a agregar el archivo vendedor.txt, sin sobrescribir los datos anteriores
#R: El archivo debe ser vendedor.txt y los datos en las Entrys deben estar escritos de manera correcta
def agregado():
    global insname
    global inscorreo
    global inssitioweb
    global insapell
    global ids
    nom = insname.get()
    corr = inscorreo.get()
    sit = inssitioweb.get()
    apell = insapell.get()
    idsr = ids
    num = randomizar1(random.randint(10,99), idsr)
    if nom == "" or corr == "" or sit == "" or apell == "":
        messagebox.showinfo("Error", "Intente de nuevo")
        insname.delete(0, END)
        inscorreo.delete(0, END)
        inssitioweb.delete(0, END)
        insapell.delete(0, END)
    else:
        arch = open("vendedor.txt", "a")
        arch.write(repr(num))
        arch.write(',')
        arch.write(nom)
        arch.write(',')
        arch.write(apell)
        arch.write(',')
        arch.write(corr)
        arch.write(',')
        arch.write(sit)
        arch.write(',')
        arch.write(repr(0))
        arch.write('\n')
        arch.close()
        ada.destroy()
        vendedoresesp()

#E: Los datos de un archivo
#S: Los datos que se mostrarán en la tabla de apps, almacenar los datos para comprobar si una app está activa o inactiva, almacenar las ids de los vendedores asociados a cada app, almacenar las ids de cada app, almacenar los nombres de las screenshots 1 y 2
#R: El archivo a entrar tiene que ser apps.txt en modo lectura y el orden de los datos en el archivo deben estar de forma correcta
def leerapps(arch):
    global txt
    global activ
    global idsvap
    global screens1
    global screens2
    global idsapp
    a = arch.readline()
    if a == '':
        arch.close()
    else:
        a = a.split(",")
        txt = txt + a[1] + '   ' + a[2] + '   ' + a[4] + '   ' + a[5] + '   ' + a[7] + '   ' + a[9] + '   ' + a[10] + '   ' + a[0] + '\n' + '\n'
        activ = activ + [a[0]]
        idsvap = idsvap + [a[1]]
        idsapp = idsapp + [a[2]]
        screens1 = screens1 + [a[11]]
        b = a[12]
        c = len(b)
        screens2 = screens2 + [b[:c - 1]]
        return leerapps(arch)

#E: El lugar a colocar la screenshot (en este caso un canvas) y un contador
#S: Asignar cada nombre de screenshot a la lista screeens1 y enviarla a una función que se encargá de colocar las imágenes
#R: Los nombres de las screenshot deben terminar en .gif y tener una resolución de 220x220
def screenshots1(lugar, c):
    global screens1
    if len(screens1) == c:
        return None
    else:
        imgr = screens1[c]
        img = PhotoImage(file = imgr)
        img = img.subsample(x = 6, y = 6)
        return nlabel1(lugar, img, c)

#E: el lugar a colocar la screenshot, la screenshot y un contador
#S: la screenshot colocada en un label en el lugar seleccionado y el contador más 1
#R: el lugar debe existir
def nlabel1(lugar, img, c):
    label = Label(lugar, image = img)
    label.pack()
    label.image = img
    return screenshots1(lugar, c + 1)

#E: el lugar a colocar la screenshot (en este caso un canvas) y un contador
#S: Asignar cada nombre de screenshot a la lista screeens2 y enviarla a una función que se encargá de colocar las imágenes
#R: Los nombres de las screenshot deben terminar en .gif y tener una resolución de 220x220
def screenshots2(lugar, c):
    global screens2
    if len(screens2) == c:
        return None
    else:
        imgr = screens2[c]
        img = PhotoImage(file = imgr)
        img = img.subsample(x = 6, y = 6)
        return nlabel2(lugar, img, c)

#E: el lugar a colocar la screenshot, la screenshot y un contador
#S: la screenshot colocada en un label en el lugar seleccionado y el contador más 1
#R: el lugar debe existir
def nlabel2(lugar, img, c):
    label = Label(lugar, image = img)
    label.pack()
    label.image = img
    return screenshots2(lugar, c + 1)

#Este es un código de interfaz gráfica de la tabla de apps, donde primero se reinician las globales txt, activ, idsvap, screens1, screens2 e idsapp y se ejecuta leerapps para obtener datos del archivo apps.txt
#Se asignan las características de la ventana app, se coloca un canvas y se colocan labels para cada dato de la tabla
#Se colocan 3 botones: el de salir de la ventana, el de agregar una app y el de activar o desactivar una app
#Se colocan 2 canvas más donde se colocan las screenshots de las apps
#Se coloca una label con los datos de la global txt, la cual tendrá los datos del archivo apps.txt
#Finalmente, ejecutan las funciones screenshot1 y screenshots 2
def appsesp():
    global app
    global txt
    global activ
    global idsvap
    global screens1
    global screens2
    global idsapp
    txt = ''
    activ = []
    idsvap = []
    screens1 = []
    screens2 = []
    idsapp = []
    arch = open("apps.txt", "r")
    leerapps(arch)
    app = Toplevel(width = 1000, height = 770)
    app.title("Lista de Apps")
    app.minsize(1000, 770)
    app.maxsize(1000, 770)
    canvasapp = Canvas(app, width = 1000, height = 770, bg = "#F8E0EC")
    canvasapp.place(x = 0, y = 0)
    cnva = Label(app, text = "Tabla de Apps", font = ("Times New Roman", "16"), bg = "#F8E0EC")
    cnva.place(x = 400, y = 10)
    idl1 = Label(app, text = "ID Vendedor", font = ("Times New Roman", "12"), bg = "#F8E0EC")
    idl1.place(x = 10, y = 70)
    idpr = Label(app, text = "ID Producto", font = ("Times New Roman", "12"), bg = "#F8E0EC")
    idpr.place(x = 110, y = 70)
    catg = Label(app, text = "Categoría", font = ("Times New Roman", "12"), bg = "#F8E0EC")
    catg.place(x = 200, y = 70)
    desc = Label(app, text = "Descripción", font = ("Times New Roman", "12"), bg = "#F8E0EC")
    desc.place(x = 270, y = 70)
    prec = Label(app, text = "Precio ($)", font = ("Times New Roman", "12"), bg = "#F8E0EC")
    prec.place(x = 360, y = 70)
    screen = Label(app, text = "Screenshots", font = ("Times New Roman", "12"), bg = "#F8E0EC")
    screen.place(x = 800, y = 70)
    descmun = Label(app, text = "Descargas Mundiales", font = ("Times New Roman", "12"), bg = "#F8E0EC")
    descmun.place(x = 440, y = 70)
    descr = Label(app, text = "Descargas Costa Rica", font = ("Times New Roman", "12"), bg = "#F8E0EC")
    descr.place(x = 590, y = 70)
    estruc = Label(app, text = "Estructura:", font = ("Times New Roman", "10"), bg = "#F8E0EC")
    estruc.place(x = 10, y = 55)
    estad = Label(app, text = "Estado", font = ("Times New Roman", "12"), bg = "#F8E0EC")
    estad.place(x = 740, y = 70)
    espa = Label(app, text = "-------------------------------------------------------------------------------------------------------------------------------------------", font = ("Times New Roman", "16"), bg = "#F8E0EC")
    espa.place(x = 10, y = 95)
    saliraps = Button(app, text = "SALIR", font = ("Times New Roman", "12"), bg = "#F8E0EC", command = app.destroy)
    saliraps.place(x = 910, y = 710)
    anadirapp = Button(app, text = "AGREGAR \n APP", font = ("Times New Roman", "12"), bg = "green", command = addapp)
    anadirapp.place(x = 650, y = 700)
    actiodesac = Button(app, text = "ACTIVAR \n Ó \n DESACTIVAR", font = ("Times New Roman", "12"), bg = "#F8E0EC", command = actodesact)
    actiodesac.place(x = 770, y = 690)
    canimg1 = Canvas(app, width = 100, height = 430, bg = "#F8E0EC")
    canimg1.place(x = 770, y = 120)
    canimg2 = Canvas(app, width = 100, height = 430, bg = "#F8E0EC")
    canimg2.place(x = 850, y = 120)
    ldap = Label(app, text = txt, font = ("Times New Roman", "12"), bg = "#F8E0EC")
    ldap.place(x = 30 , y = 130)
    screenshots1(canimg1, 0)
    screenshots2(canimg2, 0)

#Función de randomizar un número
#E: Un número al azar entre el 100 y el 999 y el respaldo de la lista ids
#S: Un número al azar entre el 100 al 999
#R: El programa no debe repetir números existentes en la lista de ids de apps
def randomizar2(num, idsr):
    global idsapp
    if idsr == []:
        return num
    elif num == int(idsr[0]):
        return randomizar2(random.randint(100,999), idsapp)
    else:
        return randomizar2(num, idsr[1:])

#Este es un código de interfaz gráfica de la ventana de agregar apps, donde primero se asigna que se usarán las globales Entry insidvend, Entry insnomap, Entry inscatesp, Entry insdescesp, Entry insdescing, Entry insprecio, Entry insscreens1 y Entry insscreens2
#Se asignan las características de la ventana aapp, se coloca un canvas y se colocan labels para indicar los datos a introducir en los Entrys
#Se colocan 2 botones: el de cancelar y cerrar la ventana y el de agregar la app
def addapp():
    global insidvend
    global insnomapp
    global inscatesp
    global insdescesp
    global insdescing
    global insprecio
    global insscreen1
    global insscreen2
    global aapp
    app.destroy()
    aapp = Toplevel(width = 400, height = 600)
    aapp.title("Añadir app")
    aapp.minsize(400, 600)
    aapp.maxsize(400, 600)
    canvaapp = Canvas(aapp, width = 400, height = 600, bg = "#F8E0EC")
    canvaapp.place(x = 0, y = 0)
    agrinfo = Label(aapp, text = "Por favor, escriba los datos que se le solicitan:", font = ("Times New Roman", "12"), bg = "#F8E0EC")
    agrinfo.place(x = 10, y = 10)
    idvend = Label(aapp, text = "ID del Vendedor:", font = ("Times New Roman", "12"), bg = "#F8E0EC")
    idvend.place(x = 10, y = 30)
    insidvend = Entry(aapp)
    insidvend.place(x = 12, y = 55)
    nomapp = Label(aapp, text = "Nombre de la App:", font = ("Times New Roman", "12"), bg = "#F8E0EC")
    nomapp.place(x = 10, y = 80)
    insnomapp = Entry(aapp)
    insnomapp.place(x = 12, y = 105)
    catesp = Label(aapp, text = "Categoría (CONSULTAR TABLA DE NÚMEROS):", font = ("Times New Roman", "12"), bg = "#F8E0EC")
    catesp.place(x = 10, y = 130)
    inscatesp = Entry(aapp)
    inscatesp.place(x = 12, y = 155)
    descesp = Label(aapp, text = "Descripción Corta (EN ESPAÑOL):", font = ("Times New Roman", "12"), bg = "#F8E0EC")
    descesp.place(x = 10, y = 180)
    insdescesp = Entry(aapp)
    insdescesp.place(x = 12, y = 205)
    descing = Label(aapp, text = "Descripción Corta (EN INGLES):", font = ("Times New Roman", "12"), bg = "#F8E0EC")
    descing.place(x = 10, y = 230)
    insdescing = Entry(aapp)
    insdescing.place(x = 12, y = 255)
    precio = Label(aapp, text = "Precio (usar dos decimales):", font = ("Times New Roman", "12"), bg = "#F8E0EC")
    precio.place(x = 10, y = 280)
    insprecio = Entry(aapp)
    insprecio.place(x = 12, y = 305)
    screen1 = Label(aapp, text = "Nombre de la primera Screenshot (añadir .gif):", font = ("Times New Roman", "12"), bg = "#F8E0EC")
    screen1.place(x = 10, y = 330)
    insscreen1 = Entry(aapp)
    insscreen1.place(x = 12, y = 355)
    screen2 = Label(aapp, text = "Nombre de la segunda Screenshot (añadir .gif):", font = ("Times New Roman", "12"), bg = "#F8E0EC")
    screen2.place(x = 10, y = 380)
    insscreen2 = Entry(aapp)
    insscreen2.place(x = 12, y = 405)
    canc = Button(aapp, text = "Cancelar", font = ("Times New Roman", "12"), bg = "#F8E0EC", command = aappdestroy)
    canc.place(x = 300, y = 550)
    anad = Button(aapp, text = "¡AÑADIR!", font = ("Times New Roman", "12"), bg = "green", command = agregadoapp)
    anad.place(x = 200, y = 550)

#E: Un botón
#S: Cerrar la ventana de agregar una app y ejecutar la ventana de la tabla de vendedores
#R: Tiene que ser el botón de cancelar de la ventana aapp
def aappdestroy():
    global aapp
    aapp.destroy()
    checkvend()

#Función de agregar una app
#E: Un botón
#S: Los datos de las Entrys en la ventana de agregar app y un número aleatorio entre el 100 al 999 y un contador
#R: Las Entrys deben tener datos escritos
def agregadoapp():
    global insidvend
    global insnomapp
    global inscatesp
    global insdescesp
    global insdescing
    global insprecio
    global insscreen1
    global insscreen2
    global idsapp
    idven = insidvend.get()
    inomap = insnomapp.get()
    cates = inscatesp.get()
    desces = insdescesp.get()
    descin = insdescing.get()
    preci = insprecio.get()
    scree1 = insscreen1.get()
    scree2 = insscreen2.get()
    idsar = idsapp
    num = randomizar2(random.randint(100,999), idsar)
    if idven == '' or inomap == '' or cates == '' or desces == '' or descin == '' or preci == '' or scree1 == '' or scree2 == '':
        messagebox.showinfo("Error", "Intente de nuevo")
        insidvend.delete(0, END)
        insnomapp.delete(0, END)
        inscatesp.delete(0, END) 
        insdescesp.delete(0, END)
        insdescing.delete(0, END)
        insprecio.delete(0, END)
        insscreen1.delete(0, END)
        insscreen2.delete(0, END)
    else:
        return agregadoapp_aux(idven, inomap, cates, desces, descin, preci, scree1, scree2, num, 0)

#E: Datos de las Entrys de la ventana de agregar apps, un número y un contador
#S: Los datos de las Entrys, el número, el contador y el archivo vendedor.txt
#R: El vendedor tiene que existir
def agregadoapp_aux(idven, inomap, cates, desces, descin, preci, scree1, scree2, num, c):
    global ids
    if len(ids) == c:
        messagebox.showinfo("Error", "El vendedor no existe")
        insidvend.delete(0, END)
        insnomapp.delete(0, END)
        inscatesp.delete(0, END)   
        insdescesp.delete(0, END)
        insdescing.delete(0, END)
        insprecio.delete(0, END)
        insscreen1.delete(0, END)
        insscreen2.delete(0, END)
    elif idven == ids[c]:
        arch = open("vendedor.txt", "r")
        return agregadoapp_aux2(idven, inomap, cates, desces, descin, preci, scree1, scree2, num, c, arch)
    else:
        return agregadoapp_aux(idven, inomap, cates, desces, descin, preci, scree1, scree2, num, c + 1)

#E: Los datos de las Entrys, el número, el contador y el archivo vendedor.txt
#S: Dos opciones: en caso que el vendedor tenga una app asociada o en caso de que no tenga una app asociada, en ambos casos se mandan los datos de las Entrys y el número. En el caso que no, se envia también el archivo vendedor.txt en modo escritura    
def agregadoapp_aux2(idven, inomap, cates, desces, descin, preci, scree1, scree2, num, c, arch):
    a = arch.readlines()
    b = a[c]
    q = len(b)
    an = a[:c]
    dn = a[c + 1:]
    arch.close()
    if b[q - 1] == '1':
        return agregadoapp_aux5(idven, inomap, cates, desces, descin, preci, scree1, scree2, num)
    else:
        arch = open("vendedor.txt", "w")
        return agregadoapp_aux3(idven, inomap, cates, desces, descin, preci, scree1, scree2, num, arch, b, an, dn)

#E: Los datos de las Entrys, el número, el archivo vendedor.txt y los datos del archivo
#S: Sobrescribir los datos del vendedor con tal de asociarlo a una app
def agregadoapp_aux3(idven, inomap, cates, desces, descin, preci, scree1, scree2, num, arch, b, an, dn):
    if an == []:
        q = len(b)
        arch.write(b[:q-2])
        arch.write(repr(1))
        arch.write("\n")
        return agregadoapp_aux4(idven, inomap, cates, desces, descin, preci, scree1, scree2, num, arch, dn)
    else:
        arch.write(an[0])
        return agregadoapp_aux3(idven, inomap, cates, desces, descin, preci, scree1, scree2, num, arch, b, an[1:], dn)

#E: Los datos de las Entrys, el número, el archivo vendedor.txt y los datos del archivo
#S: Terminar de escribir los datos en el archivo de vendedores y los datos de las Entrys y el número
def agregadoapp_aux4(idven, inomap, cates, desces, descin, preci, scree1, scree2, num, arch, dn):
    if dn == []:
        arch.close()
        return agregadoapp_aux5(idven, inomap, cates, desces, descin, preci, scree1, scree2, num)
    else:
        arch.write(dn[0])
        return agregadoapp_aux4(idven, inomap, cates, desces, descin, preci, scree1, scree2, num, arch, dn[1:])

#E: Los datos de las Entrys y el número
#S: La función de revisar vendedores
def agregadoapp_aux5(idven, inomap, cates, desces, descin, preci, scree1, scree2, num):
    global aapp
    arch = open("apps.txt", "a")
    arch.write('A')
    arch.write(',')
    arch.write(idven)
    arch.write(',')
    arch.write(repr(num))
    arch.write(',')
    arch.write(inomap)
    arch.write(',')
    arch.write(cates)
    arch.write(',')
    arch.write(desces)
    arch.write(',')
    arch.write(descin)
    arch.write(',')
    arch.write(preci)
    arch.write(',')
    arch.write(repr(0))
    arch.write(',')
    arch.write(repr(0))
    arch.write(',')
    arch.write(repr(0))
    arch.write(',')
    arch.write(scree1)
    arch.write(',')
    arch.write(scree2)
    arch.write('\n')
    arch.close()
    aapp.destroy()
    checkvend()

#Este es un código de interfaz gráfica de la ventana de activar o desactivar apps, donde primero se asigna que se usarán las globales Entry insidap
#Se asignan las características de la ventana adapp, se coloca un canvas y se colocan labels para indicar las acciones que realizan cada botón
#Se colocan 3 botones: el de cancelar y cerrar la ventana, el de activar la app y el de desactivar la app
def actodesact():
    global insidap
    global adapp
    app.destroy()
    adapp = Toplevel(width = 350, height = 300)
    adapp.maxsize(350, 300)
    adapp.title("Activar o desactivar aplicación")
    canvadapp = Canvas(adapp, width = 350, height = 300, bg = "#F8E0EC")
    canvadapp.place(x = 0, y = 0)
    insidap = Entry(adapp)
    insidap.place(x = 100, y = 100)
    labidap = Label(adapp, text = "Inserte la ID de la APP:", font = ("Times New Roman", "14"), bg = "#F8E0EC") 
    labidap.place(x = 40, y = 50)
    butacap = Button(adapp, text = "ACTIVAR", font = ("Times New Roman", "14"), bg = "green", command = activarapp)
    butacap.place(x = 40, y = 160)
    butacap = Button(adapp, text = "DESACTIVAR", font = ("Times New Roman", "14"), bg = "red", command = deactivarapp)
    butacap.place(x = 170, y = 160)
    canc = Button(adapp, text = "Cancelar", font = ("Times New Roman", "12"), bg = "#F8E0EC", command = adappdestroy)
    canc.place(x = 270, y = 250)

#E: Un botón
#S: Cerrar la ventana de activar o desactivar una app y ejecutar la ventana de la tabla de apps
#R: Tiene que ser el botón de cancelar de la ventana adapp
def adappdestroy():
    adapp.destroy()
    checkvend()

#Función de activar una app
#E: Un botón
#S: El id de la app para activarla y un contador
#R: La Entry debe tener algo escrito
def activarapp():
    global insidap
    idap = insidap.get()
    if idap == '':
        messagebox.showinfo("Error", "Intente de nuevo")
        insidap.delete(0, END)
    else:
        return activarapp_aux(idap, 0)

#E: La id de la app a activar y un contador
#S: La posición de la app a activar con el contador
#R: La app debe existir
def activarapp_aux(idap, c):
    global idsapp
    if len(idsapp) == c:
        messagebox.showinfo("Error", "Ninguna app coincide con la ID")
        insidap.delete(0, END)
    elif idap == idsapp[c]:
        return activarapp_aux2(c)
    else:
        return activarapp_aux(idap, c + 1)

#E: La posición de la app a activar
#S: Los datos del archivo apps.txt y el archivo apps.txt en modo escritura
#R: La app tiene que estar desactivada
def activarapp_aux2(c):
    global activ
    if activ[c] == 'A':
        messagebox.showinfo("Error", "Ya está activa")
        checkvend()
    else:
        arch = open("apps.txt", "r")
        a = arch.readlines()
        arch.close()
        an = a[:c]
        dn = a[c + 1:]
        b = a[c]
        arch = open("apps.txt", "w")
        return activarapp_aux3(arch, an, dn, b)

#E: Los datos del archivo apps.txt y el archivo apps.txt en modo escritura
#S: Activar la app elegida y los datos del archivo apps.txt
def activarapp_aux3(arch, an, dn, b):
    if an == []:
        arch.write("A")
        arch.write(b[1:])
        return activarapp_aux4(arch, dn)
    else:
        arch.write(an[0])
        return activarapp_aux3(arch, an[1:], dn, b)

#E: Los datos del archivo apps.txt
#S: Terminar de escribir los datos en el archivo, cerrar la ventana de activar o desactivar apps y ejecutar la función de revisar vendedores
def activarapp_aux4(arch, dn):
    global adapp
    if dn == []:
        arch.close()
        adapp.destroy()
        checkvend()
    else:
        arch.write(dn[0])
        return activarapp_aux4(arch, dn[1:])

#Función de descativar una app
#E: Un botón
#S: El id de la app para activarla y un contador
#R: La Entry debe tener algo escrito
def deactivarapp():
    global insidap
    idap = insidap.get()
    if idap == '':
        messagebox.showinfo("Error", "Intente de nuevo")
        insidap.delete(0, END)
    else:
        return deactivarapp_aux(idap, 0)

#E: La id de la app a activar y un contador
#S: La posición de la app a activar con el contador
#R: La app debe existir
def deactivarapp_aux(idap, c):
    global idsapp
    if len(idsapp) == c:
        messagebox.showinfo("Error", "Ninguna app coincide con la ID")
        insidap.delete(0, END)
    elif idap == idsapp[c]:
        return deactivarapp_aux2(c)
    else:
        return deactivarapp_aux(idap, c + 1)

#E: La posición de la app a activar
#S: Los datos del archivo apps.txt y el archivo apps.txt en modo escritura
#R: La app tiene que estar activa
def deactivarapp_aux2(c):
    global activ
    if activ[c] == 'I':
        messagebox.showinfo("Error", "Ya está inactiva")
        checkvend()
    else:
        arch = open("apps.txt", "r")
        a = arch.readlines()
        arch.close()
        an = a[:c]
        dn = a[c + 1:]
        b = a[c]
        arch = open("apps.txt", "w")
        return deactivarapp_aux3(arch, an, dn, b)

#E: Los datos del archivo apps.txt y el archivo apps.txt en modo escritura
#S: Desactivar la app elegida y los datos del archivo apps.txt
def deactivarapp_aux3(arch, an, dn, b):
    if an == []:
        arch.write("I")
        arch.write(b[1:])
        return deactivarapp_aux4(arch, dn)
    else:
        arch.write(an[0])
        return deactivarapp_aux3(arch, an[1:], dn, b)

#E: Los datos del archivo apps.txt
#S: Terminar de escribir los datos en el archivo, cerrar la ventana de activar o desactivar apps y ejecutar la función de revisar vendedores
def deactivarapp_aux4(arch, dn):
    global adapp
    if dn == []:
        arch.close()
        adapp.destroy()
        checkvend()
    else:
        arch.write(dn[0])
        return deactivarapp_aux4(arch, dn[1:])

#E: Un botón o otra función
#S: Si la global ids tiene algo escrito retorna la ventana de la tabla de apps, sino ejecuta una función auxiliar con los datos del archivo vendedor.txt
def checkvend():
    global ids
    if ids != []:
        return appsesp()
    else:
        arch = open("vendedor.txt", "r")
        return checkvend_aux(arch, '')

#E: Datos del archivo vendedor.txt y una cadena vacía
#S: Guardar los datos de las ids de los vendedores y si tienen apps asociadas a ellos. Luego retorna la función de la tabla de apps
def checkvend_aux(arch, a):
    global ids
    global apps10
    a = arch.readline()
    if a == '':
        arch.close()
        return appsesp()
    else:
        ids = ids + [a[:2]]
        q = len(a)
        apps10 = apps10 + [a[q - 2]]
        return checkvend_aux(arch, a)

#Este es un código de interfaz gráfica de la ventana de consultar las apps de los vendedores, donde primero se reinicia la global txt y se asigna que se usará la global Entry insidven
#Se asignan las características de la ventana cons, se coloca un canvas y se coloca un label para indicar la acción a hacer
#Se colocan 2 botones: el de cancelar y cerrar la ventana y el de consultar las apps en venta de un vendedor
def consultar():
    global cons
    global insidven
    global txt
    txt = ''
    cons = Toplevel(width = 350, height = 300)
    cons.maxsize(350, 300)
    cons.title("Activar o desactivar aplicación")
    canvascon = Canvas(cons, width = 350, height = 300, bg = "#F8E0EC")
    canvascon.place(x = 0, y = 0)
    insidven = Entry(cons)
    insidven.place(x = 100, y = 100)
    labidap = Label(cons, text = "Inserte la ID del vendedor:", font = ("Times New Roman", "14"), bg = "#F8E0EC") 
    labidap.place(x = 60, y = 50)
    butacap = Button(cons, text = "Consultar Apps", font = ("Times New Roman", "14"), bg = "#F8E0EC", command = consultapps)
    butacap.place(x = 95, y = 160)
    canc = Button(cons, text = "Cancelar", font = ("Times New Roman", "12"), bg = "#F8E0EC", command = cons.destroy)
    canc.place(x = 270, y = 250)

#Función de consultar las apps de un vendedor
#E: Un botón
#S: Un contador
def consultapps():
    return consultapps_aux(0)

#E: Un contador
#S: La posición del vendedor con el contador
#R: El vendedor debe tener al menos una app asociada
def consultapps_aux(c):
    global idsvap
    global insidven
    if len(idsvap) == c:
        messagebox.showinfo("Error", "El vendedor no tiene una app asociada")
    elif insidven.get() == idsvap[c]:
        return consultapps_aux2(c)
    else:
        return consultapps_aux(c + 1)

#E: La posición del vendedor con el contador
#S: Almacenar en la global txt los datos de la app del vendedor y el contador más 1
def consultapps_aux2(c):
    global idsapp
    global tprecio
    global descarmun 
    global descarcr
    global txt
    txt = txt + idsapp[c] + '                        ' + descarmun[c] + '                                            ' + descarcr[c] + '                                   ' + tprecio[c] +  "$" + '\n'
    return consultapps_aux3(c + 1)

#E: El contador de posición
#S: Dos opciones: si el vendedor tiene otra app asociada envía a que consiga los datos, en caso de que no tenga más retorna la acción de abrir una ventana
def consultapps_aux3(c):
    global idsvap
    global insidven
    if len(idsvap) == c:
        return consultapps_aux4()
    elif insidven.get() == idsvap[c]:
        return consultapps_aux2(c)
    else:
        return consultapps_aux3(c + 1)

#Este es un código de interfaz gráfica de la ventana de ver los datos de las apps de los vendedores, primero se cierra la ventana de introducir la ID
#Se asignan las características de la ventana cons2, se coloca un canvas y se colocan varios labels para indicar la las posiciones de los datos de la tabla
#Se coloca una label con los datos de la global txt
#Se coloca 1 boton el de cerrar la ventana
def consultapps_aux4():
    global txt
    cons.destroy()
    cons2 = Toplevel(width = 700, height = 500)
    cons2.maxsize(700, 500)
    cons2.minsize(700, 500)
    canvascons2 = Canvas(cons2, width = 700, height = 500, bg = "#F8E0EC")
    canvascons2.place(x = 0, y = 0)
    estruc = Label(cons2, text = "Estructura:", font = ("Times New Roman", "10"), bg = "#F8E0EC")
    estruc.place(x = 10, y = 38)
    idapp = Label(cons2, text = "ID de la APP", font = ("Times New Roman", "12"), bg = "#F8E0EC")
    idapp.place(x = 80, y = 35)
    descmun = Label(cons2, text = "Descargas Mundiales", font = ("Times New Roman", "12"), bg = "#F8E0EC")
    descmun.place(x = 175, y = 35)
    desccr = Label(cons2, text = "Descargas en Costa Rica", font = ("Times New Roman", "12"), bg = "#F8E0EC")
    desccr.place(x = 330, y = 35)
    pret = Label(cons2, text = "Precio total en ventas ($)", font = ("Times New Roman", "12"), bg = "#F8E0EC")
    pret.place(x = 500, y = 35)
    espa = Label(cons2, text = "----------------------------------------------------------------------------------------------------------------", font = ("Times New Roman", "14"), bg = "#F8E0EC")
    espa.place(x = 10, y = 70)
    dat = Label(cons2, text = txt, font = ("Times New Roman", "12"), bg = "#F8E0EC")
    dat.place(x = 80, y = 100)
    cerr = Button(cons2, text = "CERRAR", font = ("Times New Roman", "12"), bg = "red", command = cons2.destroy)
    cerr.place(x = 600, y = 450)

#E: Un botón o una acción
#S: Los datos del archivo apps.txt
def checkcons():
    global activ
    global tprecio
    global idsvap
    global descarcr
    global descarmun
    global idsapp
    idsapp = []
    descarcr = []
    descarmun = []
    idsvap = []
    tprecio = []
    activ = []
    arch = open("apps.txt", "r")
    leerconsultas(arch)

#E: Los datos del archivo apps.txt
#S: Se almacenan los datos de si una app está activa, las ids de los vendedores de las apps, las ids de las apps, las ganancias totales de las apps, las descargas mundiales y las descargas en Costa Rica, y se retorna la ventana de consultar
def leerconsultas(arch):
    global activ
    global idsvap
    global idsapp
    global tprecio
    global descarmun
    global descarcr
    a = arch.readline()
    if a == '':
        arch.close()
        return consultar() 
    else:
        a = a.split(",")
        activ = activ + [a[0]]
        idsvap = idsvap + [a[1]]
        idsapp = idsapp + [a[2]]
        tprecio = tprecio + [a[8]]
        descarmun = descarmun + [a[9]]
        descarcr = descarcr + [a[10]]
        return leerconsultas(arch)

#E: Iniciar el programa
#S: El menú del programa
#R: Debe introducir un usuario y una contraseña válida
def ent():
    if usuario.get() == "admin" and contra.get() == "admin":
        manten.deiconify()
        ingreso.destroy()
    else:
        messagebox.showinfo("Error", "Intente de nuevo")
        usuario.delete(0, END)
        contra.delete(0, END)

#Este es un código de interfaz gráfica de la ventana de ingresar al sistema
#Se asignan las características de la ventana ingreso, se coloca un canvas y se colocan dos labels para indicar la acción a hacer
#Se coloca 1 botón: El de ingresar al sistema
ingreso = Toplevel(width = 250, height = 170)
ingreso.title("Inicie Sesión")
ingreso.maxsize(250, 170)
canvasing = Canvas(ingreso, width = 250, height = 170, bg = "#F6CED8")
canvasing.place(x = 0, y = 0)
usu = Label(ingreso, text = "Usuario:", font = ("Times New Roman", "16"), bg = "#F6CED8")
usu.place(x = 15, y = 20)
usuario = Entry(ingreso)
usuario.place(x = 114, y = 25)
cont = Label(ingreso, text = "Contraseña:", font = ("Times New Roman", "16"), bg = "#F6CED8")
cont.place(x = 8, y = 70)
contra = Entry(ingreso)
contra.place(x = 114, y = 75)
ingresar = Button(ingreso, text = "INGRESAR", font = ("Times New Roman", "12"), bg = "#F6CED8",  command = ent)
ingresar.place(x = 150, y = 120)

#Este es un código de interfaz gráfica del menú del sistema
#Se asignan las características de la ventana del menú, se coloca un label para indicar la acción a hacer
#Se colocan 3 botones: el de la tabla de vendedores, el de la tabla de apps y el de la consulta
manten.title("Menú")
lisven = Label(manten, text = "Elija una acción", font = ("Times New Roman", "18"), bg = "#F8E0EC")
lisven.place(x = 70, y = 10)
vend = Button(manten, text = " Administrar \n Vendedores", font = ("Times New Roman", "14"), bg = "#F8E0EC", command = vendedoresesp)
vend.place(x = 90, y = 50)
aps = Button(manten, text = " Datos de las \n Apps", font = ("Times New Roman", "14"), bg = "#F8E0EC", command = checkvend)
aps.place(x = 90, y = 130)
cons = Button(manten, text = "Consultar", font = ("Times New Roman", "14"), bg = "#F8E0EC", command = checkcons)
cons.place(x = 105, y = 215)

#Se definen las globales para ser usadas por el programa para obtener datos
insname = Entry
inscorreo = Entry
inssitioweb = Entry
insapell = Entry
insid = Entry
insidap = Entry
insidven = Entry
insidvend = Entry
insnomapp = Entry
inscatesp = Entry
insdescesp = Entry
insdescing = Entry
insprecio = Entry
insscreen1 = Entry
insscreen2 = Entry

manten.mainloop()
