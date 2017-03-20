class LinearSearcher(object):
    def __init__(self, normalize, split, data_source, matcher, rank_finder):
        self.normalize = normalize
        self.split = split
        self.data_source = data_source
        self.object_cls = data_source.object_cls
        self.matcher = matcher
        self.rank_finder = rank_finder

    def search(self, query):
        """
        Search data by query from data source using 'linear' method

        @param query: search query
        @type query: str
        @return: found a list of objects
        """
        query = self.normalize(query)
        query_words = self.split(query)
        results = []
        for row in self.data_source.get_object_generator():
            title = self.normalize(row.title)
            title_words = self.split(title)
            query_word_to_indexes = self.matcher.get_word_to_indexes(query_words, title_words)
            if query_word_to_indexes:
                rank = self.rank_finder.find(query_word_to_indexes)
                results.append(self.object_cls(id=row.id, title=row.title, rank=rank))

        results.sort(key=lambda b: b.rank, reverse=True)
        return results

