from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.state import token_backend
from rest_framework.exceptions import AuthenticationFailed

class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        header = self.get_header(request)
        if header is None:
            raise AuthenticationFailed("Authorization credentials were not provided")

        raw_token = self.get_raw_token(header)
        if raw_token is None:
            raise AuthenticationFailed("Authorization credentials were not provided")
        try:
            validated_token = token_backend.decode(raw_token, verify=True)
        except Exception as e:
            raise InvalidToken(e)

        return validated_token.get("emp_id",None), validated_token