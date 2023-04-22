/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx}',
    './components/**/*.{js,ts,jsx,tsx}',
    './app/**/*.{js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {
      backgroundImage: {
        'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
        'gradient-conic':
          'conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))',
      },
      colors: {
        'reddit-orange': '#FF5700',
        'reddit-blue': '#9494FF',
        'reddit-gray': '#939698',
        'reddit-postline': "#CCCCCC",
        'reddit-gray-hover': '#E7E7E7',
        'reddit-gray-background': '#DAE0E6',
        'reddit-black': '#222222'
      },
      boxShadow: {
        'reddit': '0px 0px 57px 17px rgba(92,92,92,0.11)'
      }
    },
  },
  plugins: [],
}