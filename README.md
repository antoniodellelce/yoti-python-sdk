# Yoti Python SDK #

Welcome to the Yoti Python SDK. This repo contains the tools and step by step instructions you need to quickly integrate your Python back-end with Yoti so that your users can share their identity details with your application in a secure and trusted way.

## Table of Contents

1) [An Architectural view](#an-architectural-view) -
High level overview of integration

1) [References](#references) -
Guides before you start

1) [Requirements](#requirements) -
Everything you need to get started

1) [Installing the SDK](#installing-the-sdk) -
How to install our SDK

1) [SDK Project import](#sdk-project-import) -
How to install the SDK to your project

1) [Configuration](#configuration) -
Entry point explanation

1) [Handling Users](#handling-users) -
How to manage users

1) [Running the examples](#running-the-examples) -
How to retrieve a Yoti profile using the token

1) [Running the tests](#running-the-tests) -
Running tests for SDK example

1) [API Coverage](#api-coverage) -
Attributes defined

1) [Support](#support) -
Please feel free to reach out

## An Architectural View

Before you start your integration, here is a bit of background on how the integration works. To integrate your application with Yoti, your back-end must expose a GET endpoint that Yoti will use to forward tokens.
The endpoint can be configured in the Yoti Dashboard when you create/update your application. For more information on how to create an application please check our [developer page](https://www.yoti.com/developers/documentation/#login-button-setup).

The image below shows how your application back-end and Yoti integrate into the context of a Login flow.
Yoti SDK carries out for you steps 6, 7 and the profile decryption in step 8.

![alt text](login_flow.png "Login flow")

Yoti also allows you to enable user details verification from your mobile app by means of the Android (TBA) and iOS (TBA) SDKs. In that scenario, your Yoti-enabled mobile app is playing both the role of the browser and the Yoti app. Your back-end doesn't need to handle these cases in a significantly different way. You might just decide to handle the `User-Agent` header in order to provide different responses for desktop and mobile clients.

## References

* [AES-256 symmetric encryption][]
* [RSA pkcs asymmetric encryption][]
* [Protocol buffers][]
* [Base64 data][]

[AES-256 symmetric encryption]:   https://en.wikipedia.org/wiki/Advanced_Encryption_Standard
[RSA pkcs asymmetric encryption]: https://en.wikipedia.org/wiki/RSA_(cryptosystem)
[Protocol buffers]:               https://en.wikipedia.org/wiki/Protocol_Buffers
[Base64 data]:                    https://en.wikipedia.org/wiki/Base64

## Requirements

This SDK works with Python 2.6+ and Python 3.3+.

## Installing the SDK

To import the Yoti SDK inside your project, simply run the following command from your terminal:

```shell
pip install yoti
```

## SDK Project Import

You can reference the project URL by adding the following import:

```python
import "yoti_python_sdk"
```

## Configuration

After creating your application on the [Yoti Dashboard](https://www.yoti.com/dashboard/), you need to download the `.PEM` key and save it *outside* the repo (keep it private).

The variables required for the SDK to work are found in the tabs on your Yoti application's settings page ([Yoti Dashboard](https://www.yoti.com/dashboard/)). These are:

* **`YOTI_APPLICATION_ID`** - This is used to configure the [Yoti Login Button](https://www.yoti.com/developers/documentation/#2-front-end-integration).
* **`YOTI_CLIENT_SDK_ID`** - This is the SDK identifier generated by Yoti Dashboard in the Key tab when you create your app. Note this is not your Application Identifier which is needed by your client-side code.
* **`YOTI_KEY_FILE_PATH`** - This is the path to the application .pem file, we recommend keeping your .pem file outside of your repository. It can be downloaded only once from the Keys tab in your Yoti Dashboard. (e.g. /home/user/.ssh/access-security.pem).

**Please do not open the pem file** as this might corrupt the key and you will need to create a new application.

One way to configure these environment variables is to use an .env file. There are `.env.example` files supplied in the [Django](/examples/yoti_example_django/yoti_example/.env.example) and [Flask](/examples/yoti_example_flask/.env.example) example projects, which you can rename to `.env` and enter your settings into this file.

### Example Initialisation

```python
from yoti_python_sdk import Client
@app.route('/profile')
def auth():
    client = Client(YOTI_CLIENT_SDK_ID, YOTI_KEY_FILE_PATH)
    activity_details = client.get_activity_details(request.args['token'])
```

## Handling Users

When you retrieve the user profile, you receive a user ID generated by Yoti exclusively for your application.
This means that if the same individual logs into another app, Yoti will assign her/him a different ID.
You can use this ID to verify whether (for your application) the retrieved profile identifies a new or an existing user.
Here is an example of how this works:

```python
client = Client(YOTI_CLIENT_SDK_ID, YOTI_KEY_FILE_PATH)
user_profile = client.get_activity_details(token).user_profile

user_id = user_profile.get('user_id')
selfie = user_profile.get('selfie')
given_names = user_profile.get('given_names')
family_name = user_profile.get('family_name')
phone_number = user_profile.get('phone_number')
date_of_birth = user_profile.get('date_of_birth')
postal_address = user_profile.get('postal_address')
gender = user_profile.get('gender')
nationality = user_profile.get('nationality')
```

## Running the Examples

Both example applications utilise the env variables described in [Configuration](#configuration), make sure they are accessible.

* Installing dependencies: `pip install -e .[examples]` (If you're using `zsh` you need to escape the square brackets: `pip install -e .\[examples\]`)

### Flask

* Run `python examples/yoti_example_flask/app.py`

### Django

1. Change directories to the Django project: `cd examples/yoti_example_django`
2. Apply migrations before the first start by running: `python manage.py migrate`
3. Run: `python manage.py runserver 0.0.0.0:5000`

### Plugins ###

Plugins for both Django and Flask are in the `plugins/` dir. Their purpose is to make it as easy as possible to use the Yoti SDK with those frameworks. See the [Django](/plugins/django_yoti/README.md) and [Flask](/plugins/flask_yoti/README.md) README files for further details.

## Running the Tests

Run your project but please make sure you have all the correct requirements:

1. Install dependencies: `pip install -r requirements.txt`
2. Install the SDK: `python setup.py develop`
3. Execute in the main project dir: `py.test`

For information on testing with multiple Python versions, see [VERSION-SUPPORT.md](/VERSION-SUPPORT.md)

## API Coverage

* Activity Details
    * [X] User ID `user_id`
    * [X] Profile
        * [X] Photo `selfie`
        * [X] Given Names `given_names`
        * [X] Family Name `family_name`
        * [X] Mobile Number `phone_number`
        * [X] Email address `email_address`
        * [X] Date of Birth `date_of_birth`
        * [X] Address `postal_address`
        * [X] Gender `gender`
        * [X] Nationality `nationality`

## Support

For any questions or support please email [sdksupport@yoti.com](mailto:sdksupport@yoti.com).
Please provide the following to get you up and working as quickly as possible:

* Computer type
* OS version
* Version of Python being used
* Screenshot

Once we have answered your question we may contact you again to discuss Yoti products and services. If you’d prefer us not to do this, please let us know when you e-mail.
