/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    appDir: true,
  },
  images: {
    domains: ['styles.redditmedia.com']
  }
}

module.exports = nextConfig
