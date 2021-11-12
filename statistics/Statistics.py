class Statistics:
    __clients_count = 0

    @classmethod
    def up(cls):
        cls.__clients_count += 1

    @classmethod
    def down(cls):
        cls.__clients_count -= 1

    @classmethod
    def get_clients_count(cls):
        return cls.__clients_count
