// const express = require("express");
// const http = require('http');
// const fs = require('fs');

// const server = http.createServer((req, res) => {
//     fs.readFile('Album example · Bootstrap v5.2.html', (err, data) => {
//       if (err) {
//         res.writeHead(404, {'Content-Type': 'text/html'});
//         return res.end('404 Not Found');
//       }  
//       res.writeHead(200, {'Content-Type': 'text/html'});
//       res.write(data);
//       return res.end();
//     });
//   });

// server.use(express.static('public'));

// server.listen(3000,(err) => {
//     if (err) return console.log(err);
//     console.log("The server is listening on port 3000");
// });
const express = require("express");
const http = require('http');
const fs = require('fs');

const app = express();

app.use(express.static('public'));

app.get('/', (req, res) => {
  fs.readFile('Album example · Bootstrap v5.2.html', (err, data) => {
    if (err) {
      res.writeHead(404, {'Content-Type': 'text/html'});
      return res.end('404 Not Found');
    }  
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write(data);
    return res.end();
  });
});

http.createServer(app).listen(3000, (err) => {
  if (err) return console.log(err);
  console.log("The server is listening on port 3000");
});