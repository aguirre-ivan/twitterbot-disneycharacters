# Disney Twitterbot

A twitter bot that tweets random Disney characters with their information (films, TV shows, videogames)

## Installation

This bot uses tweepy module. You can install it using pip.

```
$ pip install tweepy
```

You need to create a new application on [twitter](https://developer.twitter.com/en). Get keys and access token for [credentials.py](/credentials.py)

## Usage

Edit [credentials.py](/credentials.py) and run [disney_bot.py](/disney_bot.py)

```
$ python disney_bot.py
```
You can change the tweeting time in [disney_bot.py](/disney_bot.py)
## Format tweet

```
"character name"

Films: "character films"
TV shows: "character TV shows"
Videogames: "character videogames"

"character image"
```

Example in [@DisneyCharact](https://twitter.com/DisneyCharact)

![ExampleTweet](/example.png "Example tweet")

## APIS

- [Twitter](https://developer.twitter.com/en/docs): Read and write Twitter data	
- [Disney](https://disneyapi.dev/): Information of Disney characters

## Twitterbot status

Offline