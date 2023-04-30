import { 
    EventType,
    LogLevel,
    PublicClientApplication 
} from "@azure/msal-browser";
import { toast } from "react-toast";

export const msalConfig = {
    auth: {
        clientId: "d448d19c-b7c3-4c1f-8c1b-e726b3a3ba88",
        redirectUri: "http://localhost:3000/auth",
    },
    cache: {
        cacheLocation: "sessionStorage",
        storeAuthStateInCookie: false,
    },
    system: {	
        loggerOptions: {	
            loggerCallback: (level, message, containsPii) => {	
                if (containsPii) {		
                    return;		
                }		
                switch (level) {
                case LogLevel.Error:
                    console.error(message);
                    return;
                case LogLevel.Info:
                    console.info(message);
                    return;
                case LogLevel.Verbose:
                    console.debug(message);
                    return;
                case LogLevel.Warning:
                    console.warn(message);
                    return;
                default:
                    return;
                }	
            }	
        }	
    }
};

export const msalInstance = new PublicClientApplication(msalConfig);

msalInstance.addEventCallback((event) => {
    if (event.eventType === EventType.LOGIN_SUCCESS && event.payload) {
        const payload = event.payload;
        const account = payload.account;
        msalInstance.setActiveAccount(account);
        tokenRequest.account = msalInstance.getActiveAccount();
        if (account) {
            toast.success(`Logged in as ${account.username}`);
        }
    }
});

export const loginRequest = {
    scopes: ["api://d448d19c-b7c3-4c1f-8c1b-e726b3a3ba88/user_impersonation"]
};

export const tokenRequest = {
    scopes: ["api://d448d19c-b7c3-4c1f-8c1b-e726b3a3ba88/user_impersonation"],
    account: msalInstance.getActiveAccount()
};

export const getTokenRequest = () => {
    return {
        scopes: ["api://d448d19c-b7c3-4c1f-8c1b-e726b3a3ba88/user_impersonation"],
        account: msalInstance.getActiveAccount()
    };
};
