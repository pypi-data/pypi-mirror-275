# APNS Push Notification

This Python script allows you to send push notifications to Apple devices manually. It uses the Apple Push Notification service (APNS) to deliver notifications to your application users.

## Why use initialize_apns?

The `initialize_apns` function is used to set up the APNS with your application's specific details. This includes your key ID, team ID, bundle ID, and the path to your p8 or pem file. You can also specify whether you want to use the production or sandbox environment (default is sandbox).

## How to use the script?

First, import the necessary modules:

```python
import apns
```

Then, initialize the APNS with your application's details:

```python
KEY_ID = ''
TEAM_ID = ''
BUNDLE_ID = 'com.test.app'
IS_PROD = False
P8_KEY_PATH = 'path/to/p8/key'
PEM_FILE_PATH = 'path/to/pem/file'
APNS_PRIORITY = 10
APNS_EXPIRATION = 0

apns.initialize_apns(key_id=KEY_ID,
                     team_id=TEAM_ID,
                     bundle_id=BUNDLE_ID,
                     is_prod=IS_PROD,
                     p8_key_path=P8_KEY_PATH,
                     pem_file_path=PEM_FILE_PATH,
                     apns_priority=APNS_PRIORITY,
                     apns_expiration=APNS_EXPIRATION)

apns.apns_config().verbose = True
```

Now, you can send a push notification:

```python
device_token = ""  
data = {}  
title = "Hello World!"

response: APNSResponse = apns.push(device_token=device_token, title=title, data=data, badge=1, push_type=apns.PushType.alert, collapse_id=None)
```

## Using p8 or pem file

Depending on your preference or requirements, you can use either a p8 or pem file for authentication. If you want to use a p8 file, pass the path to the `p8_key_path` parameter in the `initialize_apns` function. If you want to use a pem file, pass the path to the `pem_file_path` parameter.

## Getting a p8 file or pem file
To get the p8 or pem file for APNS push notification, you can follow these steps:

1. For p8 file:
   - Go to the Apple Developer Portal.
   - Navigate to the "Certificates, Identifiers & Profiles" section.
   - Under the "Keys" section, click on the "+" button to create a new key. (make sure to select **Apple Push Notifications service (APNs)** from the checkbox)
   - Make sure to write down the **Key ID** as you will need it later.
   - Download the generated p8 file and save it to a secure location.

2. For pem file:
   - Convert the exported .p12 file to a .pem file using the following command in the terminal:
     ```
     openssl pkcs12 -clcerts -legacy -nodes -in Certificates.p12 -out AuthKey.pem
     ```
     Replace "Certificates.p12" with the path to your .p12 file or keep it if you're in the same directory as your .p12 file.
   - Enter the password for the .p12 file when prompted (hit Enter if blank).
   - The converted pem file will be saved as "AuthKey.pem" in the current directory.

Once you have obtained the p8 or pem file, you can use it in the `initialize_apns` function by providing the path to the file in the `p8_key_path` or `pem_file_path` parameter, respectively.