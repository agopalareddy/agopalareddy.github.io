const { FlatCompat } = require('@eslint/eslintrc');
const js = require('@eslint/js');
const path = require('node:path');

const compat = new FlatCompat({
  baseDirectory: __dirname,
  resolvePluginsRelativeTo: __dirname,
  recommendedConfig: js.configs.recommended,
});

module.exports = [
  ...compat.config(require(path.join(__dirname, '.eslintrc.json'))),
];
