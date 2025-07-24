
data = {
    "uuid": "0090b126685711f0948f4fdb648c1d80",
    "c": "0aae3428db",
    "r": "ynfQrjwdSa",
    "t": "dCWYhstg83a3sXl063GLQaiLRxfKh5RHBNyTjfTpIQk="
}

function get_a() {

    for (let i = 0; i < 4; i++) {

        X = (i * 25000).toString() + '|' + ((i + 1) * 25000).toString() + '|' + data.r + '|' + data.c
        console.log(X)
        for (var s = (i * 2500);s <=((i+1)*2500); s++) {
            result = self['wp']['encSync'](data.r + s['toString'](), "hex");
            if (result['slice'](0, 10) === data.c) {
                self['postMessage'](s);
                break;
            }
        }
    }
}
get_a()