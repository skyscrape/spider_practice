const CryptoJS = require("crypto-js");

function init(v, y) {
    v = this.words = v || [],
        y != undefined ? this.sigBytes = y : this.sigBytes = v.length * 4
}






function finalize(E) {
    E && _append(E);
    var y = _doFinalize();
    return y
}

function _doFinalize() {
    var p = _data
        , h = p.words
        , m = _nDataBytes * 8
        , F = p.sigBytes * 8;
    return h[F >>> 5] |= 128 << 24 - F % 32,
        h[(F + 64 >>> 9 << 4) + 14] = 0,
        h[(F + 64 >>> 9 << 4) + 15] = m,
        p.sigBytes = h.length * 4,
        _process(),
        _hash
}
function _process(E) {
    var y, v = _data, b = v.words, B = v.sigBytes, x = 16, k = x * 4, I = B / k;
    E ? I = Math.ceil(I) : I = Math.max((I | 0) - 0, 0);
    var L = I * x
        , $ = Math.min(L * 4, B);
    if (L) {
        for (var j = 0; j < L; j += x)
            _doProcessBlock(b, j);
        y = b.splice(0, L),
            v.sigBytes -= $
    }
    return new init(y,$)
}
var d = []
var c = [];
var l = [];
(function() {
        function p(g) {
            for (var E = Math.sqrt(g), y = 2; y <= E; y++)
                if (!(g % y))
                    return !1;
            return !0
        }
        function h(g) {
            return (g - (g | 0)) * 4294967296 | 0
        }
        for (var m = 2, F = 0; F < 64; )
            p(m) && (F < 8 && (l[F] = h(Math.pow(m, 1 / 2))),
                c[F] = h(Math.pow(m, 1 / 3)),
                F++),
                m++
    }
)();
var _hash = new init(l.slice(0))
function _doProcessBlock(p, h) {
    for (var m = _hash.words, F = m[0], g = m[1], E = m[2], y = m[3], v = m[4], b = m[5], B = m[6], x = m[7], k = 0; k < 64; k++) {
        if (k < 16)
            d[k] = p[h + k] | 0;
        else {
            var I = d[k - 15]
                , L = (I << 25 | I >>> 7) ^ (I << 14 | I >>> 18) ^ I >>> 3
                , $ = d[k - 2]
                , j = ($ << 15 | $ >>> 17) ^ ($ << 13 | $ >>> 19) ^ $ >>> 10;
            d[k] = L + d[k - 7] + j + d[k - 16]
        }
        var U = v & b ^ ~v & B
            , q = F & g ^ F & E ^ g & E
            , N = (F << 30 | F >>> 2) ^ (F << 19 | F >>> 13) ^ (F << 10 | F >>> 22)
            , M = (v << 26 | v >>> 6) ^ (v << 21 | v >>> 11) ^ (v << 7 | v >>> 25)
            , P = x + M + U + c[k] + d[k]
            , te = N + q;
        x = B,
            B = b,
            b = v,
            v = y + P | 0,
            y = E,
            E = g,
            g = F,
            F = P + te | 0
    }
    m[0] = m[0] + F | 0,
        m[1] = m[1] + g | 0,
        m[2] = m[2] + E | 0,
        m[3] = m[3] + y | 0,
        m[4] = m[4] + v | 0,
        m[5] = m[5] + b | 0,
        m[6] = m[6] + B | 0,
        m[7] = m[7] + x | 0
}
var _data = new init
var _nDataBytes = 0
function _append(E) {
    typeof E == "string" && (E = m_parse(E)),
        _data = E,
        _data = E
        _nDataBytes +=E.sigBytes
}
function concat(E) {
    var y = []
        , v = E.words
        , b = 0
        , B = 204;
    for (var I = 0; I < B; I += 4)
        y[b + I >>> 2] = v[I >>> 2];
    return this.sigBytes += B,
        this
}
function m_parse(E) {
    return h_parse(unescape(encodeURIComponent(E)))
}
function h_parse(E) {
    for (var y = E.length, v = [], b = 0; b < y; b++)
        v[b >>> 2] |= (E.charCodeAt(b) & 255) << 24 - b % 4 * 8;
    return new init(v,y)
}

const GF = "zxcvbnmlkjhgfdsaqwertyuiop0987654321QWERTYUIOPLKJHGFDSAZXCVBNM"
function xre(e, t) {
    switch (arguments.length) {
        case 1:
            return parseInt(Math.random() * e + 1, 10);
        case 2:
            return parseInt(Math.random() * (t - e + 1) + e, 10);
        default:
            return 0
    }
}



function get_Data(pageNo){
    r = `keyword=&openConvert=false&pageNo=${pageNo}&pageSize=10&projectType=&publishEndTime=&publishStartTime=&secondType=A&siteCode=44&thirdType=[]&tradingProcess=&type=trading-type`
    Nonce = get_nonce()
    Timestamp = get_timestamp()
    E =  Nonce+ "k8tUyS$m" + r + Timestamp
    result= finalize(E);
    const wa = CryptoJS.lib.WordArray.create(result.words, result.sigBytes);
    obj = {
        Signature: wa.toString(CryptoJS.enc.Hex),
        Nonce: Nonce,
        Timestamp: Timestamp,
    }
    return JSON.stringify( obj)
}
function get_nonce(){
    return  [...Array(16)].map(() => GF[xre(0, 61)]).join("")
}

function get_timestamp(){
    return Date.now()
}

console.log(get_Data(1));