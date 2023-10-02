from django_unicorn.components import UnicornView

class Step1View(UnicornView):
    name = "Roman"
    email = "roman@example.com"

    def mount(self):
        self.name = "Roman"
        self.email = "roman@example.com"

    def next(self):
        self.parent.step += 1
