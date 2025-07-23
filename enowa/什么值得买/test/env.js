// === 统一补环境框架 v1.0 ===

// 核心日志系统
const dtavm = {
    log: console.log,
    missing: new Set(),
    recordMissing(objName, prop) {
        const key = `${objName}.${prop}`;
        if (!this.missing.has(key)) {
            this.missing.add(key);
            this.log(`⚠️ 缺失属性访问: ${key}`);
        }
    }
};

// 核心代理函数
function proxy(obj, objName) {
    function getMethodHandler(WatchName, target_obj) {
        return {
            apply(target, thisArg, argArray) {
                if (this.target_obj) thisArg = this.target_obj;
                const result = Reflect.apply(target, thisArg, argArray);
                dtavm.log(`📞 [${WatchName}] 调用: ${target.name}(${safeJson(argArray)}) => ${safeResult(result)}`);
                return result;
            },
            construct(target, argArray, newTarget) {
                const result = Reflect.construct(target, argArray, newTarget);
                dtavm.log(`🛠 [${WatchName}] 构造: ${target.name}(${safeJson(argArray)}) => ${safeResult(result)}`);
                return result;
            },
            target_obj
        }
    }

    function getObjHandler(WatchName) {
        return {
            get(target, propKey, receiver) {
                let result;
                try {
                    result = target[propKey];
                } catch {
                    result = undefined;
                }

                if (typeof propKey !== "symbol") {
                    if (!(propKey in target)) {
                        dtavm.recordMissing(WatchName, propKey);
                    }
                    dtavm.log(`🔎 [${WatchName}] 读取属性: ${propKey} => ${safeResult(result)}`);
                }

                if (result instanceof Object) {
                    if (typeof result === "function") {
                        return new Proxy(result, getMethodHandler(`${WatchName}.${propKey}`, target));
                    } else {
                        return new Proxy(result, getObjHandler(`${WatchName}.${propKey}`));
                    }
                }
                return result;
            },
            set(target, propKey, value) {
                dtavm.log(`✏️ [${WatchName}] 设置属性: ${propKey} = ${safeResult(value)}`);
                return Reflect.set(target, propKey, value);
            }
        }
    }

    return new Proxy(obj, getObjHandler(objName));
}

// 防止序列化失败
function safeJson(obj) {
    try { return JSON.stringify(obj); } catch { return '[Unserializable]' }
}
function safeResult(res) {
    if (res instanceof Object) return res.constructor?.name || 'Object';
    return res;
}

// === 全局初始化 ===

globalThis.window = globalThis;
globalThis.document = {};
globalThis.navigator = {};
globalThis.location = { href: "https://example.com" };
globalThis.localStorage = {};
globalThis.sessionStorage = {};
globalThis.crypto = {};
globalThis.screen = {};
globalThis.performance = {};

// 动态代理挂载
window = proxy(window, "window");
document = proxy(document, "document");
navigator = proxy(navigator, "navigator");
location = proxy(location, "location");
localStorage = proxy(localStorage, "localStorage");
sessionStorage = proxy(sessionStorage, "sessionStorage");
crypto = proxy(crypto, "crypto");
screen = proxy(screen, "screen");
performance = proxy(performance, "performance");

console.log("✅ 统一补环境框架初始化完成");

// === 加载你的目标逻辑 ===
require('./source');

// === 最后自动输出缺失属性建议 ===
console.log("\n========== 缺失补环境建议 ==========");
[...dtavm.missing].forEach(item => console.log("需要补: " + item));