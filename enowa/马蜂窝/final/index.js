// __process = process;
Object.defineProperties(globalThis, {
    [Symbol.toStringTag]: {
        value: "Window"
    }
})

window = globalThis;
delete global;
delete Buffer;
// delete process;

document = {
    cookie:''
}
location = {
    "ancestorOrigins": {},
    "href": "https://www.mafengwo.cn/travel-scenic-spot/mafengwo/10320.html",
    "origin": "https://www.mafengwo.cn",
    "protocol": "https:",
    "host": "www.mafengwo.cn",
    "hostname": "www.mafengwo.cn",
    "port": "",
    "pathname": "/travel-scenic-spot/mafengwo/10320.html",
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
        0: {
            0: {
                description: "Portable Document Format",
                enabledPlugin: {
                    0: {},
                    1: {},
                    description: "Portable Document Format",
                    filename: "internal-pdf-viewer",
                    length: 2,
                    name: "Chromium PDF Plugin"
                },
                suffixes: "pdf",
                type: "application/x-google-chrome-pdf"
            },
            1: {
                description: "Portable Document Format",
                enabledPlugin: {
                    0: {},
                    1: {},
                    description: "Portable Document Format",
                    filename: "internal-pdf-viewer",
                    length: 2,
                    name: "Chromium PDF Plugin"
                },
                suffixes: "pdf",
                type: "text/pdf"
            },
            description: "Portable Document Format",
            filename: "internal-pdf-viewer",
            length: 2,
            name: "PDF Viewer"

        },
        1: {
            0: {
                description: "Portable Document Format",
                enabledPlugin: {
                    0: {},
                    1: {},
                    description: "Portable Document Format",
                    filename: "internal-pdf-viewer",
                    length: 2,
                    name: "Chromium PDF Plugin"
                },
                suffixes: "pdf",
                type: "application/x-google-chrome-pdf"
            },
            1: {
                description: "Portable Document Format",
                enabledPlugin: {
                    0: {},
                    1: {},
                    description: "Portable Document Format",
                    filename: "internal-pdf-viewer",
                    length: 2,
                    name: "Chromium PDF Plugin"
                },
                suffixes: "pdf",
                type: "text/pdf"
            },
            description: "Portable Document Format",
            filename: "internal-pdf-viewer",
            length: 2,
            name: "Chrome PDF Viewer"

        },
        2: {
            0: {
                description: "Portable Document Format",
                enabledPlugin: {
                    0: {},
                    1: {},
                    description: "Portable Document Format",
                    filename: "internal-pdf-viewer",
                    length: 2,
                    name: "Chromium PDF Plugin"
                },
                suffixes: "pdf",
                type: "application/x-google-chrome-pdf"
            },
            1: {
                description: "Portable Document Format",
                enabledPlugin: {
                    0: {},
                    1: {},
                    description: "Portable Document Format",
                    filename: "internal-pdf-viewer",
                    length: 2,
                    name: "Chromium PDF Plugin"
                },
                suffixes: "pdf",
                type: "text/pdf"
            },
            description: "Portable Document Format",
            filename: "internal-pdf-viewer",
            length: 2,
            name: "Chrome PDF Viewer"

        },
        3: {
            0: {
                description: "Portable Document Format",
                enabledPlugin: {
                    0: {},
                    1: {},
                    description: "Portable Document Format",
                    filename: "internal-pdf-viewer",
                    length: 2,
                    name: "Chromium PDF Plugin"
                },
                suffixes: "pdf",
                type: "application/x-google-chrome-pdf"
            },
            1: {
                description: "Portable Document Format",
                enabledPlugin: {
                    0: {},
                    1: {},
                    description: "Portable Document Format",
                    filename: "internal-pdf-viewer",
                    length: 2,
                    name: "Chromium PDF Plugin"
                },
                suffixes: "pdf",
                type: "text/pdf"
            },
            description: "Portable Document Format",
            filename: "internal-pdf-viewer",
            length: 2,
            name: "Microsoft Edge PDF Viewer"

        },
        4: {
            0: {
                description: "Portable Document Format",
                enabledPlugin: {
                    0: {},
                    1: {},
                    description: "Portable Document Format",
                    filename: "internal-pdf-viewer",
                    length: 2,
                    name: "Chromium PDF Plugin"
                },
                suffixes: "pdf",
                type: "application/x-google-chrome-pdf"
            },
            1: {
                description: "Portable Document Format",
                enabledPlugin: {
                    0: {},
                    1: {},
                    description: "Portable Document Format",
                    filename: "internal-pdf-viewer",
                    length: 2,
                    name: "Chromium PDF Plugin"
                },
                suffixes: "pdf",
                type: "text/pdf"
            },
            description: "Portable Document Format",
            filename: "internal-pdf-viewer",
            length: 2,
            name: "WebKit built-in PDF"

        },
        length: 5
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
require('./source.js');

(function () {
    var cookieTemp = '';
    Object.defineProperty(document, 'cookie', {
        set: function (val) {
            if (val.indexOf('w_tsfp') != -1) {
                console.log('w_tsfp:',val.split('=')[1].split(';')[0]);
                process.exit(0);
            }
            cookieTemp = val;
            return val;
        },
        get: function () {
            return cookieTemp;
        },
    });
})();



function getCookie(){
    return document.cookie
}

