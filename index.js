const express = require("express");
const path = require("path");
const app = express();
const port = 5000;
const host = "http://localhost";
const wrongPath = `${__dirname}//testFolder/int`;
const customFile = "custom.png";
//console.log("customFile Extension", path.extname(customFile));
//console.log("normalized path:", path.normalize(wrongPath));
const customPath = path.join(__dirname, "/testFolder");
//console.log("customPath", customPath);

app.get("*", (req, res) => {
    console.log("req url", req.url);
    console.log("req baseUrl", req.baseUrl);
    console.log("req original Url", req.originalUrl);
    console.log("req path", req.path);
    console.log("req query", req.query);
    const clientNumber = req.query.no;
    res.send(`Your number is ${clientNumber}`);
});
app.listen(port, () => {
    console.log(`I'm listening on ${host}:${port}`);
});
