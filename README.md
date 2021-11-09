# Distributed system programming Assignment 1, spelling bee.

## Use of Patterns

### Template:
_This template class is using abstract methods to lay out and direct how to design and implement a game of spelling bee._
#### service/game_service.py 
- This is the blueprint for a spelling bee game implementation. Abstract methods are used to define required consistent steps (functions) to have a working game of spelling bee. If I had to implement a similar version of spelling bee. I can easily use that template and have a functional game implementation working with a server and client(s).

### Factory:
_The object factory will allow me to create an instance of a class while hiding the exact class that lies behind the instance._
#### pattern/object_factory.py
- It allows me to create an instance of a class, here solely a spelling_bee_single class using the SpellingBeeGameBuilder. But I could have other classes, for example, different types of spelling bee games. For example, the client can pass as a parameter the type of the game that they wish to play, here "Spelling Bee Single player". The server can create an instance of this game using the object factory and this message. By simply passing the message as a key, without having to know the exact class that lies behind.
    
### Singleton:
_The singleton pattern allows to instanciate a single instance of a class._
#### server/game_registry.py
- The use of singleton here is simple and make sure that we only have a single instance of the game_registry class. This instance gathers all the games that are currently being played on the server, and allows to retrieve them.
#### dao/spelling_bee_dao_singleton.py 
- The use of singleton in this dao ensures that we only load the words_dictionary.json and pangrams.json only once. Each game of spelling bee that requires this type of "dictionary", will be able to get an instance of this dao without having to create a new instance (unless there wasn't any instance yet). This instance solely interacts with both of those dictionaries.

> Ps: I would have liked to use a more layered directory structure. Such as having an "app" directory with the "server", "client" and "gameimpl". But my lack of knowledge about creating a Python package just made it impossible. Not letting file being able to import other ones.