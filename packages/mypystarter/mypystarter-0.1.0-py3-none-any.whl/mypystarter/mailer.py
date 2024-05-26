class Mailer:
    def __init__(self, mailer):
        self.mailer = mailer

    def send(self, subject, message, recipients):
        self.mailer.send(subject, message, recipients)
