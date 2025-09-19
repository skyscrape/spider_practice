const fs = require('fs');

const code = fs.readFileSync('source.js', 'utf8');
const decoded = code.replace(/\\x([0-9a-fA-F]{2})/g, (_, h) =>
    String.fromCharCode(parseInt(h, 16))
);
fs.writeFileSync('output.js', decoded);