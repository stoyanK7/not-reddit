"use client";

import Image from "next/image";
import { useIsAuthenticated, useMsal } from "@azure/msal-react";
import { useEffect, useState } from "react";
import { ToastContainer, toast } from 'react-toast';
import IsNotSignedIn from "@/app/post/create/IsNotSignedIn";
import IsSignedIn from "@/app/post/create/IsSignedIn";
import getAccessToken from "@/app/getAccessToken";
import buildJSONHeaders from "@/app/buildJSONHeaders";
import { msalInstance } from "../authConfig";

export default function AuthPage() {
    const { accounts, inProgress } = useMsal();
    const isAuthenticated = useIsAuthenticated();
    const [hydrated, setHydrated] = useState(false);

    useEffect(() => {
        setHydrated(true);
    }, []);

    useEffect(() => {
        if (isAuthenticated && !isUserRegistered()) {
            const email: string | undefined = msalInstance.getActiveAccount()?.username;
            if (email) {
                registerUser(email);
            }
        }
    }, [isAuthenticated]);

    async function isUserRegistered() {
        const accessToken = await getAccessToken();
        if (accessToken === null) {
            return;
        }
        const options = {
            method: "POST",
            headers: buildJSONHeaders(accessToken),
            body: JSON.stringify({ email: accounts[0].username })
        };
        const res: Response = await fetch(`${process.env.NEXT_PUBLIC_API_SERVICE_URL}/user/registered`, options);
        const data = await res.json();
        return data.isRegistered;
    }

    async function registerUser(email: string) {
        const accessToken = await getAccessToken();
        if (accessToken === null) {
            toast.error("Failed to get your access token.");
            return;
        }
        const res: Response = await fetch(`${process.env.NEXT_PUBLIC_API_SERVICE_URL}/user/`, {
            method: 'POST',
            headers: buildJSONHeaders(accessToken),
            body: JSON.stringify({ email }),
        });

        if (res.ok) {
            toast.success("Registered successfully.");
        }
    }

    // Render nothing until hydrated.
    if (!hydrated) {
        return null
    }

    return (
        <main className="flex flex-col bg-white w-screen h-screen justify-center items-center">
            <ToastContainer delay={8000}/>
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
                        33vw"/>
                </div>
                <h1>Welcome to <b>not-reddit</b>!</h1>
                {isAuthenticated ? <IsSignedIn /> : <IsNotSignedIn />}
                {inProgress === "login" && (<span>Logging in...</span>)}
            </div>
        </main>
    )
}
