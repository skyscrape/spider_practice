const CryptoJS = require("crypto-js");


//
// const hash = CryptoJS.SHA1("/api/movie,1756091537").toString();
//
// const token=  btoa('db213d43b41392b5ed54a2244f1b25714cb7f566,1756091537')
// let timestamp10 = Math.floor(Date.now() / 1000)
// console.log(timestamp10)
// console.log(token)

function getToken(){
    let timestamp10 = Math.floor(Date.now() / 1000)
    const hash = CryptoJS.SHA1("/api/movie," + timestamp10) .toString();

    return btoa(hash + ',' + timestamp10)
}
console.log(getToken())