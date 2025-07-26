const CryptoJs = require('crypto-js');



function get_data(){
    var a = '9622';
    var timestamp = String(Date.parse(new Date()) / 1000);

    // 使用 CryptoJS 实现 btoa (base64编码) 和 MD5
    var tokens = CryptoJs.MD5(CryptoJs.enc.Base64.stringify(CryptoJs.enc.Utf8.parse(a + timestamp))).toString();

    return tokens
}