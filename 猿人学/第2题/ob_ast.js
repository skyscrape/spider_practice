// deobfuscator.js
const fs = require('fs');
const path = require('path');

const FILE = 'index.js';   // 你的混淆文件名
const OUT  = 'index.deob.js';  // 输出文件名

// 读取目标文件
const code = fs.readFileSync(FILE, 'utf8');

// 1. 提取 _$oa 数组
const oaMatch = code.match(/var _\$oa\s*=\s*\[([\s\S]*?)\];/);
if (!oaMatch) {
    console.error('没有找到 _$oa 数组');
    process.exit(1);
}
const oa = oaMatch[1]
    .split(/,(?=(?:[^'"]|'[^']*'|"[^"]*")*$)/)
    .map(s => s.trim().replace(/^['"]|['"]$/g, ''));

// 2. 执行旋转逻辑

const rotMatch   = code.match(/\(_\$oa,\s*0x([0-9a-fA-F]+)\)/);
const b          = rotMatch ? parseInt(rotMatch[1], 16) : 0;
const shiftCount = (b + 1) % oa.length;
const oaRotated  = oa.slice(shiftCount).concat(oa.slice(0, shiftCount));

// 3. Base64 + URI 解码
function atob(str) {
    return Buffer.from(str, 'base64').toString('binary');
}
const decoded = oaRotated.map(e => {
    const bin = atob(e);
    const pct = Array.from(bin)
        .map(ch => '%' + ch.charCodeAt(0).toString(16).padStart(2, '0'))
        .join('');
    return decodeURIComponent(pct);
});

// 4. 全局替换 _$ob('0xNN')
let out = code.replace(/_\$ob\(\s*['"]0x([0-9a-fA-F]+)['"]\s*\)/g, (_, hex) => {
    return JSON.stringify(decoded[parseInt(hex, 16)] || '');
});

// 5. 去掉 _$oa、_$ob 定义（可选）
out = out
    .replace(/var _\$oa[\s\S]*?;\s*/g, '')
    .replace(/var _\$ob[\s\S]*?};\s*/g, '');

// 写入新文件
fs.writeFileSync(OUT, out, 'utf8');
console.log(`解混淆完成，已生成 ${OUT}`);