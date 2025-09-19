const CryptoJS = require('crypto-js');


function getResCode() {
    _0x40a3a2 = CryptoJS.AES.encrypt(
        CryptoJS.enc.Utf8.parse(String(Math.floor(new Date().getTime() / 1000))),
        CryptoJS.enc.Utf8.parse("1234567887654321"),
        {
            iv: CryptoJS.enc.Utf8.parse("1234567887654321"),
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        }
    );
    return CryptoJS.enc.Base64.stringify(_0x40a3a2.ciphertext);
}

console.log(getResCode());