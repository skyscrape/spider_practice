function X() {
    if (null == V) {
        for (V = new z; H < Q; ) {
            var t = Math.floor(65536 * Math.random());
            K[H++] = 255 & t
        }
        for (V.init(K),
                 H = 0; H < K.length; ++H)
            K[H] = 0;
        H = 0
    }
    return V.next()
}
Z = function() {
    function t() {}
    return t.prototype.nextBytes = function(t) {
        for (var e = 0; e < t.length; ++e)
            t[e] = X()
    }
        ,
        t
}();
function encrypt(t) {
    var e = function(t, e) {
        if (e < t.length + 11)
            return null;
        var n = []
            , i = t.length - 1;
        for (; 0 <= i && 0 < e; ) {
            var r = t.charCodeAt(i--);
            r < 128 ? n[--e] = r : 127 < r && r < 2048 ? (n[--e] = 63 & r | 128,
                n[--e] = r >> 6 | 192) : (n[--e] = 63 & r | 128,
                n[--e] = r >> 6 & 63 | 128,
                n[--e] = r >> 12 | 224)
        }
        n[--e] = 0;
        var o = new Z
            , a = [];
        for (; 2 < e; ) {
            for (a[0] = 0; 0 == a[0]; )
                o.nextBytes(a);
            n[--e] = a[0]
        }
        return n[--e] = 2,
            n[--e] = 0,
            new _(n)
    }(t, 128);
    if (null == e)
        return null;
    var n = this.doPublic(e);
    if (null == n)
        return null;
    var i = n.toString(16);
    return 0 == (1 & i.length) ? i : "0" + i
}

console.log(encrypt('qazone123'));