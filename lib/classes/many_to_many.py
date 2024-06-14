from collections import Counter

class Article:
    _all_articles = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Author must be of type Author.")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be of type Magazine.")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        
        
        
        self._author = author
        self._magazine = magazine
        self._title = title
        self.__class__._all_articles.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("Author must be of type Author.")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise TypeError("Magazine must be of type Magazine.")
        self._magazine = value
        
class Author:
    def __init__(self, name):
        if not isinstance(name,str):
            raise TypeError("Name must be of type str")
        if len(name) == 0:
            raise ValueError('Name must be longer than 0 characters')
        self._name = name

    @property
    def name(self):
        return self._name

    def articles(self):
        return [article for article in Article._all_articles if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be of type Magazine.")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        return Article(self, magazine, title)

    def topic_areas(self):
        mag_categories = [article.magazine.category for article in self.articles()]
        if mag_categories:
            return list(set(mag_categories))
        return None

class Magazine:
    _all_magazines = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._name = name
        self._category = category
        self.__class__._all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value,str) and (2 <= len(value) <=16):
            self._name = value
        else:
            raise ValueError('Name must be of type string and between 2 and 16 characters')

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = value

    def articles(self):
        return [article for article in Article._all_articles if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        if titles:
            return titles
        return None

    def contributing_authors(self):
        authors = Counter(article.author for article in self.articles())
        result = [author for author, count in authors.items() if count > 2]
        return result if result else None

    @classmethod
    def top_publisher(cls):
     if not cls._all_magazines:
        return None
     top_magazine = max(cls._all_magazines, key=lambda mag: len(mag.articles()))
     return top_magazine if top_magazine.articles() else None