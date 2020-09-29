const https = require("https");
const fs = require("fs");
const express = require("express");




const options = {
  key: fs.readFileSync("private-key.pem"),
  cert: fs.readFileSync("public-cert.pem"),
  rejectUnauthorized: false
};

const app = express();

app.use((req, res) => {
  console.log(req)
  res.writeHead(200);
  //res.end("hello world\n");
});

app.listen(8000);

https.createServer(options, app).listen(8080);
