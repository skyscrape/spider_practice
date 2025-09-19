



// E = 'sfV20N04JmibOKurk8tUyS$mkeyword=&openConvert=false&pageNo=20&pageSize=10&projectType=&publishEndTime=&publishStartTime=&secondType=A&siteCode=44&thirdType=[]&tradingProcess=&type=trading-type1754882871505'
// E = CryptoJs.enc.Utf8.parse(E);
// console.log(E);
// h = E.words;
// m = 1632;
// F = 1632;
// h[F >>> 5] |= 128 << 24 - F % 32,
// h[(F + 64 >>> 9 << 4) + 14] = 0,
// h[(F + 64 >>> 9 << 4) + 15] = m,
//     p_sigBytes = 256
// console.log(E);
const CryptoJS = require('crypto-js');

const key = {
    words: [
        -502823668, 674667645, 1428120970, 1651855396,
        275583986, 559425526, 1572667705, -171331467
    ],
    sigBytes: 32
};

// 1) 构造成 WordArray
const wa = CryptoJS.lib.WordArray.create(key.words, key.sigBytes);

// 2) 正确的输出方式（密钥是二进制！用 Hex 或 Base64）
console.log('HEX :', wa.toString(CryptoJS.enc.Hex));
// console.log('BASE64:', wa.toString(CryptoJS.enc.Base64));
