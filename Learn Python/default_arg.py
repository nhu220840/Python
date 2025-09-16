import time

def net_price(list_price, discount, tax = 0.05):
    return list_price * (1 - discount) * (1 + tax)

def count(end, start = 0):
    for x in range(start, end + 1):
        print(x)
        time.sleep(1)
    print("DONE!")

if __name__ == '__main__':
    print(net_price(500, 0.01))
    count(10)