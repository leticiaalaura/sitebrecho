/** @type {import('tailwindcss').Config} */
module.exports = {
  future: {
    removeDeprecatedGapUtilities: true,
    purgeLayersByDefault: true,
  },
  purge: {
    enabled: false, //true for production build
    content: [
      '../**/templates/*.html',
      '../**/templates/**/*.html'
    ]
  },
  theme: {
    extend: {},
    fontFamily: {
      'display': ['Oswald'],
      'body': ['"Open Sans"'],
    }
  },
  variants: {},
  plugins: [],
}