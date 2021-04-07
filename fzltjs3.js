function Book(title, author, ISBN, numCopies) {
    this.title = title;
    this.author = author;
    this.ISBN = ISBN;
    this.numCopies = numCopies;
}
// Here the function is declared on prototype, because we don't need to create a new instance
// of this function each time we make a new object.
// Each instance can access this function from its prototype and doesn't create a new one each time...
Book.prototype.getAvailability = function () {
    if (this.numCopies == 0) {
        return "Out of stock";
    } else if (this.numCopies < 10) {
        return "Low stock";
    }
    return "In stock";
}