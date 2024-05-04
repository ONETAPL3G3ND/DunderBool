class User:
    def __init__(self):
        self.connected = False

    def Connect(self):
        self.connected = True

    def Disconnection(self):
        self.connected = False

    def __bool__(self):
        return self.connected


if __name__ == "__main__":
    user = User()
    user.Connect()

    if bool(user):
        print("Connected")
    else:
        print("Not connected")

    user.Disconnection()

    if bool(user):
        print("Connected")
    else:
        print("Not connected")