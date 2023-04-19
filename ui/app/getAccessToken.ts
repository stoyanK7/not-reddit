import {AuthenticationResult, IPublicClientApplication} from "@azure/msal-browser";
import {loginRequest} from "@/app/loginRequest";

export default async function getAccessToken(instance: IPublicClientApplication, accounts: any[]) {
    const tokenResponse: AuthenticationResult = await instance
        .acquireTokenSilent({scopes: loginRequest.scopes, account: accounts[0]})
    return tokenResponse.accessToken;
}
