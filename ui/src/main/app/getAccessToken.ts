import {AuthenticationResult, IPublicClientApplication} from "@azure/msal-browser";
import { loginRequest } from "@/app/authConfig";

export default async function getAccessToken(instance: IPublicClientApplication, accounts: any[]) {
    if (!accounts.length) {
        return null;
    }

    const tokenResponse: AuthenticationResult = await instance
        .acquireTokenSilent({scopes: loginRequest.scopes, account: accounts[0]})
    return tokenResponse.accessToken;
}
