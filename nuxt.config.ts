// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    debug: false,
    modules: [
        '@nuxtjs/tailwindcss',
        'nuxt-icon'
    ],
    postcss: {
        plugins: {
            tailwindcss: {},
            autoprefixer: {}
        }
    },
    runtimeConfig: {
        debug: !!process.env.DEBUG,
        public: {
            API_URL: process.env.NUXT_PUBLIC_API_URL
        }
    },
    tailwindcss: {
        configPath: '~/tailwind.config.js',
        cssPath: '~/assets/css/tailwind.css'
    },
    app: {
        head: {
            bodyAttrs: {
                class: 'bg-body min-h-screen text-white'
            }
        }
    }
});
