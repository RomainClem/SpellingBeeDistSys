import pattern.object_factory as object_factory


class GameFactory(object_factory.ObjectFactory):
    def get(self, game_type, **kwargs):
        return self.create(game_type, **kwargs)


