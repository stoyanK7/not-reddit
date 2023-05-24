import {
    AuthenticatedTemplate,
    UnauthenticatedTemplate,
    useMsal
} from "@azure/msal-react";
import Image from "next/image";
import Link from "next/link";
import { useEffect, useState } from "react";
import { toast } from "react-toast";

import LogoutButton from "@/components/LogoutButton";
import { loginRequest, msalInstance } from "@/utils/authConfig";
import buildAuthorizationHeader from "@/utils/buildAuthorizationHeader";
import fromApi from "@/utils/fromApi";
import getAccessToken from "@/utils/getAccessToken";


export default function Auth() {
    const { accounts } = useMsal();
    const isAuthenticated = accounts.length > 0;
    const [hasUserConsented, setHasUserConsented] = useState(false);
    const [isRegistered, setIsRegistered] = useState(false);

    useEffect(() => {
        async function checkRegistrationStatus() {
            let internalIsRegistered;
            if (isAuthenticated) {
                internalIsRegistered = await isUserRegistered();
                setIsRegistered(internalIsRegistered);
            }
        }

        checkRegistrationStatus();
    }, [isAuthenticated]);

    useEffect(() => {
        async function getUserName() {
            if (isAuthenticated && isRegistered) {
                const username = await getUsername();
                localStorage.setItem("username", username);
            }
        }
        getUserName();
    }, [isAuthenticated, isRegistered]);

    async function isUserRegistered() {
        const accessToken = await getAccessToken();
        if (accessToken === null) {
            toast.error("Failed to get access token");
            return;
        }
        const res = await fetch(fromApi("/api/user/registered"), {
            method: "GET",
            credentials: "include",
            headers: buildAuthorizationHeader(accessToken),
        });
        const data = await res.json();
        return data.registered;
    }

    async function registerUser() {
        const accessToken = await getAccessToken();
        if (accessToken === null) {
            toast.error("Failed to get your access token.");
            return;
        }
        const res = await fetch(fromApi("/api/user"), {
            method: "POST",
            credentials: "include",
            headers: buildAuthorizationHeader(accessToken),
        });

        if (res.ok) {
            toast.success("Registered successfully.");
            setIsRegistered(true);
        }
    }

    async function getUsername() {
        const accessToken = await getAccessToken();
        if (accessToken === null) {
            toast.error("Failed to get your access token");
            return;
        }

        const res = await fetch(fromApi("/api/user/username"), {
            method: "GET",
            credentials: "include",
            headers: buildAuthorizationHeader(accessToken),
        });

        if (!res.ok) {
            toast.error("Failed getting your username");
            return;
        }
        const data = await res.json();
        return data.username;
    }

    const handleChecked = () => {
        setHasUserConsented(!hasUserConsented);
    };

    async function handleRegister() {
        if (isAuthenticated && !isRegistered) {
            if (!hasUserConsented) {
                toast.error("Please consent to the terms.");
                return;
            }
            await registerUser();
        }
    }

    return (
        <main
            className="flex flex-col w-screen h-screen justify-center items-center">
            <div
                className="rounded-sm bg-white p-4 m-2 flex flex-col justify-center items-center
                gap-2 shadow-reddit border border-reddit-postline w-1/3">
                <h1>Welcome to <b>not-reddit</b>!</h1>
                <AuthenticatedTemplate>
                    {isAuthenticated && !isRegistered && (
                        <>
                            <p
                                className="italic underline text-center">
                                By registering, you consent to the storage of your email for
                                identification
                                purposes. We prioritize your privacy and will only use your email
                                for
                                essential account-related communication.
                            </p>
                            <label>
                                <input
                                    type="checkbox"
                                    checked={hasUserConsented}
                                    onChange={handleChecked} />
                                I consent to the above.
                            </label>
                            <button
                                disabled={!hasUserConsented}
                                className="p-2 rounded-sm bg-reddit-orange text-white"
                                onClick={handleRegister} >
                                Register
                            </button>
                        </>
                    )}
                    {isAuthenticated && isRegistered && (
                        <>
                            <span
                                data-testid="youAreSignedIn">
                                <b
                                    className="text-reddit-orange">
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
                        </>
                    )}
                    <LogoutButton />
                </AuthenticatedTemplate>
                <UnauthenticatedTemplate>
                    <span
                        data-testid="nobodySignedIn">There are currently no users signed in!</span>
                    <div
                        className="relative overflow-visible w-1/2 h-10 hover:cursor-pointer">
                        <Image
                            style={{ objectFit: "contain" }}
                            alt="User avatar"
                            src="/ms-symbollockup-signin-light.svg"
                            fill
                            onClick={() => msalInstance.loginRedirect(loginRequest)}
                            data-testid="signIn" />
                    </div>
                </UnauthenticatedTemplate>
            </div>
        </main>
    );
}
