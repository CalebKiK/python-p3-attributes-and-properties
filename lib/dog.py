APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Mutt", breed="Mastiff"):
        # First, check name validity to avoid unnecessary breed setting
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name
        else:
            self._name = None
            print("Name must be string between 1 and 25 characters.")
        
        # Only set breed if the name was valid
        if self._name is not None:
            if breed in APPROVED_BREEDS:
                self._breed = breed
            else:
                self._breed = None
                print("Breed must be in list of approved breeds.")

    def get_name(self):
        print("Getting dog name")
        return self._name
    
    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            print(f"Name set to {name}")
            self._name = name
        else: 
            print("Name must be string between 1 and 25 characters.")
            
    name = property(get_name, set_name)
    
    def get_breed(self):
        print("Getting dog breed")
        return self._breed 
    
    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            print(f"Your dog breed is {breed}")
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")
            
    breed = property(get_breed, set_breed)