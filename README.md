# darbird-python

![](https://img.shields.io/pypi/v/darbird.svg)

> The SDK provides convenient access to the Darbird APIs to python apps.


## Documentation
Take a look at the [API docs here](https://developers.darbird.com/).

## Install

```bash
$ pip  install darbird # python 2.7.x

OR

$ python -m pip install darbird # python 2.7.x

OR

$ pip3 install darbird # python 3.6.x

OR

$ python3 -m pip install darbird # python 3.6.x

```

## Usage

The package needs to be configured with your app username and API key, which you can get from the [dashboard](https://console.darbird.com/).

> Your receipent number must be in an International Number example (+234xxxxxxxxxx)

```python
# import package
import darbird


# Initialize SDK
username = "YOUR_USERNAME"    # use 'sandbox' for development in the test environment
api_key = "YOUR_API_KEY"      # use your sandbox app API key for development in the test environment
darbird.initialize(username, api_key)


# Initialize a service e.g. SMS
sms = darbird.SMS


# Use the service synchronously
response = sms.send("Hello Message!", ["+2547xxxxxx"])
print(response)

# Or use it asynchronously
def on_finish(error, response):
    if error is not None:
        raise error
    print(response)

sms.send("Hello Message!", ["+2547xxxxxx"], callback=on_finish)    

```

See [example](example/) for more usage examples.


## Initialization

Initialize the SDK by calling `darbird.initialize(username, api_key)`. After initialization, you can get instances of offered services as follows:

- [SMS](#sms): `darbird.SMS`
- [Voice](#airtime): `darbird.Voice`
- [MMS](#payments): `darbird.MMS`
- [Authy](#voice): `darbird.Authy`


### `Sms`

- `send(message: str, recipients: str, sender_id: str = None, enqueue: bool = False)`: Send a message.

    - `message`: SMS content. `REQUIRED`
    - `recipients`: Phone numbers. `REQUIRED`
    - `sender_id`: Shortcode or alphanumeric ID that is registered with your Darbird account.
    - `enqueue`: Set to `true` if you would like to deliver as many messages to the API without waiting for an acknowledgement from telcos.

- `sendschedule(message: str, recipients: str, schedule: str, sender_id: str = None, enqueue: bool = False))`: Send a premium SMS

    - `message`: SMS content. `REQUIRED`
    - `recipients`: An array of phone numbers. `REQUIRED`
    - `schedule`: Date like this format: m/d/Y h:i A.  `REQUIRED`
    - `sender_id`: Shortcode or alphanumeric ID that is registered with your Darbird account.
    - `enqueue`: Set to `true` if you would like to deliver as many messages to the API without waiting for an acknowledgement

### `Voice`

- `send(message: str, recipients: str, sender_id: str = None, enqueue: bool = False)`: Send a message.

    - `message`: SMS content. `REQUIRED`
    - `recipients`: Phone numbers. `REQUIRED`
    - `sender_id`: Shortcode or alphanumeric ID that is registered with your Darbird account.
    - `enqueue`: Set to `true` if you would like to deliver as many messages to the API without waiting for an acknowledgement from telcos.
    

### `MMS`

- `send(message: str, recipients: str, media_url:str, sender_id: str = None, enqueue: bool = False)`: Send a message.

    - `message`: SMS content. `REQUIRED`
    - `recipients`: Phone numbers. `REQUIRED`
    - `sender_id`: Shortcode or alphanumeric ID that is registered with your Darbird account.
    - `media_url`: A link of your mms media.
    - `enqueue`: Set to `true` if you would like to deliver as many messages to the API without waiting for an acknowledgement from telcos.

### `Authy`

- `send(message: str, recipients: str, media_url:str, sender_id: str = None, enqueue: bool = False)`: Send a message.

    - `to_number`: Phone numbers. `REQUIRED`
    - `token_lenght`: Token Lenght. `REQUIRED`
    - `sender_id`: Shortcode or alphanumeric ID that is registered with your Darbird account.
    - `msg_type`: Authenication type eg. voice or sms.


- `authverify(self, recipients, code, sender_id=None, unicodes=False, callback=None)`: Verify Token.

    - `to_number`: Phone numbers. `REQUIRED`
    - `auth_code`: Receieved Authenication code. `REQUIRED`
    - `sender_id`: Shortcode or alphanumeric ID that is registered with your Darbird account.



## Development
```shell
$ git clone https://github.com/darbird/darbird-python.git
$ cd darbird-python
$ touch .env
```

Make sure your `.env` file has the following content then run `python -m unittest discover -v`

```ini
# AT API
USERNAME=sandbox
API_KEY=some_key
```

## Issues

If you find a bug, please file an issue on [our issue tracker on GitHub](https://github.com/darbirdLtd/darbird-python/issues).