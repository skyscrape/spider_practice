const CryptoJs = require("crypto-js");


function getSign(obj) {
    e = {
        "channel": obj
    }
    delete e.sign;
    for (var t = [], n = Object.keys(e).sort(), r = 0; r < n.length; r++) {
        var i = n[r]
            , a = e[i];
        t.push(i),
            t.push(a)
    }
    t.push("iIndex");
    var s = t.join("_")
        , c = CryptoJs.MD5(s).toString();
    return c
}
