const plugin = require('tailwindcss/plugin');
module.exports = plugin(function ({matchUtilities, theme}) {
    matchUtilities({
        'grid-cols-fit': (value) => ({
            'grid-template-columns': `repeat(auto-fit, minmax(${value}, 1fr))`
        }),
        'grid-cols-fill': (value) => ({
            'grid-template-columns': `repeat(auto-fill, minmax(${value}, 1fr))`
        }),
    });
});