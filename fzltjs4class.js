function Movie(title, director, genre, releaseYear, rating) {
    this.title = title;
    this.director = director;
    this.genre = genre;
    this.releaseYear = releaseYear;
    this.rating = rating;

}

//All instances can reach and use this method over prototype by reference.
Movie.prototype.getOverview = function () {
    return `${this.title}, a(n) ${this.genre} film directed by ${this.director} was released 
    in ${this.releaseYear}. It received a rating of ${this.rating}.`;
}

const Spiderman = new Movie("Spiderman", "Sam Raimi", "Action", 2002, 87);
const Batman = new Movie("The Dark Knight", "Christopher Nolan", "Action", 2008, 83);

console.log(Spiderman.getOverview());
console.log(Batman.getOverview());
console.log(Batman);


class MovieClass {
    constructor(title, director, genre, releaseYear, rating) {
        this.title = title;
        this.director = director;
        this.genre = genre;
        this.releaseYear = releaseYear;
        this.rating = rating;
    }
    getOverview() {
        return `${this.title}, a(n) ${this.genre} film directed by ${this.director} was released 
        in ${this.releaseYear}. It received a rating of ${this.rating}.`;
    }
}

const SpidermanClass = new MovieClass("Spiderman", "Sam Raimi", "Action", 2002, 87);
console.log(SpidermanClass.getOverview());