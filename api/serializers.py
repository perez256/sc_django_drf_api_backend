from rest_framework import serializers
from api.models import User, FeedBack, ResearchLab, Marketing, BookRide
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

        extra_kwargs = {
            'password': {'write_only': True}
        }


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = '__all__'

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBack
        fields = '__all__'


class ResearchLabSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchLab
        fields = '__all__'


class MarketingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marketing
        fields = '__all__'


class BookRideSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookRide
        fields = '__all__'
