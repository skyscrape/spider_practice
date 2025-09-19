
const CryptoJs = require("crypto-js");








e = '{"inviteMethod":"","businessClassfication":"","mc":"","lx":"ZBGS","dwmc":"","pageIndex":2}'


t = CryptoJs.MD5(e).toString()
timeStamp = new Date().getTime()
a = {
    "inviteMethod": "",
    "businessClassfication": "",
    "mc": "",
    "lx": "ZBGS",
    "dwmc": "",
    "pageIndex": 2,
    "sign": t,
    "timeStamp": timeStamp
}

let str ='MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCfCXKr7oBNLDpCWn9NbJDpr0aJTnYfAvoQLePfoaK85wvO2w+4nA/srKeKtdbKx2IdRi/SNgIRyaNLxQu2od4OPOVicfKJA5RY0/u5LskCowcu3PnxeteHYCS95cYrBVu42DCdQ8ubASlwclQ5v7HpUNdxZxeuU3IerN/QIAGcXwIDAQAB';
function parse_key(e) {
    try {
        var t = 0
            , n = 0
            , r = /^\s*(?:[0-9A-Fa-f][0-9A-Fa-f]\s*)+$/
            , o = r.test(e) ? g.decode(e) : b.unarmor(e)
            , i = O.decode(o);
        if (3 === i.sub.length && (i = i.sub[2].sub[0]),
        9 === i.sub.length) {
            t = i.sub[1].getHexStringValue(),
                this.n = I(t, 16),
                n = i.sub[2].getHexStringValue(),
                this.e = parseInt(n, 16);
            var a = i.sub[3].getHexStringValue();
            this.d = I(a, 16);
            var s = i.sub[4].getHexStringValue();
            this.p = I(s, 16);
            var l = i.sub[5].getHexStringValue();
            this.q = I(l, 16);
            var c = i.sub[6].getHexStringValue();
            this.dmp1 = I(c, 16);
            var u = i.sub[7].getHexStringValue();
            this.dmq1 = I(u, 16);
            var d = i.sub[8].getHexStringValue();
            this.coeff = I(d, 16)
        } else {
            if (2 !== i.sub.length)
                return !1;
            var f = i.sub[1]
                , h = f.sub[0];
            t = h.sub[0].getHexStringValue(),
                this.n = I(t, 16),
                n = h.sub[1].getHexStringValue(),
                this.e = parseInt(n, 16)
        }
        return !0
    } catch (p) {
        return !1
    }
}
v = {
    "0": 52,
    "1": 53,
    "2": 54,
    "3": 55,
    "4": 56,
    "5": 57,
    "6": 58,
    "7": 59,
    "8": 60,
    "9": 61,
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 9,
    "K": 10,
    "L": 11,
    "M": 12,
    "N": 13,
    "O": 14,
    "P": 15,
    "Q": 16,
    "R": 17,
    "S": 18,
    "T": 19,
    "U": 20,
    "V": 21,
    "W": 22,
    "X": 23,
    "Y": 24,
    "Z": 25,
    "a": 26,
    "b": 27,
    "c": 28,
    "d": 29,
    "e": 30,
    "f": 31,
    "g": 32,
    "h": 33,
    "i": 34,
    "j": 35,
    "k": 36,
    "l": 37,
    "m": 38,
    "n": 39,
    "o": 40,
    "p": 41,
    "q": 42,
    "r": 43,
    "s": 44,
    "t": 45,
    "u": 46,
    "v": 47,
    "w": 48,
    "x": 49,
    "y": 50,
    "z": 51,
    "+": 62,
    "/": 63,
    "-": 62,
    "_": 63,
    "=": -1,
    " ": -1,
    "\f": -1,
    "\n": -1,
    "\r": -1,
    "\t": -1,
    " ": -1,
    " ": -1,
    " ": -1
}
function decode(e) {
    var t;
    if (false) {
        var n = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
            , r = "= \f\n\r\t \u2028\u2029";
        for (v = Object.create(null),
                 t = 0; t < 64; ++t)
            v[n.charAt(t)] = t;
        for (v["-"] = 62,
                 v["_"] = 63,
                 t = 0; t < r.length; ++t)
            v[r.charAt(t)] = -1
    }
    var o = []
        , i = 0
        , a = 0;
    for (t = 0; t < e.length; ++t) {
        var s = e.charAt(t);
        if ("=" == s)
            break;
        if (s = v[s],
        -1 != s) {
            if (void 0 === s)
                throw new Error("Illegal character at offset " + t);
            i |= s,
                ++a >= 4 ? (o[o.length] = i >> 16,
                    o[o.length] = i >> 8 & 255,
                    o[o.length] = 255 & i,
                    i = 0,
                    a = 0) : i <<= 6
        }
    }
    switch (a) {
        case 1:
            throw new Error("Base64 encoding incomplete: at least 2 bits missing");
        case 2:
            o[o.length] = i >> 10;
            break;
        case 3:
            o[o.length] = i >> 16,
                o[o.length] = i >> 8 & 255;
            break
    }
    return o
}

console.log(decode(e));



