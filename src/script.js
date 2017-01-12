var fs = require('fs');

var obj;

fs.readFile('data.json', 'utf8', function (err, data) {
    if (err) throw err;
    obj = JSON.parse(data);
});

var dat = JSON.stringify(obj, null, 2);

document.getElementById("body").innerHTML = dat;