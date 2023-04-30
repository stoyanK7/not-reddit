import {
    AuthenticatedTemplate,
    UnauthenticatedTemplate,
    useIsAuthenticated
} from "@azure/msal-react";
import Image from "next/image";
import Link from "next/link";
import { useEffect, useRef } from "react";
import { toast, ToastContainer } from "react-toast";

import LogoutButton from "@/components/LogoutButton";
import { loginRequest, msalInstance } from "@/utils/authConfig";
import buildJSONHeaders from "@/utils/buildJSONHeaders";
import fromApi from "@/utils/fromApi";
import getAccessToken from "@/utils/getAccessToken";


export default function Auth() {
    const isAuthenticated = useIsAuthenticated();
    const hasFetchedData = useRef(false);

    useEffect(() => {
        async function checkRegistrationStatus() {
            const isRegistered = await isUserRegistered();
            if (isAuthenticated && !isRegistered) {
                const email = msalInstance.getActiveAccount()?.username;
                if (email) {
                    await registerUser(email);
                }
            }
        }

        if (hasFetchedData.current === false) {
            checkRegistrationStatus();
            hasFetchedData.current = true;
        }
    }, [isAuthenticated]);


    async function isUserRegistered() {
        const accessToken = await getAccessToken();
        if (accessToken === null) {
            return;
        }
        const res = await fetch(fromApi("/api/user/registered"), {
            method: "GET",
            headers: buildJSONHeaders(accessToken),
        });
        const data = res.json();
        return data.isRegistered;
    }

    async function registerUser() {
        const accessToken = await getAccessToken();
        if (accessToken === null) {
            toast.error("Failed to get your access token.");
            return;
        }
        const res = await fetch(fromApi("/api/user"), {
            method: "POST",
            headers: buildJSONHeaders(accessToken),
        });

        if (res.ok) {
            toast.success("Registered successfully.");
        }
    }

    return (
        <main
            className="flex flex-col w-screen h-screen justify-center items-center">
            <ToastContainer
                delay={8000} />
            <div
                className="rounded-sm bg-white p-4 m-2 flex flex-col justify-center items-center
                gap-2 shadow-reddit border border-reddit-postline">
                <h1>Welcome to <b>not-reddit</b>!</h1>
                <AuthenticatedTemplate>
                    <span>
                        <b
                            className="text-reddit-orange" data-cy="accountsAmount">
                            You&nbsp;
                        </b>
                        are signed in!
                    </span>
                    <Link
                        href="/">
                        <button
                            className="p-2 rounded-sm bg-reddit-orange text-white">
                            Go to home page
                        </button>
                    </Link>
                    <span>or..</span>
                    <LogoutButton />
                </AuthenticatedTemplate>
                <UnauthenticatedTemplate>
                    <span
                        data-cy="nobodySignedIn">There are currently no users signed in!</span>
                    <div
                        className="relative overflow-visible w-1/2 h-10 hover:cursor-pointer">
                        <Image
                            style={{ objectFit: "contain" }}
                            alt="User avatar"
                            src="/ms-symbollockup-signin-light.svg"
                            fill
                            onClick={() => msalInstance.loginRedirect(loginRequest)}
                            data-cy="signIn" />
                    </div>
                </UnauthenticatedTemplate>
            </div>
        </main>
    );
}
