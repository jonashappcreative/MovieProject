from abc import ABC, abstractmethod

class IStorage(ABC):
    '''
    Docstring:
    This abstract class will be the backbone for the interface of your project.
    In the interface you do not implement functions itsself, you just define them!
    This is the basis object for all your different Data Import Options
    (One Object Handles CSV, one JSON, one TXT, ...)
    '''
    @abstractmethod
    def _list_movies(self):
        pass

    @abstractmethod
    def _add_movie(self, title, year, rating, poster):
        pass

    @abstractmethod
    def _delete_movie(self, title):
        pass

    @abstractmethod
    def _update_movie(self, title, rating):
        pass
