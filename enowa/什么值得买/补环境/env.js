__process = process;


window = global;
delete global;
delete Buffer;
delete process;

document = {
    cookie:''
}
location = {
    "ancestorOrigins": {},
    "href": "https://post.smzdm.com/",
    "origin": "https://post.smzdm.com",
    "protocol": "https:",
    "host": "post.smzdm.com",
    "hostname": "post.smzdm.com",
    "port": "",
    "pathname": "/",
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
require('./probev3.js');

(function () {
    var cookieTemp = '';
    Object.defineProperty(document, 'cookie', {
        set: function (val) {
            if (val.indexOf('w_tsfp') != -1) {
                console.log('w_tsfp:',val.split('=')[1].split(';')[0]);
                __process.exit(0);
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