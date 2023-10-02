from django_unicorn.components import UnicornView

class Step2View(UnicornView):
    address = ""
    city = ""
    state = ""
    zip_code = ""

    def mount(self):
        self.address = "123 Main St"
        self.city = "Anytown"
        self.state = "CA"
        self.zip_code = "12345"

    def next(self):
        self.parent.step += 1

    def previous(self):
        self.parent.step -= 1
