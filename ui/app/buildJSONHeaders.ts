export default function buildJSONHeaders(accessToken: string) {
    return {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${accessToken}`
    };
}
