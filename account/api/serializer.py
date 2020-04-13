from rest_framework import serializers
from account.models import Account
class RegisterationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model = Account
        fields = ['email','password','password2']
        extra_kwargs = {
            'password':{'write_only':True}
        }
    def save(self):
        print("----------------")
        print(self.validated_data['email'])
        print(self.validated_data['password'])
        print(self.validated_data['password2'])
        print("------------------------")
        acc = Account(email = self.validated_data['email'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        print(self.validated_data['email'])
        print(password)
        print(password2)
        if password!=password2:
            raise serializers.ValidationError({
                'error':'Passowrd does not match'
            })

        acc.set_password(password)
        acc.save()
        return acc