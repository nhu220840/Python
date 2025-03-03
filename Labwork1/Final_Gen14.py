import math
import threading

class Tank:
    def __init__(self, hitPoint, damage, armor, price):
        self.__hitPoint = hitPoint
        self.__damage = damage
        self.__armor = armor
        self.__price = price

    def getHitPoint(self):
        return self.__hitPoint

    def getDamage(self):
        return self.__damage

    def getArmor(self):
        return self.__armor

    def getPrice(self):
        return self.__price

    def setHitPoint(self, hp):
        self.__hitPoint = hp

    def setDamage(self, d):
        self.__damage = d

    def setArmor(self, a):
        self.__armor = a

    def setPrice(self, p):
        self.__price = p

    def __str__(self):
        return f"Tank infor:\nHitPoint: {self.__hitPoint}, Damage: {self.__damage}, Armor: {self.__armor}, Price: {self.__price}, Strength: {self.getStrength()}\n"

    def getStrength(self):
        return math.sqrt(self.__hitPoint ** 2 + self.__damage ** 2 + self.__armor ** 2)

def thread1(tanks, total_cost=75):
    result = []
    tanks.sort(key=lambda x: x[0].getPrice())
    for tank in tanks:
        if total_cost - tank[0].getPrice() < 0:
            break
        total_cost -= tank[0].getPrice()
        result.append(tank[1])
    return result

def thread2(tanks, total_cost=75):
    result = []
    tanks.sort(key=lambda x: x[0].getStrength(), reverse=True)
    for tank in tanks:
        if total_cost - tank[0].getPrice() < 0:
            break
        total_cost -= tank[0].getPrice()
        result.append(tank[1])
    return result

def input_handler(tanks, filename='input.txt'):
    try:
        with open(filename, "r") as f:
            num = int(f.readline().strip())
            for i in range(num):
                line = f.readline().strip()
                hp, d, a, p = line.split()
                tanks.append([Tank(int(hp), int(d), int(a), int(p)), i + 1])
    except Exception as e:
        print(f"Error: {e}")
    return tanks
    
def output_handler(tanks, filename='output.txt'):
    try:
        with open(filename, 'w') as f:
            for tank in tanks:
                f.write(str(tank[0]))
                f.write(str(tank[1]) + "\n")
            f.write(str(thread1(tanks)) + "\n")
            f.write(str(thread2(tanks)) + "\n")
    except Exception as e:
        print(f"Error: {e}")

def main():
    tanks = []
    tanks = input_handler(tanks)

    t1 = threading.Thread(target=thread1, args=(tanks,))
    t2 = threading.Thread(target=thread2, args=(tanks,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    output_handler(tanks)

if __name__ == "__main__":
    main()