import { getTokenRequest, msalInstance } from "@/utils/authConfig";

export default async function getAccessToken() {
    if (!getTokenRequest().account) {
        return null;
    }

    const tokenResponse = await msalInstance.acquireTokenSilent(getTokenRequest());
    return tokenResponse.accessToken;
}
