from constants import TYPE_TO_SEARCHER, LINEAR_TYPE_SEARCHER
from data_sources.file_data_source import CSVFileDataSource
from matchers.simple_matcher import SimpleMatcher
from rank_finders.count_rank_finder import CountRankFinder
from utils import upper_case, space_split, Book


class Searcher(object):
    normalize = upper_case
    split = space_split
    data_source = CSVFileDataSource(Book)
    matcher = SimpleMatcher
    rank_finder = CountRankFinder
    type = LINEAR_TYPE_SEARCHER

    searcher = TYPE_TO_SEARCHER.get(type)(normalize, split, data_source, matcher, rank_finder)

    @classmethod
    def search(cls, query):
        """
        Search data by query from data source

        @param query: search query
        @type query: str
        @return: found a list of objects
        """
        return cls.searcher.search(query)
