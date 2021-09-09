## product name - tourism products api v1


### what is this?
 a django-based backend with an api that should manage tourist locations: name of the place, brief description, pictures of the place and all of that. it also generates a unique QRcode for each location for users to scan if they want to see the tourist attraction or book a visit to said place

### why am i making it?
i built this as part of my solution to the 2020 facebook build for sdg hackathon. it was a huge learning experience as is had to work with a deadline; i had just started to learn to use django and this experience forced me to learn in real time

![gif of working prototype](https://pbs.twimg.com/media/EpZF-4tXcAQTTBe?format=jpg&name=900x900)
<center style=color:grey;>a screenshot of the frontend</center>

### want to use it?
please do this at your own risk. this was made under stressful conditions and at a time when i was still getting into programming

but if you insist:
```
git clone https://github.com/dibrinsofor/backend-product-APIs
```
once you've cloned the repo, navigate to the local directory and install all of the requirements in the "requirements.txt" file
```
pip install -r requirements.txt
```
😬 and then....**drumroll
```
python manage.py runserver
```
that should get the server up and running and then i detail all of the expected and actual endpoints of the project on [here](https://www.twitter.com/notdibri)

### how it works
basic crud functionalities, and then generates a qrcode for each tourist attraction that returns a web page of said attraction and its description. i 100 percent did not explain this well

#### technologies
this was built entirely with love on an eventful day with:

- django
- pillow
- django serializers
- django REST framework
- hosted on heroku
- 💛 

### what's coming next
we did not continue working on the project after we got cut and that sucks but you know. i plan to clean this up and undo some of the mistakes i made the first time

### want to help make this better?
i will send you a gift basket if you acc contribute to this...jk. we were too ambitious and tried to implement too many features instead of working on an mvp but if you think you can help fix this then by all means, please do

[//]: # (So depending on use case, you may want to keep the documentation short. in that case you may not need to include the last two sections or you can)
