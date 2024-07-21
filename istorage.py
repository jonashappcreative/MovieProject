from abc import ABC, abstractmethod


class IStorage(ABC):
    """
    Docstring:
    This abstract class will be the backbone for the interface of your project.
    In the interface you do not implement functions itself, you just define them!
    This is the basis object for all your different Data Import Options
    (One Object Handles CSV, one JSON, one TXT, ...)
    """

    @abstractmethod
    def _list_movies(self):
        pass

    @abstractmethod
    def _add_movie(self):
        """
        Add a film to the movies list.
        Does not need any arguments as we are puling the movie data from the API anyway
        :return: None
        """
        pass

    @abstractmethod
    def _delete_movie(self):
        """
        Deletes a film from the list. Does not need a title since we ask in the function.
        A check if there are even films to delete firsthand would be great.
        :return: None
        """
        pass

    @abstractmethod
    def _update_movie(self, title, rating):
        pass
