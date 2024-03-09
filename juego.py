import random

class Personaje:
    def __init__(self, nombre, salud):
        self.nombre = nombre
        self.salud = salud
        self.intentos_huir = 0
        self.items_utilizados = set()

    def atacar_monstruo(self):
        # Simula el ataque al monstruo
        return random.randint(10, 20)

    def recibir_dano(self, cantidad_dano):
        # Recibe daño del monstruo
        self.salud -= cantidad_dano
        print(f"Recibiste {cantidad_dano} de daño. Tu salud actual es {self.salud}.")

        if self.salud > 100:
            self.salud = 100
            print("¡Vida al máximo!")

    def usar_pocion(self):
        # Simula el uso de una poción para recuperar salud
        salud_recuperada = random.randint(20, 30)
        self.salud += salud_recuperada

        if self.salud > 100:
            self.salud = 100
            print("¡Vida al máximo!")
        else:
            print(f"Has usado una poción y recuperaste {salud_recuperada} de salud. ¡Ahora tu salud es {self.salud}!")

    def usar_escudo(self):
        # Simula el uso de un escudo para reducir el daño recibido
        dano_reducido = random.randint(5, 15)
        print(f"Has usado un escudo. Redujiste {dano_reducido} de daño recibido.")

    def usar_bendicion(self):
        # Simula el uso de una bendición que reduce aleatoriamente o aumenta la salud del personaje
        if random.choice([True, False]):
            aumento_salud = random.randint(5, 15)
            self.salud += aumento_salud
            print(f"Has recibido la bendición de los dioses. Tu salud aumentó en {aumento_salud}.")

            if self.salud > 100:
                self.salud = 100
                print("¡Vida al máximo!")
        else:
            print("Los dioses te abandonaron en este momento.")

    def usar_comida(self):
        # Simula el uso de comida que aumenta aleatoriamente la salud del personaje
        aumento_salud = random.randint(10, 20)
        self.salud += aumento_salud
        print(f"Has comido algo. Tu salud aumentó en {aumento_salud}.")

        if self.salud > 100:
            self.salud = 100
            print("¡Vida al máximo!")

    def usar_encantamiento(self):
        # Simula el uso de un encantamiento que aleatoriamente mejora o empeora la situación del personaje
        if random.choice([True, False]):
            print("El encantamiento te ha beneficiado en este momento.")
            self.usar_pocion()
        else:
            print("El encantamiento te ha traído problemas. Te has topado con un monstruo adicional.")

    def usar_hierbas_medicinales(self):
        # Simula el uso de hierbas medicinales que aleatoriamente aumentan o disminuyen la salud del personaje
        cambio_salud = random.randint(-10, 15)
        self.salud += cambio_salud
        if cambio_salud >= 0:
            print(f"Las hierbas medicinales te han beneficiado. Tu salud aumentó en {cambio_salud}.")
        else:
            print(f"Las hierbas medicinales te han afectado. Tu salud disminuyó en {-cambio_salud}.")

        if self.salud > 100:
            self.salud = 100
            print("¡Vida al máximo!")

def seleccionar_personaje():
    print("Selecciona tu personaje:")
    print("1. Mago")
    print("2. Héroe")
    print("3. Experto en Trampas")

    opcion = input("Elige un personaje (1-3): ")
    
    if opcion == "1":
        return Personaje("Mago", 100)
    elif opcion == "2":
        return Personaje("Héroe", 100)
    elif opcion == "3":
        return Personaje("Experto en Trampas", 100)
    else:
        print("Opción no válida. Intenta de nuevo.")
        return seleccionar_personaje()

def enfrentar_monstruo(personaje):
    monstruos = ["slime", "esqueleto", "araña", "fantasma"]
    monstruo_actual = random.choice(monstruos)

    print(f"Te has topado con un {monstruo_actual}. ¿Qué harás, {personaje.nombre}?")
    print("1. Pelear")
    print("2. Evadir")
    print("3. Usar poción")
    print("4. Usar escudo")
    print("5. Usar bendición de dios")
    print("6. Comer algo")
    print("7. Usar encantamiento")
    print("8. Usar hierbas medicinales")

    opcion = input("Elige una opción (1-8): ")

    if opcion == "1":
        # Elige pelear
        dano_recibido = personaje.atacar_monstruo()
        print(f"Atacaste al {monstruo_actual}. Le hiciste {dano_recibido} de daño.")
        if personaje.salud < 50:
            usar_pocion = input("Tu salud está por debajo del 50. ¿Quieres usar una poción? (s/n): ")
            if usar_pocion.lower() == "s":
                personaje.usar_pocion()
        return dano_recibido
    elif opcion == "2":
        # Elige evadir
        print(f"Lograste evadir al {monstruo_actual}. ¡Buena elección!")
        personaje.intentos_huir += 1

        if personaje.intentos_huir == 3:
            print("Has intentado evadir tres veces consecutivas. ¡Debes combatir con las bestias ahora!")
            personaje.intentos_huir = 0  # Reinicia el contador de intentos de huir
        return 0
    elif opcion == "3":
        # Elige usar poción
        personaje.usar_pocion()
        return 0
    elif opcion == "4":
        # Elige usar escudo
        personaje.usar_escudo()
        return 0
    elif opcion == "5":
        # Elige usar bendición de dios
        personaje.usar_bendicion()
        return 0
    elif opcion == "6":
        # Elige comer algo
        personaje.usar_comida()
        return 0
    elif opcion == "7":
        # Elige usar encantamiento
        personaje.usar_encantamiento()
        return 0
    elif opcion == "8":
        # Elige usar hierbas medicinales
        personaje.usar_hierbas_medicinales()
        return 0
    else:
        print("Opción no válida. Intenta de nuevo.")
        return enfrentar_monstruo(personaje)

def main():
    personaje = seleccionar_personaje()

    while personaje.salud > 0:
        dano_recibido = enfrentar_monstruo(personaje)
        personaje.recibir_dano(dano_recibido)

        if personaje.salud <= 0:
            print(f"Tu salud ha llegado a 0. ¡El juego ha terminado!")
        else:
            print(f"Tu salud actual es {personaje.salud}.\n")

if __name__ == "__main__":
    main()
