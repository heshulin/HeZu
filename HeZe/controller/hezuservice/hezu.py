from HeZe.models import SendHezu, User


class hezu():
    def sendhezu(self, UserId, Information, Address, Picture, Number):
        try:
            s = SendHezu()
            s.UserId = UserId
            s.Information = Information
            s.Address =Address
            s.Picture = Picture
            s.Number = int(Number)
            s.Delete = 0
            s.save()
            return 1
        except Exception as e:
            print(e)
            return 0
