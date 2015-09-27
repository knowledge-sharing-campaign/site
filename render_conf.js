var fs = require("fs");

// Original author: Krasimir Tsonev (krasimirtsonev.com)
function render(template, options) {
    var re = /<%([^%>]+)?%>/g,
        reExp = /(^( )?(if|for|else|switch|case|break|{|}))(.*)?/g,
        code = 'var r=[];\n',
        cursor = 0,
        match;

    function add(line, js) {
        js ? (code += line.match(reExp) ? line + '\n' : 'r.push(' + line + ');\n') :
            (code += line != '' ? 'r.push("' + line.replace(/"/g, '\\"') + '");\n' : '');
        return add;
    }

    while (match = re.exec(template)) {
        add(template.slice(cursor, match.index))(match[1], true);
        cursor = match.index + match[0].length;
    }

    add(template.substr(cursor, template.length - cursor));
    code += 'return r.join("");';
    return new Function(code.replace(/[\r\t\n]/g, '')).apply(options);
}

var template = fs.readFileSync("app/server_configs/nginx.conf.template", "utf-8");

renderedConfig = render(template, {
    client_max_body_size: "75M",
    name: "ksc_site",
    port: process.argv[2],
    static_root: [process.cwd(), "/app/"].join(''),
    worker_connections: 1024,
    worker_processes: 5
});

fs.writeFileSync("app/server_configs/nginx.conf", renderedConfig);
