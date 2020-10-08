import pymongo
import pprint

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]
print(mydb)

"""
songs.db
[
    {
        name: "name of the song",
        songid: "randomid that's a string",
        author: "string of the author's name",
        genre: "string of the genre",
        votes: optional. it is default zero, int.
        postedBy: "string person who posted",
        songLink: "spotify embedded"
    }
    
    other songs dicts...
]

user.db
[
    {
        userid: "user's unique id"
        songs suggested: [a list of songids that the user has suggested]
        role: "the user's role. could be either user/mod/admin/banned "
    }
]
"""

""" primary methods (pretty important) """


# takes in list of song dicts and adds to db
def addSongs(songs):
    pass


# takes in list of song ids and removes those song dicts from db
def deleteSongs(ids):
    pass


# takes in list of song ids and returns those song dicts from db
def getSongs(ids):
    return  # something


# takes in list of user dicts and adds to db
def addUsers(users):
    pass


# takes in list of user ids and removes those user dicts from db
def deleteUsers(ids):
    pass


# takes in list of user ids and returns them from db
def getUsers(ids):
    return  # something


# simply removes all songs from db
def deleteAllSongs():
    pass


# takes in a key and a value and adds those keys and values to each individual user's dicts that don't already have that
# particular key assigned
def addField(key, value):
    pass


""" secondary methods (not too important but will be used) """


# replace one genre with another genre for ALL songs in songs db
def replaceGenre(old, new):
    pass


# replace a particular songs genre with another genre
def setSongGenre(songid, genre):
    pass


# set user's key "role" to have value role
def setUserRole(userid, role):
    pass


"""are for testing code :3"""

pprint.pprint(getSongs(ids))
