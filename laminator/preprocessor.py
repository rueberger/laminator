""" This module contains the Preprocessor abstract class
"""


from abc import ABC, abstractmethod


class Preprocessor(ABC):
    """ Abstract interface for preprocessors
    """


    def preprocess(self, pipeline_spec):
        """ Does the following steps:

        1. Parses pipeline_spec into the chained spec specific to this Preprocessor,
        2. Fetches the data handle from the parent preprocessor
        3. calls self._preprocess with chained_spec and data handle
        4. saves output of preprocess in file store (pass to self.stash)
        5. closes data handle from parent (even if things failed)
        """
        # TODO: implement (not abstract)
        pass


    def provide(self, pipeline_spec):
        """ Does the following:

        Returns a data handle for the preprocessed data, built according to pipeline_spec

        Builds the data if necessary
        """
        # TODO: implement (not abstract)
        pass


    def stash(self, chained_spec, transformed_data):
        """ Stash transformed data in datastore

        Does the following:

        1. write transformed_data to datastore, mirroring dict structure
        2. add chained_spec to datastore spec lookup
        """
        # TODO: implement (not abstract)
        pass

    def get_parent_hash(self, pipeline_spec):
        """ Get the hash of the parent spec chain (Merkle tree)
        """
        # TODO: implement (not abstract)
        pass


    @abstractmethod
    def _preprocess(self, data_handle, chained_spec):
        """ Preprocessing core logic

        Args:
          data_handle
          chained_spec

        Returns:
          transformed data in dict with structure mirroring desired datastore structure

        """
        pass


    @property
    @abstractmethod
    def store_path(self):
        """ Returns absolute path to the datastore for this preprocessor
        """
        pass


    @property
    @abstractmethod
    def parent(self):
        """ Return parent preprocessor *class*
        """
        pass
