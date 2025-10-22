/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./site_WPWM/templates/**/*.html",
  ],
  theme: {
    extend: {
      fontFamily: {
        'midtown': ['Midtown Groveed', 'sans-serif'],
      },
      colors: {
        'pantone-2768': '#071D49',
      },
    },
  },
  plugins: [],
}
