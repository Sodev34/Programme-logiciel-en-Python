class Round:
    def __init__(self, round_name, round_start, round_end):
        self.round_name = round_name
        self.round_start = round_start
        self.round_end = round_end
        self.matches = []

    def list_round(self):
        return [self.round_name, self.round_start, self.round_end, self.matches]
