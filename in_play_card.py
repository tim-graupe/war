class In_Play_Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __str__(self):
        return f"""
            +-----------+
            | {self.value:<2}        |
            |           |
            |     {self.suit:<6}|
            |           |
            |        {self.value:>2} |
            +-----------+
            """


