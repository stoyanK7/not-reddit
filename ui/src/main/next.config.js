/** @type {import("next").NextConfig} */
const nextConfig = {
    reactStrictMode: true,
    images: {
        domains: ["styles.redditmedia.com",
            "localhost",
            "notredditapi.switzerlandnorth.cloudapp.azure.com",
            "notredditui.switzerlandnorth.cloudapp.azure.com"
        ]
    },
};

module.exports = nextConfig;
