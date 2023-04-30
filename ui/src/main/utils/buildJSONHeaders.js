export default function buildJSONHeaders(accessToken) {
    return {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${accessToken}`
    };
}
