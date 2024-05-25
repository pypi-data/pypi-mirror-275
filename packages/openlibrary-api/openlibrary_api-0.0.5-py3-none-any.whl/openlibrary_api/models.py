

class Work:
    """
    Currently supported fields:
    olid: str
    full_title: str
    subjects: list[Subject]
    authors: list[Author]
    description: str
    covers: list[str] (contains keys to covers but does not load them)
    """
    def __init__(
            self,
            olid: str,
            title: str,
            subjects: list["Subject"],
            authors: list["Author"],
            description: str,
            covers: list[str],
    ):
        self.olid = olid
        self.title = title
        self.subjects = subjects
        self.authors = authors
        self.description = description
        self.covers = covers

    def __repr__(self) -> str:
        return f"""
        <Work (olid={self.olid}, 
        title={self.title}, 
        authors={self.authors}, 
        subjects={self.subjects},
        description={self.description},
        covers={self.covers}
        )>"""

class Edition:
    """
    Currently supported fields:
    olid: str
    publishers: list[str]
    publish_date: datetime
    full_title: str
    languages: list[str]
    number_of_pages: int
    works: list[Work]
    physical_format: str
    isbn_10: str
    isbn_13: str
    contributions: list[str]
    """
    def __init__(
            self,
            olid: str,
            publishers: list[str],
            publish_date: str,
            full_title: str,
            authors: list["Author"],
            languages: list[str],
            number_of_pages: int,
            works: list[Work],
            physical_format: str,
            isbn_10: str,
            isbn_13: str,
            contributions: list[str]
    ):
        self.olid = olid
        self.publishers = publishers
        self.publish_date = publish_date
        self.full_title = full_title
        self.authors = authors
        self.languages = languages
        self.number_of_pages = number_of_pages
        self.works = works
        self.physical_format = physical_format
        self.isbn_10 = isbn_10
        self.isbn_13 = isbn_13
        self.contributions = contributions

    def __repr__(self) -> str:
        return f"""
        <Edition (olid={self.olid}, 
        publishers={self.publishers},
        publish_date={self.publish_date}, 
        full_title={self.full_title},
        authors={self.authors}, 
        languages={self.languages}, 
        number_of_pages={self.number_of_pages}, 
        works={self.works},
        physical_format={self.physical_format},
        isbn_10={self.isbn_10}, 
        isbn_13={self.isbn_13},
        contributions={self.contributions}
        )>"""

class Author:
    """
    Currently supported fields:
    olid: str
    name: str
    bio: str
    birth_date: str
    death_date: str
    photos: list[int] (a list of photo ids for OpenLibrary, does not load the images)
    """
    def __init__(
            self,
            olid: str,
            name: str,
            bio: str,
            birth_date: str,
            death_date: str,
            photos: list[int]
    ):
        self.olid = olid
        self.name = name
        self.bio = bio
        self.birth_date = birth_date
        self.death_date = death_date
        self.photos = photos

    def __repr__(self) -> str:
        return f"""
        <Author (olid={self.olid}, 
        name={self.name}, 
        bio={self.bio}, 
        photos={self.photos}
        )>"""

class Subject:
    pass
