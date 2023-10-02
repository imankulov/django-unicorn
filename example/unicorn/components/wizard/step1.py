from django_unicorn.components import UnicornView

class Step1View(UnicornView):
    name = ""
    email = ""

    def mount(self):
        self.name = "Test"
        self.email = ""

    def next(self):
        self.parent.step += 1
