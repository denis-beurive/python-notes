# Factory

    class Animal:

        @staticmethod
        def get_dog() -> '__class__':
            return Animal('dog')

        @staticmethod
        def get_cat() -> '__class__':
            return Animal('cat')

        def __init__(self, specie: str):
            self.specie: str = specie

    dog = Animal.get_dog()
    cat = Animal.get_cat()
