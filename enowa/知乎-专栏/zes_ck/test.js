dtavm = {}
dtavm.log = console.log
function proxy(obj, objname, type) {
    return obj;
}
summary = console.log
require_ = require;
pocess_ = process;
delete global;
delete require;
delete process;
delete __dirname;
delete __filename;
delete module;
delete exports;

// 重写全局对象名称
Object.defineProperties(globalThis, {
    [Symbol.toStringTag]: {
        value: 'Window'
    }
});
// 重写全局对象原型链
function setTostringAndstringTag(obj, dictValue) {
    // 重写toString方法
    obj.toString = function toString() {
        return 'function ' + obj.name + '() { [native code] }';
    }
    // 重写Symbol.toStringTag属性
    Object.defineProperty(obj, Symbol.toStringTag, {
        value: '' + obj.name,
    });
    // 重写原型链Symbol.toStringTag属性
    Object.defineProperty(obj.prototype, Symbol.toStringTag, {
        value: '' + obj.name,
    });
    // 重写原型链toString方法
    obj.prototype.toString = function toString() {
        return '[object ' + obj.name + ']';
    }

    if (dictValue) {
        // 重写原型链属性或者方法
        if (dictValue['prototype_func_type']) {
            dictValuep = dictValue['prototype_func_type'];
            for (let key in dictValuep) {
                if (!obj.prototype.hasOwnProperty(key)) {
                    obj.prototype[key] = dictValuep[key];
                }
            }
        }
        // 重写对象属性或者方法
        if (dictValue['object_func_type']) {
            dictValueo = dictValue['object_func_type'];
            for (let key in dictValueo) {
                if (!obj.hasOwnProperty(key)) {
                    obj[key] = dictValueo[key];
                }
            }
        }
    }
};
// 重写原型链
function setprotoof(prototypes) {
    for (let i = 0; i < prototypes.length; i++) {
        let ctx = prototypes[i] + '.__proto__';
        let name__ = ctx;
        let boolc = false;
        for (let j = 0; j < prototypes.length; j++){
            if (boolc) {
                ctx += '.__proto__';
                name__ += '=' + prototypes[j] + '.prototype;\n' + ctx;
            }
            if (prototypes[j] === prototypes[i]) {
                boolc = true;
            }
        }
        eval(name__);
    }
}

EventTarget = function EventTarget() { throw new TypeError("Illegal constructor"); };
setTostringAndstringTag(EventTarget, {
    // 重写对象属性或者方法
    'object_func_type': null,
    // 重写对象原型链属性或者方法
    'prototype_func_type':null
});
WindowProperties = function Window() {throw new TypeError("Illegal constructor");};
setTostringAndstringTag(WindowProperties, {
    // 重写对象属性或者方法
    'object_func_type': {
        PERSISTENT: 1,
        TEMPORARY: 2,
    },
    // 重写对象原型链属性或者方法
    'prototype_func_type': {
        PERSISTENT: 1,
        TEMPORARY: 2,
        addEventListener:function addEventListener(){}
    }
});

Window = function Window() {throw new TypeError("Illegal constructor");};
setTostringAndstringTag(Window, {
    // 重写对象属性或者方法
    'object_func_type': {
        PERSISTENT: 1,
        TEMPORARY: 2,
    },
    // 重写对象原型链属性或者方法
    'prototype_func_type': {
        PERSISTENT: 1,
        TEMPORARY: 2,
    }
});

Location = function Location() { throw new TypeError("Illegal constructor"); };
setTostringAndstringTag(Location, {
    // 重写对象属性或者方法
    'object_func_type': null,
    // 重写对象原型链属性或者方法
    'prototype_func_type': null
});
Node = function Node() { throw new TypeError("Illegal constructor"); };
setTostringAndstringTag(Node, {
    // 重写对象属性或者方法
    'object_func_type': null,
    // 重写对象原型链属性或者方法
    'prototype_func_type':null
});
Document = function Document() { throw new TypeError("Illegal constructor"); };
setTostringAndstringTag(Document, {
    // 重写对象属性或者方法
    'object_func_type': null,
    // 重写对象原型链属性或者方法
    'prototype_func_type':null
});
HTMLDocument = function HTMLDocument() { throw new TypeError("Illegal constructor"); };
setTostringAndstringTag(HTMLDocument, {
    // 重写对象属性或者方法
    'object_func_type': null,
    // 重写对象原型链属性或者方法
    'prototype_func_type':null
});
Storage = function Storage() { throw new TypeError("Illegal constructor"); };
local = {};
setTostringAndstringTag(Storage, {
    // 重写对象属性或者方法
    'object_func_type': null,
    // 重写对象原型链属性或者方法
    'prototype_func_type': {
        clear: function clear() {
            local = {};
        },
        getItem: function getItem(key) {
            if (!Object.keys(local).includes(key)) {
                return null;
            }
            return local[key];
        },
        setItem: function setItem(key, value) {
            local[key] = value;
        },
        removeItem: function removeItem(key) {
            delete local[key];
        },
        key: function key(index) {
            return Object.keys(local)[index];
        },
        length: 0,
        get length() {
            return Object.keys(local).length;
        }
    }
});

window = globalThis;
window.toString = function () {
    return '[object Window]'
}
setprotoof(['window', 'Window', 'WindowProperties','EventTarget'])

location = {
    "ancestorOrigins": {},
    "href": "https://zhuanlan.zhihu.com/p/429932998",
    "origin": "https://zhuanlan.zhihu.com",
    "protocol": "https:",
    "host": "zhuanlan.zhihu.com",
    "hostname": "zhuanlan.zhihu.com",
    "port": "",
    "pathname": "/p/429932998",
    "search": "",
    "hash": "",
    'reload': function () {
        pocess_.exit(0);
    }
};
location.__proto__ = Location.prototype;

HTMLMetaElement = function HTMLMetaElement() { throw new TypeError("Illegal constructor"); };
setTostringAndstringTag(HTMLMetaElement, null);
require_('./content.js');
zh_zse_ck = {
    id: 'zh-zse-ck',
    charset: 'utf-8',
    content: contentc,
    getAttribute: function (res) {
        if (res === 'content') {
            return this.content;
        }
    }
};
zh_zse_ck.__proto__ = HTMLMetaElement.prototype;

DOMStringMap = function DOMStringMap() { throw new TypeError("Illegal constructor"); };
setTostringAndstringTag(DOMStringMap, null);
dOMStringMap = {
    assetsTrackerConfig: '{"appName":"zse_ck","trackJSRuntimeError":true}'
};
dOMStringMap.__proto__ = DOMStringMap.prototype;

HTMLScriptElement = function HTMLScriptElement() { throw new TypeError("Illegal constructor"); };
setTostringAndstringTag(HTMLScriptElement, null);
data_assets = {
    dataset: dOMStringMap
};
data_assets.__proto__ = HTMLScriptElement.prototype;
document = {
    querySelector: function () {
        if (arguments[0] === 'script[data-assets-tracker-config]') {
            return data_assets
        }
    },
    currentScript: data_assets,
    addEventListener: function () { },
    getElementById: function (res) {
        if (res === 'zh-zse-ck') {
            return zh_zse_ck
        }
    },
    referrer:''
};
setprotoof(['document', 'HTMLDocument', 'Document', 'Node', 'EventTarget'])

localStorage = {};
sessionStorage = {};
localStorage.__proto__ = Storage.prototype;
sessionStorage.__proto__ = Storage.prototype;

// 代理器封装
function get_enviroment(proxy_array) {
    for(var i=0; i<proxy_array.length; i++){
        handler = '{\n' +
            '    get: function(target, property, receiver) {\n' +
            '        summary("方法:", "get  ", "对象:", ' +
            '"' + proxy_array[i] + '" ,' +
            '"  属性:", property, ' +
            '"  属性类型:", ' + 'typeof property, ' +
            // '"  属性值:", ' + 'target[property], ' +
            '"  属性值类型:", typeof target[property]);\n' +
            '        return target[property];\n' +
            '    },\n' +
            '    set: function(target, property, value, receiver) {\n' +
            '        summary("方法:", "set  ", "对象:", ' +
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

require_('./emo.js');
(function () {
    'use strict';
    var cookieTemp = '';
    Object.defineProperty(document, 'cookie', {
        set: function (val) {
            if (val.length >= 100) {
                dtavm.log(val);
            }
            cookieTemp = val;
            summary(val);
            return val;
        },
        get: function () {
            summary(cookieTemp)
            return cookieTemp;
        },
    });
})();