"use client";

import Image from "next/image";
import Link from "next/link";
import { useMsal } from "@azure/msal-react";
import { EventMessage, EventType, InteractionRequiredAuthError } from "@azure/msal-browser";
import { useEffect, useState } from "react";
import { loginRequest } from "@/app/loginRequest";

export default function Auth() {
    const { instance, accounts, inProgress } = useMsal();
    const [isRegistered, setIsRegistered] = useState(true);
    const [hydrated, setHydrated] = useState(false);

    useEffect(() => {
        setHydrated(true);

        instance.enableAccountStorageEvents();
        instance.addEventCallback((message: EventMessage) => {
            if (message.eventType === EventType.LOGIN_SUCCESS) {
                console.log(message.payload);
                instance.setActiveAccount(accounts[0]);
            }
        });
    }, []);

    function makeRequest() {
        instance.acquireTokenSilent(loginRequest)
            .then(async tokenResponse => {
                const headers = new Headers();
                const bearer = "Bearer " + tokenResponse.accessToken;
                headers.append("Authorization", bearer);
                const options = {
                    method: "POST",
                    headers: headers,
                    body: JSON.stringify({ email: "asd@asdas.com" })
                };

                const res = await fetch(`${process.env.NEXT_PUBLIC_API_SERVICE_URL}/user/registered`, options);
                const data = await res.json();
                console.log(data);
            }).catch(async (error) => {
                console.log(error);
                if (error instanceof InteractionRequiredAuthError) {
                    return instance.acquireTokenPopup(loginRequest);
                }
            })

    }

    // Render nothing until hydrated.
    if (!hydrated) { return null }

    return (
        <main className="flex bg-white w-screen h-screen justify-center items-center">
            <div className="rounded-sm bg-white p-4 m-2 flex flex-col justify-center items-center
                gap-2 shadow-reddit border border-reddit-postline">
                <div className="relative overflow-visible w-1/2 h-10">
                    <Image
                        style={{ objectFit: 'contain' }}
                        src="/logo-full.png"
                        alt="Application logo"
                        fill
                        sizes="(max-width: 768px) 100vw,
                        (max-width: 1200px) 50vw,
                        33vw" />
                </div>
                <h1>Welcome to <b>not-reddit</b>!</h1>
                {accounts.length > 0 && (
                    <>
                        <span>There are currently
                            &nbsp;<b className="text-reddit-orange">{accounts.length}</b>&nbsp;
                            users signed in!
                        </span>
                        <Link href="/">
                            <button className="p-2 rounded-sm bg-reddit-orange text-white">
                                Go to home page
                            </button>
                        </Link>
                        <span>or..</span>
                        <button className="p-2 rounded-sm bg-red-800 text-white"
                            onClick={() => instance.logoutPopup()}>Logout</button>
                    </>
                )}
                {inProgress === "login" && (
                    <span>Logging in...</span>
                )}
                {accounts.length === 0 && inProgress !== "login" && (
                    <>
                        <span>There are currently no users signed in!</span>
                        <div className="relative overflow-visible w-1/2 h-10 hover:cursor-pointer">
                            <Image
                                style={{ objectFit: 'contain' }}
                                alt="User avatar"
                                src="/ms-symbollockup-signin-light.svg"
                                fill
                                onClick={() => instance.loginPopup(loginRequest)} />
                        </div>
                    </>
                )}
            </div>
            <button onClick={makeRequest}>MAKE REQUEST</button>
        </main>
    )
}
