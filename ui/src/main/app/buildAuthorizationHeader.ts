export default function buildAuthorizationHeader(accessToken: string) {
    return {
        'Authorization': `Bearer ${accessToken}`
    };
}
