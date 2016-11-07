class Integration:
    """Base integration class for default behaviour of integrations"""
    def notify(self):
        pass


class DummyIntegration(Integration):
    """Example integration"""
    def notify(self):
        print("I was notified")
