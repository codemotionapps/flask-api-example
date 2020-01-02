
This is a simple example of Ora's OAuth 2 API flow.

To test it out, you should put your app's client_id and client_secret. The redirect_uri you should provide to Ora is http://localhost:5001/redirect-uri
Here is an article explaining how to create OAuth app in Ora https://help.ora.pm/article/79-getting-started-with-ora-public-api

Put your CLIENT_ID and CLIENT_SECRET in the app/config.py file.

To start the server you should run this commands:
```
cd flask-api-example
pip3 install -r requirements.txt
python3 app.py
```