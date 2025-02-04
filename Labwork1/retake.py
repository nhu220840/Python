import os
import subprocess

class Reservation:
    def __init__(self, guest, paid, room):
        self.guest = guest
        self.paid = paid
        self.room = room

    def greet(self):
        return f"Hello, {self.guest}! - Room: {self.room}"
    
class LongReservation(Reservation):
    def __init__(self, guest, paid, room, months):
        super().__init__(guest, paid, room)
        self.months = months

    def greet(self):
        return f"Hello, {self.guest}! - Room: {self.room} - {self.months} months"
    
    def save(self, filename):
        try:
            with open(filename, "w") as f:
                f.write(f"Guest: {self.guest}\nPaid: {self.paid}\nRoom: {self.room}\nMonths: {self.months}\n")
        except Exception as e:
            print(f"Error: {e}")

    def save_compress(self, filename):
        self.save(filename)

        os.system(f"zip 'output.zip' {filename}")
        # subprocess.run(f"zip output.zip {filename}", shell=True)

customer = Reservation("Emmanuel Macron", True, "R408")

#Test case
# print(customer.greet())

# long_term_customer1 = LongReservation("Angela Merkel", False, "S502", 12)
# print(long_term_customer1.greet())

# long_term_customer1.save("./Labwork1/reservation_info.txt") 
# long_term_customer1.save_compress("./Labwork1/reservation_info2.txt") 



