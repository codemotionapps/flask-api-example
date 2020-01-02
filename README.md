
This is a simple example of Ora's OAuth 2 API flow.

To test it out, you should firstly create an OAuth app in Ora: Here is a link to a help article that will help you with creating the app: https://help.ora.pm/article/79-getting-started-with-ora-public-api
While creating the OAuth app, you will need to provide a redirect_uri. The uri for this example is:
```
http://localhost:5001/redirect-uri
```
After you create the app, you will receive CLIENT_ID and CLIENT_SECRET. Put them in the `app/config.py` file.

To start the server you should run this commands:
```
cd flask-api-example
pip3 install -r requirements.txt
python3 app.py
```
