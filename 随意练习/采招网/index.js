const CryptoJS = require("crypto-js");


var variate = {
    key: { "words": [863652730, 2036741733, 1164342596, 1782662963], "sigBytes": 16 },
    aceIV: { "words": [1719227713, 1314533489, 1397643880, 1749959510], "sigBytes": 16 },
    xgGjcArray: [],
    xgGjcIndex: 0,

}
function get_data(str) {

    var nContent = CryptoJS.AES.decrypt(str, variate.key, {
        iv: variate.aceIV,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.ZeroPadding
    })
    var constr = CryptoJS.enc.Utf8.stringify(nContent)
    return  constr

}
