const CryptoJs = require('crypto-js');




function get_data(num) {
    tim = Date.parse(new Date()) / 1000;
    word = tim.toString() + '|' + num;
    var srcs = CryptoJs.enc.Utf8.parse(word);
    mes = CryptoJs.enc.Utf8.parse('wdf2ff*TG@*(F4)*YH)g430HWR(*)wse')
    var encrypted = CryptoJs.AES.encrypt(srcs, mes, {
        mode: CryptoJs.mode.ECB,
        padding: CryptoJs.pad.Pkcs7
    });
    return encrypted.toString();
}

