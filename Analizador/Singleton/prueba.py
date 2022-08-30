from Singleton import *
if __name__ == '__main__':
    singleton1 = Singleton.getInstance()
    singleton2 = Singleton.getInstance()
    singleton1.addConsola("hola \n")
    singleton2.addConsola("Soy una prueba Singleton\n")
    singleton2.addConsola("Para probar la consola")
    singleton1.addConsola("\nPRUEBA FINAL")
    print(singleton1.getConsola())