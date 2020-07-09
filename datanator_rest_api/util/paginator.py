class Paginator:

    def __init__(self, count, docs):
        """Paginator init
        
        Args:
            count (:obj:`int`): total number of files
            docs (:obj:`Iter`): complete documents
        """
        self.count = count
        self.docs = docs

    def page(self, _from=0, size=10):
        """Calculate page information.

        Args:
            _from (:obj:`int`, optional): Page starting from. Defaults to 0.
            size (:obj:`int`, optional): page size. Defaults to 10.

        Returns:
            (:obj:`list`): page info
        """
        result = []
        starting_record = _from * size
        if self.count - starting_record >= size:            
            for doc in self.docs[starting_record: starting_record+size]:
                result.append(doc)
            return result
        elif 0 < self.count - starting_record < size:
            for doc in self.docs[starting_record:]:
                result.append(doc)
            return result 
        else:
            return result