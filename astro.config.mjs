import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import markdoc from '@astrojs/markdoc';

// https://astro.build/config
export default defineConfig({
  site: 'https://github.com/CoconutPhishers',
  base: '/buzzctf_writeup23/',
  integrations: [
    markdoc(),
    starlight({
      title: 'BuzzCTF',
      editLink: {
        baseUrl: 'https://github.com/CoconutPhishers/buzzctf_writeup/edit/main/',
      },
      social: {
        github: 'https://github.com/CoconutPhishers',
        discord: 'https://discord.gg/4EpHk9KnJf'
      },
      sidebar: [
        {
          label: 'BuzzCTF',
          autogenerate: { directory: 'buzzctf'}
        },
      ],
      customCss: ['/src/assets/theme.css']
    }),
  ],
});
