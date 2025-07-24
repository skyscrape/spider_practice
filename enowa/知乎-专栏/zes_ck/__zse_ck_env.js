dtavm = {}
dtavm.log = console.log
function proxy(obj, objname, type) { 
    return obj;
}

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

dtavm = {}
dtavm.log = console.log
function proxy(obj, objname, type) {
    function getMethodHandler(WatchName, target_obj) {
        let methodhandler = {
            apply(target, thisArg, argArray) {
                if (this.target_obj) {
                    thisArg = this.target_obj
                }
                let result = Reflect.apply(target, thisArg, argArray)
                if (target.name !== "toString") {
                    if (target.name === "addEventListener") {
                        dtavm.log(`调用者 => [${WatchName}] 函数名 => [${target.name}], 传参 => [${argArray[0]}], 结果 => [${result}].`)
                    } else if (WatchName === "window.console") {
                    } else {
                        dtavm.log(`调用者 => [${WatchName}] 函数名 => [${target.name}], 传参 => [${argArray}], 结果 => [${result}].`)
                    }
                } else {
                    dtavm.log(`调用者 => [${WatchName}] 函数名 => [${target.name}], 传参 => [${argArray}], 结果 => [${result}].`)
                }
                return result
            },
            construct(target, argArray, newTarget) {
                var result = Reflect.construct(target, argArray, newTarget)
                dtavm.log(`调用者 => [${WatchName}] 构造函数名 => [${target.name}], 传参 => [${argArray}], 结果 => [${(result)}].`)
                return result;
            }
        }
        methodhandler.target_obj = target_obj
        return methodhandler
    }

    function getObjhandler(WatchName) {
        let handler = {
            get(target, propKey, receiver) {
                let result = target[propKey]
                if (result instanceof Object) {
                    if (typeof result === "function") {
                        dtavm.log(`调用者 => [${WatchName}] 获取属性名 => [${propKey}] , 是个函数`)
                        return new Proxy(result, getMethodHandler(WatchName, target))
                    } else {
                        dtavm.log(`调用者 => [${WatchName}] 获取属性名 => [${propKey}], 结果 => [${(result)}]`);
                    }
                    return new Proxy(result, getObjhandler(`${WatchName}.${propKey}`))
                }
                if (typeof (propKey) !== "symbol") {
                    dtavm.log(`调用者 => [${WatchName}] 获取属性名 => [${propKey?.description ?? propKey}], 结果 => [${result}]`);
                }
                return result;
            },
            set(target, propKey, value, receiver) {
                if (value instanceof Object) {
                    dtavm.log(`调用者 => [${WatchName}] 设置属性名 => [${propKey}], 值为 => [${(value)}]`);
                } else {
                    dtavm.log(`调用者 => [${WatchName}] 设置属性名 => [${propKey}], 值为 => [${value}]`);
                }
                return Reflect.set(target, propKey, value, receiver);
            },
            has(target, propKey) {
                var result = Reflect.has(target, propKey);
                dtavm.log(`针对in操作符的代理has=> [${WatchName}] 有无属性名 => [${propKey}], 结果 => [${result}]`)
                return result;
            },
            deleteProperty(target, propKey) {
                var result = Reflect.deleteProperty(target, propKey);
                dtavm.log(`拦截属性delete => [${WatchName}] 删除属性名 => [${propKey}], 结果 => [${result}]`)
                return result;
            },
            defineProperty(target, propKey, attributes) {
                var result = Reflect.defineProperty(target, propKey, attributes);
                dtavm.log(`拦截对象define操作 => [${WatchName}] 待检索属性名 => [${propKey.toString()}] 属性描述 => [${(attributes)}], 结果 => [${result}]`)
                // debugger
                return result
            },
            getPrototypeOf(target) {
                var result = Reflect.getPrototypeOf(target)
                dtavm.log(`被代理的目标对象 => [${WatchName}] 代理结果 => [${(result)}]`)
                return result;
            },
            setPrototypeOf(target, proto) {
                dtavm.log(`被拦截的目标对象 => [${WatchName}] 对象新原型==> [${(proto)}]`)
                return Reflect.setPrototypeOf(target, proto);
            },
            preventExtensions(target) {
                dtavm.log(`方法用于设置preventExtensions => [${WatchName}] 防止扩展`)
                return Reflect.preventExtensions(target);
            },
            isExtensible(target) {
                var result = Reflect.isExtensible(target)
                dtavm.log(`拦截对对象的isExtensible() => [${WatchName}] isExtensible, 返回值==> [${result}]`)
                return result;
            },
        }
        return handler;
    }

    if (type === "method") {
        return new Proxy(obj, getMethodHandler(objname, obj));
    }
    return new Proxy(obj, getObjhandler(objname));
}
// window = proxy(window, 'window');
// document = proxy(document, 'document');
// navigator = proxy(navigator, 'navigator');
// location = proxy(location, 'location');


require_('./w.js');
(function () {
    'use strict';
    var cookieTemp = '';
    Object.defineProperty(document, 'cookie', {
      set: function (val) {
        if (val.length >= 100) {
            dtavm.log(val);
        }
        cookieTemp = val;
        return val;
      },
      get: function () {
        return cookieTemp;
      },
    });
})();