lyq = console.log
window = global;
delete global;
delete Buffer;
delete process;

const http = require('http');

let cachedCookie = '';
let ready = false;

_encrypt = 1
window.__g = {}

document = {
    cookie:'',
    querySelector: function (ele){
        lyq('document querySelector:::',ele)
    },
    currentScript: function (ele){
        lyq('document currentScript:::',ele)
    },
    getElementById(elementId) {
        lyq('document currentScript:::', elementId)
    },
}
location = {
    "ancestorOrigins": {},
    "href": "https://zhuanlan.zhihu.com/p/252861467",
    "origin": "https://zhuanlan.zhihu.com",
    "protocol": "https:",
    "host": "zhuanlan.zhihu.com",
    "hostname": "zhuanlan.zhihu.com",
    "port": "",
    "pathname": "/p/252861467",
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




function get_enviroment(proxy_array) {
    for(var i=0; i<proxy_array.length; i++){
        handler = '{\n' +
            '    get: function(target, property, receiver) {\n' +
            '        lyq("方法:", "get  ", "对象:", ' +
            '"' + proxy_array[i] + '" ,' +
            '"  属性:", property, ' +
            '"  属性类型:", ' + 'typeof property, ' +
            // '"  属性值:", ' + 'target[property], ' +
            '"  属性值类型:", typeof target[property]);\n' +
            '        return target[property];\n' +
            '    },\n' +
            '    set: function(target, property, value, receiver) {\n' +
            '        lyq("方法:", "set  ", "对象:", ' +
            '"' + proxy_array[i] + '" ,' +
            '"  属性:", property, ' +
            '"  属性类型:", ' + 'typeof property, ' +
            // '"  属性值:", ' + 'target[property], ' +
            '"  属性值类型:", typeof target[property]);\n' +
            '        return Reflect.set(...arguments);\n' +
            '    }\n' +
            '}'
        eval('try{\n' + proxy_array[i] + ';\n'
            + proxy_array[i] + '=new Proxy(' + proxy_array[i] + ', ' + handler + ')}catch (e) {\n' + proxy_array[i] + '={};\n'
            + proxy_array[i] + '=new Proxy(' + proxy_array[i] + ', ' + handler + ')}')
    }
}
proxy_array = ['window', 'document', 'location', 'navigator', 'history','screen']

get_enviroment(proxy_array)



