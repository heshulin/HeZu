from HeZe.models import Attention, User


class Attentionservice(object):
    def attention_other(self,UserPhone,SecretKey,BefocusonId):
        try:
            user = User.objects.filter(UserPhone=UserPhone).first()
            print(user.SecretKey)
            print(SecretKey)
            if user.SecretKey == SecretKey:
                attentioninfo = Attention()
                attentioninfo.UserId = user.UserId
                attentioninfo.BefocusonId  = BefocusonId
                attentioninfo.save()
                array = {
                    'msg': '成功',
                    'state': '1'
                }
            else:
                array = {
                    'msg': '请登录',
                    'state': '0'
                }
            return array
        except Exception as e:
            array = {
                'msg': '出现未知的错误了请等等',
                'state': '0'
            }
            return array
