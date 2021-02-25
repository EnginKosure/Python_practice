class Pagination:

    def __init__(self, items=0, pageSize=10):
        self.items = items
        self.pageSize = int(pageSize)
        self.totalPages = 1 if not self.items else (
            len(self.items) + self.pageSize) // self.pageSize
        self.currentPage = 1

    def getItems(self):
        return self.items

    def getPageSize(self):
        return self.pageSize

    def getCurrentPage(self):
        return self.currentPage

    def prevPage(self):
        if self.currentPage == 1:
            return self
        self.currentPage -= 1
        return self

    def nextPage(self):
        if self.currentPage >= self.totalPages:
            return self
        self.currentPage += 1
        return self

    def firstPage(self):
        self.currentPage = 1
        return self

    def lastPage(self):
        self.currentPage = self.totalPages
        return self

    def goToPage(self, page):
        page = int(page)
        if page < 1:
            page = 1
        if page > self.totalPages:
            page = self.totalPages
        self.currentPage = page
        return self

    def getVisibleItems(self):
        start_idx = (self.currentPage - 1) * self.pageSize
        return self.items[start_idx:start_idx + self.pageSize]
