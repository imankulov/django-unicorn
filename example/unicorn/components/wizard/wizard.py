from django_unicorn.components import UnicornView


class WizardView(UnicornView):
    step = 1

    def next(self):
        self.step += 1

    def previous(self):
        self.step -= 1

    def finish(self):
        self.step = 1
