
window = global;
delete global;
delete Buffer;
delete process;

const http = require('http');

let cachedCookie = '';
let ready = false;

// 启动 HTTP 服务
const server = http.createServer((req, res) => {
    if (req.url === '/get' && req.method === 'GET') {
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({
            success: ready,
            value: cachedCookie
        }));
    } else {
        res.writeHead(404);
        res.end();
    }
});
server.listen(3000, () => {
    console.log('JS参数服务启动，监听端口 3000');
});

document = {
    cookie:''
}
location = {
    "ancestorOrigins": {},
    "href": "https://www.mafengwo.cn/wenda/detail-18342660.html",
    "origin": "https://www.mafengwo.cn",
    "protocol": "https:",
    "host": "www.mafengwo.cn",
    "hostname": "www.mafengwo.cn",
    "port": "",
    "pathname": "/wenda/detail-18342660.html",
    "search": "",
    "hash": ""
}

navigator = {
    appCodeName:"Mozilla",
    appName:"Netscape",
    appVersion:"5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
    language:"zh-CN",
    cookieEnabled:true,
    doNotTrack:null,
    hardwareConcurrency:8,
    languages:['zh-CN', 'en', 'en-GB', 'en-US'],
    platform:"Win32",
    product:"Gecko",
    productSub:"20030107",
    userAgent:"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
    vendor:"Google Inc.",
    vendorSub:"",
    webdriver:false,
    plugins: {
        length:5
    }
}

local = {}
localStorage ={
    getItem: function (k) {
        return local[k]
    },
    setItem:function(k,v){
        local[k] = v
    },
    clear:function(){
        local = {}
    },
    removeItem:function(k){
        delete local[k]
    }
}
sess = {}
sessionStorage = {
    getItem: function (k) {
        return sess[k]
    },
    setItem:function(k,v){
        sess[k] = v
    },
    clear:function(){
        sess = {}
    },
    removeItem:function(k){
        delete sess[k]
    }
}
addEventListener = function () { }
window.open = function () { }
window.XMLHttpRequest = function () { }


require('./new_probe.js');


(function () {
    var cookieTemp = '';
    Object.defineProperty(document, 'cookie', {
        set: function (val) {
            if (val.includes('w_tsfp')) {
                const value = val.split('=')[1].split(';')[0];
                console.log('发现 w_tsfp:', value);
                cachedCookie = value;
                ready = true;
            }
            cookieTemp = val;
            return val;
        },
        get: function () {
            return cookieTemp;
        },
    });
})();


