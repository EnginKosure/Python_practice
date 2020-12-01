var http = require('http');

console.log('http', http)

http.createServer((req, res) => {
    res.end('Hello from server')
}).listen(3000)