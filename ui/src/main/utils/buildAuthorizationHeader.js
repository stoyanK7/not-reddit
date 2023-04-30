export default function buildAuthorizationHeader(accessToken) {
    return {
        "Authorization": `Bearer ${accessToken}`
    };
}
