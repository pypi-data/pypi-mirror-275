from functools import lru_cache

from ._container import DataStoreContainer


@lru_cache
def _get_datastore():
    from ._datastore import DataStore

    return DataStore()


def get_store(name: str) -> DataStoreContainer:
    """
    Get a store container by name. The `DataStoreContainer` is a wrapper
    around the data store that provides a get and set method to interact
    with the data store.

    Example usage:

        .. code-block:: python

            from automizor import datastore

            # Get a data store countries
            countries = datastore.get_store("countries")

            # Initialize or update json store
            countries.set([
                {
                    "name": "United States",
                    "code": "US",
                },
                {
                    "name": "Canada",
                    "code": "CA",
                },
            ])

            # Get values from json store
            result = countries.get()

            # Get a data store movies
            movies = datastore.get_store("movies")

            # Initialize or update kkv store
            movies.set({
                "US": {
                    "action": {
                        "Die Hard": 1988,
                        "The Matrix": 1999
                    }
                }
            })

            # Get values from kkv store
            result = movies.get("US")
            result = movies.get("US", "action")

            # Insert or update values
            movies.set({
                "US": {
                    "action": {
                        "Die Hard": 1988,
                        "The Matrix": 1999,
                        "John Wick": 2014
                    },
                    "comedy": {
                        "The Hangover": 2009,
                        "Superbad": 2007
                    }
                }
            })

            # Delete secondary key
            movies.set({
                "US": {
                    "action": None
                }
            })

            # Delete primary key
            movies.set({
                "US": None
            })

    """

    datastore = _get_datastore()
    return DataStoreContainer(
        datastore=datastore,
        name=name,
    )
