def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        # new_add=address.replace(".","[.]")

        return address.replace(".","[.]")
