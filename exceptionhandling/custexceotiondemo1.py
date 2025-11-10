class InvalidStringError(Exception):
    
    def __init__(self, *args):
        super().__init__(*args)

try:
    name = "  ram   "        
    if " " in name:
        raise InvalidStringError("string is not valid...")
except InvalidStringError as e:
    print(e)
    