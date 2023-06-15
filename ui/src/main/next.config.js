/** @type {import("next").NextConfig} */

const ContentSecurityPolicy = `
  default-src 'self' ${process.env.NEXT_PUBLIC_API_SERVICE_URL};
  script-src 'self' 'unsafe-inline' 'unsafe-eval' ${process.env.NEXT_PUBLIC_API_SERVICE_URL};
  style-src 'self' 'unsafe-inline' ${process.env.NEXT_PUBLIC_API_SERVICE_URL};
  img-src 'self' blob: data: ${process.env.NEXT_PUBLIC_API_SERVICE_URL};
  connect-src 'self' ${process.env.NEXT_PUBLIC_API_SERVICE_URL} login.microsoftonline.com;
  object-src 'self' ${process.env.NEXT_PUBLIC_API_SERVICE_URL};
  media-src 'self' ${process.env.NEXT_PUBLIC_API_SERVICE_URL};
  frame-src 'self' ${process.env.NEXT_PUBLIC_API_SERVICE_URL};
  font-src 'self' ${process.env.NEXT_PUBLIC_API_SERVICE_URL};
  form-action 'self' ${process.env.NEXT_PUBLIC_API_SERVICE_URL};
`;

const securityHeaders = [
    {
      key: 'Content-Security-Policy',
      value: ContentSecurityPolicy.replace(/\s{2,}/g, ' ').trim()
    },
    {
      key: 'X-Frame-Options',
      value: 'DENY'
    },
    {
      key: 'X-Content-Type-Options',
      value: 'nosniff'
    }
  ];

const nextConfig = {
    reactStrictMode: true,
    images: {
        domains: [
            "localhost",
            "notredditapi.switzerlandnorth.cloudapp.azure.com",
            "notredditui.switzerlandnorth.cloudapp.azure.com"
        ]
    },
    async headers() {
        return [
          {
            source: '/(.*)',
            headers: securityHeaders
          }
        ];
    }
};

module.exports = nextConfig;
