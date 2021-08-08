# Pokemon Crawler

Project started from https://docs.docker.com/compose/django/

Some useful commands:

* `docker-compose up`
* `docker-compose exec web bash`
* `docker-compose exec web python -m pip install -r requirements.txt`


Thoughts:

I have found out that im am not good at setting up projects. A bit of time was wasted trying to get pytest to work. It complianed about DJANGO_SETTINGS_MODULE missing. So i wrote some tests using traditional Django tests.

Design:
The design of the api crawler was interesting. I didnt know what an api crawler is at first, i thought to use scrapy but thats a bit of a powerhouse, I assume api crawling is similar to web crawling. so Requests package is all i need.
I designed the function to pull data depending on the game ie blue, yellow and i tried to allow small number of pokemon to be pulled, and resumed. Because the api is free and open, im not sure they will like me pulling massive amount of data in one go. I ran out of time but in future i can limit the requests.

Implementation:
Basically I added one model which links to pokemon and the version, this should allow updates without destroying old data. so Gengar can have entrys from blue, red, gold etc. so i think this hits the requirement `so it's important your crawler can catch new Pokémon and update facts about existing ones`
