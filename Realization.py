from abc import ABC, abstractmethod

# The Interface
class PaymentProcessor(ABC):
    
    @abstractmethod
    def process_payment(self, amount: float):
        """All payment methods MUST implement this method."""
        pass
