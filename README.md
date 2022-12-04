# FREE SMS 💻
Send SMS to others for FREE &amp; from your PC!

### What is this?
Free Sms is an Open Source initiative of [MrShadowDev](https://github.com/MrShadowDev) with which you can send sms, without the need for a phone number or a mobile device.

### Setup 
* [Download Here](https://github.com/MrShadowDev/Free-SMS/archive/refs/heads/main.zip)
* Unzip it to your Desktop.
* Open ``Command Prompt`` on the folder and type:
```python
pip install twilio
```
* Create your account [here](https://www.twilio.com/try-twilio) to be able to use this.
* Change your **SID** & **Auth_Token** in sms.py 
```python
SID = 'CHANGE_HERE'
Auth_Token = 'CHANGE_HERE'
```
* Change the following sentence in sms.js
```python
cl.messages.create(body='CHANGE_THE_TEXT_TO_SEND', from_='THE_NUMBER_PROVIDED_IN_TWILIO, to= 'PHONE_NUMBER_OF_RECEIVER')
```
