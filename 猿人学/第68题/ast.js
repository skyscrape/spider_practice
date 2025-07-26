// deobf.js
// 用法：在和 w.js 同目录下运行 `node deobf.js`
// 会生成和覆盖 index.js，所有算式都被算成了纯数字。

const fs   = require('fs');
const path = require('path');

const INPUT  = path.join(__dirname, 'w.js');
const OUTPUT = path.join(__dirname, 'index.js');

let code = fs.readFileSync(INPUT, 'utf8');

// 1. 合并简单的 'a'+'b' → 'ab'
code = code.replace(
    /'((?:\\x[0-9A-Fa-f]{2}|[^'])*)'\s*\+\s*'((?:\\x[0-9A-Fa-f]{2}|[^'])*)'/g,
    (_, a, b) => `'${a + b}'`
);

// 2. 解码所有 \xNN → 对应字符
code = code.replace(/\\x([0-9A-Fa-f]{2})/g, (_, hex) =>
    String.fromCharCode(parseInt(hex, 16))
);

// 3. 把 0x... → 十进制数字
code = code.replace(/0x[0-9A-Fa-f]+/g, match =>
    String(parseInt(match, 16))
);

// 4. **全量计算**剩下的任何算术表达式：
//    匹配 -?数字 (运算符 -+*/ -?数字)+，然后用 eval 得到最终数字
code = code.replace(
    /-?\d+(?:\s*[-+*/]\s*-?\d+)+/g,
    expr => {
        try {
            return String(eval(expr));
        } catch {
            return expr;
        }
    }
);

// 5. 再合并一次可能残留的拼接（可选）
code = code.replace(
    /'([^']*)'\s*\+\s*'([^']*)'/g,
    (_, a, b) => `'${a + b}'`
);

// 写出还原后的脚本
fs.writeFileSync(OUTPUT, code, 'utf8');
console.log('✅ 完整还原并写入：', OUTPUT);