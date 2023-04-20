import { LogLevel } from "@azure/msal-browser";

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
            loggerCallback: (level: LogLevel, message: string, containsPii: boolean) => {	
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

export const loginRequest = {
    scopes: ["api://d448d19c-b7c3-4c1f-8c1b-e726b3a3ba88/user_impersonation"]
};
