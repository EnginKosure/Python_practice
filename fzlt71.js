var http = require('http');

// console.log('http', http)

http.createServer((req, res) => {
    console.log(req);
    console.log('req url', req.url);
    if (req.url === "/") {
        res.end('Hello from homepage');
    } else {
        res.writeHead(404);
        res.end(http.STATUS_CODES[404])
    }
}).listen(3007)