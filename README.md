# Django_auth_jwt_tenant
This is a library to enable auth from another Django project using JWT.

From your **Django Main** project define a Key to sign JWT and use the same Key in `JWT_SECRET_KEY` setting to validate the JWT token provided in the **Authorization Header**.

## Installation
```
pip install django-auth-jwt-tenant
```
## Usage
Set JWT
```
JWT_SECRET_KEY = DjangoProject_Token_Provider.JWT_SECRET_KEY
```

Example to protect a GraphQL View.
![usage example](https://raw.githubusercontent.com/CarlosMart626/django_auth_jwt_tenant/master/django_auth_jwt_tenant.png "Usage example")


Now you can authenticate using token from another Django Project.

## Contributing
After cloning this repo, ensure dependencies are installed by running:

```
pip install -e ".[test]"
```

After developing, the full test suite can be evaluated by running:

```
py.test django_auth_jwt_tenant --cov=django_auth_jwt_tenant # Use -v -s for verbose mode
```

## Configuration
Default values of configuration. Define any of this values in your settings.
```
JWT_ENCODE_HANDLER = django_auth_jwt_tenant.utils.jwt_encode_handler
JWT_DECODE_HANDLER = django_auth_jwt_tenant.utils.jwt_decode_handler
JWT_PAYLOAD_HANDLER = django_auth_jwt_tenant.utils.jwt_payload_handler
JWT_PAYLOAD_GET_USER_ID_HANDLER = django_auth_jwt_tenant.utils.jwt_get_user_id_from_payload_handler
JWT_SECRET_KEY = settings.SECRET_KEY
JWT_ALGORITHM = 'HS256'
JWT_VERIFY = True
JWT_VERIFY_EXPIRATION = True
JWT_LEEWAY = 0
JWT_EXPIRATION_DELTA = datetime.timedelta(seconds=300)
JWT_ALLOW_REFRESH = False
JWT_REFRESH_EXPIRATION_DELTA = datetime.timedelta(seconds=300)
JWT_AUTH_HEADER_PREFIX = 'Bearer'
```