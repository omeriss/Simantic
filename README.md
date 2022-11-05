# Simantic
This is a app for the semantle game.
The client is written with react native and the server is written in python using flask.
The goal of the game is to guess the secret word, the player can do it by trying to guess words, for each word the player guesses he gets data about how similar his word is to the word he needs to find.
This is done by using word2vec. By representing each word by a vector and training a machine learning model to find the vectors for each word (I used Wikipedia to train the model)  We can find how similar each word is to the word the player is trying to guess.
