const CryptoJS = require("crypto-js")


const key = '1|python-spider.com|yuanrenxue.com|大威天龙，大罗法咒';
const iv = 'aiding1234567891';

function X(k, n = iv) {
    const encrypted = CryptoJS.AES.encrypt(
        key,
        CryptoJS.enc.Utf8.parse(iv),
        {
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        }
    );
    return encrypted.toString();
}

console.log(X(key, iv));  // 可能调用 X 或返回某个最终字符串