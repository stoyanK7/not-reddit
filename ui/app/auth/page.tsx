"use client";

import Image from "next/image";
import {useMsal} from "@azure/msal-react";
import {
    EventMessage,
    EventType,
} from "@azure/msal-browser";
import {useEffect, useState} from "react";
import {ToastContainer, toast} from 'react-toast';
import IsNotSignedIn from "@/app/post/create/IsNotSignedIn";
import IsSignedIn from "@/app/post/create/IsSignedIn";
import getAccessToken from "@/app/getAccessToken";
import buildJSONHeaders from "@/app/buildJSONHeaders";
import IsNotRegistered from "@/app/IsNotRegistered";

export default function AuthPage() {
    const {instance, accounts, inProgress} = useMsal();
    const [isRegistered, setIsRegistered] = useState(true);
    const [hydrated, setHydrated] = useState(false);

    useEffect(() => {
        setHydrated(true);
        checkIfUserIsRegistered();

        instance.enableAccountStorageEvents();
        instance.addEventCallback((message: EventMessage) => {
            if (message.eventType === EventType.LOGIN_SUCCESS) {
                checkIfUserIsRegistered();
                toast.success("Logged in successfully.");
            }
        });
    }, []);

    async function checkIfUserIsRegistered() {
        const accessToken: string | null = await getAccessToken(instance, accounts);
        if (accessToken === null) {
            return;
        }
        const options = {
            method: "POST",
            headers: buildJSONHeaders(accessToken),
            body: JSON.stringify({email: accounts[0].username})
        };
        const res: Response = await fetch(`${process.env.NEXT_PUBLIC_API_SERVICE_URL}/user/registered`, options);
        const data = await res.json();
        setIsRegistered(data.isRegistered);
    }

    // Render nothing until hydrated.
    if (!hydrated) {
        return null
    }

    return (
        <main className="flex flex-col bg-white w-screen h-screen justify-center items-center">
            <ToastContainer/>
            <div className="rounded-sm bg-white p-4 m-2 flex flex-col justify-center items-center
                gap-2 shadow-reddit border border-reddit-postline">
                <div className="relative overflow-visible w-1/2 h-10">
                    <Image
                        style={{objectFit: 'contain'}}
                        src="/logo-full.png"
                        alt="Application logo"
                        fill
                        sizes="(max-width: 768px) 100vw,
                        (max-width: 1200px) 50vw,
                        33vw"/>
                </div>
                <h1>Welcome to <b>not-reddit</b>!</h1>
                {accounts.length > 0 && <IsSignedIn/>}
                {inProgress === "login" && (<span>Logging in...</span>)}
                {accounts.length === 0 && inProgress !== "login" && <IsNotSignedIn/>}
            </div>
            {!isRegistered && <IsNotRegistered/>}
        </main>
    )
}
