import { AuthenticationResult } from "@azure/msal-browser";
import { getTokenRequest, msalInstance } from "@/app/authConfig";

export default async function getAccessToken() {
    if (!getTokenRequest().account) {
        return null;
    }

    const tokenResponse: AuthenticationResult = await msalInstance
                                                    .acquireTokenSilent(getTokenRequest());
    return tokenResponse.accessToken;
}
