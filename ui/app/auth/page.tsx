"use client";

import Image from "next/image";
import Link from "next/link";
import { useMsal } from "@azure/msal-react";

export default function Auth() {
    const { instance, accounts, inProgress } = useMsal();

    return (
        <main className="flex w-screen h-screen justify-center items-center">
            <div className="rounded-sm bg-white p-4 m-2 flex flex-col justify-center items-center
                gap-2">
                <div className="relative overflow-visible w-1/2 h-10">
                    <Image
                        style={{ objectFit: 'contain' }}
                        src="/logo-full.png"
                        alt="Application logo"
                        fill />
                </div>
                <h1>Welcome to <b>not-reddit</b>!</h1>
                {accounts.length > 0 && (
                    <>
                        <span>There are currently {accounts.length} users signed in!</span>
                        <Link href="/">
                            <button className="p-2 rounded-sm bg-reddit-orange text-white">
                                Go to home page
                            </button>
                        </Link>
                        <span>or..</span>
                        <button className="p-2 rounded-sm bg-red-800 text-white"
                            onClick={() => instance.logout()}>Logout</button>
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
                                onClick={() => instance.loginPopup()} />
                        </div>
                    </>
                )}
            </div>
        </main>
    )
}