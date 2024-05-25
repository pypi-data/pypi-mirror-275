import logging
import time
from collections import OrderedDict
from typing import Any

import requests

from openlibrary_api.errors import *
from openlibrary_api.models import *

logger = logging.getLogger(__name__)

class _Cache:
    def __init__(
            self,
            size: int
    ):
        self.cache = OrderedDict(default=None)
        self.cache_size = size

    def get(self, id: str):
        return self.cache.get(id)
    
    def add(self, item_id, item):
        self.cache[item_id] = item
        if len(self.cache) > self.cache_size:
            for key in self.cache.keys():
                self.cache.popitem(key)
                return
    
    def empty(self):
        self.cache = OrderedDict(default=None)


class OpenLibraryAPI:
    base_url = "http://openlibrary.org/"

    def __init__(
            self, 
            works_cache_size=10,
            editions_cache_size=20,
            authors_cache_size=10,
            languages_cache_size=20
            ):
        self.works_cache = _Cache(works_cache_size)
        self.editions_cache = _Cache(editions_cache_size)
        self.authors_cache = _Cache(authors_cache_size)
        self.languages_cache = _Cache(languages_cache_size)

    def __make_request(self, request: str) -> dict:
        """
        Args:
            request (str): the request to send

        Raises:
            StatusCodeException: Error raised if status code is not 200
            APIErrorException: Error raised if error found in response dict keys

        Returns:
            dict containing response data
        """
        start = time.time()
        logger.debug(f"Sending request: {request}")
        result = requests.get(request, timeout=4)
        logger.debug(f"Received response:\nTime Taken: {time.time()-start}s\nCode: {result.status_code}\nContent: {result.json()}")
        if result.status_code != 200:
            raise StatusCodeException(result.status_code, request)
        data = result.json() #type: dict
        if "error" in data.keys():
            raise APIErrorException(data["error"], request)
        return data

    
    def __make_olid_request(self, type: str, olid: str) -> dict:
        """
        Args:
            type (str): "books", "authors", "works"
            olid (str): OpenLibrary ID (OLID) of item

        Returns:
            dict: json encoded response from server
        """
        request = OpenLibraryAPI.base_url + type + "/" + olid + ".json"
        return self.__make_request(request)
    
    def __make_isbn_request(self, isbn: str) -> dict:
        """
        Args:
            isbn (str): isbn to look up

        Returns:
            dict: json encoded response from server
        """
        request = OpenLibraryAPI.base_url + "isbn/" + isbn + ".json"
        return self.__make_request(request)
    
    def __make_language_request(self, language_code: str) -> dict:
        """
        Args:
            language_code (str): language code i.e "en", "ge", "fr" etc

        Returns:
            dict: json encoded response from server
        """
        request = OpenLibraryAPI.base_url + "languages/" + language_code + ".json"
        return self.__make_request(request)
    
    def __get_authors(self, authors: list[dict[str, Any]]) -> list[Author]:
        """Iterates through a list of author OLIDs from a work or edition request and gets the Author objects for them

        Args:
            authors (list[dict[str, dict[str, str]]]): A list of authors provided by the "authors" key from a work or edition request

        Returns:
            list[Author]: the list of Author objects
        """
        author_objs = []
        for author in authors:
            if "author" in author.keys():
                author = author["author"] #type: dict[str, str]
            olid = author["key"].replace("/authors/", "")
            author_objs.append(self.get_author_by_olid(olid, True))
        return author_objs

    def __get_works(self, works: list[dict[str, str]]) -> list[Work]:
        """Iterates through a list of work OLIDs from an edition request and gets the Work objects for them

        Args:
            works (list[dict[str, str]]): A list of works provided by the works key from an edition request

        Returns:
            list[Work]: the list of Work objects
        """
        work_objs = []
        for work in works:
            olid = work["key"].replace("/works/", "")
            work_objs.append(self.get_work_by_olid(olid))
        return work_objs
    
    def __get_languages(self, languages: list[dict[str, str]]) -> list[str]:
        """Iterates through a list of language codes from an edition request and gets the language names in English for them

        Args:
            languages (list[str]): list of language codes provided by the "languages" key

        Returns:
            list[str]: A list of English-translated language names
        """
        language_names = []
        for language in languages:
            language = language["key"]
            language = language.replace("/languages/", "")
            cache_hit = self.languages_cache.get(language)
            if cache_hit != None:
                language_names.append(cache_hit)
                continue
            name = self.__make_language_request(language)["name_translated"]["en-gb"][0]
            self.languages_cache.add(language, name)
            language_names.append(name)
        return language_names
    
    def __build_edition_from_result(self, result: dict) -> Edition:
        olid = result["key"].replace("/books/", "")
        works = self.__get_works(result["works"]) if "works" in result.keys() else []
        authors = self.__get_authors(result["authors"]) if "authors" in result.keys() else []
        languages = self.__get_languages(result["languages"]) if "languages" in result.keys() else []
        edition = Edition(
            olid, 
            result["publishers"] if "publishers" in result.keys() else [], 
            result["publish_date"] if "publish_date" in result.keys() else "unknown", 
            result["title"] if "title" in result.keys() else "unknown", 
            authors,
            languages, 
            result["number_of_pages"] if "number_of_pages" in result.keys() else -1, 
            works, 
            result["physical_format"] if "physical_format" in result.keys() else "unknown",
            result["isbn_10"] if "isbn_10" in result.keys() else "unknown",
            result["isbn_13"] if "isbn_13" in result.keys() else "unknown",
            result["contributions"] if "contributions" in result.keys() else []
            )
        self.editions_cache.add(olid, edition)

    def get_edition_by_isbn(self, isbn: str) -> Edition | None:
        result = self.__make_isbn_request(isbn)
        if result is None:
            return None
        return self.__build_edition_from_result(result)     
        
    def get_work_by_olid(self, olid: str, cache=True) -> Work | None:
        if cache:
            cache_hit = self.authors_cache.get(olid)
            if cache_hit != None:
                return cache_hit
        result = self.__make_olid_request("works", olid)
        if result is None:
            return None
        authors = self.__get_authors(result["authors"]) if "authors" in result.keys() else []
        work = Work(
            olid, 
            result["title"] if "title" in result.keys() else "unknown", 
            result["subjects"] if "subjects" in result.keys() else [],
            authors,
            result["description"] if "description" in result.keys() else "", 
            result["covers"] if "covers" in result.keys() else []
            )
        self.works_cache.add(olid, work)
        return work

    def get_edition_by_olid(self, olid: str, cache=True) -> Edition | None:
        if cache:
            cache_hit = self.editions_cache.get(olid)
            if cache_hit != None:
                return cache_hit
        result = self.__make_olid_request("books", olid)
        if result is None:
            return None
        return self.__build_edition_from_result(result)
        

    def get_author_by_olid(self, olid: str, cache=True) -> Author | None:
        if cache:
            cache_hit = self.authors_cache.get(olid)
            if cache_hit != None:
                return cache_hit
        result = self.__make_olid_request("authors", olid)
        if result is None:
            return None
        author = Author(
            olid, 
            result["name"] if "name" in result.keys() else None, 
            result["bio"] if "bio" in result.keys() else None, 
            result["birth_date"] if "birth_date" in result.keys() else None,
            result["death_date"] if "death_date" in result.keys() else None,
            result["photos"] if "photos" in result.keys() else None
            )
        self.authors_cache.add(olid, author)
        return author
    
    #TODO: implement getting cover images
    def get_cover_by_id(self, cover: int):
        pass
    
    #TODO: implement getting author photos
    def get_author_photo_by_id(self, photo: int):
        pass
    
    def clear_cache(self):
        self.authors_cache.empty()
        self.works_cache.empty()
        self.editions_cache.empty()

if __name__ == "__main__":
    api = OpenLibraryAPI()
    logging.basicConfig(level=logging.DEBUG, filename="test_log.log")
    print(api.get_edition_by_isbn("0140328726"))