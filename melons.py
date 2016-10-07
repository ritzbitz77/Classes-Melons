"""This file should have our order classes in it."""

class AbstractMelonOrder(object):
    """General melon order attributes"""

    def __init__(self, species, qty):
        """General melon order"""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.base_price = 5

    def get_total(self):
        """Calculate price."""

       
        total = (1 + self.tax) * self.qty * self.base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""
        
        super(DomesticMelonOrder, self).__init__(species, qty)
        self.order_type = "domestic"
        self.tax = 0.08
        


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        super(InternationalMelonOrder, self).__init__(species, qty)
        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
