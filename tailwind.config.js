import colors from 'tailwindcss/colors';
import forms from '@tailwindcss/forms';
import gridUtils from './tailwind-plugins/gridUtils';

/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        './pages/**/*.vue',
        './components/**/*.vue',
        './layouts/**/*.vue',
        './nuxt.config.ts',
        './app.vue'
    ],
    theme:   {
        screens: {
            xs:    '320px',
            sm:    '640px',
            md:    '768px',
            lg:    '1024px',
            xl:    '1280px',
            '2xl': '1536px',
            '3xl': '1920px'
        },
        extend:  {
            colors:    {
                body:      colors.slate[900],
                bodyLight: colors.slate[800],
                primary:   colors.pink[700],
                secondary: colors.green[400]
            },
            minHeight: ({theme}) => ({
                ...theme('spacing')
            })
        }
    },
    plugins: [forms, gridUtils]
};

