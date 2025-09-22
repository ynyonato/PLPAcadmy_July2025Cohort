class Smartphone:
    def __init__(self, brand, model, mdate, color, on_state=False):
        self.brand = brand
        self.model = model
        self.mdate = mdate
        self.color = color
        self.on_state = on_state  # fixed variable name

    def turn_on(self):
        self.on_state = True
    
    def turn_off(self):
        self.on_state = False

    def show_info(self):
        if self.on_state:
            print(f"The phone {self.brand} {self.model} manufactured on {self.mdate} is ON.")
        else:
            print(f"The phone {self.brand} {self.model} manufactured on {self.mdate} is OFF.")

# Inheritance layer example to show polymorphism or encapsulation
class SmartPhoneWithCamera(Smartphone):
    def __init__(self, brand, model, mdate, color, on_state=False, camera_megapixels=12):
        super().__init__(brand, model, mdate, color, on_state)
        self.camera_megapixels = camera_megapixels

    def take_picture(self):
        if self.on_state:
            print(f"Taking a picture with {self.camera_megapixels}MP camera.")
        else:
            print("Turn on the phone first.")

    # Override show_info to add camera info (polymorphism)
    def show_info(self):
        super().show_info()
        print(f"Camera: {self.camera_megapixels}MP")

# Usage example
phone = Smartphone("Apple", "iPhone 13", "2021-09", "Black")
phone.show_info()
phone.turn_on()
phone.show_info()

camera_phone = SmartPhoneWithCamera("Samsung", "Galaxy S21", "2021-01", "Silver", camera_megapixels=108)
camera_phone.turn_on()
camera_phone.show_info()
camera_phone.take_picture()
