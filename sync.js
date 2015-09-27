var fs = require("fs");
var path = require("path");

var config = {
    source: "app/static",
    destination: "/opt/ksc/static"
};

function rmrf(path) {
    if (fs.existsSync(path)) {
        fs.readdirSync(path).forEach(function(file, index) {
            var curPath = path + "/" + file;
            if (fs.lstatSync(curPath).isDirectory()) {
                rmrf(curPath);
            } else {
                fs.unlinkSync(curPath);
            }
        });
        fs.rmdirSync(path);
    }
}

function cpr(src, dest) {
    var exists = fs.existsSync(src);
    var stats = exists && fs.statSync(src);
    var isDirectory = exists && stats.isDirectory();

    if (exists && isDirectory) {
        fs.mkdirSync(dest);
        fs.readdirSync(src).forEach(function(childItemName) {
            cpr(path.join(src, childItemName), path.join(dest, childItemName));
        });
    } else {
        fs.linkSync(src, dest);
    }
}

rmrf(config.destination);
cpr(config.source, config.destination);

fs.watch(config.source, function(event, filename) {
    rmrf(config.destination);
    cpr(config.source, config.destination);
});
