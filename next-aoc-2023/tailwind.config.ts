import type { Config } from 'tailwindcss'

const config: Config = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      backgroundImage: {
        '7-pipe': "url('/images/7-pipe.svg')",
        'L-pipe': "url('/images/L-pipe.svg')",
        'F-pipe': "url('/images/F-pipe.svg')",
        'J-pipe': "url('/images/J-pipe.svg')",
        'h-pipe': "url('/images/h-pipe.svg')",
        'v-pipe': "url('/images/v-pipe.svg')",
      },
    },
  },
  plugins: [],
}
export default config
