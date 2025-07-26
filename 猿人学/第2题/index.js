window = global;
const CryptoJs = require('crypto-js');

document = {

}

location = {

}

var _$oa = ['aW5pdA==', 'YXN0aXM=', 'eHhkUUI=', 'c3RyaW5n', 'Y29uc3RydWN0b3I=', 'bG9n', 'WW9hb04=', 'VHZ2SnE=', 'YWlkaW5nX3dpbg==', 'REZza2k=', 'Y01XU1Q=', 'U3lLZ3M=', 'aW5wdXQ=', 'a1lPUWk=', 'Y0NGT3Y=', 'aHZZUnM=', 'VXhMZFM=', 'RENJeWU=', 'dEFCTVE=', 'bFNHWmg=', 'U0hZRGU=', 'UmJVQVg=', 'SVFhQmM=', 'b1Fqd2I=', 'elhFak0=', 'Qk9PY2M=', 'QmVrbW4=', 'd1pOZnc=', 'Z2dlcg==', 'YnRvYQ==', 'YkVXZU0=', 'dEVmWkE=', 'RUtHUEQ=', 'Y2hhaW4=', 'cmVsb2Fk', 'dXBrZEI=', 'Z3p5VHg=', 'TUpEUUI=', 'Z25MY3Q=', 'd2hpbGUgKHRydWUpIHt9', 'akNjUGc=', 'UFJ2Y1o=', 'ZGlUR2g=', 'aXlZbEQ=', 'c3RhdGVPYmplY3Q=', 'cUdla0g=', 'aHdaT2M=', 'emNmWnI=', 'QlVxeUY=', 'Q1hDaXk=', 'dXhEb3E=', 'YXBwbHk=', 'UVlEeEQ=', 'c1lBbXc=', 'ZnVuY3Rpb24gKlwoICpcKQ==', 'Tkt2dlc=', 'V0FaeVk=', 'VHlHcHU=', 'anRvUW8=', 'dk9wY3Y=', 'aGZkZWo=', 'b0thZmU=', 'UWFmZ2s=', 'b3pWWXU=', 'SmZzRmQ=', 'aHhmTm4=', 'UFdLcGY=', 'VGpOVGs=', 'Q3dpSGg=', 'VkVCbXY=', 'aEh5amk=', 'WGtVS3o=', 'T0ZTdVk=', 'R0JOUVU=', 'OyBwYXRoPS8=', 'VlZJa2U=', 'Qk1qcmM=', 'Y2FsbA==', 'dHBkVGc=', 'b0FTRHc=', 'U3BoTGo=', 'eEpYckM=', 'R1NYTms=', 'S2xHUmQ=', 'VUxSSVY=', 'QXFsWFQ=', 'eXpKenc=', 'Q2VLQlk=', 'Y291bnRlcg==', 'RHRRb2k=', 'dGVzdA==', 'RHhoU1g=', 'b3ZBSW8=', 'TWVWZ0o=', 'SlhqeHA=', 'Sk94cWY=', 'bEd4aHE=', 'RnpNaHc=', 'WUpVaUc=', 'VEFjSkM=', 'cEx1ZmM=', 'YWN0aW9u', 'XCtcKyAqKD86W2EtekEtWl8kXVswLTlhLXpBLVpfJF0qKQ==', 'WXdWcFE=', 'YlJnd28=', 'eld6T0I=', 'QkRMQU4=', 'RGtId3o=', 'YnhpYmc=', 'Qkl3Tkk=', 'c2lnbj0='];
(function (a, b) {
    var c = function (f) {
        while (--f) {
            a['push'](a['shift']());
        }
    };
    c(++b);
}(_$oa, 0xd6));
var _$ob = function (a, b) {
    a = a - 0x0;
    var c = _$oa[a];
    if (_$ob['StgKyw'] === undefined) {
        (function () {
            var f;
            try {
                var h = Function('return\x20(function()\x20' + '{}.constructor(\x22return\x20this\x22)(\x20)' + ');');
                f = h();
            } catch (i) {
                f = window;
            }
            var g = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=';
            f['atob'] || (f['atob'] = function (j) {
                var k = String(j)['replace'](/=+$/, '');
                var l = '';
                for (var m = 0x0, n, o, p = 0x0; o = k['charAt'](p++); ~o && (n = m % 0x4 ? n * 0x40 + o : o, m++ % 0x4) ? l += String['fromCharCode'](0xff & n >> (-0x2 * m & 0x6)) : 0x0) {
                    o = g['indexOf'](o);
                }
                return l;
            });
        }());
        _$ob['UUSGRu'] = function (e) {
            var f = atob(e);
            var g = [];
            for (var h = 0x0, j = f['length']; h < j; h++) {
                g += '%' + ('00' + f['charCodeAt'](h)['toString'](0x10))['slice'](-0x2);
            }
            return decodeURIComponent(g);
        };
        _$ob['xEKorY'] = {};
        _$ob['StgKyw'] = !![];
    }
    var d = _$ob['xEKorY'][a];
    if (d === undefined) {
        c = _$ob['UUSGRu'](c);
        _$ob['xEKorY'][a] = c;
    } else {
        c = d;
    }
    return c;
};
(function () {
    var a = {
        'TAcJC': function (d, e) {
            return d !== e;
        },
        'hfdej': 'RqWqW',
        'MJDQB': _$ob('0x1'),
        'GBNQU': function (d, e) {
            return d === e;
        },
        'JOxqf': _$ob('0x23'),
        'NqiIv': function (d, e) {
            return d + e;
        },
        'xxdQB': 'debu',
        'xJXrC': _$ob('0x24'),
        'vOpcv': _$ob('0x6d'),
        'cMWST': function (d, e) {
            return d(e);
        },
        'hHyji': function (d, e) {
            return d !== e;
        },
        'FqAgY': 'QNTuP',
        'OFSuY': _$ob('0x1e'),
        'tpdTg': _$ob('0x3e'),
        'DtQoi': _$ob('0x6e'),
        'TjNTk': function (d, e) {
            return d(e);
        },
        'FzMhw': _$ob('0x8'),
        'SphLj': _$ob('0x29'),
        'AqlXT': _$ob('0x14'),
        'gzyTx': function (d, e) {
            return d !== e;
        },
        'JazIV': _$ob('0x16'),
        'astis': _$ob('0x38'),
        'bxibg': function (d) {
            return d();
        },
        'BDLAN': function (d, e, f) {
            return d(e, f);
        },
        'gnLct': '此网页受【爱锭云盾\x20V1.0\x20动态版】保护',
        'JfsFd': function (d, e) {
            return d + e;
        },
        'upkdB': _$ob('0x10'),
        'YJUiG': function (d, e) {
            return d(e);
        },
        'lGxhq': function (d, e) {
            return d / e;
        },
        'hxfNn': function (d, e) {
            return d + e;
        },
        'ULRIV': function (d, e) {
            return d + e;
        },
        'vODrl': _$ob('0x7'),
        'zWzOB': _$ob('0x52')
    };
    var b = function () {
        if (a[_$ob('0x51')](a[_$ob('0x67')], a[_$ob('0x67')])) {
            var d = !![];
            return function (e, f) {
                if (a[_$ob('0x6b')](a[_$ob('0x44')], a[_$ob('0x2d')])) {
                    var g = d ? function () {
                        if (f) {
                            var h = f['apply'](e, arguments);
                            f = null;
                            return h;
                        }
                    } : function () {
                    };
                    d = ![];
                    return g;
                } else {
                    var i = fn[_$ob('0x3b')](context, arguments);
                    fn = null;
                    return i;
                }
            };
        } else {
            return ![];
        }
    }();
    (function () {
        var d = {
            'iyYlD': function (e, f) {
                return a['NqiIv'](e, f);
            },
            'oKafe': a[_$ob('0xa')],
            'ovAIo': a[_$ob('0x59')],
            'TvvJq': a[_$ob('0x43')],
            'cqwAY': function (e, f) {
                return a[_$ob('0x12')](e, f);
            },
            'jtoQo': function (e, f) {
                return a[_$ob('0x4e')](e, f);
            },
            'ozVYu': a['FqAgY'],
            'oQjwb': a[_$ob('0x50')],
            'RbUAX': a[_$ob('0x56')],
            'BOOcc': a[_$ob('0x61')],
            'kYOQi': function (e, f) {
                return a[_$ob('0x4b')](e, f);
            },
            'XkUKz': a[_$ob('0x69')],
            'rLbkZ': a[_$ob('0x58')],
            'tEfZA': a[_$ob('0x5d')],
            'CwiHh': function (e, f) {
                return a[_$ob('0x2c')](e, f);
            },
            'umFIY': a['JazIV'],
            'hwZOc': a[_$ob('0x9')],
            'PWKpf': function (e) {
                return a[_$ob('0x5')](e);
            }
        };
        a[_$ob('0x3')](b, this, function () {
            var e = {
                'VEBmv': function (i, j) {
                    return d['cqwAY'](i, j);
                }
            };
            if (d[_$ob('0x42')](d[_$ob('0x47')], d[_$ob('0x1f')])) {
                var f = new RegExp(d[_$ob('0x1d')]);
                var g = new RegExp(d[_$ob('0x21')], 'i');
                var h = d[_$ob('0x15')](_$oc, d[_$ob('0x4f')]);
                if (!f[_$ob('0x62')](d[_$ob('0x33')](h, d['rLbkZ'])) || !g[_$ob('0x62')](d[_$ob('0x33')](h, d[_$ob('0x27')]))) {
                    d[_$ob('0x15')](h, '0');
                } else {
                    if (d[_$ob('0x4c')](d['umFIY'], d[_$ob('0x36')])) {
                        d[_$ob('0x4a')](_$oc);
                    } else {
                        if (ret) {
                            return debuggerProtection;
                        } else {
                            FYnSYl[_$ob('0x4d')](debuggerProtection, 0x0);
                        }
                    }
                }
            } else {
                (function () {
                    return !![];
                }[_$ob('0xc')](QJpHco['iyYlD'](QJpHco[_$ob('0x45')], QJpHco[_$ob('0x64')]))[_$ob('0x55')](QJpHco[_$ob('0xf')]));
            }
        })();
    }());
    console[_$ob('0xd')](a[_$ob('0x2e')]);
    // var c = new Date()['valueOf']();
    var c = 1587102734000
    token = window[_$ob('0x25')](a[_$ob('0x48')](a['upkdB'], a['YJUiG'](String, c)));
    md = a[_$ob('0x6a')](CryptoJs.MD5, window[_$ob('0x25')](a[_$ob('0x48')](a[_$ob('0x2b')], a[_$ob('0x6a')](String, Math['round'](a[_$ob('0x68')](c, 0x3e8))))));
    document['cookie'] = a[_$ob('0x48')](a[_$ob('0x48')](a['JfsFd'](a[_$ob('0x48')](a[_$ob('0x49')](a[_$ob('0x5c')](a['vODrl'], Math['round'](a[_$ob('0x68')](c, 0x3e8))), '~'), token), '|'), md), a[_$ob('0x2')]);
    console.log(document)
    // location[_$ob('0x2a')]();
}());

function _$oc(a) {
    var b = {
        'DxhSX': function (d, e) {
            return d(e);
        },
        'YwVpQ': function (d, e) {
            return d === e;
        },
        'NKvvW': _$ob('0xb'),
        'mCRCf': _$ob('0x2f'),
        'lSGZh': _$ob('0x60'),
        'zcfZr': function (d, e) {
            return d !== e;
        },
        'pLufc': function (d, e) {
            return d + e;
        },
        'YoaoN': function (d, e) {
            return d / e;
        },
        'MeVgJ': 'length',
        'uSMPY': function (d, e) {
            return d === e;
        },
        'THSEI': function (d, e) {
            return d % e;
        },
        'BMjrc': _$ob('0x41'),
        'VVIke': function (d, e) {
            return d + e;
        },
        'BIwNI': 'debu',
        'JXjxp': _$ob('0x24'),
        'EgTkN': 'action',
        'Qafgk': function (d, e) {
            return d !== e;
        },
        'bOvRf': _$ob('0x17'),
        'EKGPD': _$ob('0x18'),
        'DFski': function (d, e) {
            return d + e;
        },
        'DCIye': _$ob('0x34'),
        'uxDoq': _$ob('0x3e'),
        'sYAmw': _$ob('0x6e'),
        'VtHWa': _$ob('0x8'),
        'diTGh': function (d, e) {
            return d + e;
        },
        'MMktA': 'chain',
        'oASDw': _$ob('0x14'),
        'Bekmn': function (d) {
            return d();
        },
        'yzJzw': function (d, e, f) {
            return d(e, f);
        },
        'fKXxE': function (d, e) {
            return d === e;
        },
        'GSXNk': _$ob('0x4'),
        'SyKgs': function (d, e) {
            return d === e;
        },
        'tABMQ': _$ob('0x1c'),
        'zXEjM': _$ob('0x40'),
        'bEWeM': function (d, e) {
            return d(e);
        }
    };

    function c(d) {
        var e = {
            'jCcPg': function (f, g) {
                return b['DxhSX'](f, g);
            }
        };
        if (b[_$ob('0x0')](typeof d, b[_$ob('0x3f')])) {
            return function (f) {
            }[_$ob('0xc')](b['mCRCf'])[_$ob('0x3b')](b[_$ob('0x1b')]);
        } else {
            if (b[_$ob('0x37')](b[_$ob('0x6c')]('', b[_$ob('0xe')](d, d))[b[_$ob('0x65')]], 0x1) || b['uSMPY'](b['THSEI'](d, 0x14), 0x0)) {
                if (b[_$ob('0x37')](b[_$ob('0x54')], b[_$ob('0x54')])) {
                    e[_$ob('0x30')](result, '0');
                } else {
                    (function () {
                        return !![];
                    }[_$ob('0xc')](b[_$ob('0x53')](b[_$ob('0x6')], b[_$ob('0x66')]))[_$ob('0x55')](b['EgTkN']));
                }
            } else {
                if (b[_$ob('0x46')](b['bOvRf'], b[_$ob('0x28')])) {
                    (function () {
                        return ![];
                    }['constructor'](b[_$ob('0x11')](b[_$ob('0x6')], b['JXjxp']))[_$ob('0x3b')](b[_$ob('0x19')]));
                } else {
                    var h = firstCall ? function () {
                        if (fn) {
                            var i = fn[_$ob('0x3b')](context, arguments);
                            fn = null;
                            return i;
                        }
                    } : function () {
                    };
                    firstCall = ![];
                    return h;
                }
            }
        }
        b['DxhSX'](c, ++d);
    }

    try {
        if (a) {
            if (b['fKXxE'](b[_$ob('0x5a')], b[_$ob('0x5a')])) {
                return c;
            } else {
                return c;
            }
        } else {
            if (b[_$ob('0x13')](b[_$ob('0x1a')], b[_$ob('0x20')])) {
                var f = {
                    'PRvcZ': b[_$ob('0x3a')], 'gWNiT': b[_$ob('0x3d')], 'QYDxD': function (g, h) {
                        return b[_$ob('0x63')](g, h);
                    }, 'CXCiy': b['VtHWa'], 'CeKBY': function (g, h) {
                        return b[_$ob('0x32')](g, h);
                    }, 'qGekH': b['MMktA'], 'KlGRd': b[_$ob('0x57')], 'JFJOT': function (g) {
                        return b[_$ob('0x22')](g);
                    }
                };
                b[_$ob('0x5e')](vqXyh, this, function () {
                    var g = new RegExp(f[_$ob('0x31')]);
                    var h = new RegExp(f['gWNiT'], 'i');
                    var i = f[_$ob('0x3c')](_$oc, f[_$ob('0x39')]);
                    if (!g[_$ob('0x62')](f[_$ob('0x5f')](i, f[_$ob('0x35')])) || !h[_$ob('0x62')](f['CeKBY'](i, f[_$ob('0x5b')]))) {
                        f[_$ob('0x3c')](i, '0');
                    } else {
                        f['JFJOT'](_$oc);
                    }
                })();
            } else {
                b[_$ob('0x26')](c, 0x0);
            }
        }
    } catch (f) {
    }
}